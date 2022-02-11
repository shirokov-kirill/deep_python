def generate_header():
    return "\\documentclass[a4paper,12pt,twoside]{book} \\usepackage[english]{babel} \\usepackage[utf8]{inputenc} " \
           "\\pagestyle{headings} "


def create_cell_generator(row):
    i = -1

    def generator():
        nonlocal i
        i += 1
        return row[i]

    return generator


def create_row_generator(lst):
    i = -1

    def generator():
        nonlocal i
        i += 1
        cell_generator = create_cell_generator(lst[i])
        return " " + cell_generator() + " & " + cell_generator()
    return generator


def generate_rows(lst, res, i, generator):
    if i < len(lst) - 1:
        return res + generator() + " \\\\ \\hline " + generate_rows(lst, res, i + 1, generator)
    else:
        return generator()


def generate_table(lst):
    row_generator = create_row_generator(lst)
    return "\\begin{center} \\begin{tabular}{ |c|c| } \\hline" + generate_rows(lst, "", 0, row_generator) + \
           " \\\\ \\hline \\end{tabular} \\end{center}"


def generate_latex_doc(lst):
    return generate_header() + " \\begin{document} " + generate_table(lst) + " \\end{document}"


listik = [["1", "array"], ["2", "list"], ["3", "vector"], ["4", "queue"], ["5", "deque"]]
print(generate_latex_doc(listik))
