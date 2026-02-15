# import libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
import re

# veri seti yükle
df = pd.read_csv("spam.csv", encoding="latin-1")
text = df['v2']

# Veri Temizleme Bloğu
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))
def clean_text(text):
    
    #buyuk kucuk harf
    text = text.lower()
    
    #rakamları temizleme
    text = re.sub(r"\d+", "", text)
    
    #ozel karakterlerin temzilenmesi
    text = re.sub(r"[^\w\s]", "", text)
    
    #kısa kelimelerin temizlenmesi
    text = " ".join(word for word in text.split() if len(word)>2)
    
    #stop words silinmesi
    text = " ".join(word for word in text.split() if word.lower() not in stop_words)
    
    return text #temizlenmiş text'i return et
# metinleri temzileme
cleaned_text = [clean_text(row) for row in text]



# tfıdf
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_text)

# kelime kümesini incele
feature_names = vectorizer.get_feature_names_out()
tf_idf_score = X.mean(axis=0).A1 # Her kelimenin tf-idf değerleri

# tfıdf skorlarını içeren bir df oluştur
df_tfidf = pd.DataFrame({"word":feature_names,"tfidf_score": tf_idf_score})

#skorları sırala ve sonucları incele

df_tfidf_sorted = df_tfidf.sort_values(by="tfidf_score",ascending=False)
print(df_tfidf_sorted.head(10))
