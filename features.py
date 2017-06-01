
#
# Michael Siderius
# features.py
#


import string
import re
#import enchant

# fetch_avg_len(entry)
# returns average length of words in entry
#
def fetch_avg_len(entry):
    words = entry.split()
    avg = sum(len(word) for word in words)/len(words)
    return avg

# fetch_num_punctuations(entry)
# returns number of punctuatons
#
def fetch_num_punctuations(entry):
    return count(entry, string.punctuation)

# fetch_num_one_letter_tok(entry)
# return number of 1 char tokens
#
def fetch_num_one_letter_tok(entry):
    return sum(1 for x in entry.split() if len(x) == 1)

# fetch_num_urls
# return number of urls
#
def fetch_num_urls(entry):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', entry)
    return len(urls)

# fetch_len_in_tokens(entry)
# return length of entry in tokens
#
def fetch_len_in_tokens(entry):
    return len(re.findall(r'\w+', line))

# fetch_num_periods(entry)
# return number of periods
#
def fetch_num_periods(entry):
    return entry.count('.')

# fetch_num_question_marks(entry)j
# return number of question marks symbols
#
def fetch_num_question_marks(entry):
    return entry.count('?')

# fetch_num_quotes(entry)
# return number of quotation symbols
#
def fetch_num_quotes(entry):
    return entry.count('"')

# fetch_num_repeated_punc(entry)
# returns the amount of repeated punctuation
#
def fetch_num_repeated_punc(entry):
    l=[run for run, leadchar in re.findall(r'(([^\w\s])\2+)',entry)]
    count = 0
    for c in l:
        count = count + len(c)
    return count

# fetch_num_capitals(entry)
# return the number of capital letters
#
def fetch_num_capitals(entry):
    return sum(1 for c in entry if c.isupper())

# fetch_words(entry)
# returns a list of tokenized words without punctuation
#
def fetch_words(entry):
    return re.compile('\w+').findall(entry)

# fetch_num_unknown_words(entry)
# returns the number of words not in eng dict. used for mispellings etc
#
def fetch_num_unknown_words(entry):
    count = 0
    l = fetch_words(entry)
    for w in l:
        d=enchant.Dict("en_US")
        if d.check(w):
            count = count + 1
    return count
    
#
#
#
def fetch_num_blacklist_words(entry):
    ###
    return 1
#
#
#
def fetch_num_polite_words(entry):
    ###
    return 1

#
#
#
def fetch_num_modal_words(entry):
    modals = ['can', 'could', 'may', 'might', 'must', 'will', 'should', 'would','shall']
    
    count=0
    l = fetch_words(entry)
    for w in l:
        if w.lower() in modals:
            count = count + 1

    return count
















