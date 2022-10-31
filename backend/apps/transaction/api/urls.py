# Django imports
from django.urls import path


# Views imports
from apps.transaction.api.views import (
    transaction_api_view,
    transaction_detail_view
)


# Urls
urlpatterns = [
    path(
        'transaction/',
        transaction_api_view,
        name='transaction_api_view'
    ),
    path(
        'transaction/<int:pk>/',
        transaction_detail_view,
        name='transaction_detail_api_view'
    )
]