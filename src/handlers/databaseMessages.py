# built in
import sqlite3
import os
import datetime

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


class Database:
    def __init__(self, path=None):
        if not path:
            path = self.make_path()
        self.path = path
        self.connection = None
        self.cursor = None

    @staticmethod
    def make_path():
        this_dir = os.path.dirname(os.path.abspath(__file__))
        src_dir = os.path.dirname(this_dir)
        data_dir = os.path.join(os.path.dirname(src_dir), "data")
        os.makedirs(data_dir, exist_ok=True)
        db_path = os.path.join(data_dir, "db.sqlite")
        return db_path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
                uuid INTEGER,
                sender TEXT,
                target TEXT,
                text TEXT,
                channel INTEGER,
                timestamp TEXT
            );
            """
        )
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.connection.commit()
        self.connection.close()
        self.connection = None
        self.cursor = None

    def insert(self, uuid, sender, target, text, channel, timestamp):
        if not self.connection:
            raise RuntimeError(
                'No connection found, please use `with Database("/path") as db:` syntax'
            )
        self.cursor.execute(
            "INSERT INTO messages VALUES (?, ?, ?, ?, ?, ?);",
            [uuid, sender, target, text, channel, timestamp],
        )


def onMessage(packet, interface):
    uuid = packet["id"]
    sender = packet["fromId"]
    target = packet["toId"]
    text = packet["decoded"]["payload"].decode()
    channel = packet.get("channel", 0)
    timestamp = datetime.datetime.fromtimestamp(packet["rxTime"])
    timestamp = timestamp.isoformat()
    with Database() as db:
        db.insert(uuid, sender, target, text, channel, timestamp)

def get_function_and_event():
    return onMessage, "meshtastic.receive.text"