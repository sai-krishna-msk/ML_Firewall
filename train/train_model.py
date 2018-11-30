

import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

df = pd.read_csv("payloads.csv")
df.info()
df.replace('', np.nan, inplace=True)
df.dropna(subset=['payload' ,'is_malicious'  ], inplace=True)

df.head()


count_vectorizer = CountVectorizer(analyzer='char', min_df=10)
xgb = XGBClassifier(seed=0)
pipeline = Pipeline([
    ('count_vectorizer', count_vectorizer),
    ('xgb', xgb)
])

pipeline.fit(df['payload'], df['is_malicious'])

''' for saving the model, we dont use pickle because we have save the state of the model not only the weights'''
from sklearn.externals import joblib

joblib.dump(pipeline, 'model.pkl', compress = 1)

