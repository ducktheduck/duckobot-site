
from django.contrib import admin
from django.urls import path
from Stats.views import home_view, login_page, spotify_page

urlpatterns = [
    path('', home_view, name = "home"),
    path('login/', login_page, name = "login"),
    path('spotify/', spotify_page, name = "spotify"),
    path('admin/', admin.site.urls),
]

