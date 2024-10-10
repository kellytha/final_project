from django.contrib import admin
from .models import Experiment, CodingChallenge, UserProgress

# Register your models here.
admin.site.register(Experiment)
admin.site.register(CodingChallenge)
admin.site.register(UserProgress)