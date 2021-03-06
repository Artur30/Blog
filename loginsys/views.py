from django.shortcuts import render, render_to_response, redirect, reverse
from django.contrib import auth
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from loginsys.forms import UserRegisterForm


def login(request):
    """
    Function for logging in
    :param request:
    :return:
    """
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse('article:articles'))
        else:
            args['login_error'] = 'Пользователь не найден'
            return render_to_response('login.html', args)
    else:
        return render(request, 'loginsys/login.html', args)


def logout(request):
    """
    Function for logging out
    :param request:
    :return:
    """
    auth.logout(request)
    return redirect(reverse('article:articles'))


def register(request):
    """
    Function for register user
    :param request:
    :return:
    """
    args = {}
    args.update(csrf(request))
    args['form'] = UserRegisterForm()
    if request.POST:
        new_user_form = UserRegisterForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(
                username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password1'],
                first_name=new_user_form.cleaned_data['first_name'], last_name=new_user_form.cleaned_data['last_name'],
                email=new_user_form.cleaned_data['email']
            )
            auth.login(request, new_user)
            return redirect(reverse('article:articles'))
        else:
            args['form'] = new_user_form
    return render(request, 'loginsys/register.html', args)

