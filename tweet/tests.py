from django.test import TestCase
from django.contrib.auth.models import User

from .models import Tweet, Comment
from .forms import TweetForm, CommentForm


# Create your tests here.
class TestTweet(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='rahmatjon1', password='Qwerty.11')
        self.tweet = Tweet.objects.create(user=self.user, hashtag='#Tarix', question='Amir Temur qachon tugilgan?')

    def test_tweet(self):
        self.assertEqual(str(self.tweet), f"{self.user.username} - {self.tweet.question}")

    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_fail_status_code(self):
        response = self.client.get('/')
        self.assertNotEquals(response.status_code, 404)


class CommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teshaxon', password='teshaxon.1')
        self.tweet = Tweet.objects.create(user=self.user, hashtag='#Tarix', question='Amir Temur qachon tugilgan?')
        self.comment = Comment.objects.create(user=self.user, tweet=self.tweet, text='Amir Temur 1336.')

    def test_comment_str(self):
        self.assertEqual(str(self.comment), f"{self.user.username} - {self.comment.text}")

    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class TweetFormTest(TestCase):
    def test_tweet_form_true(self):
        form_data = {
            'hashtag': 'Tarix', 'question': 'Amir Temur qachon tugilgan?'
        }

        form = TweetForm(data=form_data)
        self.assertTrue(form.is_valid())
        print(form.errors)

    def test_tweet_form_false(self):
        form_data = {
            'hashtag': '#sanat',
            'question': 'sanatdagi shok',
        }
        form = TweetForm(data=form_data)
        self.assertFalse(form.is_valid())



class CommentFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teshaboy', password='teshaboy.1')
        self.tweet = Tweet.objects.create(user=self.user, hashtag='#Sport', question='Amir Temur qachon tugilgan')

    def test_comment_form_true(self):
        form_data = {'text': 'qachon vafot etgan?'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())