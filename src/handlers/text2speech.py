# 3rd party
import pyttsx3

def onMessage(packet, interface):
    text = packet["decoded"]["payload"].decode()
    pyttsx3.speak(text)

def get_function_and_event():
    return onMessage, "meshtastic.receive.text"
