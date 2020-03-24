from fpdf import FPDF

FILE = 'problems.txt'
TITLE = 'Problem Set 1'
PDF_NAME = 'problems.pdf'


class PDF(FPDF):
    def header(self):
        self.set_font('Courier', 'B', 15)
        w = self.get_string_width(self.title) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, self.title, 0, 1, 'L')
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Courier', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def add_problem(self, num, content):
        self.set_font('Courier', '', 12)
        self.multi_cell(0, 4, str(num) + ". " + content)
        self.ln()

    def print_problem(self, num, content):
        self.add_page()
        self.add_problem(num, content)


def read_pages(file):

    problem_list = []
    f = open(file)
    for line in f:
        problem_list.append(line)
    return problem_list


pdf = PDF()
pdf.set_title(TITLE)

problems = read_pages(FILE)

for i in range(0, len(problems)):
    pdf.print_problem(i + 1, problems[i])

pdf.output(PDF_NAME, 'F')
