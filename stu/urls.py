from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('', views.logout_view, name='logout'),

    # INDEX PAGE
    path('index/', views.index, name='stu'),

    # STAFF CRUD
    path('staff/staff', views.staff, name='staff'),
    path('staff/staff-update/<id>', views.staff, name='update_staff'),
    path('staff/staff-delete/<id>', views.staff_delete, name='delete_staff'),
    path('staff/staff-list', views.staff_list, name='staff_list'),

    path('register', views.register, name='register'),

    path('patient/patient', views.patient, name='patient'),
    path('patient/patient-update/<id>', views.patient, name='patient_update'),
    path('patient/delete-patient/<id>', views.delete_patient, name='patient_delete'),
    path('shared/patient-list', views.patient_list, name='patient_list'),

    # DEPARTMENT CRUD
    path('shared/department', views.department, name='department'),
    path('shared/dept-update/<id>', views.department, name='dept-update'),
    path('shared/dept-delete/<id>', views.delete_department, name='dept-delete'),
    path('shared/department-list', views.department_list, name='department_list'),

    # ROLE CRUD
    path('shared/role', views.role, name='role'),
    path('shared/role-update/<id>', views.role, name='role-update'),
    path('shared/role-delete/<id>', views.delete_role, name='role-delete'),
    path('shared/role-list', views.role_list, name='role_list'),

    # INVENTORY CRUD
    path('druginventory/druginventory', views.drug_inventory, name='druginventory'),
    path('druginventory/update/<id>', views.drug_inventory, name='update'),
    path('druginventory/delete/<id>', views.drug_inventory_delete, name='delete'),
    path('druginventory/druginventory-list', views.drug_inventory_list, name='druginventory_list'),

    # BILLING
    path('billing/billing', views.billing, name='billing'),
    path('billing/edit-bill/<id>', views.billing, name='update_bills'),
    path('billing/delete-bill/<id>', views.delete_bills, name='delete_bills'),
    path('billing/list', views.billing_list, name='billing_list'),

    # LAB
    path('lab/lab', views.lab, name='lab'),
    path('lab/edit-lab/<id>', views.lab, name='update_lab'),
    path('lab/delete-lab/<id>', views.delete_bills, name='delete_lab'),
    path('lab/list', views.lab_list, name='lab_list'),
]
