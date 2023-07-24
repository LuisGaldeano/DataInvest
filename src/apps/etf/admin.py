from django.contrib import admin
from .models.etf_isin import IsinETF
from .models.etf_prices import PricesETF
from .models.etf_info import InfoETF
from .models.operations_record import OperationsRecord
from .models.etf_financial_data import FinancialDataETF
from .models.capital_contributions import CapitalContribution

admin.site.register(IsinETF)
admin.site.register(PricesETF)
admin.site.register(InfoETF)
admin.site.register(OperationsRecord)
admin.site.register(FinancialDataETF)
admin.site.register(CapitalContribution)

