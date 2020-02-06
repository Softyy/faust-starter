from .. import app

from ..models.message import Message

TOPIC_NAME = 'message_topic'
TOPIC_PARTITIONS = 3

messages_topic = app.topic(TOPIC_NAME, value_type=Message)


# Get the messages
@app.agent(messages_topic)
async def process(messages):
    async for message in messages:
        print(f'{message.body} from {message.from_name} to {message.to_name}')

# This seconds the messages to kafka
@app.timer(interval=1.0)
async def example_sender(app):
    await messages_topic.send(
        value=Message(body='Hello', from_name='Faust', to_name='you')
    )
