from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

from item.models import Category
from item.models import Item

from .forms import SignupForm
from .forms import LoginForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form = SignupForm()
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    else:
        form = SignupForm()

    context = {
        'form': form
    }
    return render(request, 'core/signup.html', context)

def login(request):
    return auth_views.LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm)(request)