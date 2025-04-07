from datetime import datetime
from pymongo import MongoClient
import time

def typing(sentence, start_time, end_time):
    
    date = datetime.now().strftime("%B %d %I:%M%p")
    time_passed = end_time - start_time
    minutes = time_passed / 60
    words = len(sentence.split())
    wpm = words/minutes

    #https://www.samyoung.co.nz/2018/12/typing-typing-typing.html
    if wpm < 30:
        speed = "Slow/Beginner"
    elif wpm < 40:
        speed = "Intermediate/Average"
    else:
        speed = "Fast/Advanced"

    #db stuffff
    result = {
    "text": sentence,
    "wpm": wpm,
    "speed": speed,
    "date": date,
    }



