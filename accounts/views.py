# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.models import User # Import User model

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home') # Redirect to a home page (create this later)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                # Redirect to a success page.
                # Check if 'next' parameter exists for redirecting after login
                next_url = request.POST.get('next') or request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('home') # Redirect to a home page
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form, 'next': request.GET.get('next', '')})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login') # Redirect to login page

def password_reset_request_view(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': request.META['HTTP_HOST'], # or settings.SITE_DOMAIN
                        'site_name': 'CulturaConnect', # or settings.SITE_NAME
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http', # use 'https' in production
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                        messages.success(request, "A message with reset password instructions has been sent to your inbox.")
                        return redirect('password_reset_done')
                    except Exception as e:
                        messages.error(request, f"An error occurred: {e}")
                        return redirect('password_reset_request')
            else:
                messages.error(request, "No user is associated with this email address.")
                return redirect('password_reset_request')

    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password_reset_request.html", context={"form":password_reset_form})

def password_reset_done_view(request):
    return render(request, 'accounts/password_reset_done.html')

def password_reset_confirm_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and log in now.")
                return redirect('login')
            else:
                messages.error(request, "Password reset link was invalid, possibly because it has already been used. Please request a new password reset.")
        else:
            form = SetPasswordForm(user)
        return render(request, 'accounts/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Password reset link was invalid, possibly because it has already been used. Please request a new password reset.")
        return redirect('password_reset_request')

def password_reset_complete_view(request):
    return render(request, 'accounts/password_reset_complete.html')