# Meshtastic Handler

## Overview
A simple framework to run custom commands on receipt of Meshtastic packets.

## Getting started
### Installation and Setup
```bash
git clone https://github.com/bmswens/Meshtastic-Handler.git
cd Meshtastic-Handler
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running
`python ./src/hander.py`

## What's Included

### databaseMessages.py
This file will write all incoming messages to a sqlite database in the a `messages` table.

### log.py
This file will log the text of incoming messages to `stdout`.

### text2speech.py
This file will play the text of incoming messages as audio over your speakers.

## Customizing
Add or remove files from in `src/handlers/`.

All files must be `.py` files and implement a `get_function_and_event()` function
which returns a function and a string which represents the topic to subscribe to.

Several examples are located in `src/handlers/` folder.

[See here for list of topics.](https://python.meshtastic.org/index.html#published-pubsub-topics)

## Run on startup
If your system has `cron`, you can add a line similar to the follow to run on reboot.

`@reboot /path/to/venv/python /path/to/src/handler.py`

Or you could implement it as a service.

## Authors

* **Brandon Swenson**- *Initial work* - [bmswens](https://github.com/bmswens)

## License

This project, like Meshtastic, is licensed under the GNU General Public License - see the [LICENSE.txt](LICENSE.txt) file for details