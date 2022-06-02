class HTMLGernerator:

    @classmethod
    def build(cls, repo):
        itens = ''.join(
            f'<strong>ID: </strong>{repos.id} <strong>ID: </strong>{repos.name} <strong>ID: </strong>{repos.stargazers_count}\n'
            for repos in repo)
        return f'<p>{itens}</p>'