from django.contrib import admin
from app.models import Company , Employee
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','about','about','added_data','active')
    search_fields=('name','location','added_data')
admin.site.register(Company,CompanyAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','about','designation','company')
    list_filter=('company',)
admin.site.register(Employee,EmployeeAdmin)
