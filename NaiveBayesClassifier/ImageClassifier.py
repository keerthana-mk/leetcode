from __future__ import print_function, division

import warnings
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from future.utils import iteritems
from scipy.stats import multivariate_normal as mvn
from sklearn import datasets
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')
# % matplotlib inline

# Import datasets, classifiers and performance metrics
digits = datasets.load_digits()

# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Split data into 50% train and 50% test subsets
#
X_train, X_test, Y_train, Y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)


class GaussianNaiveBayes(object):
    """
    Gaussian Naive Bayes with smoothing
    Naive Bayes are a group of supervised machine learning classification
    algorithms based on the Bayes theorem. It is a simple classification technique, that scales
    linearly functionality with the data.

    Gaussian Naive Bayes is a variant of Naive Bayes that follows Gaussian normal distribution
    and supports continuous data. Gaussian Naive Bayes assumes independence of the features,
    which means the covariance matrices are diagonal matrices.
    """

    def fit(self, X, Y, smoothing=1e-2):
        self.gaussians = dict()
        self.priors = dict()
        labels = set(Y)
        for c in labels:
            current_x = X[Y == c]
            self.gaussians[c] = {
                'mean': current_x.mean(axis=0),
                'var': current_x.var(axis=0) + smoothing,
            }
            self.priors[c] = float(len(Y[Y == c])) / len(Y)

    def score(self, X, Y):
        """ Compute the accuracy of the model"""
        P = self.predict(X)
        return np.mean(P == Y)

    def predict(self, X):
        N, D = X.shape
        K = len(self.gaussians)
        P = np.zeros((N, K))
        # iteritems() is a dictionary method, which returns a lazily constructed
        # sequence of all (key, value) pairs in the dictionary.
        for c, g in iteritems(self.gaussians):
            mean, var = g['mean'], g['var']  # note covariance matrices are diagonal matrices
            P[:, c] = mvn.logpdf(X, mean=mean, cov=var) + np.log(self.priors[c])  # P(y_i=class|X_i)
        # display(pd.DataFrame(P, columns=self.gaussians.keys()).head()) # posterior probs P(y=class|image)
        return np.argmax(P, axis=1)  # return a column of class predictions; one for each example row


if __name__ == '__main__':
    # Learn the Gaussian Naive Bayes digits classifier on the train subset
    clf = GaussianNaiveBayes()
    t0 = datetime.now()
    clf.fit(X_train, Y_train)
    print("Training time:", (datetime.now() - t0))

    t0 = datetime.now()
    print(f"Train accuracy:{clf.score(X_train, Y_train):.3f}", )
    print("Time to compute train accuracy:", (datetime.now() - t0), "Train size:", len(Y_train))

    t0 = datetime.now()
    print(f"Test accuracy:{clf.score(X_test, Y_test):.3f}")
    print("Time to compute test accuracy:", (datetime.now() - t0), "Test size:", len(Y_test))

    # Predict the value of the digit on the test subset
    predicted = clf.predict(X_test)
    print("\n\n")
    # Visualize predictions
    _, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
    for ax, image, prediction, true_label in zip(axes, X_test, predicted, Y_test):
        ax.set_axis_off()
        image = image.reshape(8, 8)
        ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
        ax.set_title(f"Prediction: {prediction}\ntrue label: {true_label}")