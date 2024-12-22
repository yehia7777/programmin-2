class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        return f"Title: {self.title}\nContent: {self.content}"


class ReportSaver:
    @staticmethod
    def save_to_file(report, filename):
        with open(filename, 'w') as file:
            file.write(report)


# استخدام الكلاسات
report = Report("Sales Report", "This is the sales report content.")
report_content = report.generate_report()

saver = ReportSaver()
saver.save_to_file(report_content, "report.txt")
