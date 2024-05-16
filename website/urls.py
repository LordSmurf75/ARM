from django.urls import path, include
from . import views
from .views import slet_koncert, band_list

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('about/', views.about, name="about"),
    path('bestyrelse/<int:pk>', views.bestyrelse, name="bestyrelse"),
    path('spillede_koncerter/', views.spillede_koncerter, name='spillede_koncerter'),
    path('frivillig/', views.frivillig, name='frivillig'),
    path('vagter/<int:pk>', views.vagter, name='vagter'),
    path('opret_koncert', views.opret_koncert, name='opret_koncert'),
    path('opret_spillested', views.opret_spillested, name='opret_spillested'),
    path('slet/<int:koncert_id>/', slet_koncert, name='slet_koncert'),
    path('rediger_koncert/<int:pk>', views.rediger_koncert, name='rediger_koncert'),
    path('bands/', band_list, name='band_list'),
    path('spillesteder', views.spillested, name='spillesteder'),
]
