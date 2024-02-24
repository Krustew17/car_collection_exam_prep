from django.urls import path

from carcollection.profile_app.views import CreateProfileView, \
    DetailsProfileView, EditProfileView, DeleteProfileView

urlpatterns = (
    path('create/', CreateProfileView.as_view(template_name='profile/profile-create.html'), name='create profile'),
    path('details/', DetailsProfileView.as_view(), name='profile details'),
    path('delete/', DeleteProfileView.as_view(), name='delete profile'),
    path('edit/', EditProfileView.as_view(), name='edit profile')
)
