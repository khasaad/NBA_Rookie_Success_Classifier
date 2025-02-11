import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score, accuracy_score, precision_score, f1_score


class ScoreClassifier:
    def __init__(self, classifier, dataset, labels, n_splits=3, random_state=50):
        """
        Initializes the evaluator with the classifier, dataset, labels, and cross-validation parameters.
        """
        self.classifier = classifier
        self.labels = labels
        self.dataset = dataset
        self.n_splits = n_splits
        self.random_state = random_state
        self.recall = 0
        self.accuracy = 0
        self.precision = 0
        self.f1score = 0
        self.confusion_mat = np.zeros((2, 2))

    def __call__(self):
        """
        Makes the instance callable to perform evaluation and print results.
        """
        self.evaluate()
        self.print_results()

    def evaluate(self):
        """
        Performs cross-validation and computes the confusion matrix, recall score, accuracy, precision and F1 score.
        """
        kf = KFold(n_splits=self.n_splits, random_state=self.random_state, shuffle=True)

        for training_ids, test_ids in kf.split(self.dataset):
            training_set = self.dataset[training_ids]
            training_labels = self.labels[training_ids]
            test_set = self.dataset[test_ids]
            test_labels = self.labels[test_ids]

            self.classifier.fit(training_set, training_labels)
            predicted_labels = self.classifier.predict(test_set)

            self.confusion_mat += confusion_matrix(test_labels, predicted_labels)
            self.recall += recall_score(test_labels, predicted_labels)
            self.accuracy += accuracy_score(test_labels, predicted_labels)
            self.precision += precision_score(test_labels, predicted_labels)
            self.f1score += f1_score(test_labels, predicted_labels)

        self.recall /= self.n_splits
        self.accuracy /= self.n_splits
        self.precision /= self.n_splits
        self.f1score /= self.n_splits

    def print_results(self):
        """
        Prints the confusion matrix, recall score, accuracy, precision and F1 score.
        """
        print("Confusion matrix :")
        print(self.confusion_mat)
        print("Recall : ", self.recall)
        print("Accuracy : ", self.accuracy)
        print("Precision : ", self.precision)
        print("F1 score : ", self.f1score)
