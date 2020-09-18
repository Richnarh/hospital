from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import *
from .models import *


# @unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user_group = request.POST.get('group_name')

        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')

            print('Username: ', username, '\n Password: ', password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:

                login(request, user)
                return redirect('/index')
            else:
                messages.error(request, 'Incorrect username or password')
                return redirect('/')
    form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
# @admin_only
def index(request):
    return render(request, 'index.html')


@login_required
# #(allowed_roles=['Physician'])
def staff(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = StaffForm()
        else:
            obj = Staff.objects.get(pk=id)
            form = StaffForm(instance=obj)
        return render(request, 'staff/staff.html', {'form': form})
    else:
        if id == 0:
            form = StaffForm(request.POST)
            print("Init()")
        else:
            obj = Staff.objects.get(pk=id)
            form = StaffForm(request.POST, instance=obj)
            # print("First instance: Obj "+obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Action successful!')
        return redirect('staff_list')


@login_required
# #(allowed_roles=['Physician'])
def staff_delete(request, id):
    staffObj = Staff.objects.get(id=id)
    staffObj.delete()
    messages.info(request, 'Staff deleted successfully!')
    return redirect('staff_list')


@login_required
# #(allowed_roles=['Physician'])
def staff_list(request):
    return render(request, 'staff/staff_list.html', {'staff_list': Staff.objects.all()})


# def setup_password(request):
#     if request.method == 'POST':
#         staff_id = request.POST['staff_id']
#         password = request.POST['password']
#         # data = SetupPassword(staff_id=staff_id, password=password)
#         if Staff.objects.filter(staff_id=staff_id).exists():
#             if SetupPassword.objects.filter(staff_id=staff_id).exists():
#                 SetupPassword.objects.update(
#                     staff_id=staff_id,
#                     password=password
#                 )
#                 messages.info(request, 'Password updated successfully!')
#                 return redirect('setup_password')
#
#             setup_password_el = SetupPassword.objects.create(
#                 staff_id=staff_id,
#                 password=password
#             )
#             setup_password_el.save()
#             messages.info(request, 'Password saved successfully!')
#             return redirect('setup_password')
#         else:
#             messages.warning(request, 'Please this staff ID does not exist')
#             return redirect('setup_password')
#     else:
#         return render(request, 'register.html')
# @login_required
# def setup_password(request, id=0):
#     if request.method == 'GET':
#         if id == 0:
#             form = SetupPasswordForm()
#         else:
#             obj = SetupPassword.objects.get(pk=id)
#             form = SetupPasswordForm(instance=obj)
#         return render(request, 'register.html', {'form': form})
#     else:
#         if id == 0:
#             form = SetupPasswordForm(request.POST)
#         else:
#             obj = SetupPassword.objects.get(pk=id)
#             form = SetupPasswordForm(request.POST, instance=obj)
#
#         if form.is_valid():
#
#             staff_id = form.cleaned_data.get('staff_id')
#             password = form.cleaned_data.get('password')
#
#             if Staff.objects.filter(staff_id=staff_id).exists():
#                 if SetupPassword.objects.filter(staff_id=staff_id).exists():
#                     SetupPassword.objects.update(staff_id=staff_id, password=password)
#                     messages.success(request, 'Password updated!')
#                     return redirect('setup_password')
#                 form.save()
#                 messages.success(request, 'Action successful!')
#             else:
#                 messages.error(request, 'The entered staff ID does not exist')
#         return render(request, 'register.html', {'form': form})


@unauthenticated_user
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Pharmacist')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    else:
        return render(request, 'users/register.html', {'form': form})


@login_required
#(allowed_roles=['Physician'])
def patient(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = PatientForm()
        else:
            obj = Patient.objects.get(pk=id)
            form = PatientForm(instance=obj)
        return render(request, 'patient/patient.html', {'form': form})
    else:
        if id == 0:
            form = PatientForm(request.POST)
        else:
            obj = Patient.objects.get(pk=id)
            form = PatientForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Action successful!')

        return render(request, 'patient/patient.html', {'form': form})


@login_required
def patient_list(request):
    return render(request, 'patient/patient_list.html', {'patient_list': Patient.objects.all()})


@login_required
#(allowed_roles=['Physician'])
def delete_patient(request, id):
    patients = Patient.objects.get(id=id)
    patients.delete()
    messages.info(request, 'Patient deleted successfully!')
    return redirect('patient_list')


@login_required
#(allowed_roles=['Physician'])
def department(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = DepartmentForm()
        else:
            dept = Department.objects.get(pk=id)
            form = DepartmentForm(instance=dept)
        return render(request, 'shared/department.html', {'form': form})
    else:
        if id == 0:
            form = DepartmentForm(request.POST)
        else:
            dept = Department.objects.get(pk=id)
            form = DepartmentForm(request.POST, instance=dept)
        if form.is_valid():
            form.save()
            messages.success(request, 'Action successful!')
        return redirect('department_list')


@login_required
#(allowed_roles=['Physician'])
def delete_department(request, id):
    drug = Department.objects.get(pk=id)
    drug.delete()
    messages.success(request, 'Action successful!')
    return redirect('department_list')


@login_required
#(allowed_roles=['Physician'])
def department_list(request):
    return render(request, 'shared/department_list.html', {'department_list': Department.objects.all()})


@login_required
#(allowed_roles=['Physician'])
def role(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = RoleForm()
        else:
            obj = Role.objects.get(pk=id)
            form = RoleForm(instance=obj)
        return render(request, 'shared/role.html', {'form': form})
    else:
        if id == 0:
            form = RoleForm(request.POST)
        else:
            obj = Role.objects.get(pk=id)
            form = RoleForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Action successful!')
        return redirect('role_list')


@login_required
#(allowed_roles=['Physician'])
def role_list(request):
    return render(request, 'shared/role_list.html', {'role_list': Role.objects.all()})


@login_required
#(allowed_roles=['Physician'])
def delete_role(request, id):
    roles = Role.objects.get(pk=id)
    roles.delete()
    messages.success(request, 'Action successful!')
    return redirect('role_list')


@login_required
#(allowed_roles=['Pharmacist'])
def drug_inventory(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = DrugInventoryForm()
        else:
            drug = DrugInventory.objects.get(pk=id)
            form = DrugInventoryForm(instance=drug)
        return render(request, 'druginventory/druginventory.html', {'form': form})
    else:
        if id == 0:
            form = DrugInventoryForm(request.POST)
        else:
            drug = DrugInventory.objects.get(pk=id)
            form = DrugInventoryForm(request.POST, instance=drug)
        if form.is_valid():
            form.save()
            messages.success(request, 'Action successful!')
        return redirect('druginventory_list')


@login_required
#(allowed_roles=['Pharmacist'])
def drug_inventory_delete(request, id):
    drug = DrugInventory.objects.get(pk=id)
    drug.delete()
    messages.success(request, 'Action successful!')
    return redirect('druginventory_list')


@login_required
#(allowed_roles=['Pharmacist'])
def drug_inventory_list(request):
    return render(request, 'druginventory/druginventory_list.html', {'druginventory_list': DrugInventory.objects.all()})


@login_required
#(allowed_roles=['Accountant'])
def billing(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = BillingForm()
        else:
            obj = Billing.objects.get(pk=id)
            form = BillingForm(instance=obj)
        return render(request, 'billing/billing.html', {'form': form})
    else:
        if id == 0:
            form = BillingForm(request.POST)
        else:
            obj = Billing.objects.get(pk=id)
            form = BillingForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Action successful!')
        return redirect('billing_list')


@login_required
#(allowed_roles=['Accountant'])
def billing_list(request):
    return render(request, 'billing/billing_list.html', {'billing': Billing.objects.all()})


@login_required
#(allowed_roles=['Accountant'])
def delete_bills(request, id):
    bill = Billing.objects.get(pk=id)
    bill.delete()
    messages.success(request, 'Action successful!')
    return redirect('billing_list')


@login_required
#(allowed_roles=['Physician'])
def lab(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = LabForm()
        else:
            obj = Lab.objects.get(pk=id)
            form = LabForm(instance=obj)
        return render(request, 'lab/lab.html', {'form': form})
    else:
        if id == 0:
            form = LabForm(request.POST)
        else:
            obj = Lab.objects.get(pk=id)
            form = LabForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Action successful!')
        return render(request, 'lab/lab.html', {'form': form})


@login_required
#(allowed_roles=['Physician'])
def lab_list(request):
    return render(request, 'lab/lab_list.html', {'lab': Lab.objects.all()})


@login_required
#(allowed_roles=['Physician'])
def delete_lab(request, id):
    _lab = Lab.objects.get(pk=id)
    _lab.delete()
    messages.success(request, 'Action successful!')
    return redirect('lab_list')


@login_required
def logout_view(request):
    logout(request)
    print('logout triggered')
    return redirect('/')
