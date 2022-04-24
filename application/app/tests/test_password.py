from django.test import TestCase
from app.forms import ExtendedRegisterForm


class UserPasswordRegistrationTest(TestCase):

    def test_password_only_lower_latin_letter(self):
        user = {'username': 'username1', 'email': 'test1@test.test', 'password1': 'password',
                'password2': 'password'}
        form = ExtendedRegisterForm(user)
        self.assertFalse(form.is_valid())

    def test_password_only_upper_latin_letter(self):
        user = {'username': 'username2', 'email': 'test2@test.test', 'password1': 'PASSWORD',
                'password2': 'PASSWORD'}
        form = ExtendedRegisterForm(user)
        self.assertFalse(form.is_valid())

    def test_password_only_number(self):
        user = {'username': 'username3', 'email': 'test3@test.test', 'password1': '1281209324',
                'password2': '1281209324'}
        form = ExtendedRegisterForm(user)
        self.assertFalse(form.is_valid())

    def test_password_only_number_latin_letter_all_case(self):
        user = {'username': 'username4', 'email': 'test4@test.test', 'password1': 'PAsWORD312',
                'password2': 'PAsWORD312'}
        form = ExtendedRegisterForm(user)
        self.assertFalse(form.is_valid())

    def test_password_number_latin_letter_all_case_symbol(self):
        user = {'username': 'username5', 'email': 'test5@test.test', 'password1': 'PAsWORD312!',
                'password2': 'PAsWORD312!'}
        form = ExtendedRegisterForm(user)
        self.assertTrue(form.is_valid())

    def test_password_number_latin_letter_all_case_symbol_less_8(self):
        user = {'username': 'username6', 'email': 'test6@test.test', 'password1': 'Pa1!',
                'password2': 'Pa1!'}
        form = ExtendedRegisterForm(user)
        self.assertFalse(form.is_valid())

    def test_password_number_cyrillic_letter_all_case_symbol(self):
        user = {'username': 'username7', 'email': 'test7@test.test', 'password1': 'Пароль123!',
                'password2': 'Пароль123!'}
        form = ExtendedRegisterForm(user)
        self.assertTrue(form.is_valid())

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