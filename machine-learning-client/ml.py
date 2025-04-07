from datetime import datetime
from pymongo import MongoClient
import time
from difflib import SequenceMatcher

def typing(true_sentence: str, user_input: str, start_time, end_time):
    
    date = datetime.now().strftime("%B %d %I:%M%p")
    time_passed = end_time - start_time
    minutes = time_passed / 60
    words = len(user_input.split())
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
    "text": user_input,
    "wpm": wpm,
    "speed": speed,
    "date": date,
    "accuracy": calculate_accuracy(true_sentence, user_input)
    }



def calculate_accuracy(true_sentence: str, user_input: str) -> float:
    """
    Calculate the accuracy score between two strings using similarity ratio.
    :param true_sentence: The reference string.
    :param user_input: The string to compare.
    :return: Accuracy score as a float between 0 and 1.
    """
    return SequenceMatcher(None, true_sentence, user_input).ratio()


