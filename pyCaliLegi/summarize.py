
from pyCaliLegi import extractor
from pyCaliLegi import scoring
from pyCaliLegi import filter
import os

# Most of this code was taken from 
# https://github.com/LazoCoder/Article-Summarizer

def summarize_bill(browser):
    bill_text = extract_bill_text(browser)
    return summarize(bill_text)

def extract_bill_text(browser):
    bill = browser.find_element_by_id('bill_all')
    return bill.text

def summarize(text, num_of_sentences=3):
    # Summarize a file. The length of the summary will be the number of sentences specified.
    file = './temp.txt'
    with open(file, 'w') as handle:
        handle.write(text)

    # Extract all the words and sentences and get their respective scores.
    all_words = extractor.get_words(file)
    word_scores = scoring.get_word_scores(all_words)
    all_sentences = extractor.get_sentences(file)
    all_sentences = filter.omit_transition_sentences(all_sentences)
    sentence_scores = scoring.get_sentence_scores_list(all_sentences, word_scores)

    if num_of_sentences > len(all_sentences):
        print("The summary cannot be longer than the text.")
        return

    # Get x sentences with the highest scores, in chronological order.
    threshold = scoring.x_highest_score(sentence_scores, num_of_sentences)
    top_sentences = scoring.top_sentences(all_sentences, sentence_scores, threshold)

    # Put the top sentences into one string.
    summary = ""
    for sentence in top_sentences:
        summary += sentence + " "
    summary = summary[:-1]
    os.remove(file)

    return summary