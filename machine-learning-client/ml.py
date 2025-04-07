from datetime import datetime
from pymongo import MongoClient
import time
from difflib import SequenceMatcher

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



def calculate_accuracy(str1: str, str2: str) -> float:
    """
    Calculate the accuracy score between two strings using similarity ratio.
    :param str1: The reference string.
    :param str2: The string to compare.
    :return: Accuracy score as a float between 0 and 1.
    """
    return SequenceMatcher(None, str1, str2).ratio()


