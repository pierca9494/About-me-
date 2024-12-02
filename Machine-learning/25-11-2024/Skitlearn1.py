from sklearn.datasets import load_iris



data= load_iris()
X = data.data  # le caratteristiche
y = data.target  # le etichette



from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X) 

# print(X_scaled)

# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X, y)
# predictions = model.predict(X)
# print(predictions)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
predictions = knn.predict(X)
print(predictions)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)