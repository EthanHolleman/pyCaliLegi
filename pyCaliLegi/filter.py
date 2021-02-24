# This omits "transition" sentences. Transition sentences are those that refer to subsequent sentence.
#
# Example: Sentence B comes right after sentence A. Sentence B also refers to sentence A. If sentence
# B is included in the summary but sentence A is not included in the summary, then this will distort
# the meaning of the sentence.
#
# Example: "Cats like to play. They also like to eat". The second sentence here refers to the first.
# Therefore it should be omitted.

# Most of this code was taken from 
# https://github.com/LazoCoder/Article-Summarizer

from pyCaliLegi import parser
from pyCaliLegi import extractor
from pyCaliLegi import WORD_LIST_DIR

def print_usage():
    # Display the parameters and what they mean.
    print('''
    Usage:
        filter.py <article.txt>
    ''')


def get_transition_phrases():
    lines = open(str(WORD_LIST_DIR.joinpath("transition_phrases.txt"))).readlines()
    result = []
    for line in lines:
        result.append(line.lstrip().rstrip())
    return result


def is_transition_phrase(transition_phrases, sentence):
    lower = sentence.lower()
    for phrase in transition_phrases:
        if lower.startswith(phrase):
            return True
    return False



def omit_transition_sentences(sentences):
    transition_phrases = get_transition_phrases()
    result = []
    for sentence in sentences:
        if not is_transition_phrase(transition_phrases, sentence):
            result.append(sentence)
    return result


