# built in
import logging

# logging setup
LOGGING_FORMAT = "[%(asctime)s] [LOGGING] %(message)s"
logging.basicConfig(format=LOGGING_FORMAT, datefmt="%Y-%m-%dT%H:%M:%S", level=logging.INFO)

def onMessage(packet, interface):
    text = packet["decoded"]["payload"].decode()
    logging.info(text)

def get_function_and_event():
    return onMessage, "meshtastic.receive.text"
