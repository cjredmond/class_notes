import requests


class DataMiner:
    def __init__(self):
        self.url = "http://projects.fivethirtyeight.com/2016-election-forecast/updates.json"
        self.response_json = []
        self.latest = {}
        self.latest_id = 0
        self.last_id = 0
        self.diffs = []
        self.base_sms = ""

    def get_data(self):
        self.response_json = requests.get(self.url).json()
        self.latest = self.response_json['updates'][0]
        self.latest_id = self.latest['added']
        self.diffs = self.latest['diffs']

    @property
    def is_new_data(self):
        self.get_data()
        if self.latest_id == self.last_id:
            return False
        self.last_id = self.latest_id
        return True

    @property
    def message(self):
        base_sms = ""
        for candidate in self.diffs['now-cast']:
            current = float(candidate['winprob']['current'])
            previous = float(candidate['winprob']['prev'])
            diff = round((current - previous) * 100, 2)
            base_sms += "{}: {}, Diff: {}\n".format(candidate['candidate'], current * 100, diff)
        self.base_sms = base_sms
        return self.base_sms
