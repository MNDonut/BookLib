from django.shortcuts import redirect, render
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect uses 'login' url, not just render page
            # it'll render CustomLoginForm and you don't have to give it as a parameter in 'render
            return redirect('login')
        else:
            return render(request, 'registration.html', {'form': form})

    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)