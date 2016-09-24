# In this exercise we'll examine a learner which has high bias, and is incapable of
# learning the patterns in the data.
# Use the learning curve function from sklearn.learning_curve to plot learning curves
# of both training and testing error.

from sklearn.linear_model import LinearRegression
from sklearn.learning_curve import learning_curve
import matplotlib.pyplot as plt
from sklearn.metrics import explained_variance_score, make_scorer
from sklearn.cross_validation import KFold
import numpy as np

# Set the learning curve parameters; you'll need this for learning_curves
size = 1000
cv = KFold(size, shuffle=True)
score = make_scorer(explained_variance_score)

# Create a series of data that forces a learner to have high bias
X = np.reshape(np.random.normal(scale=2, size=size), (-1, 1))
y = np.array([[1 - 2 * x[0] + x[0] ** 2] for x in X])


def plot_curve():
    reg = LinearRegression()
    reg.fit(X, y)
    print "Regressor score: {:.4f}".format(reg.score(X, y))

    # TODO: Use learning_curve imported above to create learning curves for both the
    #       training data and testing data. You'll need 'size', 'cv' and 'score' from above.

    training_sizes, training_scores, testing_scores = learning_curve(reg, X, y,
                                                                     cv=cv, scoring=score)
    training_scores_mean = np.mean(training_scores, axis=1)
    testing_scores_mean = np.mean(testing_scores, axis=1)

    # TODO: Plot the training curves and the testing curves
    #       Use plt.plot twice -- one for each score. Be sure to give them labels!
    plt.plot(training_sizes, training_scores_mean, 'o-', color='r', label="Training Score")
    plt.plot(training_sizes, testing_scores_mean, 'o-', color='g', label='Cross-validatrion score')

    # Plot aesthetics
    plt.ylim(0, 1)
    plt.ylabel("Curve Score")
    plt.xlabel("Training Points")
    plt.legend(bbox_to_anchor=(1.1, 1.1))
    plt.show()

plot_curve()