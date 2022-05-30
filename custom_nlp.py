import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

import string
from typing import Iterable

sentence_punctuations = [',', ';', ':', '.']

stop_words = nltk.corpus.stopwords.words('english')

tokenizer_key_word = nltk.RegexpTokenizer(r'\w+')
ps = nltk.stem.WordNetLemmatizer()


def have_question_mark(text: str) -> int:
    return int("?" in text)

def have_exclamation_mark(text: str) -> int:
    return int("!" in text)

def ratio_uppercase_characters(text: str) -> float:
    return sum([c.isupper() for c in text]) / len(text)

def number_sentence_punctuations(text: str) -> int:
    return sum([c in sentence_punctuations for c in text])

def remove_all_punctuations(text: str) -> str:
    for punct in string.punctuation:
        text = text.replace(punct, '')
        
    return text

def remove_stop_words(text: str) -> str:
    text = remove_all_punctuations(text)
    
    text_list = text.split(" ")
    
    return " ".join([word for word in text_list if word not in stop_words])

def ratio_of_stopwords(text: str) -> float:
    text = remove_all_punctuations(text)
    
    text_list = text.split(" ")
    
    return len([word for word in text_list if word in stop_words]) / len(text_list)



class TFIDFTransformer:

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.features = None

    def fit(self, texts: Iterable[str]):
        
        corpus = self.get_corpus(texts)
        
        self.vectorizer.fit(corpus)

        self.features = {value: key for key, value in self.vectorizer.vocabulary_.items()}

        return self

    def transform(self, texts: Iterable[str]) -> np.ndarray:
        corpus = self.get_corpus(texts)

        return self.vectorizer.transform(corpus).toarray()

    @staticmethod
    def get_corpus(texts: Iterable[str]) -> list:
        corpus = []
        for text in texts:
            doc = TFIDFTransformer.get_document_from_string(text)
            corpus.append(" ".join(doc))

        return corpus

    @staticmethod
    def get_document_from_string(text: str) -> list:
        return [ps.lemmatize(word) for word in remove_stop_words(" ".join(tokenizer_key_word.tokenize(text))).split(" ")]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


