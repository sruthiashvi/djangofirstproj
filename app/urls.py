from django.urls import path
from . import views
from . views import TodosListView
from . views import TodosCreateView,TodosDetailView,TodosUpdateView,TodosDeleteView
urlpatterns = [
    #path("admin/", admin.site.urls),
    #path("",include('app.urls')) #new
    #path("",views.home,name="home"),
    path("",TodosListView.as_view(),name="home"),
    path("todo/new",TodosCreateView.as_view(),name="todoscreate"),
    path("todo/<int:pk>/",TodosDetailView.as_view(),name="tododetail"),
    path("todo/<int:pk>/update/",TodosUpdateView.as_view(),name="todosmodel_form"),
    path("todo/<int:pk>/delete",TodosDeleteView.as_view(),name="delete"),
    path("about/",views.about,name="about"),
    path("add",views.add,name="add"),
    path("register",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    #path("delete/",views.delete,name="delete"),
    

]
