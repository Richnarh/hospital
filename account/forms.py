from django.forms import ModelForm
from stu.models import SetupPassword


class loginForm(ModelForm):
    class Meta:
        model = SetupPassword

        fields = '__all__'
        labels = {
            'staff_id': '',
            'password': ''
        }

    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)
