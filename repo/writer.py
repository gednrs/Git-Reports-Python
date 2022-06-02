from repo.file_writer import ReportFileWriter

class ReportWriter:
    def write(report, writer=ReportFileWriter):
        writer.write(report)