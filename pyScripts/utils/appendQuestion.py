import random
from utils import appendSolution
from pylatex import Document, Package, Section, Command, Itemize, NoEscape
from pylatex.base_classes import Environment, CommandBase, Arguments, Options

class Question(Environment):
    _latex_name = 'questions'

class Choice(Environment):
    _latex_name = 'choices'

# always correct option is 1st

def append_choice(doc, kr_dic, marks, options):
    doc.append(Command('question', options=Options(str(marks))))
    doc.append('_____________________')
    with doc.create(Choice()):
        options[0].insert(0,Command('CorrectChoice'))
        for option in options[1:]:
            option.insert(0, Command('choice'))
        # Shuffle the choices to randomize their order
        random.shuffle(options)
        # Append shuffled choices to the document
        options_question = options.copy()
        for e in options_question:
            if (len(e) == 3):
                appendSolution.append_solution(e.pop(),doc)   
        for choice_cmd, choice_text in options_question:
            doc.append(choice_cmd)
            doc.append(choice_text)

    



