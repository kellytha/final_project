from django.shortcuts import render, redirect
from .models import Experiment, CodingChallenge
import random
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# Create your views here.
def index(request):
    experiments = Experiment.objects.all()
    coding_challenges = CodingChallenge.objects.all()

    if experiments and coding_challenges:
        experiment = random.choice(experiments)
        coding_challenge = random.choice(coding_challenges)
    else:
        experiment = coding_challenge = None 

    context = {
        'experiment': experiment,
        'coding_challenge': coding_challenge
    }

    return render(request, 'learning/index.html', context) 

def profile(request):
    return render(request, 'learning/profile.html')

experiments_data = [
    {'title': 'Experiment 1', 'description': 'Description of Experiment 1'},
    {'title': 'Experiment 2', 'description': 'Description of Experiment 2'}
]

coding_challenges_data = [
    {'title': 'Challenge 1', 'description': 'Description of Challenge 1'},
    {'title': 'Challenge 2', 'description': 'Description of Challenge 2'}
]

from django.shortcuts import render
from .models import Experiment

def experiments_view(request):
    experiments = Experiment.objects.all() 
    return render(request, 'learning/index.html', {'experiments': experiments})


def coding_challenges_view(request):
    coding_challenges = CodingChallenge.objects.all()  
    return render(request, 'learning/codingchallenges.html', {'coding_challenges': coding_challenges})

@login_required
def  complete_progress(request, experiment_id, challenge_id):
    experiment = Experiment.objects.get(id=experiment_id)
    challenge = CodingChallenge.objects.get(id=challenge_id)

    UserProgress.object.get_or_create(
        user=request.user,
        experiment=experiment,
        challenge=challenge
    )

    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'learning/register.html', {'form': form})

    

def profile(request):
    
    stem_resources = [
        {'title': 'Khan Academy', 'description': 'Free online courses, lessons, and practice in math, science, computer programming, history, art history, economics, and more.'},
        {'title': 'Coursera', 'description': 'Online courses from top universities and organizations worldwide.'},
        {'title': 'edX', 'description': 'Offers free online courses from universities like Harvard and MIT.'},
        {'title': 'MIT OpenCourseWare', 'description': 'A web-based publication of virtually all MIT course content.'},
        {'title': 'NASA STEM Engagement', 'description': 'Resources and activities to inspire students in STEM education.'},
    ]
    return render(request, 'learning/profile.html', {'stem_resources': stem_resources})
