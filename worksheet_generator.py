from fpdf import FPDF


class PDF(FPDF):
    def add_problem(self, num, content):
        self.set_font("Times", '', 12)
        self.multi_cell(0, 5, content)
        self.ln()

    def print_problem(self, num, content):
        self.add_page()
        self.add_problem(num, content)


pdf = PDF()
pdf.set_title("Problem Set 1")

problems = ["Ariel was playing basketball. 1 of her shots went in the hoop. 2 of her shots did not go in the hoop. How many shots were there in total?",
            "Adrianna has 10 pieces of gum to share with her friends. There wasn’t enough gum for all her friends, so she went to the store to get 3 more pieces of gum. How many pieces of gum does Adrianna have now?"
            "How many cookies did you sell if you sold 320 chocolate cookies and 270 vanilla cookies?"]

for i in range(0, len(problems)):
    pdf.print_problem(i + 1, problems[i])

pdf.output('ps123.pdf', 'F')
