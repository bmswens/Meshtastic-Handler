# built in
import time

# 3rd party
from pubsub import pub
from meshtastic.serial_interface import SerialInterface

# custom
import handlers

def main():
    modules = handlers.get_all_modules()
    for module in modules:
        func, event = module.get_function_and_event()
        pub.subscribe(func, event)
    interface = SerialInterface()
    while True:
        time.sleep(0.1)


if __name__ == "__main__":
    main()