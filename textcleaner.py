import re
#import spacy
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
# nlp = spacy.load('en')
# "january", "febuary","march", "april", "may","june","july","august","september","october","november","december"
stopwords = ["sees","a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also",
    	        "although","always","am","among", "amongst", "amoungst", "amount", "an", "and", "another", "any","anyhow","anyone","anything","anyway",
                 "anywhere", "are", "around", "as",  "at", "back","be", "became", "because","become","becomes", "becoming", "been", "before", "behind", "being", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", 
                 "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", 
                 "elsewhere", "empty", "enough", "etc", "even",  "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", 
                 "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt",
                   "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how",
                    "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter",
                     "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", 
                     "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody",
                      "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other",
                       "others","reuters","otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re",
                        "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", 
                        "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", 
                        "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore",
                         "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru",
                          "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", 
                          "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein",
                         "whereupon", "wherever", "whether", "which", "while", "whither", "who","whoever", "whole", "whom", "whose", "why", "will","'will", "with", 
                         "within", "without", "would", "yet","pay", "breakingviews","you","your", "yours", "yourself", "yourselves", "the", ",",":",";",".","-","!","?","a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also",
    	        "although","always","am","among", "amongst", "amoungst", "amount", "an", "and", "another", "any","anyhow","anyone","anything","anyway",
                 "anywhere", "are", "around", "as",  "at", "back","be", "became", "because","become","becomes", "becoming", "been", "before", "behind", "being", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", 
                 "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", 
                 "elsewhere", "enough", "etc", "even",  "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fill", "find", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt",
                   "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how",
                    "however" "ie", "if", "in", "inc", "indeed" "into", "is", "it", "its", "itself", "keep", "last", "latter",
                     "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", 
                     "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody",
                      "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other",
                       "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re",
                        "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", 
                        "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore",
                         "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru",
                          "thus", "to", "together", "too", "top", "toward", "towards", "un", "under", "until", "up", "upon", "us", "very", 
                          "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein",
                         "whereupon", "wherever", "whether", "which", "while", "whither", "who","whoever", "whole", "whom", "whose", "why", "will", "with", 
                         "within", "without", "would", "yet","pay", "breakingviews","you", "your", "yours", "yourself", "yourselves", "the", "update", "exclusive:", "deal", "says", "new",
                          "powerball","mega millions", "UPDATE ", "growth",  "war", "sources","pm","poll", "reuters","Trump", "AP","ap"]

test = ["U.S negotiators; to meet Taliban delegation in Islamabad on Feb 18: Taliban spokesman", "Turkish MP says Ankara sticking to Russian missile pruchase", "EU asylum applications will fall to below half crisis peak"]

def cleantext(doc):
    word_list = doc.split()
    filtered_words = [word for word in word_list if word.lower() not in stopwords]
    r = re.compile(r'[a-z]+-*[a-z]*', re.I)
    cleaned = r.findall(" ".join(filtered_words))
    filtered = " ".join(cleaned)
    return filtered

def cleantexts(docs):
    cleaned = []
    for doc in docs:
        cleaned.append(cleantext(doc))
    return cleaned
n = 0

# def pos_cleaner(doc):
#     word_list = word_tokenize(doc)
#     lemmatizer = WordNetLemmatizer()
#     sent = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
#     processes = nlp(sent)
#     filtered_words = [word for word in word_list if word not in stopwords]
#     filtered = " ".join(filtered_words)
#     return filtered
def list_cleaner(doc):
    word_list = doc
    lemmatizer = WordNetLemmatizer()
    filtered_words = [word for word in word_list if word not in stopwords]
    return filtered_words


#print(test[n])
#print(pos_cleaner(test[n]))
