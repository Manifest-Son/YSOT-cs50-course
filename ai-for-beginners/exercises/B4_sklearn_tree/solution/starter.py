"""Exercise B4: decision tree on iris with scikit-learn."""

import os


def train(plot=False, out_path="tree_plot.png"):
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    data = load_iris()
    X, y = data.data, data.target
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(Xtr, ytr)
    pred = model.predict(Xte)
    acc = float(accuracy_score(yte, pred))
    if plot:
        plt.figure()
        plt.scatter(Xte[:, 0], Xte[:, 1], c=pred)
        plt.title("Decision tree predictions")
        plt.savefig(out_path)
    return acc


# Try changing: modify this file and re-run the tests.
