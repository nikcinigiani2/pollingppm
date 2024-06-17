from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.


from rest_framework import generics
from .Models import Poll, Choice
from .Serializer import PollSerializer, ChoiceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from .Forms import PollForm, ChoiceFormSet, ChoiceForm
from django.http import JsonResponse



def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'Register.html', {'form': form})

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

def home(request, poll_id=None):
    polls = Poll.objects.all()
    choices = Choice.objects.all()
    new_poll = None
    if poll_id:
        new_poll = Poll.objects.get(id=poll_id)
    return render(request, 'home.html', {'polls': polls, 'choices': choices, 'new_poll': new_poll})



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
            return render(request, 'Login.html', {'form': form})
    else:
        # Show blank login form
        form = AuthenticationForm()
        return render(request, 'Login.html', {'form': form})


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .Models import Poll, Choice



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


def CreatePoll(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        choices = request.POST.getlist('choices')

        if question is not None:
            poll = Poll(question=question, user=request.user)
            poll.save()

        for choice in choices:
            choice = Choice(poll=poll, text=choice)
            choice.save()

        return redirect('home')
    return render(request, 'CreatePoll.html')

from django import forms

class CreatePollForm(forms.Form):
    question = forms.CharField(max_length=200, required=True)



def Logout(request):
    return render(request, 'login')

def delete_Poll(request, poll_id):
    if request.method == 'DELETE':
        poll = Poll.objects.get(id=poll_id)
        if request.user == poll.user:
            poll.delete()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Non autorizzato'}, status=403)
    else:
        return JsonResponse({'success': False, 'error': 'Metodo non valido'}, status=405)


def vote(request, poll_id, choice_id):
    poll = Poll.objects.get(id=poll_id)
    choice = Choice.objects.get(id=choice_id)

    if request.user in poll.responded_users.all():
        return JsonResponse({'success': False, 'error': 'User has already voted'})

    choice.votes += 1
    choice.save()

    poll.responded_users.add(request.user)
    poll.save()

    return JsonResponse({'success': True})


def home(request):
    polls = Poll.objects.all()
    choices = Choice.objects.all()
    return render(request, 'home.html', {'polls': polls, 'choices': choices})