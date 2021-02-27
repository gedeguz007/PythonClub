from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting, MeetingMinutes, Event
from .forms import MeetingForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def resources(request):
    resource_list = Resource.objects.all()
    return render (request, 'club/resources.html', {'resource_list': resource_list})

def meetings(request):
     meetings_list = Meeting.objects.all()
     return render (request, 'club/meetings.html', {'meetings_list': meetings_list})

def meetingdetail(request, id):
    meeting_info = get_object_or_404(Meeting, pk=id)
    return render (request, 'club/meetingdetail.html', {'meeting_info' : meeting_info})

@login_required
def newMeeting(request):
    form = MeetingForm

    if request.method == 'POST':
        form = MeetingForm(request.POST)

        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = MeetingForm

    else:
        form = MeetingForm()

    return render(request, 'club/newmeeting.html', {'form': form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')