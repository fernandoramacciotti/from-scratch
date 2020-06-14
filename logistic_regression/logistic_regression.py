import numpy as np

# logistic regression with optimized with gradient descent
class LogisticRegression:
    def __init__(self, intercept=True, niter=1000, lr=0.01, w0="zeros", verbose=True):
        self.intercept = intercept
        self.niter = niter
        self.lr = lr
        self.w0 = w0  # weights initial values
        self.verbose = verbose

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _loss(self, X, y, coef):
        # J(coef)
        # X is the input data
        # y is the target
        # h = sigmoid(X * coef)
        # where coef are the estimated coefficients
        h = self._sigmoid(np.dot(X, coef))
        return np.mean(-y * np.log(h) - (1 - y) * np.log(1 - h))

    def _compute_gradient(self, X, y, coef):
        # derivative dJ(coef)/dcoef = (1 / n) X'(sigmoid(X * coef) - y)
        # n is the number of samples
        n = X.shape[0]
        h = self._sigmoid(np.dot(X, coef))
        return np.dot(np.transpose(X), h - y) / X.shape[0]

    def _coef_update(self, coef, lr, grad):
        # one gradient step
        # coef_new = coef - lr * grad
        return coef - lr * grad

    def _optimization_step(self, X, y, coef):
        # do the whole optimzation step
        # i.e. computes the loss, gradient and updates coefs
        loss = self._loss(X, y, coef)
        grad = self._compute_gradient(X, y, coef)
        coef_new = self._coef_update(coef, self.lr, grad)
        return (coef_new, loss, grad)

    def _add_intercept(self, X):
        ones = np.ones((X.shape[0], 1))
        return np.concatenate((ones, X), axis=1)

    def _wgt_init(self, X):
        if self.w0 == "zeros":
            coef = np.zeros(X.shape[1])
        else:
            raise NotImplementedError
        return coef

    def fit(self, X, y):
        # fit logistic regression

        # intercept
        if self.intercept:
            X = self._add_intercept(X)
        # init weights
        self.coef_ = self._wgt_init(X)
        # loop
        for iter in range(self.niter):
            opt_step = self._optimization_step(X, y, self.coef_)
            self.coef_, self.loss_, self.grad_ = opt_step

            # print every 100-th iter if desired
            if (iter + 1) % 100 == 0:
                if self.verbose:
                    print(f"Iter {iter+1}/{self.niter} | Loss {self.loss_:.4f}")
        # done
        self.is_fitted = True

    def predict_proba(self, X):
        # intercept
        if self.intercept:
            X = self._add_intercept(X)
        return self._sigmoid(np.dot(X, self.coef_))

    def predict(self, X):
        return (self.predict_proba(X) > 0.5) * 1
