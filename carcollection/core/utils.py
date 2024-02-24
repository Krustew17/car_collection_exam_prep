from django.core.exceptions import ValidationError

from carcollection.profile_app.models import ProfileModel


def validate_year(min_year, max_year, value):
    if value < min_year or value > max_year:
        raise ValidationError("Year must be between 1980 and 2049")


def get_user_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist:
        return


class DisableFields:
    disabled_fields = ()
    fields = {}

    def _disable_fields(self):
        if self.disabled_fields == "__all__":
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for field in fields:
            if field in self.fields:
                field = self.fields[field]
                field.widget.attrs['readonly'] = 'readonly'


def get_total_car_sum(cars):
    return sum(x.price for x in cars)
