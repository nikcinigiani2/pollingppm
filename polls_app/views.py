from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


from rest_framework import generics
from .models import Poll, Choice
from .serializer import PollSerializer, ChoiceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceCreate(generics.CreateAPIView):
    serializer_class = ChoiceSerializer

    def post(self, request, *args, **kwargs):
        poll_id = self.kwargs.get('poll_id')
        request.data.update({'poll': poll_id})
        return super().post(request, *args, **kwargs)

class Vote(APIView):
    def put(self, request, pk, choice_id):
        choice = Choice.objects.get(pk=choice_id, poll_id=pk)
        choice.votes += 1
        choice.save()
        return Response()


def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page
        else:
            # Form is not valid, show errors
            return render(request, 'login.html', {'form': form})
    else:
        # Show blank login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Poll, Choice

def index(request):
    latest_polls = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_polls': latest_polls}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice


