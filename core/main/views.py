from django.shortcuts import render

from .models import Category  
from .models import Users

# Create your views here.

def home(request):
    mycategories = Category.objects.all()
    context = {
        'mycategories':mycategories
    }
    return render(request, 'home.html', context)

def user(request):
    myusers = Users.objects.all()
    print('akjhfkjashf')
    context = {
        'myusers':myusers
    }
    return render(request, 'user.html', context)
    