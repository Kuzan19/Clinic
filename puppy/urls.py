from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home),
    path('home', views.HomePageView.as_view()),
    path('about_us', views.AboutUsView.as_view(), name='about_page'),
    path('service', views.ServiceView.as_view()),
    path('contact', views.ContactView.as_view(), name='contact_page'),
    path('pet_boarding', views.PetBoardingView.as_view(), name='pet_board_page'),
    path('done', views.DoneView.as_view(), name='done_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
