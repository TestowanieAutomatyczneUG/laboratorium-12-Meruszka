import requests


class User:
    def __init__(self) -> None:
        self.data = requests.get("https://randomuser.me/api/").json()
    
    def getData(self):
        return self.data

    def getEmail(self):
        return self.getData().get('results')[0].get('email')    

    def isMature(self):
        return self.getData().get('results')[0].get('dob').get('age') > 18
