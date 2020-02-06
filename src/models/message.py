from faust import Record


class Message(Record):
    from_name: str
    to_name: str
    body: str
