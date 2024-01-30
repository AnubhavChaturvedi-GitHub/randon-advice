import random
from Head.Ear import *
from Data.dlg_data.dlg import *
from Head.Mouth import speak
from Function.check_online_ofline import is_online
from friday.Fspeak import fspeak
from Function.random_advice import get_random_advice
from Function.command import cmd
import time

def advice():
    while True:
        x = [600, 550, 580, 400, 3000, 800, 700, 8200 ,8000, 50 ,568]
        x = random.choice(x)
        time.sleep(x)
        speak("I have some suggestion for you, sir")
        text = listen().lower()
        if "yes tell me" in text or "yes" in text:
            advice = get_random_advice()
            speak(advice)
        else:
            speak("no probelm , i think you need some advice so i give")


def jarvis():
    t1 = threading.Thread(target=cmd)
    t2 = threading.Thread(target=advice)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def check_jarvis():
    if is_online():
        jarvis()
    else:
        x = random.choice(ofline_dlg)
        fspeak(x)


check_jarvis()
