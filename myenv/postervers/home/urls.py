from django.urls import path

from .import views,admin_view,deigner_view,vister_views
from .views import RegistrationView
urlpatterns = [
path('reg', RegistrationView.as_view(), name='registration'),
    path("",views.home,name="index"),
    path("login_page",views.Login_page,name="login_page"),

    path("logout_view",views.logout_view,name='logout_view'),
    path('admin_dash',views.admin_dash,name='admin_dash'),
    path("designer_dash",views.designer_dash,name="designer_dash"),
    path('visiter_dash',views.visiter_dash,name='visiter_dash'),
    #admin
     path("des_view",admin_view.des_view,name = "des_view"),
    path("desinger_approval/<int:id>/",admin_view.desinger_approval,name='desinger_approval'),
    #designer]
    path('payment/',vister_views.payment,name='payment'),
    path('success_payment',vister_views.success_payment,name='success_payment'),
    path('cart_browse_posters/',vister_views.cart_browse_posters,name='cart_browse_posters'),
    path('tasks/', deigner_view.task_list, name='task_list'),
    path('task/<int:task_id>/', deigner_view.task_detail, name='task_detail'),
    path('upload_poster/', deigner_view.upload_poster, name='upload_poster'),
    path('create_task/', deigner_view.create_task, name='create_task'),
    path('browse_posters/', deigner_view.browse_posters, name='browse_posters'),
    path('submit_design_request/', deigner_view.submit_design_request, name='submit_design_request'),
    path('design_requests/', deigner_view.design_requests, name='design_requests'),
    path('search/', deigner_view.search_poster, name='search_poster'),  # URL for the search functionality
    path('poster/<int:pk>/',deigner_view.poster_detail, name='poster_detail'),  # URL for the poster detail page
]