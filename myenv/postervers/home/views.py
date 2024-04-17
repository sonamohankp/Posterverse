from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import *
# Create your views here.
from django.views import View

from .forms import LoginRegister, UsersRegister,DesignerRegister


# def home(request):
#     return render(request,'test.html')

def home(request):
    return render(request,'index.html')

def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        print(password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:

                return redirect('admin_dash')
            elif user.is_users:

                return redirect('visiter_dash')



            elif user.is_company:
                user_profile = user.company.get()

                if user_profile.status:
                    return redirect('designer_dash')
                else:
                    messages.info(request, 'Waiting for admin approval')

                # return redirect('company_dash')


        else:
            messages.info(request, 'Invalid Credentials')
    return render(request,'Login.html')

def admin_dash(request):
    return render(request,'admin_dash.html')

def designer_dash(request):
    return render(request,'designer_dash.html')


def visiter_dash(request):
    return render(request,'vister_dash.html')


class RegistrationView(View):
    def get(self, request):
        user = LoginRegister()
        users_form = UsersRegister()

        cmp_form = DesignerRegister()
        return render(request,'register.html', {"user": user, "users_form": users_form,
                                            "cmp_form": cmp_form})

    def post(self,request):
        user = LoginRegister(request.POST)
        users_form = UsersRegister(request.POST)

        cmp_form = DesignerRegister(request.POST)

        if user.is_valid() and users_form.is_valid():

            a = user.save(commit=False)
            print(a)
            a.is_users = True
            a.save()
            user1 = users_form.save(commit=False)
            print(user1)
            user1.user = a
            user1.save()
            return redirect('login_page')

        elif user.is_valid() and cmp_form.is_valid():
            print("2")
            a = user.save(commit=False)
            a.is_company = True
            a.save()
            user1 = cmp_form.save(commit=False)
            user1.user = a
            user1.save()
            return redirect('login_page')

        return render(request, 'register.html',  {"user": user, "users_form": users_form,
                                             "cmp_form": cmp_form})




def logout_view(request):
    logout(request)
    return redirect('login_page')

def browse_posters(request):
    posters = Poster.objects.all()
    return render(request, 'designer/browse_posters.html', {'posters': posters})