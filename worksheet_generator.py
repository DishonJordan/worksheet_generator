from fpdf import FPDF

FILE = 'problems.txt'


class ProblemObject:

    title = 'default'
    problems_and_lines = []

    def __init__(self, title, problems_and_lines):
        self.title = title
        self.problems_and_lines = problems_and_lines

    def get_problem(self, index):
        return self.problems_and_lines[index][0]

    def get_lines(self, index):
        return int(self.problems_and_lines[index][1])


class PDF(FPDF):
    def header(self):
        self.set_font('Courier', 'B', 15)
        w = self.get_string_width(self.title) + 6
        self.set_x((210 - w) / 2)
        self.cell(0, 9, self.title, 0, 1, 'L')
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

    def print_problem(self, num, content, lines):
        print(lines, content)
        self.add_problem(num, content)
        self.ln(lines * 5)


def read_pages(file):
    f = open(file)
    i = 0
    title = ''
    problems = []

    for line in f:
        if i is 0:
            title = line.strip()
        else:
            line_split = line.split(" ", 1)
            problems.append((line_split[1], line_split[0]))
        i += 1

    p = ProblemObject(title, problems)

    return p


pdf = PDF()
problems = read_pages(FILE)
pdf.set_title(problems.title)
print()
pdf.add_page()

for i in range(0, len(problems.problems_and_lines)):
    pdf.print_problem(i + 1, problems.get_problem(i), problems.get_lines(i))

pdf.output(problems.title + '.pdf', 'F')
