import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Poll


class PollModelTests(TestCase):

    def test_was_published_recently_in_future(self):
        """was_published_recently returns False for polls whose date_pub is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_poll = Poll(date_pub=time)
        self.assertIs(future_poll.was_published_recently(), False)

    def test_was_published_old(self):
        """was_published_recently() returns False for polls whose date_pub older than 1 day."""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_poll = Poll(date_pub=time)
        self.assertIs(old_poll.was_published_recently(), False)

    def test_was_published_recently(self):
        """was_published_recently() returns True for polls whose date_pub within the last day."""
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recently_poll = Poll(date_pub=time)
        self.assertIs(recently_poll.was_published_recently(), True)
