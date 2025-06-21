from django.contrib.auth import logout
from django.utils import timezone


class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.timeout = 150

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        last_activity = request.session.get('last_activity')
        now = timezone.now().timestamp()

        if last_activity:
            elapsed = now - last_activity
            if elapsed > self.timeout:
                logout(request)
                request.session.flush()
        request.session['last_activity'] = now
        return self.get_response(request)
