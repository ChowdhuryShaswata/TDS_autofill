from .models import NameGenerator, TDSUser
from .generate_email import generate_email
from .password import PasswordGenerator


def addNamesToGenerator(name, location="dummy_location", category="dummy_category"):
    """create a NameGenerator object with the given <name>, <location>, and <category>"""
    NameGenerator.objects.create(username=name, location=location, category=category)


def createUser(username, password="dummy_password", email="dummy_email"):
    TDSUser.objects.create(username=username, password=password, email=email)


def autofillUser():
    randNames = NameGenerator.objects.all()
    users = TDSUser.objects.all()
    existingUsers = []
    for user in users:
        existingUsers.append(user.username)

    new_username = ""
    new_email = generate_email()
    new_password = PasswordGenerator.generate_password(15)


    for randName in randNames:
        if randName.username not in existingUsers:
            new_username = randName.username
            break
    return new_username, new_email, new_password
