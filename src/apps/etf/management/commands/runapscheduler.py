import logging
from django.conf import settings
import yfinance as yf
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from django.core.management.base import BaseCommand
from datetime import datetime
from ...models.etf_isin import IsinETF
from ...models.etf_info import InfoETF
from ...models.etf_prices import PricesETF
from ...models.etf_financial_data import FinancialDataETF

logger = logging.getLogger(__name__)


def download_data():
    tickers = IsinETF.objects.values_list('ticker_yf', flat=True)
    for ticker in tickers:
        logger.info(f"Adding {ticker}")
        etf = yf.Ticker(ticker)
        etf_info = etf.info
        etf_ticker = etf_info['symbol']
        etf_isin = IsinETF.objects.get(ticker_yf=etf_ticker)

        logger.info(f"Starting infoETF for {ticker}")
        InfoETF.objects.get_or_create(
            currency=etf_info['currency'],
            fundFamily=etf_info['fundFamily'],
            fundInceptionDate=etf_info['fundInceptionDate'],
            legalType=etf_info['legalType'],
            exchange=etf_info['exchange'],
            quoteType=etf_info['quoteType'],
            symbol=etf_info['symbol'],
            underlyingSymbol=etf_info['underlyingSymbol'],
            shortName=etf_info['shortName'],
            longName=etf_info['longName'],
            firstTradeDateEpochUTC=etf_info['firstTradeDateEpochUtc'],
            timeZoneFullName=etf_info['timeZoneFullName'],
            timeZoneShortName=etf_info['timeZoneShortName'],
            external_uuid=etf_info['uuid'],
            messageBoardId=etf_info['messageBoardId'],
            isin=etf_isin,
        )

        # Download prices of the day if it exists or historical if not
        logger.info(f"Starting PricesETF for {ticker}")
        try:
            PricesETF.objects.get(isin_id=etf_isin)
            created_prices = True

        except:
            created_prices = False

        if created_prices:
            etf_day_prices = etf.history(period="1day")
            PricesETF.objects.get_or_create(
                date=etf_day_prices['date'],
                open=etf_day_prices['Open'],
                high=etf_day_prices['High'],
                low=etf_day_prices['Low'],
                close=etf_day_prices['Close'],
                volume=etf_day_prices['Volume'],
                dividends=etf_day_prices['Dividends'],
                splits=etf_day_prices['Stock Splits'],
                capital_gains=etf_day_prices['Capital Gains'],
                isin=etf_isin,
            )

        else:
            etf_all_prices = etf.history(period="max")
            for index, row in etf_all_prices.iterrows():
                PricesETF.objects.get_or_create(
                    date=index.date(),
                    open=row['Open'],
                    high=row['High'],
                    low=row['Low'],
                    close=row['Close'],
                    volume=row['Volume'],
                    dividends=row['Dividends'],
                    splits=row['Stock Splits'],
                    capital_gains=row['Capital Gains'],
                    isin=etf_isin,
                )

            # Download financial data
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d')

            logger.info(f"Starting financialdataETF for {ticker}")
            FinancialDataETF.objects.get_or_create(
                date=formatted_date,
                fiftyTwoWeekLow=etf_info['fiftyTwoWeekLow'],
                fiftyTwoWeekHigh=etf_info['fiftyTwoWeekHigh'],
                fiftyDayAverage=etf_info['fiftyDayAverage'],
                twoHundredDayAverage=etf_info['twoHundredDayAverage'],
                ytdReturn=etf_info['ytdReturn'],
                beta3Year=etf_info['beta3Year'],
                threeYearAverageReturn=etf_info['threeYearAverageReturn'],
                fiveYearAverageReturn=etf_info['fiveYearAverageReturn'],
                isin=etf_isin,
            )

            logger.info(f"Finished extraction for {ticker}")


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            download_data,
            trigger=CronTrigger(minute="*/1"),  # Execute every 24 hours
            id="download_data",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'download_data'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
