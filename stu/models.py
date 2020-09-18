import uuid
from enum import auto, Enum

from django.db import models
# Create your models here.

GENDER_CHOICES = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('NOT SPECIFIED', 'not specified'),
]


TITLE_CHOICE = (
    ('MR', 'Mr'),
    ('MRS', 'Mrs'),
    ('MS', 'Ms'),
    ('DR', 'Dr'),
    ('PROF.', 'Prof'),
    ('REV', 'Rev'),
    ('NOT SPECIFIED', 'not specified'),
)

MARITAL_STATUS_CHOICE = (
    ('SINGLE', 'Single'),
    ('MARRIED', 'Married'),
    ('SEPARATED', 'Separated'),
    ('WIDOWED', 'Widowed'),
    ('DIVORCED', 'Divorced'),
    ('NOT SPECIFIED', 'not specified'),
)

PATIENT_CHOICES = (
    ('student', 'Student'),
    ('non student', 'Non Student'),
    ('not specified', 'not specified'),
)


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dept_name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    hod = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.dept_name


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role_name = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.role_name


class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    staff_id = models.CharField(max_length=255, blank=True, null=True, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50, choices=TITLE_CHOICE, default='NOT SPECIFIED')
    surname = models.CharField(max_length=250, blank=True, null=True, help_text='NOTE: Only alphabets allowed')
    other_name = models.CharField(max_length=250, blank=True, null=True, help_text='NOTE: Only alphabets allowed')
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='NOT SPECIFIED')
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICE, default='NOT SPECIFIED')
    phone = models.CharField(max_length=10, blank=True, null=True, unique=True, help_text='NOTE: Only digits allowed')
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True, help_text='NOTE: Only alphabets allowed')
    appointment_date = models.DateField(blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True, help_text='NOTE: Only alphabets allowed')
    position = models.CharField(max_length=250, blank=True, null=True, help_text='NOTE: Only alphabets allowed')
    home_town = models.CharField(max_length=250, blank=True, null=True, help_text='NOTE: Only alphabets allowed')
    email = models.EmailField(max_length=250, blank=True, null=True, unique=True)
    next_of_kin = models.CharField(max_length=250, blank=True, null=True, help_text='NOTE: Only alphabets allowed')
    institution = models.CharField(max_length=250, blank=True, null=True, help_text='NOTE: Only alphabets allowed')
    special_role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.staff_id


class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.CharField(max_length=100, blank=True, null=True)
    patient_id = models.CharField(max_length=100, blank=True, null=True, unique=True)
    nhis_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    nhis_scheme_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True, help_text='NOTE: Only alphabets allowed')
    other_name = models.CharField(max_length=100, blank=True, null=True, help_text='NOTE: Only alphabets allowed')
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='NOT SPECIFIED')
    type_of_patient = models.CharField(max_length=100, choices=PATIENT_CHOICES, default='NOT SPECIFIED')
    dob = models.DateField(auto_now_add=False, null=True, blank=True)
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICE, default='NOT SPECIFIED')
    phone = models.CharField(max_length=10, null=True, blank=False, unique=True, help_text='NOTE: Only digits allowed')
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.patient_id


class DrugInventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    drug_name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    quantity = models.IntegerField(null=True, blank=True, help_text='NOTE: Only digits allowed')
    cost_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=0.00, help_text='NOTE: Only digits allowed')
    selling_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=0.00, help_text='NOTE: Only digits allowed')
    signatory = models.CharField(max_length=255, blank=True, null=True,  help_text='NOTE: Only alphabets allowed')
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.drug_name


class SetupPassword(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    staff_id = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True, help_text='')
    password = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.staff_id


class Billing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    drug = models.ForeignKey(DrugInventory, on_delete=models.CASCADE, blank=True, null=True)
    nhis_number = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    cost_of_service = models.FloatField(default=0.00, help_text='NOTE: for non student only')

    def __str__(self):
        return self.patient


class Lab(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, null=True)
    test_type = models.CharField(max_length=255, null=True, blank=True, help_text='e.g Malaria test, HIV test, etc.')
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=255, null=True, blank=True)
