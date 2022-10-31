# Django imports
from django.urls import path


# Views imports
from apps.account.api.views import (
    account_api_view,
    account_detail_view
)


# Urls
urlpatterns = [
    path(
        'account/',
        account_api_view,
        name='account_api_view'
    ),
    path(
        'account/<int:pk>/',
        account_detail_view,
        name='account_detail_api_view'
    )
]