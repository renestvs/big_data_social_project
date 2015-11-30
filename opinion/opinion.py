from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from Preproc import Utils
#from stemming.porter2 import stem
from sklearn import cross_validation

utl = Utils()
corpus = []
annotation = []

input_file = open("new_sts.csv","r")

for line in input_file:
    vec = line.split(';')
    annotation.append(vec[1].replace('\n',''))
    vec[0] = vec[0].lower()
    vec[0] = utl.remove_marks(vec[0])
    vec[0] = utl.replace_mentions(vec[0])
    vec[0] = utl.delete_links(vec[0])
    phrase = ''
    for elem in vec[0].split(' '):
        try:
            elem = stem(elem)
        except:
            pass
        phrase = phrase+' '+elem
    corpus.append(phrase.replace('\n',''))

vectorizer = CountVectorizer(min_df = 0.0, max_df = 1.0)
number_of_examples = len(corpus)
transform = vectorizer.fit_transform(corpus)
feature_list = vectorizer.get_feature_names()

X = vectorizer.transform(corpus)

clf = MultinomialNB()

scores = cross_validation.cross_val_score(clf, X, annotation, cv=10)

print scores