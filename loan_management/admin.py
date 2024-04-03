# admin.py in loan app
from django.utils.safestring import mark_safe

from django.contrib import admin
from .models import Loan, LoanType, LoanAttachment

from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

class LoanAttachmentInline(admin.TabularInline):
    model = LoanAttachment
    extra = 1  # Number of extra empty forms to display


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):    
    list_display = ('get_employee_photo', 'employee_name', 'loan_type', 'amount', 'interest_rate', 'start_date', 'end_date', 'status')
    search_fields = ('employee__employeeName',)
    list_filter = (
        ('loan_type__name', DropdownFilter),
        #('jobTitleID__jobTitle', DropdownFilter),
        ('status', ChoiceDropdownFilter),
    )

    def get_employee_photo(self, obj):
        return mark_safe(f'<img src="{obj.employee.photo.url}" width="50" height="50" />')
    get_employee_photo.short_description = 'Photo'

    def employee_name(self, obj):
        return obj.employee.employeeName
    employee_name.short_description = 'Employee Name'

    class Media:
        css = {
            'all': ('admin_custom.css',),  # Path to your custom CSS file
        }
    inlines = [LoanAttachmentInline]

@admin.register(LoanType)
class LoanTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(LoanAttachment)
