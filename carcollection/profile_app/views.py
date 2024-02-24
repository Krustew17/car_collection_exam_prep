from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from carcollection.car.models import CarModel
from carcollection.core.utils import get_user_profile, get_total_car_sum
from carcollection.profile_app.forms import CreateProfileForm, EditProfileForm
from carcollection.profile_app.models import ProfileModel


# Create your views here.
# def create_profile(request):
#     profile = get_user_profile()
#
#     if request.method == 'GET':
#         form = CreateProfileForm()
#     else:
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('catalogue')
#     context = {
#         'user_profile': profile,
#         'form': form,
#     }
#
#     return render(request, 'profile/profile-create.html', context)

#
# def profile_details(request):
#     profile = get_user_profile()
#     cars = CarModel.objects.all()
#     total_car_sum = get_total_car_sum(cars)
#     context = {
#         'user_profile': profile,
#         'car_sum': total_car_sum,
#     }
#     return render(request, 'profile/profile-details.html', context)
#
#
# def edit_profile(request):
#     profile = get_user_profile()
#     if request.method == 'GET':
#         form = EditProfileForm(instance=profile)
#     else:
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile details')
#     context = {
#         'user_profile': profile,
#         'form': form
#     }
#     return render(request, 'profile/profile-edit.html', context)


# def delete_profile(request):
#     profile = get_user_profile()
#     cars = CarModel.objects.all()
#     if request.method == 'POST':
#         profile.delete()
#         cars.delete()
#         return redirect('home page')
#     context = {
#         'user_profile': profile,
#     }
#     return render(request, 'profile/profile-delete.html', context)


class CreateProfileView(CreateView):
    model = ProfileModel
    form_class = CreateProfileForm
    success_url = reverse_lazy('home page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_profile'] = get_user_profile()
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class DetailsProfileView(View):
    def get(self, request):
        profile = get_user_profile()
        cars = CarModel.objects.all()
        total_car_sum = get_total_car_sum(cars)
        context = {
            'user_profile': profile,
            'car_sum': total_car_sum,
        }
        return render(request, 'profile/profile-details.html', context)


class EditProfileView(UpdateView):
    profile = get_user_profile()
    model = ProfileModel
    form_class = EditProfileForm
    template_name = 'profile/profile-edit.html'

    def get_object(self, queryset=None):
        return ProfileModel.objects.all().first()

    def get_success_url(self):
        return reverse_lazy('profile details')


class DeleteProfileView(DeleteView):
    model = CarModel
    template_name = 'profile/profile-delete.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return ProfileModel.objects.all().first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = get_user_profile()
        return context
