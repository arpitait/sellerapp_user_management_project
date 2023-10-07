from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed


class StaticApiKeyAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_secret = request.META.get("HTTP_API_SECRET")

        if api_secret == settings.API_SECRET:
            return (None, None)
        raise AuthenticationFailed("API secret authentications failed")