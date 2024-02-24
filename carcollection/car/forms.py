from django import forms

from carcollection.car.models import CarModel
from carcollection.core.utils import DisableFields


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = "__all__"


class CreateCarForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(DisableFields, BaseCarForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    class Meta:

        model = CarModel
        fields = "__all__"

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance
