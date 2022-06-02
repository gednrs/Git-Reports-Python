from urllib import response
from github.client import GitHubClient
from repo.parser import RepoParser
from repo.reports.html_gen import HTMLGernerator
from repo.reports.markdown_gen import MarkdownGernerator
from repo.reports_gen import ReportsGenerator
from repo.writer import ReportWriter

if __name__ == '__main__':

    username = 'gednrs'
    response = GitHubClient.get_user_repos(username)

    if response['status_code'] == 200:
        repos = RepoParser.parser(response['body'])
        html_report = ReportsGenerator.build(HTMLGernerator, repos)
        markdown_report = ReportsGenerator.build(MarkdownGernerator, repos)
        print(html_report)
        print(markdown_report)
        ReportWriter.write(html_report)
        # ReportWriter.write(markdown_report)

    else:
        print(response['body'])