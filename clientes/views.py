from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect


# Create your views here.
@login_required
def list_clientes(request):
    return render(request, 'post/feed.html')

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'user/login.html', {'error': 'Invalid username and password'})

    return render(request, 'user/login.html')