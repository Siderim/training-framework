
#
# @author: Michael Siderius
# @desc: Framework for text classification.  
# @lang: Python2.7
#
# @flags: -o $output.csv, -m $model , -tr $trainingSet.csv , -te $testingSet.csv
#

import re
from unidecode import unidecode

# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def preprocess_text(text):
	text = text.lower()
	text = unidecode(text)
	text = remove_rt(text)
	text = remove_twitter
	_user_mentions(text)
	text = remove_hashtags(text)
	text = remove_links(text)
	text = remove_special_chars(text)
	text = remove_numbers(text)
	
	return text

# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def remove_rt(text):
	return re.sub('RT ', '', text)

# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def remove_twitter_user_mentions(text):
	return re.sub(r'(?:@[\w_]+)', '', text)

# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def remove_hashtags(text):
	return re.sub(r'(?:\#+[\w_]+[\w\'_\-]*[\w_]+)', '', text)

# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def remove_links(text):
	return re.sub(r'http\S+', '', text)

# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def remove_special_chars(text):
	return re.sub(r'[^\w\s\']', '', text)

# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def remove_numbers(text):
	return re.sub(r'\d', '', text)





