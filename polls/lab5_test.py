import urllib.request

from django.test import SimpleTestCase, TestCase, TransactionTestCase, LiveServerTestCase
from django.utils import timezone

from .models import Question


# 1. SimpleTestCase

class SimplePageTests(SimpleTestCase):
    def test_indexpage_statuscode(self):
        response = self.client.get('/polls/')
        self.assertEqual(response.status_code, 200)


# 2. TestCase

class QuestionDatabaseTests(TestCase):
    def test_create_question(self):
        question = Question.objects.create(
            question_text="Test Question",
            pub_date=timezone.now()
        )
        self.assertEqual(question.question_text, "Test Question")

    def test_question_exists_in_database(self):
        Question.objects.create(
            question_text="Another Question",
            pub_date=timezone.now()
        )
        count = Question.objects.count()
        self.assertEqual(count, 1)


# 3. TransactionTestCase

class QuestionTransactionTests(TransactionTestCase):
    def test_transaction_question_insert(self):
        Question.objects.create(
            question_text="Transaction Test Question",
            pub_date=timezone.now()
        )
        self.assertEqual(Question.objects.count(), 1)


# 4. LiveServerTestCase

class LiveServerPageTests(LiveServerTestCase):
    def test_live_server_index(self):
        url = self.live_server_url + '/polls/'
        response = urllib.request.urlopen(url)
        self.assertEqual(response.status, 200)