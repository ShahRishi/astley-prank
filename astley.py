import webbrowser
import time
import random

def spamAstley():
    for x in range (3):
        site = 'https://youtu.be/dQw4w9WgXcQ'
        webbrowser.open_new(site)
        seconds = random.randrange(5, 10)
        time.sleep(seconds)
