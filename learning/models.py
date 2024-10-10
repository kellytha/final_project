from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Experiment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class CodingChallenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    challenge= models.ForeignKey(CodingChallenge, on_delete=models.CASCADE)
    completed= models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.experiment.title} / {self.challenge.title}'
    


class MyModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
