from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import VisitorsModel, OurTeamModel, PetsModel, GetInTouchModel
from .forms import GetInTouchForm


class HomePageView(View):
    """Представление главной страницы"""
    def get(self, request):
        return render(request, 'puppy/index.html')

    def post(self):
        pass


class AboutUsView(ListView):
    """Представление страницы About Us"""
    model = VisitorsModel
    template_name = 'puppy/about_us.html'
    context_object_name = 'visitors'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['teammates'] = OurTeamModel.objects.all()
        return context


class ServiceView(View):
    """Представление страницы Service"""
    def get(self, request):
        return render(request, 'puppy/service.html')

    def post(self):
        pass


class PetBoardingView(ListView):
    """Представление страницы Pet Boarding"""
    model = PetsModel
    template_name = 'puppy/pet_boarding.html'
    context_object_name = 'pets'


class ContactView(CreateView):
    """Представление страницы Contact"""
    model = GetInTouchModel
    form_class = GetInTouchForm
    template_name = "puppy/contact.html"
    success_url = "done"


class DoneView(TemplateView):
    """Представление страницы оповещающей об успешной отправке формы"""
    template_name = 'puppy/done.html'











def home(request):
    """Представление страницы редирект на домашнюю страницу :) """
    return HttpResponseRedirect('home')
