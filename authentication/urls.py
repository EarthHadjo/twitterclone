from django.urls import path
from authentication import views


urlpatterns = [
   path("login/", views.login_view, name="login"),
   path("logout_view/", views.logout_view),

]
