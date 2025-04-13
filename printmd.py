from IPython.display import Latex
from IPython.display import display

def mdMatrix(label, arr):
    str = f"$${label}" + "= \\begin{pmatrix}" + " \\\\ ".join([' & '.join(["{:.2f}".format(elem) for elem in line.astype(float)]) for line in arr]) + "\\end{pmatrix}$$"
    return  Latex(str)

def mdVector(label, arr):
    str = f"$${label}" + "= \\begin{pmatrix}" + " \\\\ ".join(["{:.2f}".format(elem) for elem in arr]) + "\\end{pmatrix}$$"
    return  Latex(str)

def mdLabelNumber(label, num, pres = 4):
    str = f"$${label}" + f"= {num:10.{pres}f}$$"
    return Latex(str)

def printMd(str):
    display(Latex(str))