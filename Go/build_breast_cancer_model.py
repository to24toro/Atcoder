import lightgbm as lgb
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

n_estimators = 30
d_train = lgb.Dataset(X_train, label=y_train)
params = {
    'boosting_type': 'gbdt',
    'objective': 'multiclass',
    'num_class': 3,
}
clf = lgb.train(params, d_train, n_estimators)
y_pred = clf.predict(X_test)
y_pred_raw = clf.predict(X_test, raw_score=True)

clf.save_model('lg_iris.model')  # save the model in txt format
np.savetxt('lg_iris_true_predictions.txt', y_pred)
np.savetxt('lg_iris_true_predictions_raw.txt', y_pred_raw)
np.savetxt('iris_test.tsv', X_test, delimiter='\t')