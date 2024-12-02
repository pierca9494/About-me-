from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Caricamento del dataset Wine
data = load_wine()
X = data.data
y = data.target

# Esplorazione dei dati
print(f"Feature names: {data.feature_names}")
print(f"Target names: {data.target_names}")
print(f"Shape of dataset: {X.shape}")
print(f"Classes distribution: {np.bincount(y)}")

# Suddivisione del dataset in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# skf = StratifiedKFold(n_splits= 5, shuffle= True, random_state= 42 )

# Creazione del modello base
clf = RandomForestClassifier(random_state=42)

# Definizione della griglia di iperparametri
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'criterion': ['gini', 'entropy'],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Ricerca degli iperparametri con GridSearchCV
grid_search = GridSearchCV(estimator=clf, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Migliori iperparametri trovati
print("Best Parameters:", grid_search.best_params_)

# Valutazione del modello ottimizzato
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# Calcolo delle metriche di valutazione
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")

# Matrice di confusione
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=data.target_names, yticklabels=data.target_names)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()

# Importanza delle caratteristiche
feature_importances = pd.DataFrame({
    'Feature': data.feature_names,
    'Importance': best_model.feature_importances_
}).sort_values(by='Importance', ascending=False)

print("Feature Importances:")
print(feature_importances)

# Visualizzazione delle importanze
sns.barplot(x='Importance', y='Feature', data=feature_importances)
plt.title("Feature Importances")
plt.show()

# Discussione dei risultati
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))
