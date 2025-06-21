from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from accounts.views import google_login, google_callback, CustomLoginView, RegisterView, ProfileUpdateView, \
    ProfileDetailView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('google/login/', google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('google/callback/', google_callback, name='google_callback'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "accounts/reset_password.html", email_template_name = "accounts/password_reset_email.html", subject_template_name="accounts/password_reset_subject.txt",
                                                                 success_url=reverse_lazy('password_reset_done')), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_form.html",
                                                                               success_url=reverse_lazy('password_reset_complete')), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_done.html"), name ='password_reset_complete'),
    path('profile/update', ProfileUpdateView.as_view(template_name="accounts/profile_update.html"), name='profile_update'),
    path('profile/', ProfileDetailView.as_view(template_name="accounts/profile.html"), name='profile' )
]