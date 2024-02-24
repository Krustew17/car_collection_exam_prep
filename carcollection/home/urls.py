from django.urls import path

from carcollection.home.views import IndexView, CatalogueView

urlpatterns = (
    path('', IndexView.as_view(), name='home page'),
    path('catalogue/', CatalogueView.as_view(template_name='common/catalogue.html'), name='catalogue'),
)
