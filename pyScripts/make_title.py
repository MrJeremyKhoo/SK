from pylatex import Document, Package, Section, Command, Itemize, NoEscape
from pylatex.base_classes import Environment, CommandBase, Arguments, Options

def title(doc):
    doc.preamble.append(Command('title', NoEscape(fr'Strawberry \& kimchi')))
    doc.preamble.append(Command('author', 'Practise hard :)'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

