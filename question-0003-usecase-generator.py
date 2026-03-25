from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def generar_caso_de_uso_entrenar_clasificador_paneles():
    # Generar datos aleatorios
    n_samples = np.random.randint(20, 50)
    n_features = 2 # Voltaje y Temperatura
    
    X = np.random.rand(n_samples, n_features) * 100
    # Generar etiquetas y basadas en una lógica simple + ruido
    y = (X[:, 0] < 40).astype(int) 
    
    # Lógica para el output esperado
    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X)
    
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_scaled, y)
    predicciones = clf.predict(X_scaled)
    
    return {
        "X": X,
        "y": y
    }, (clf, predicciones)

# Comprobación
inputs, output = generar_caso_de_uso_entrenar_clasificador_paneles()
print("Inputs (Primeras 2 filas de X):", inputs['X'][:2])
print("Modelo generado:", output[0])
print("Predicciones (Primeras 5):", output[1][:5])
