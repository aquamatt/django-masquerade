from django import forms
from django.conf import settings

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
USERNAME_FIELD = getattr(settings, 'MASQUERADE_USERNAME_FIELD', 'username')


class MaskForm(forms.Form):
    mask_user = forms.CharField(max_length=75, label="Username")

    def clean_mask_user(self):
        username = self.cleaned_data['mask_user']
        try:
            kwargs = {USERNAME_FIELD: username}
            u = User.objects.get(**kwargs)
        except User.DoesNotExist:
            raise forms.ValidationError("Invalid username")
        return username
