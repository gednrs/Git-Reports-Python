class MarkdownGernerator:

    @classmethod
    def build(cls, repo):
        itens = ''.join(
            f'**ID: **{repos.id} **ID: **{repos.name} **ID: **{repos.stargazers_count}\n'
            for repos in repo)
        return f'##REPOS \n\n{itens}'