from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", _("Student")
        EXPERT = "EXPERT", _("Expert")

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    # Common fields for both Student and Expert
    groups = models.ManyToManyField( Group, related_name="muser_groups")
    user_permissions = models.ManyToManyField( Permission, related_name="muser_permissions")
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    programme = models.CharField(max_length=50, blank=True)
    school = models.CharField(max_length=100, blank=True)
    courses = models.CharField(max_length=200, blank=True)

class Expert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    programme_of_expertise = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField(default=0)
    courses = models.TextField(blank=True)
    verified = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
