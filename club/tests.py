from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import MeetingForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):

    def setUp(self):
        self.meeting = Meeting(meeting_title = 'Fun with python games', meeting_date = datetime.date(2021, 2, 6), meeting_time = datetime.time(12, 30), meeting_location = 'Neumos', meeting_agenda = 'python games')

    def test_typestring(self):
        self.assertEqual(str(self.meeting), 'Fun with python games')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'club_meeting')

class MeetingMinutesTest(TestCase):

    def setUp(self):
        self.meeting_id = Meeting(meeting_title = 'Fun with python games')
        self.user = User(username = 'user1')
        self.minutes = MeetingMinutes(meeting_id = self.meeting_id)

    def test_typestring(self):
        self.assertEqual(str(self.meeting_id), 'Fun with python games')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'club_meetingminutes')

class ResourceTest(TestCase):
    
    def setUp(self):
        self.resource = Resource(resource_name = 'W3', resource_type = 'tutorial', resource_url ='https://www.w3schools.com/python', date_entered = (2021, 1, 27), description = 'tutorial')
        self.user = User(username = 'user1')

    def test_typestring(self):
        self.assertEqual(str(self.resource), 'W3')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'club_resource')

class EventTest(TestCase):
    
    def setUp(self):
        self.event = Event(event_title = 'python_games', location = 'zoom', date = (2021, 2, 28), time = (12), description = 'Fun for all')
        self.user = User(username ='user1')

    def test_typestring(self):
        self.assertEqual(str(self.event), 'python_games')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'club_event')

class NewMeetingForm(TestCase):
    def test_meetingform(self):
        data = {
            'meeting_title':'beginner projects',
            'meeting_date':'2021-2-19',
            'meeting_time':'',
            'meeting_location': 'RayGun Lounge',
            'meeting_agenda': 'projects for beginners',
        }
        form = MeetingForm (data)
        self.assertTrue(form.is_valid)

class MeetingForm_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password ='P@ssw0rd1')
        self.meeting =  Meeting.objects.create (
            meeting_title = 'Mini Programming Projects',
            meeting_date = '2021-3-5',
            meeting_time = '18:00',
            meeting_location = 'The Cuff',
            meeting_agenda = 'mini python projects'
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newmeeting/')