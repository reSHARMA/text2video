import os, random

def getSong(mood):
    return random.choice(os.listdir("./music/" + mood))
