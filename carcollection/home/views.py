from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.generic.base import ContextMixin

from carcollection.car.models import CarModel
from carcollection.core.utils import get_user_profile


# Create your views here.
# def index(request):
#     profile = get_user_profile()
#     context = {
#         'user_profile': profile,
#     }
#     return render(request, 'common/index.html', context)


# def catalogue(request):
#     profile = get_user_profile()
#     cars = CarModel.objects.all()
#     cars_count = CarModel.objects.all().count()
#     context = {
#         'user_profile': profile,
#         'cars': cars,
#         'cars_count': cars_count,
#     }
#     return render(request, 'common/catalogue.html', context)


class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_profile'] = get_user_profile()
        return context


class CatalogueView(ListView):
    model = CarModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['cars'] = CarModel.objects.all()
        context['user_profile'] = get_user_profile()
        context['cars_count'] = CarModel.objects.all().count()
        return context
