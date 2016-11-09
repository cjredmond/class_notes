import requests
from data_miner import DataMiner

dm = DataMiner()
dm.get_data()
base_sms = dm.message

from twilio.rest import TwilioRestClient

class Messenger:
    account_sid = "ACd56e034034da4b3f88e61c4748fcbe39"
    auth_token  = "750d0a9f84df32c1639380b93db8567c"

    def __init__(self):
        self.client = TwilioRestClient(self.account_sid, self.auth_token)

    def send(self, message):
        message = self.client.messages.create(body=message, to="+16313344271", from_="+16319047079")
