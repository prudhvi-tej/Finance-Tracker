from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewset
from .analytics import summary, category_summary, monthly_summary, recent_transactions

router=DefaultRouter()
router.register(r'transactions',TransactionViewset)

urlpatterns=[
    path('',include(router.urls)),
    path('summary/', summary),
    path('category-summary/', category_summary),
    path('monthly-summary/', monthly_summary),
    path('recent/', recent_transactions),
]