from django.test import TestCase
from django.contrib.auth.models import User

from .models import UserModel
from .forms import SignUpForm, UserProfileForm, UserUpdateForm


# Create your tests here.
class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teshabek', password='teshabek.2')
        self.user_model = UserModel.objects.create(user=self.user, fullname='Teshabek Boltayev', phone_number='123456789', gender='Male')

    def test_user_model_str(self):
        self.assertEqual(str(self.user_model), self.user.username)

    def test_user_model_fields(self):
        self.assertEqual(self.user_model.fullname, 'Teshabek Boltayev')
        self.assertEqual(self.user_model.phone_number, '123456789')
        self.assertEqual(self.user_model.gender, 'Male')


class SignUpFormTest(TestCase):
    def test_signup_form_true(self):
        form_data = {'username': 'teshaboy', 'email': 'teshaboy@mail.com', 'password1': 'tesha123', 'password2': 'tesha123'}
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_signup_form_false(self):
        form_data = {'username': 'teshaboy', 'email': 'teshaboy@mail.com', 'password1': 'tesha123', 'password1': 'tesha123'}
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_signup_form_false2(self):
        form_data = {'username': 'teshaboy', 'email': 'teshaboy@mail.com', 'password1': 'tesha13', 'password2': 'tesha123'}
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_signup_form_false3(self):
        form_data = {'username': 'teshaboy', 'email': 'teshaboy#mail.com', 'password1': 'tesha123', 'password2': 'tesha123'}
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())


class UserProfileFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teshabek', password='teshabek.1')
        self.user_model = UserModel.objects.create(user=self.user, fullname='teshabek Olmosov', phone_number='123456789', gender='Male')

    def test_user_profile_form_true(self):
        form_data = {'fullname': 'teshabek', 'phone_number': '987654321', 'gender': 'Male'}
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())


class UserUpdateFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teshabek', password='teshabek.1')
        self.user_model = UserModel.objects.create(user=self.user, fullname='teshabek Olmosov', phone_number='123456789', gender='Male')

    def test_user_update_form_true(self):
        form_data = {'fullname': 'teshabek Boytoyev'}
        form = UserUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())
