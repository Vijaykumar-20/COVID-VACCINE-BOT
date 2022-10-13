import requests
import json
from pprint import pprint
from datetime import datetime

from requests import sessions


def sample_responses(input_text):
    user_message=str(input_text).lower()
    if user_message in("hello","hi","sup"):
        return "Hey! how's it going ?😊"
    if user_message in("who are you","who are you?"):
        return "You know who😜"
    if user_message in("time","time?"):
        now=datetime.now()
        date_time=now.strftime("%d/%m/%y,%H:%M:%S")

        return str(date_time)
    



    return "Can you stick to bot language please?😁.Use /help command if u dont know bot language🌝"
