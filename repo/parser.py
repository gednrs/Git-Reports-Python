from models.model import Repos

class RepoParser:

    @classmethod
    def parser(cls, response):
        repos = []
        for i in range(len(response)):
            repo = response[i]
            repo = Repos(repo['id'], repo['name'], repo['stargazers_count'])
            print(repo)
            repos.append(repo)
        return repos