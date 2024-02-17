from .query import addNamesToGenerator
import random

# This function will preload data into the database
def load_initial_namegenerator_data():
    usernames = ['Alex123', 'Joseph345', 'Martin', 'Sophia', 'Ted', 'John', 'Tim678']
    locations = ['Toronto', 'Montreal', 'Quebec', 'New York', 'Vancouver', 'Regina', 'Calgary']
    categories = ['Sport', 'Politics', 'Technology', 'Science']
    
    length = len(usernames)
    for i in range(length):
        categ = random.choice(categories)
        username = usernames[i] + '-' + 'Journalist'
        loc = locations[i]
        addNamesToGenerator(username, location=loc, category=categ)

