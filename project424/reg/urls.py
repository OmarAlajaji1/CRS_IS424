from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name= "reg" 



urlpatterns=[
    path('',views.index, name='index'),
    path("login",views.login_view,name="login_view"),
    path("signup",views.signup,name="signup"),
    path('<str:cid>/display',views.display , name='display'),
    path('<str:cid>/add',views.add , name='add'),
    path('update',views.update,name='update'),
    path('<str:cid>/remove',views.remove , name='remove'),
    path("logout", views.logout_view, name="logout_view")

]

urlpatterns += staticfiles_urlpatterns()

