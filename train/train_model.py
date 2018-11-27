

import pandas as pd
import numpy as np

df = pd.read_csv("payloads.csv")
df.info()
df.replace('', np.nan, inplace=True)
df.dropna(subset=['payload' ,'is_malicious'  ], inplace=True)

df.head()

from sklearn.model_selection import train_test_split


x_train, x_test, y_train, y_test = train_test_split(df['payload'], df['is_malicious'], test_size=0.2,
                                                    stratify=df['is_malicious'], random_state=0)

x_train, x_dev, y_train, y_dev = train_test_split(x_train, y_train, test_size=0.2,
                                                  stratify=y_train, random_state=0)
print('Train:', len(y_train), 'Dev:', len(y_dev), 'Test:', len(y_test))

from sklearn.feature_extraction.text import CountVectorizer

count_vectorizer = CountVectorizer(analyzer='char', min_df=10)
n_grams_train = count_vectorizer.fit_transform(x_train)
n_grams_dev = count_vectorizer.transform(x_dev)

print('Number of features:', len(count_vectorizer.vocabulary_))
print(y_train)

from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score

sgd = SGDClassifier(random_state=0)
sgd.fit(n_grams_train, y_train)
y_pred_sgd = sgd.predict(n_grams_dev)
print("SGDClassifier accuracy:", accuracy_score(y_dev, y_pred_sgd))

from sklearn.dummy import DummyClassifier
dummy_clf = DummyClassifier(strategy='most_frequent')
dummy_clf.fit(n_grams_train, y_train)
print("DummyClassifier accuracy:", dummy_clf.score(n_grams_dev, y_dev))

from sklearn.metrics import precision_score, recall_score
print('Precision:', precision_score(y_dev, y_pred_sgd))
print('Recall:', recall_score(y_dev, y_pred_sgd))

from sklearn.metrics import average_precision_score
print('Average precision:', average_precision_score(y_dev, y_pred_sgd))

from sklearn.pipeline import Pipeline

from xgboost import XGBClassifier

count_vectorizer = CountVectorizer(analyzer='char', min_df=10)
xgb = XGBClassifier(seed=0)
pipeline = Pipeline([
    ('count_vectorizer', count_vectorizer),
    ('xgb', xgb)
])

pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_dev)
y_pred_proba = pipeline.predict_proba(x_dev)

print('Average precision:', average_precision_score(y_dev, y_pred_proba[:, 1]))
print('Precision:', precision_score(y_dev, y_pred))
print('Recall:', recall_score(y_dev, y_pred))

import numpy as np

def get_top_k_indices(l, k=10):
    ind = np.argpartition(l, -k)[-k:]
    return ind[np.argsort(l[ind])[::-1]]

feature_names = {v: k + ' (n_gram)' for k, v in count_vectorizer.vocabulary_.items()}
for idx in get_top_k_indices(xgb.feature_importances_, 10):
    print('Importance: {:.3f} Feature: {}'.format(xgb.feature_importances_[idx], feature_names[idx]))

"""* Final training"""

pipeline.fit(df['payload'], df['is_malicious'])

from sklearn.externals import joblib

joblib.dump(pipeline, 'filename.pkl', compress = 1)

"""Till here you have trained you model and saved it
Below is code for loading it and testing it out
"""

from sklearn.externals import joblib
loaded_model = joblib.load('finalModel.pkl')
loaded_model.predict([x])
