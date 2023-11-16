from django.shortcuts import render, redirect, HttpResponse

# все что прописали в models.py, forms.py импортируем в views.py для, того чтобы привезять это все!
from .forms import LoginForm, RegistrationForm
from .models import User, UserProfile, New

# Для регестрации и логаута пользевателей из профеля
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def main_page(request):
    news = New.objects.all()

    return render(request, 'index.html', context={'news': news})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)  # Передайте объект запроса как первый аргумент
                return redirect('/')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', context={'form': form})



# функция регистрации
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()           
            UserProfile.objects.create(user=user)

            return redirect('/login')
            
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')




