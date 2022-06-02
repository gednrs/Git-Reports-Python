class Repos:

    def __init__(self, id, name, stargazers_count):
        self._id = id
        self._name = name
        self._stargazers_count = stargazers_count

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def stargazers_count(self):
        return self._stargazers_count

    def __str__(self):
        return f'id: {self._id} name: {self._name} stars: {self._stargazers_count}'