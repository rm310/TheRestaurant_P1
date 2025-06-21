from django.utils import translation

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_language = getattr(request.user, 'language', 'en')
        translation.activate(user_language)
        response = self.get_response(request)
        translation.deactivate()
        return response