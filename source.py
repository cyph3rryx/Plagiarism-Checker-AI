import nltk
from nltk.corpus import stopwords
from collections import Counter
import spacy
nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    # remove stopwords and punctuations
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def similarity_score(text1, text2):
    # preprocess text
    tokens1 = preprocess(text1)
    tokens2 = preprocess(text2)
    
    # create document objects
    doc1 = nlp(' '.join(tokens1))
    doc2 = nlp(' '.join(tokens2))
    
    # compute similarity score
    return doc1.similarity(doc2)

def check_plagiarism(file1, file2, threshold=0.8):
    # read files
    with open(file1, 'r') as f1:
        text1 = f1.read()
    with open(file2, 'r') as f2:
        text2 = f2.read()
    
    # compute similarity score
    score = similarity_score(text1, text2)
    
    # check if plagiarism is detected
    if score > threshold:
        print(f"Plagiarism detected! Score: {score:.2f}")
    else:
        print("No plagiarism detected.")
