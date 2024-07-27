import random
from question_type import 은는, 이에요
from utils import appendQuestion, appendSolution

from pylatex import Document, Package, Section, Command, Itemize, NoEscape
from pylatex.base_classes import Environment, CommandBase, Arguments, Options
class Question(Environment):
    _latex_name = 'questions'

def random_correct_choice(kr_dict):
    rand = random.randint(0,1)
    correct_choice = ""
    if rand == 0: #personal
       correct_choice = 은는.correct_choice_personal(kr_dict) + " " + 이에요.correct_choice_personal(kr_dict)
    elif rand == 1:
       correct_choice = 은는.correct_choice_object(kr_dict) + " " + 이에요.correct_choice_object(kr_dict)
    return correct_choice

def random_wrong_choice(kr_dict):
    rand = random.randint(0,1)
    if rand == 0:
        return random_wrong_choice_personal(kr_dict)
    elif rand == 1:
        return random_wrong_choice_object(kr_dict)

def random_wrong_choice_personal(kr_dict):
    rand = random.randint(0,2)
    wrong_choice, solution = 은는.wrong_choice_personal(kr_dict); 
    wrong_choice2, solution2 = 이에요.wrong_choice_personal(kr_dict); 
    if rand == 0:
        wrong_choice = 은는.correct_choice_personal(kr_dict); 
        solution = wrong_choice
    elif rand == 1:
        wrong_choice2 = 이에요.correct_choice_personal(kr_dict); 
        solution2 = wrong_choice2
    elif rand == 2:
        pass

    wrong_choice_sum = wrong_choice + " " + wrong_choice2;
    solution_sum = solution + " " + solution2;
    return [f"{wrong_choice_sum}", f"{solution_sum}"]

def random_wrong_choice_object(kr_dict):
    rand = random.randint(0,2)
    wrong_choice, solution = 은는.wrong_choice_object(kr_dict); 
    wrong_choice2, solution2 = 이에요.wrong_choice_object(kr_dict); 
    if rand == 0:
        wrong_choice = 은는.correct_choice_object(kr_dict); 
        solution = wrong_choice
    elif rand == 1:
        wrong_choice2 = 이에요.correct_choice_object(kr_dict); 
        solution2 = wrong_choice2
    elif rand == 2:
        pass

    wrong_choice_sum = wrong_choice + " " + wrong_choice2;
    solution_sum = solution + " " + solution2;
    return [f"{wrong_choice_sum}", f"{solution_sum}"]

def each_choice(kr_dict):
    correct_choice = random_correct_choice(kr_dict);
    wrong_choice = random_wrong_choice(kr_dict);

    return [[f"{correct_choice}"],
            wrong_choice
        ]

def make_choice(doc, kr_dic, marks, total):
    doc.append(Command('section', arguments='Multiple Choice'))
    doc.append('Choose the correct sentence')
    with doc.create(Question()):
        for i in range(total):
            choice = each_choice(kr_dic)
            appendQuestion.append_choice(doc, kr_dic, marks, choice);
