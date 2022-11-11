from django.urls import path
from django.views.generic import TemplateView

from .views import (
    UserLoginView, UserLogoutView,
    UserProfileUpdateView, UserRegisterView,
    user_activate, user_profile_view, user_reactivate,
)


app_name = 'accounts'

urlpatterns = [
    # register urls
    path('register/activate/<str:sign>/', user_activate, name='register_activate'),

    path(
        'register/done/',
        TemplateView.as_view(template_name='accounts/user_register_done.html'),
        name='register_done'
    ),

    path('register/', UserRegisterView.as_view(), name='register'),

    # login / logout urls
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    # profile urls
    path('profile/', user_profile_view, name='profile'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),

    # resend activation email
    path('activation/failed/', user_reactivate, name='activation_failed'),
]
