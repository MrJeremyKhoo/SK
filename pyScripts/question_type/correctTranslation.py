import random

from utils import appendQuestion
 
from pylatex import Document, Package, Section, Command, Itemize, NoEscape
from pylatex.base_classes import Environment, CommandBase, Arguments, Options

class Question(Environment):
    _latex_name = 'questions'

class Choice(Environment):
    _latex_name = 'choices'

def each_choice(kr_dic):
    # Select a random word from the dictionary
    choice_word = random.choice(list(kr_dic.keys()))
    # Select the correct translation corresponding to the chosen word
    correct_translation = kr_dic[choice_word]
    # Select another random word from the dictionary (for the wrong translation)
    wrong_choice_word = random.choice(list(kr_dic.keys()))
    wrong_translation = kr_dic[random.choice(list(kr_dic.keys()))]
    # Ensure the wrong translation is different from the correct one
    while kr_dic[wrong_choice_word] == wrong_translation:
        wrong_translation = kr_dic[random.choice(list(kr_dic.keys()))]
       # Define choices
    choices = [
        [f"{choice_word} - {correct_translation}"],
        [f"{wrong_choice_word} - {wrong_translation}"]
    ]
    return choices
    

def make_choice(doc, kr_dic, marks, total):
    doc.append(Command('section', arguments='Multiple Choice'))
    doc.append('Choose the correct translation')
    with doc.create(Question()):
        for i in range(total):
            appendQuestion.append_choice(doc, kr_dic, marks, each_choice(kr_dic));

