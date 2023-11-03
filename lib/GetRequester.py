import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(URL)
        return response.content 
        pass

    def load_json(self):
        response_data = []
        responses = json.loads(self.get_response_body())
        for response in responses:
            response_data.append(response)

        return response_data

        pass