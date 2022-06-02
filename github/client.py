import requests
import json

class GitHubClient:

    API_BASE_URL = 'https://api.github.com'
    
    @classmethod
    def get_user_repos(self, users):
        response = requests.get(
            f'{self.API_BASE_URL}/users/{users}/repos'
        )

        if response.status_code == 200:
            return {'status_code': 200, 'body': response.json()}
        else:
            return {
                'status_code': response.status_code, 
                'body': 'Error while getting repos'
            }