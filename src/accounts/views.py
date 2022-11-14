from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.signing import BadSignature
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import ReactivationLinkForm, UserRegisterForm, UserUpdateForm
from .utils import signer


class UserRegisterView(CreateView):
    model = get_user_model()
    template_name = 'accounts/user_register.html'
    success_url = reverse_lazy('accounts:register_done')
    form_class = UserRegisterForm


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'accounts/bad_signature.html')
    user = get_object_or_404(get_user_model(), username=username)
    if user.is_activated:
        template = 'accounts/user_is_activated.html'
    else:
        template = 'accounts/user_activation_done.html'
        user.is_activated = True
        user.is_active = True
        user.save()
    return render(request, template)


def user_reactivate(request):
    from .apps import user_register
    if request.method == 'GET':
        form = ReactivationLinkForm()
    elif request.method == 'POST':
        form = ReactivationLinkForm(request.POST)
        user_email = request.POST.get('email')
        user = get_object_or_404(get_user_model(), email=user_email)
        user_register.send(sender=user, instance=user)
        return render(request, 'accounts/user_reactivation_done.html')
    return render(request, 'accounts/user_reactivation.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'


class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/user_logout.html'


@login_required
def user_profile_view(request):
    return render(request, 'accounts/user_profile.html')


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/user_profile_update.html'
    model = get_user_model()
    success_url = reverse_lazy('accounts:profile')
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return self.request.user


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/password_change.html'
    from_class = PasswordChangeForm
    success_url = reverse_lazy('index')
    success_message = "Password was changed successfully"
