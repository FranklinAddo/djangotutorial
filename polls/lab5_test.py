import urllib.request

from django.test import SimpleTestCase, TestCase, TransactionTestCase, LiveServerTestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question

# 1. SimpleTestCase
class SimpleTests(SimpleTestCase):
    def test_index_page_statuscode(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)


# 2. TestCase
class QuestionTests(TestCase):
    # Test creating a question
    def test_create_question(self):
        question = Question.objects.create(
            question_text="Test Question",
            pub_date=timezone.now()
        )
        self.assertEqual(question.question_text, "Test Question")

    # Test that question exists in database
    def test_question_exists(self):
        Question.objects.create(
            question_text="Another Question",
            pub_date=timezone.now()
        )
        count = Question.objects.count()
        self.assertEqual(count, 1)


# 3. TransactionTestCase
class TransactionTests(TransactionTestCase):
    def test_insert_question(self):
        Question.objects.create(
            question_text="Transaction Test Question",
            pub_date=timezone.now()
        )
        self.assertEqual(Question.objects.count(), 1)


# 4. LiveServerTestCase
class LiveServerTests(LiveServerTestCase):
    def test_live_server_index(self):
        url = self.live_server_url + reverse("polls:index")
        response = urllib.request.urlopen(url)
        self.assertEqual(response.status, 200)
