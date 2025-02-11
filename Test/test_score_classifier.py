from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from Classifier_evaluator import ScoreClassifier


def test_evaluate():
    # Create a dataset for testing
    features, labels = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=42)

    # Initialize the classifier (for example LogisticRegression)
    classifier = LogisticRegression()

    # Create an instance of ScoreClassifier
    evaluator = ScoreClassifier(classifier, features, labels)

    # Perform the evaluation
    evaluator.evaluate()

    # Check the confusion matrix has the shape 2x2
    assert evaluator.confusion_mat.shape == (2, 2), "The confusion matrix should be 2x2 of shape"

    # Check recall value is between 0 and 1
    assert 0 <= evaluator.recall <= 1, "Recall should be between 0 and 1"