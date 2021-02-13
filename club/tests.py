from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime

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