from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model();

# Create your models here.
class ExpertProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	areas_of_expertise = models.ManyToManyField('AreaOfExpertise')
	qualifications = models.TextField(blank=True)

	def __str__(self):
		return self.user.username

class StudentProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	courses_of_expertise = models.ManyToManyField('Course')
	qualifications = models.TextField(blank=True)

	def __str__(self):
		return self.user.username
