# Esercizio:

# Utilizzando il dataset "Wine" disponibile in scikit-learn, sviluppa un modello di classificazione per prevedere la classe del vino basandoti sulle sue caratteristiche chimiche. Esegui una ricerca degli iperparametri utilizzando GridSearchCV e valuta le prestazioni del modello utilizzando la validazione incrociata.



# Istruzioni:

# Carica il dataset "Wine" utilizzando sklearn.datasets.load_wine().
# Esplora i dati per comprendere le caratteristiche e le classi presenti.
# Suddividi il dataset in set di training e test.
# Crea un modello di classificazione utilizzando RandomForestClassifier.
# Definisci una griglia di iperparametri, ad esempio variando il numero di stimatori (n_estimators), la profondità massima (max_depth) e il criterio di qualità dello split (criterion).
# Utilizza GridSearchCV per trovare la migliore combinazione di iperparametri, utilizzando una validazione incrociata con 5 fold.
# Dopo aver trovato i migliori iperparametri, addestra il modello ottimizzato sull'intero set di training.
# Valuta le prestazioni del modello sul test set utilizzando metriche come l'accuratezza, la precisione, il richiamo e l'F1-score.
# Visualizza la matrice di confusione per analizzare in dettaglio le prestazioni del modello.
# Discuta i risultati e l'importanza delle diverse caratteristiche nel modello finale.

# Importa le librerie necessarie
import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from IPython.display import display
import seaborn as sns
import matplotlib.pyplot as plt

# Carica il dataset "Wine"
wine = load_wine()

X = wine.data
y = wine.target

# Crea un DataFrame con i dati e le etichette delle caratteristiche
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)

# Aggiungi la colonna delle classi
df['target'] = wine.target

# Stampa il DataFrame
display(df)

# Esplora i dati
print("Caratteristiche del dataset:", wine.feature_names)
print("Classi del vino:", wine.target_names)
print("Dimensione del dataset:", X.shape)

# Suddividi il dataset in set di training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea un modello di classificazione utilizzando 

rf = RandomForestClassifier(random_state=42) 
# Definisci una griglia di iperparametri 
param_grid = { 'n_estimators': [50, 100, 200], 
              'max_depth': [None, 10, 20, 30],
              'criterion': ['gini', 'entropy'] 
              } 
# Utilizza GridSearchCV per trovare la migliore combinazione di iperparametri 
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='accuracy') 
grid_search.fit(X_train, y_train) # Stampa i migliori iperparametri trovati 
print("Migliori iperparametri:", grid_search.best_params_) 
# Addestra il modello ottimizzato sull'intero set di training 
best_rf = grid_search.best_estimator_ 
best_rf.fit(X_train, y_train) 
# Valuta le prestazioni del modello sul test set 
y_pred = best_rf.predict(X_test) 
accuracy = accuracy_score(y_test, y_pred) 
precision = precision_score(y_test, y_pred, average='weighted') 
recall = recall_score(y_test, y_pred, average='weighted') 
f1 = f1_score(y_test, y_pred, average='weighted') 
print("Accuratezza:", accuracy) 
print("Precisione:", precision) 
print("Richiamo:", recall) 
print("F1-score:", f1) 
# Visualizza la matrice di confusione 
conf_matrix = confusion_matrix(y_test, y_pred) 
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=wine.target_names, yticklabels=wine.target_names) 
plt.xlabel('Predicted') 
plt.ylabel('Actual') 
plt.title('Confusion Matrix') 
plt.show() 
# Discute i risultati e l'importanza delle caratteristiche 
print("Report di classificazione:\n", classification_report(y_test, y_pred, target_names=wine.target_names)) 
feature_importances = pd.Series(best_rf.feature_importances_, index=wine.feature_names).sort_values(ascending=False) 
print("Importanza delle caratteristiche:\n", feature_importances)
