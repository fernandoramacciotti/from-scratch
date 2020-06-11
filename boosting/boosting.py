import numpy as np
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier


class VanillaBoosting(object):
    def __init__(self, n_iter=10, alpha=0.1, max_depth=4):
        self.n_iter = n_iter
        self.alpha = alpha
        self.max_depth = max_depth

    def fit(self, X, y=None):
        # init first weak learner
        self.log_preds_ = list()
        self.weak_learners_ = list()
        self.mse_ = list()
        H = np.zeros_like(y)
        # iterate
        for iter in range(self.n_iter):
            # residuals
            ti = y - H
            # fit weak learner
            h = DecisionTreeRegressor(max_depth=self.max_depth)
            h.fit(X, ti)
            # step towards prediction
            H = H + self.alpha * h.predict(X)
            # logging
            self.log_preds_.append(H)
            self.weak_learners_.append(h)
            # MSE
            mse = np.mean(np.sqrt(np.sum(np.power(y - H, 2))))
            self.mse_.append(mse)
            print(f"Iter {iter+1}: MSE = {mse:.5f}")

        self.booster_ = H
        return self

    def predict(self, X):
        pred = 0
        for iter in range(self.n_iter):
            pred = pred + self.alpha * self.weak_learners_[iter].predict(X)
        return pred


if __name__ == "__main__":
    from sklearn.datasets import make_classification

    X, y = make_classification(random_state=42)
    boost = VanillaBoosting()
    boost.fit(X, y)
    preds = boost.predict(X)
    print(preds)
