from django.db import models
from employees.models import Employee

class LoanType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Loan(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])

    def __str__(self):
        return f"Loan for {self.employee.employeeName} ({self.employee.jobTitleID.jobTitle})"

class LoanAttachment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='attachments')
    title = models.CharField(max_length=100, default='Default Title', verbose_name=("Title"))
    attachment = models.FileField(upload_to='loan_attachments/')

    def __str__(self):
        return f"Attachment for Loan: {self.loan.id}"
