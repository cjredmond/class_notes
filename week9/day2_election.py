import requests
import time

from data_miner import DataMiner
from messenger import Messenger

messenger = Messenger()
dm = DataMiner()


while True:
    if dm.is_new_data:
        base_sms = dm.message
        print(base_sms)
        messenger.send(base_sms)
    time.sleep(600)
