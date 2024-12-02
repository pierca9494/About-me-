import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Predicted labels:", y_pred[:5])
print("Actual labels:", y_test[:5])
accuracy = accuracy_score(y_test, y_pred)



print("Valori di y (target):", y)
print("Etichette corrispondenti:", iris.target_names)
print(f"Accuracy: {accuracy:.2f}")