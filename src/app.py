import os
import faust

FAUST_APP = os.getenv('FAUST_APP', 'faust-ml-starter')
# use rocksdb for prod, and memory for dev.
FAUST_STORE = os.getenv('FAUST_STORE', 'memory://')
FAUST_BROKERS = os.getenv('FAUST_BROKERS', 'kafka://localhost:9092')

app = faust.App(FAUST_APP, broker=FAUST_BROKERS, store=FAUST_STORE)
