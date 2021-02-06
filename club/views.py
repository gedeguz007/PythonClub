from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting, MeetingMinutes, Event


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