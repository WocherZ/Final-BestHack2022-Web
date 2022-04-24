from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.decorators.http import require_GET
from django.views.generic.base import TemplateView, View
from django.contrib.auth.views import LogoutView

from .forms import *

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class Currency_rate(View):
    def get(self, request, *args, **kwargs):
        context = {}
        currency1 = kwargs['currency1']  # USD
        currency2 = kwargs['currency2']  # RUB
        cur1 = get_object_or_404(Currencies, code=currency1)
        cur2 = get_object_or_404(Currencies, code=currency2)
        context['currency1'] = cur1.name
        context['currency1_code'] = cur1.code
        context['currency2'] = cur2.name
        context['currency2_code'] = cur2.code


        currencies_rate = get_object_or_404(CurrenciesRates,
                                            first_currency_id=cur2.id,
                                            second_currency_id=cur1.id)
        context['current_rate'] = float(currencies_rate.current_rate)

        try:
            user_property = UserProperties.objects.filter(user_id=request.user.id).get(currency_id=cur1.id)
            context['user_property'] = user_property.number
        except ObjectDoesNotExist:
            context['user_property'] = 0

        context['user_balance'] = ExtendedUser.objects.filter(username=request.user.username).get().balance

        return render(request, template_name='currency_rate.html', context=context)


    def post(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        pass

def login_request(request):
    if request.method == "POST":
        form = AuthForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if User.objects.filter(username=username).exists() and not User.objects.get(username=username).is_active:
                return redirect('block')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                request.session.set_expiry(30 * 60)
                return redirect('account')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthForm()
    return render(request=request, template_name="login.html", context={"form": form})


def block(request):
    if request.GET and User.objects.filter(username=request.GET['username']).exists():
        user = User.objects.get(username=request.GET['username'])
        user.is_active = False
        user.save()
    return render(request, template_name='block.html')

class Logout(LogoutView):
    next_page = '/'



class Registration(View):
    def post(self, request, *args, **kwargs):
        form = ExtendedRegisterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request=request, username=username, password=raw_password)
            login(request, user)
            request.session.set_expiry(30 * 60)
            return redirect('account')
        return render(request, 'registration.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = ExtendedRegisterForm()
        return render(request, 'registration.html', {'form': form})


@login_required
def account(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    else:
        return redirect('profile')


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html",
                  context={"password_reset_form": password_reset_form})


def error_404(request, exception):
    return render(request, '404.html')


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def currencies(request):
    context = {'currencies': []}
    for cur_object in CurrenciesRates.objects.all():
        context['currencies'].append({
            'first_currency': cur_object.first_currency,
            'second_currency': cur_object.second_currency,
            'currency_rate': str(cur_object.current_rate),
            'link': '/currency_rate/' + str(cur_object.second_currency.code) +
                    '/' + str(cur_object.first_currency.code) + '/'
        })
    return render(request, template_name='currencies.html', context=context)

def about(request):
    return render(request, template_name='about.html')

def themes(request):
    pass

def dark_theme(request):
    # JAZZMIN_UI_TWEAKS["dark_mode_theme"]
    # request.session['theme'] = 1
    # return redirect('home')
    pass

def ligth_theme(request):
    # JAZZMIN_UI_TWEAKS["theme"]
    # request.session['theme'] = 0
    # return redirect('home')
    pass