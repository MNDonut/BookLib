from django.shortcuts import redirect, render
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # change to index
            return render(request, 'registration.html', {})
        else:
            return render(request, 'registration.html', {'form': form})

    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)