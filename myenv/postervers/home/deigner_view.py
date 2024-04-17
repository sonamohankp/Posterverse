
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def task_detail(request, task_id):
    task = DesignTask.objects.get(id=task_id)
    if request.method == 'POST':
        form = DesignSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.task = task
            submission.designer = request.user
            submission.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = DesignSubmissionForm()
    return render(request, 'designer/task_details.html', {'task': task, 'form': form})
@login_required
def create_task(request):
    if request.method == 'POST':
        form = DesignTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = DesignTaskForm()
    return render(request, 'designer/create_task.html', {'form': form})



def task_list(request):
    tasks = DesignTask.objects.all()
    return render(request, 'designer/task_list.html', {'tasks': tasks})
def task_detail(request, task_id):
    task = get_object_or_404(DesignTask, id=task_id)
    if request.method == 'POST':
        form = DesignSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.task = task
            submission.designer = request.user
            submission.save()
            
            # Increment the revision count of the task
            task.revision_count += 1
            task.save()
            
            return redirect('task_detail', task_id=task_id)
    else:
        form = DesignSubmissionForm()
    return render(request, 'designer/task_details.html', {'task': task, 'form': form})
@login_required
def browse_posters(request):
    posters = Poster.objects.all()
    return render(request, 'designer/browse_posters.html', {'posters': posters})

def upload_poster(request):
    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('browse_posters')  # Redirect to browse posters page after successful upload
    else:
        form = PosterForm()
    return render(request, 'designer/upload_poster.html', {'form': form})


@login_required
def submit_design_request(request):
    if request.method == 'POST':
        form = DesignRequestForm(request.POST, request.FILES)
        if form.is_valid():
            design_request = form.save(commit=False)
            design_request.user = request.user
            design_request.save()
            return redirect('design_requests')
    else:
        form = DesignRequestForm()
    return render(request, 'designer/submit_design_request.html', {'form': form})

@login_required
def design_requests(request):
    user_requests = DesignRequest.objects.filter(user=request.user)
    return render(request, 'designer/design_requests.html', {'user_requests': user_requests})

def poster_detail(request, pk):
    # Retrieve the poster object with the given primary key (pk)
    poster = get_object_or_404(Poster, pk=pk)
    # Render the template with the poster object
    return render(request, 'designer/poster_detail.html', {'poster': poster})
def search_poster(request):
    if request.method == 'GET':
        title = request.GET.get('title', '')
        if title:
            try:
                # Assuming title is unique, if not, you might want to handle multiple results
                poster = Poster.objects.get(title=title)
                return redirect('poster_detail', pk=poster.pk)  # Redirect to poster detail page
            except Poster.DoesNotExist:
                # Handle case where poster with given title doesn't exist
                return render(request, 'designer/poster_not_found.html')
        else:
            # Handle case where no title is provided
            return render(request, 'designer/search_poster.html')
from django.shortcuts import render, get_object_or_404
from .models import Poster

# @login_required
# def add_to_cart(request, poster_id):
#     poster = Poster.objects.get(pk=poster_id)
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart.posters.add(poster)
#     return redirect('cart')
# @login_required
# def cart(request):
#     cart = Cart.objects.get_or_create(user=request.user)
#     return render(request, 'cart.html', {'cart': cart})