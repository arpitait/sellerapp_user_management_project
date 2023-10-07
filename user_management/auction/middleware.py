from django.http import HttpResponseForbidden

class AdminApiSecretMiddleware:
    def __int__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_secret = request.META.get('HTTP_X_API_SECRET')
        if api_secret == 'your_static_secret':
            request.user.is_staff = True
        return self.get_response(request)