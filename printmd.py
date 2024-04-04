from IPython.display import Latex

def mdMatrix(label, arr):
    str = f"$${label}" + "= \\begin{pmatrix}" + " \\\\ ".join([' & '.join(["{:.2f}".format(elem) for elem in line.astype(float)]) for line in arr]) + "\\end{pmatrix}$$"
    return  Latex(str)

def mdVector(label, arr):
    str = f"$${label}" + "= \\begin{pmatrix}" + " \\\\ ".join(["{:.2f}".format(elem) for elem in arr]) + "\\end{pmatrix}$$"
    return  Latex(str)