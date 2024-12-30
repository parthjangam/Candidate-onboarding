from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=255,blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255,blank=True, null=True)
    permanent_address = models.CharField(max_length=255, blank=True, null=True)
    current_address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50,blank=True, null=True)
    passport = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=15,blank=True, null=True)
    pan_no = models.CharField(max_length=50, blank=True, null=True)
    visa = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=255,blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=15,blank=True, null=True)
    relocation_availability = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
