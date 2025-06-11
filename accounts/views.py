from django.contrib.auth.views import LoginView

from restaurantsystem.models import Orders
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import RegisterForm


class RegisterView(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

from .models import CustomUser


def google_callback(request):
    code = request.GET.get('code')
    token_url = 'https://oauth2.googleapis.com/token'
    data = {
        'code': code,
        'client_id': 'ВАШ_ID',
        'client_secret': 'ВАШ_SECRET',
        'redirect_uri': 'http://localhost:8000/accounts/google/callback/',
        'grant_type': 'authorization_code'
    }
    token_response = requests.post(token_url, data=data).json()
    access_token = token_response['access_token']

    user_info = requests.get(
        'https://www.googleapis.com/oauth2/v2/userinfo',
        headers={'Authorization': f'Bearer {access_token}'}
    ).json()

    email = user_info['email']
    user, created = CustomUser.objects.get_or_create(email=email)
    login(request, user)
    return redirect('home')


from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView


class OrdersListView(PermissionRequiredMixin, ListView):
    model = Orders
    template_name = 'restaurantsystem/orders.html'
    permission_required = 'app.view_post'


import requests
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import get_user_model

User = get_user_model()



def google_login(request):
    scope = "https://www.googleapis.com/auth/userinfo.email"
    redirect_uri = settings.GOOGLE_REDIRECT_URI
    return redirect(
        f"https://accounts.google.com/o/oauth2/v2/auth?"
        f"response_type=code&client_id={settings.GOOGLE_CLIENT_ID}"
        f"&redirect_uri={redirect_uri}&scope={scope}"
    )



def google_callback(request):
    code = request.GET.get('code')
    if not code:
        return redirect('login')

    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        'code': code,
        'client_id': settings.GOOGLE_CLIENT_ID,
        'client_secret': settings.GOOGLE_CLIENT_SECRET,
        'redirect_uri': settings.GOOGLE_REDIRECT_URI,
        'grant_type': 'authorization_code',
    }


    token_response = requests.post(token_url, data=token_data).json()
    access_token = token_response.get('access_token')


    user_info_response = requests.get(
        'https://www.googleapis.com/oauth2/v2/userinfo',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    user_data = user_info_response.json()
    email = user_data.get('email')


    user, created = User.objects.get_or_create(email=email)
    if created:
        user.username = email
        user.save()

    login(request, user)
    return redirect('index')


