# Importar las bibliotecas necesarias
import pandas as pd  # Para trabajar con datos en formato tabular
from sklearn.model_selection import train_test_split  # Para dividir el conjunto de datos en entrenamiento y prueba
from sklearn.feature_extraction.text import CountVectorizer  # Para convertir texto en características numéricas
from nltk.corpus import stopwords  # Lista de palabras vacías en español
from sklearn.metrics import accuracy_score # Calcular la precisión del modelo
from sklearn.naive_bayes import MultinomialNB # Importar el modelo de Naive Bayes Multinomial

# Leer el conjunto de datos desde un archivo CSV
datafull = pd.read_csv('/home/cscc/Documents/Proyects/Trabajo-de-grado/media/entrenamiento.csv', delimiter=',')

# Crear un DataFrame con los datos leídos
datafull_set = pd.DataFrame(data=datafull)

# Extraer las columnas "Title" (texto) y "Category" (categoría) como variables de entrada (X) y objetivo (y)
X, y = datafull_set['title'], datafull_set['category']

# Definir el número máximo de características a extraer (tamaño del vocabulario)
max_features = 1000

# Crear un vectorizador de recuento de palabras con las configuraciones específicas
cou_vectorizer = CountVectorizer(max_features=max_features, stop_words=stopwords.words('spanish'), ngram_range=(1, 2))

# Aplicar el vectorizador para convertir el texto en una representación numérica
X_counts = cou_vectorizer.fit_transform(X)

# Convertir la representación dispersa a una matriz densa
X = X_counts.toarray()

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.25)

# Crear una instancia del clasificador Multinomial Naive Bayes
classifier = MultinomialNB()

# Entrenar el modelo con los datos de entrenamiento
classifier.fit(X_train, y_train)

# Realizar predicciones en los datos de prueba
y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

# Imprimir la precisión del modelo
print("Accuracy:", accuracy)

# Definir una lista de prueba con una sola frase
test = ['ingeniero de datos']

# Aplicar el vectorizador al dato de prueba
X_counts = cou_vectorizer.transform(test)
X = X_counts.toarray()

# Realizar una predicción en el dato de prueba
predic = classifier.predict(X)

# Imprimir la categoría predicha
print(predic[0])
