# Django imports
from django.urls import path


# Views imports
from apps.wallet.api.views import (
    wallet_api_view,
    wallet_detail_view
)


# Urls
urlpatterns = [
    path(
        'wallet/',
        wallet_api_view,
        name='wallet_api_view'
    ),
    path(
        'wallet/<int:pk>/',
        wallet_detail_view,
        name='wallet_detail_api_view'
    )
]