from .query import addNamesToGenerator, createUser, autofillUser
from django.test import TestCase
from .models import NameGenerator
from .password import PasswordGenerator
from .generate_email import generate_email
from django.urls import reverse
from .views import register_user
import pytest
from django.test.client import RequestFactory
from .models import NameGenerator, TDSUser


class NameGeneratorTestCase(TestCase):
    def setUp(self):
        addNamesToGenerator(name="Tim")
        addNamesToGenerator(name="Tara")

    def test_names_get_added(self):
        """Test addNamesToGenerator from the setup adds names in the database table as expected"""
        tim = NameGenerator.objects.get(username="Tim")
        tara = NameGenerator.objects.get(username="Tara")
        self.assertEqual(tim.__str__(), "Tim")
        self.assertEqual(tara.__str__(), "Tara")


class TDSUserTestCase(TestCase):
    def setUp(self):
        createUser(username="Tim")
        createUser(username="Tara")

    def test_names_get_added(self):
        """Test createUser from the setup adds names in the database table as expected"""
        tim = TDSUser.objects.get(username="Tim")
        tara = TDSUser.objects.get(username="Tara")
        self.assertEqual(tim.__str__(), "Tim")
        self.assertEqual(tara.__str__(), "Tara")


class AutofillTestCase(TestCase):
    def setUp(self):
        # two potential names in the name generator table
        addNamesToGenerator(name="Tim")
        addNamesToGenerator(name="Tara")
        # one of them is already being used as a user name
        createUser(username="Tim")

    def test_names_get_added(self):
        """Test autofillUser returns a potential username from NameGenerator 
            table that is not already being used by a user"""
        new_username, new_email, new_passord = autofillUser() 
        # autofill should return username not already in use i.e. Tara
        self.assertEqual(new_username, "Tara")



class PasswordGeneratorTestCase(TestCase):
    def test_generate_password(self):
        password = PasswordGenerator.generate_password(12)

        self.assertEqual(len(password), 12)

class GenerateEmailTestCase(TestCase):
    def test_generate_email(self):
        email_address = generate_email()
        self.assertTrue(email_address.__contains__('@') and email_address.__contains__('.'))


class ViewTestCase(TestCase):
    def test_register_view(self):
        path = reverse("register")
        request = RequestFactory().get(path)
        response = register_user(request)
        assert response.status_code == 200