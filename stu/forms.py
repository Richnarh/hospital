from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from .models import DrugInventory, Department, Staff, Role, Patient, Billing, Lab


SetupPassword = get_user_model()


TITLE_CHOICE = (
    ('MR', 'Mr'),
    ('MRS', 'Mrs'),
    ('MS', 'Ms'),
    ('DR', 'Dr'),
    ('PROF.', 'Prof'),
    ('REV', 'Rev'),
    ('NOT SPECIFIED', 'not specified'),
)

GENDER_CHOICES = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('NOT SPECIFIED', 'not specified'),
]


MARITAL_STATUS_CHOICE = (
    ('SINGLE', 'Single'),
    ('MARRIED', 'Married'),
    ('SEPARATED', 'Separated'),
    ('WIDOWED', 'Widowed'),
    ('DIVORCED', 'Divorced'),
    ('NOT SPECIFIED', 'not specified'),
)

PATIENT_CHOICES = (
    ('STUDENT', 'Student'),
    ('NON_STUDENT', 'Non Student'),
    ('NOT SPECIFIED', 'not specified'),
)


class DrugInventoryForm(ModelForm):
    drug_name = forms.CharField(
        widget=forms.widgets.TextInput(attrs={"placeholder": "Enter drug name"}), label=False, required=False
    )
    quantity = forms.DecimalField(
        widget=forms.widgets.TextInput(attrs={'pattern': '[0-9]+', 'placeholder': 'Only digits allowed.'}), label=False
    )
    cost_price = forms.DecimalField(
        widget=forms.widgets.TextInput(attrs={'pattern': '[0-9]+', 'placeholder': 'Only digits allowed.'}), label=False, required=False
    )
    selling_price = forms.IntegerField(
        widget=forms.widgets.TextInput(attrs={'pattern': '[0-9]+', 'placeholder': 'Only digits allowed.'}), label=False, required=False
    )
    signatory = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'pattern': '[A-Za-z ]+', 'placeholder': 'Only alphabets allowed.'}), label=False, required=False
    )
    remark = forms.CharField(
        widget=forms.Textarea(), label=False, required=False
    )

    class Meta:
        model = DrugInventory
        exclude = ['id', 'date']


class DepartmentForm(ModelForm):
    dept_name = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'required': True}), label=False
    )
    hod = forms.CharField(
        widget=forms.widgets.TextInput(), label=False
    )

    class Meta:
        model = Department
        exclude = ['id']

# 'pattern':'[A-Za-z ]+' validate to take alphabet only


class StaffForm(ModelForm):
    class Meta:
        model = Staff

        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'appointment_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'email': forms.EmailInput(),
            'phone': forms.TextInput(attrs={'pattern': '[0-9]+'}),
            'surname': forms.TextInput(attrs={'pattern': '[A-Za-z ]+'}),
            'other_name': forms.TextInput(attrs={'pattern': '[A-Za-z ]+'}),
            'nationality': forms.TextInput(attrs={'pattern': '[A-Za-z ]+'}),
            'home_town': forms.TextInput(attrs={'pattern': '[A-Za-z ]+'}),
            'qualification': forms.TextInput(attrs={'pattern': '[A-Za-z ]+'}),
            'position': forms.TextInput(attrs={'pattern': '[A-Za-z ]+'}),
            'next_of_kin': forms.TextInput(attrs={'pattern': '[A-Za-z ]+'}),
            'institution': forms.TextInput(attrs={'pattern': '[A-Za-z ]+'})
        }

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        self.fields['department'].required = True
        self.fields['special_role'].required = True
        self.fields['staff_id'].required = True

        self.fields['department'].empty_label = 'Choose...'
        self.fields['special_role'].empty_label = 'Choose...'


class PatientForm(ModelForm):
    class Meta:
        model = Patient

        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'phone': forms.TextInput(attrs={'pattern': '[0-9]+'}),
            'surname': forms.TextInput(attrs={'pattern': '[A-Za-z ]+'}),
            'other_name': forms.TextInput(attrs={'pattern': '[A-Za-z ]+'}),
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['patient_id'].required = True
        self.fields['gender'].required = True
        self.fields['phone'].required = True
        self.fields['address'].required = True
        self.fields['type_of_patient'].required = True


class RoleForm(ModelForm):
    role_name = forms.CharField(
        widget=forms.widgets.TextInput(), label=False
    )

    class Meta:
        model = Role
        exclude = ['id']


# class SetupPasswordForm(ModelForm):
#     class Meta:
#         model = SetupPassword
#         fields = '__all__'
#
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
#             'password': forms.PasswordInput(attrs={'placeholder': 'Enter password'})
#         }
#
#     def __init__(self, *args, **kwargs):
#         super(SetupPasswordForm, self).__init__(*args, **kwargs)
#         self.fields['username'].required = True
#         self.fields['username'].label = ''
#
#         self.fields['password'].required = True
#         self.fields['password'].label = ''


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLoginForm(forms.Form):
    class Meta:
        model = User
        help_texts = {
            'username': None,
        }

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean(self, *args, **kwargs):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #
    #     if username and password:
    #         user = authenticate(username=username, password=password)
    #         if not user:
    #             raise forms.ValidationError('this user does not exist')
    #         if not user.check_password(password):
    #             raise forms.ValidationError('incorrect password')
    #         if not user.is_active:
    #             raise forms.ValidationError('this user is not active')
    #     return super(UserLoginForm, self).clean(*args, **kwargs)


class BillingForm(ModelForm):
    class Meta:
        model = Billing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BillingForm, self).__init__(*args, **kwargs)
        self.fields['patient'].empty_label = 'Choose...'
        self.fields['patient'].required = True
        self.fields['drug'].required = False
        self.fields['drug'].empty_label = 'Choose...'
        self.fields['cost_of_service'].required = False


class LabForm(ModelForm):
    class Meta:
        model = Lab
        fields = '__all__'

        widgets = {
            'description': forms.TextInput()
        }

    def __init__(self, *args, **kwargs):
        super(LabForm, self).__init__(*args, **kwargs)
        self.fields['patient'].empty_label = 'Choose...'
        self.fields['patient'].required = True
        self.fields['staff'].required = True
        self.fields['staff'].empty_label = 'Choose...'
        self.fields['test_type'].required = True
