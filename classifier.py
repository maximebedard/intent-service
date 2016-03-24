from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files

train = load_files('train')
text_clf = Pipeline([
  ('vect', CountVectorizer()),
  ('tfidf', TfidfTransformer()),
  ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42))
])
text_clf = text_clf.fit(train.data, train.target)

def intent(comment_body):
  predictions = text_clf.predict([comment_body])
  return train.target_names[predictions[0]]

