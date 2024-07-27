
import random
from utils import appendQuestion, appendSolution
from pylatex import Document, Package, Section, Command, Itemize, NoEscape
from pylatex.base_classes import Environment, CommandBase, Arguments, Options

class Question(Environment):
    _latex_name = 'questions'

def solution(word):
    k_word = word['korean_word'];
    final_conso = word['final_consonant'];
    if (word['is_noun'] != None):
        conjugation = conju(final_conso, True)
        return f"{k_word}{conjugation}"
    else:
        return "명사가 아닌 단어는 굴절될 수 없습니다."


def conju(const, iscorrect):
    if (const == None and iscorrect) or (const != None and not iscorrect):
        return "는"
    else:
        return "은"

def correct_choice(kr_list):
    choice_word = random.choice(kr_list)
    correct_is_noun = choice_word['is_noun'];

    while (correct_is_noun == None):
        choice_word = random.choice(kr_list)
        correct_is_noun = choice_word['is_noun'];

    correct_answer = choice_word['korean_word'];
    correct_conjugation = conju(choice_word['final_consonant'], True)
    return f"{correct_answer}" + f"{correct_conjugation}"
    
def correct_choice_personal(kr_list):
    choice_word = random.choice(kr_list)
    correct_is_noun = choice_word['is_noun'];
    while ((correct_is_noun != 'personal' and correct_is_noun != 'person_pronoun') or choice_word['korean_word'] == '나'):
        choice_word = random.choice(kr_list)
        correct_is_noun = choice_word['is_noun'];
    correct_answer = choice_word['korean_word'];
    correct_conjugation = conju(choice_word['final_consonant'], True)
    return f"{correct_answer}" + f"{correct_conjugation}"
    
def correct_choice_object(kr_list):
    choice_word = random.choice(kr_list)
    correct_is_noun = choice_word['is_noun'];

    while (correct_is_noun != 'obj_pronoun'): 
        choice_word = random.choice(kr_list)
        correct_is_noun = choice_word['is_noun'];

    correct_answer = choice_word['korean_word'];
    correct_conjugation = conju(choice_word['final_consonant'], True)
    return f"{correct_answer}" + f"{correct_conjugation}"
    
def wrong_choice(kr_list):
    wrong_choice_word = random.choice(kr_list)
    wrong_answer = wrong_choice_word['korean_word'];
    wrong_conjugation = conju(wrong_choice_word['final_consonant'], False)
    correct_solution = solution(wrong_choice_word)

    return f"{wrong_answer}" + f"{wrong_conjugation}", correct_solution

def wrong_choice_object(kr_list):
    wrong_choice_word = random.choice(kr_list)
    is_noun = wrong_choice_word['is_noun'];

    while (is_noun != 'obj_pronoun'): 
        wrong_choice_word = random.choice(kr_list)
        is_noun = wrong_choice_word['is_noun'];

    wrong_answer = wrong_choice_word['korean_word'];
    wrong_conjugation = conju(wrong_choice_word['final_consonant'], False)
    correct_solution = solution(wrong_choice_word)

    return f"{wrong_answer}" + f"{wrong_conjugation}", correct_solution

def wrong_choice_personal(kr_list):
    wrong_choice_word = random.choice(kr_list)
    is_noun = wrong_choice_word['is_noun'];

    while (is_noun != 'personal' and is_noun != 'person_pronoun' or wrong_choice_word['korean_word'] == '나'): 
        wrong_choice_word = random.choice(kr_list)
        is_noun = wrong_choice_word['is_noun'];

    wrong_answer = wrong_choice_word['korean_word'];
    wrong_conjugation = conju(wrong_choice_word['final_consonant'], False)
    correct_solution = solution(wrong_choice_word)

    return f"{wrong_answer}" + f"{wrong_conjugation}", correct_solution


def each_choice(kr_list):
    wrong_str, solution = wrong_choice(kr_list)
    choices = [
        [correct_choice(kr_list)],
        [wrong_str, solution]
    ]

    return choices, solution


def make_choice(doc, kr_dic, marks, total):
    doc.append(Command('section', arguments='Multiple Choice'))
    doc.append('Choose the correct sentence')
    with doc.create(Question()):
        for i in range(total):
            choice, solution = each_choice(kr_dic)
            appendQuestion.append_choice(doc, kr_dic, marks, choice);
            appendSolution.append_solution(solution, doc)
