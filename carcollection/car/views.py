from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from carcollection.car.forms import CreateCarForm, EditCarForm, DeleteCarForm
from carcollection.car.models import CarModel
from carcollection.core.utils import get_user_profile
from django.views import View


# Create your views here.
# def create_car(request):
#     profile = get_user_profile()
#     if request.method == 'GET':
#         form = CreateCarForm()
#     else:
#         form = CreateCarForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('catalogue')
#     context = {
#         'user_profile': profile,
#         'form': form,
#     }
#     return render(request, 'car/car-create.html', context)


# def car_details(request, pk):
#     profile = get_user_profile()
#     car = CarModel.objects.filter(pk=pk).get()
#     context = {
#         'user_profile': profile,
#         'car': car,
#     }
#     return render(request, 'car/car-details.html', context)

class CreateCar(CreateView):
    model = CarModel
    form_class = CreateCarForm
    template_name = 'car/car-create.html'
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        profile = get_user_profile()
        context = super().get_context_data(**kwargs)
        context['user_profile'] = profile
        return context


class CarDetails(DetailView):
    model = CarModel
    template_name = 'car/car-details.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        profile = get_user_profile()
        context = super().get_context_data(**kwargs)
        context['user_profile'] = profile
        return context


class EditCar(UpdateView):
    model = CarModel
    form_class = EditCarForm
    template_name = 'car/car-edit.html'
    context_object_name = 'car'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        profile = get_user_profile()
        context = super().get_context_data(**kwargs)
        context['user_profile'] = profile
        return context

    def get_success_url(self):
        return reverse_lazy('details car', kwargs={'pk': self.object.pk})


class DeleteCar(DeleteView):
    model = CarModel
    pk_url_kwarg = 'pk'
    template_name = 'car/car-delete.html'
    success_url = reverse_lazy('catalogue')

# def edit_car(request, pk):
#     profile = get_user_profile()
#     car = CarModel.objects.filter(pk=pk).get()
#     if request.method == 'GET':
#         form = EditCarForm(instance=car)
#     else:
#         form = EditCarForm(request.POST, instance=car)
#         if form.is_valid():
#             form.save()
#             return redirect('details car', pk=pk)
#     context = {
#         'user_profile': profile,
#         'pk': pk,
#         "form": form,
#     }
#     return render(request, 'car/car-edit.html', context)

#
# def delete_car(request, pk):
#     profile = get_user_profile()
#     car = CarModel.objects.filter(pk=pk).get()
#     if request.method == 'GET':
#         form = DeleteCarForm(instance=car)
#     else:
#         form = DeleteCarForm(request.POST, instance=car)
#         if form.is_valid():
#             form.save()
#             return redirect('catalogue')
#     context = {
#         'user_profile': profile,
#         'form': form,
#     }
#     return render(request, 'car/car-delete.html', context)
