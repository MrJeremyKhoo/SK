from pylatex import Document, Package, Section, Command, Itemize, NoEscape
from pylatex.base_classes import Environment, CommandBase, Arguments, Options

class Solution(Environment):
    _latex_name = 'solution'

def append_solution(solution, doc):
    with doc.create(Solution()):
            doc.append(solution)

