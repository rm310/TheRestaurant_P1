from gettext import translation

from django.shortcuts import redirect


class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated is False and request.path != '/login/':
            return redirect('login')
        return self.get_response(request)


