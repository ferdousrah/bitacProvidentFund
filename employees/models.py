from django.db import models

class Organization(models.Model):
    organizationID = models.AutoField(primary_key=True)
    organizationName = models.CharField(max_length=100, verbose_name="প্রতিষ্ঠানের নাম")

    def __str__(self):
        return self.organizationName

class Section(models.Model):
    sectionID = models.AutoField(primary_key=True)
    organizationID = models.ForeignKey(Organization, on_delete=models.CASCADE)
    sectionName = models.CharField(max_length=100, verbose_name="শাখার নাম")

    def __str__(self):
        return self.sectionName

class JobTitle(models.Model):
    jobTitleID = models.AutoField(primary_key=True)
    jobTitle = models.CharField(max_length=100, verbose_name="পদবীর নাম")

    def __str__(self):
        return self.jobTitle


class SalaryGrade(models.Model):
    gradeID = models.AutoField(primary_key=True)
    gradeTitle = models.CharField(max_length=100, verbose_name="বেতন স্কেল")

class Employee(models.Model):
    employeeID = models.AutoField(primary_key=True)
    employeeName = models.CharField(max_length=100, verbose_name="নাম")
    nationalID = models.CharField(max_length=20, verbose_name="জাতীয় পরিচয়পত্র নম্বর")
    employeeNo = models.CharField(max_length=20, verbose_name="কর্মচারী নম্বর")
    jobTitleID = models.ForeignKey(JobTitle, on_delete=models.CASCADE, verbose_name="পদবী")
    memorialNo = models.CharField(max_length=20, verbose_name="স্মারক নং")
    employmentType = models.IntegerField(choices=((1, 'কর্মকর্তা'), (2, 'কর্মচারী'), (3, 'পি আর এল')), verbose_name="চাকরির ধরন", default=1)
    dateOfBirth = models.DateField(verbose_name="জন্ম তারিখ")
    joiningDate = models.DateField(verbose_name="যোগদানের তারিখ")
    email = models.EmailField(max_length=100, verbose_name="ইমেইল")
    mobileNo = models.CharField(max_length=20, verbose_name="মোবাইল নম্বর")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="ফটো")
    organizationID = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="প্রতিষ্ঠান")
    sectionID = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="শাখা")
    gradeID = models.ForeignKey(SalaryGrade, on_delete=models.CASCADE, verbose_name="বেতন স্কেল")
    gpfAccountNo = models.CharField(max_length=20, verbose_name="জিপিএফ হিসাব নম্বর")
    basicSalary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="মূল বেতন")
    epfPercent = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="ইপিএফ শতকরা")
    cpfPercent = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="সিপিএফ শতকরা")
    displayOrder = models.IntegerField(verbose_name="ডিসপ্লে অর্ডার")
    employmentStatus = models.IntegerField(choices=((1, 'চাকরিজীবী'), (2, 'পিআরএল'), (3, 'অবসরপ্রাপ্ত'), (0, 'নিষ্ক্রিয়')), verbose_name="কর্মসংস্থানের অবস্থা")
