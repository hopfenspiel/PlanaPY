import requests
from requests.structures import CaseInsensitiveDict
import json
import pandas as pd
from time import gmtime, strftime
import time

class AnaplanAPI: 
    def __init__(self):
        self.headers = CaseInsensitiveDict()
        self.headers['Content-Length'] = "0"
        self.token = ""
        self.response_results = dict()
        self.api_url = "https://api.anaplan.com/2/0/"
        self.token_url = "https://auth.anaplan.com/token/"
        
    def acquire_token(self, username, password):
        URL = self.token_url + "authenticate"
        
        try:
            self.resp = requests.post(
                URL
                ,auth=(username, password)
            )
            self.response_results = self.resp.json()
            self.token = self.response_results['tokenInfo']['tokenValue']
            self.headers['authorization'] = "AnaplanAuthToken {0}".format(self.token)

        except Exception as e:
            print('Error occurred: {0}'.format(e))
        
        return self.resp.status_code
    
    def token_check(self):
        if not self.token:
            print("No active token. Please first run the acquire_token function.")
        return self.token
        
    def token_details(self):
        URL = self.token_url + "validate"
        
        if not self.token_check():
            return
        
        try:
            self.resp = requests.get(URL, headers=self.headers)
            self.response_results = self.resp.json()
        except Exception as e:
            print("Error occurred: {0}".format(e))
        
        print(self.resp.status_code)
        return self.resp.json()
    
    def refresh_token(self):
        URL = self.token_url + "refresh"

        if not self.token_check():
            return
        
        try:
            self.resp = requests.post(URL, headers=self.headers)
            self.response_results = self.resp.json()
            self.token = self.response_results['tokenInfo']['tokenValue']
        except Exception as e:
            print("Error occurred: {0}".format(e))
            
        return self.resp.status_code
    
    def end_session(self):
        URL = self.token_url + "logout"
        
        if not self.token_check():
            return
        
        try:
            self.resp = requests.post(URL, headers=self.headers)
            print("Successfully ended session.")
        except Exception as e:
            print("Error occurred: {0}".format(e))
            
        return self.resp.status_code  
		
