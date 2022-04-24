from django.test import TestCase
from app.forms import ExtendedRegisterForm


class UserPasswordRegistrationTest(TestCase):

    def test_wrong_mail(self):
        user = {'username': 'username7', 'email': 'test7', 'password1': 'Пароль123!',
                'password2': 'Пароль123!'}
        form = ExtendedRegisterForm(user)
        self.assertFalse(form.is_valid())

    def test_cyrillic_username(self):
        user = {'username': 'пользователь8', 'email': 'test8@test.test', 'password1': 'Пароль123!',
                'password2': 'Пароль123!'}
        form = ExtendedRegisterForm(user)
        self.assertTrue(form.is_valid())


    def test_login_less_6(self):
        user = {'username': 'польз', 'email': 'test9@test.test', 'password1': 'Пароль123!',
                'password2': 'Пароль123!'}
        form = ExtendedRegisterForm(user)
        self.assertFalse(form.is_valid())

    def test_login_more_16(self):
        user = {'username': 'пользовательпользователь', 'email': 'test10@test.test', 'password1': 'Пароль123!',
                'password2': 'Пароль123!'}
        form = ExtendedRegisterForm(user)
        self.assertFalse(form.is_valid())

    def test_right_login(self):
        user = {'username': 'пользователь', 'email': 'test10@test.test', 'password1': 'Пароль123!',
                'password2': 'Пароль123!'}
        form = ExtendedRegisterForm(user)
        self.assertTrue(form.is_valid())