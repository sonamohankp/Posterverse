
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def cart_browse_posters(request):
    posters = Poster.objects.all()
    return render(request, 'all_potser.html', {'posters': posters})

def upload_poster(request):
    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cart_browse_posters')  # Redirect to browse posters page after successful upload
    else:
        form = PosterForm()
    return render(request, 'designer/upload_poster.html', {'form': form})

def payment(request):
    posters = Poster.objects.all()
    return render(request,'payment.html', {'posters': posters})
def success_payment(request):
    return render(request,'success_payment.html')
