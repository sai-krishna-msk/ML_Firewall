






def test(item):
    from sklearn.externals import joblib
    import numpy as np
    loaded_model = joblib.load('finalModel.pkl')
    result = np.max(loaded_model.predict([" {} ".format(item)]))
    return result







def train():

    import pandas as pd
    import numpy as np
    from sklearn.feature_extraction.text import CountVectorizer

    df = pd.read_csv("payloads.csv")
    df.info()
    df.replace('', np.nan, inplace=True)
    df.dropna(subset=['payload' ,'is_malicious'  ], inplace=True)

    from sklearn.pipeline import Pipeline

    from xgboost import XGBClassifier

    count_vectorizer = CountVectorizer(analyzer='char', min_df=10)
    xgb = XGBClassifier(seed=0)
    pipeline = Pipeline([
        ('count_vectorizer', count_vectorizer),
        ('xgb', xgb)
    ])

    pipeline.fit(df['payload'], df['is_malicious'])


    from sklearn.externals import joblib

    joblib.dump(pipeline, 'filename.pkl', compress = 1)
