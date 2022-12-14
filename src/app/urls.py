"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from accounts.views import PasswordsChangeView

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView

from task.views import get_status, home, run_task


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/', include('accounts.urls')),

    # password urls change/reset
    path('password/change/', PasswordsChangeView.as_view(), name='password_change'),

    path(
        'password/reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html',
            html_email_template_name='registration/email/password_reset_email.html',
            subject_template_name='registration/email/password_reset_subject.txt',
        ),
        name='password_reset'
    ),

    path(
        'password/reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'
    ),

    path(
        'password/reset/confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),

    path(
        'password/reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'
    ),

    # quiz urls
    path('quiz/', include('quiz.urls')),
    path('home/', home, name='task_home'),
    path('tasks/<task_id>/', get_status, name='get_status'),
    path('tasks/', run_task, name='run_task'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
