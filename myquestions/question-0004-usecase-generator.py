import pandas as pd
import numpy as np

def generar_caso_de_uso_analizar_eficiencia_rutas():
    # 1. Generación de datos aleatorios (Input)
    n = np.random.randint(5, 10)
    umbral = np.random.uniform(0.1, 0.2)
    df_in = pd.DataFrame({
        'ruta_id': [f'R_{i}' for i in range(n)],
        'distancia_km': np.random.uniform(50, 200, n),
        'litros_consumidos': np.random.uniform(5, 40, n)
    })
    
    # 2. Lógica para generar el resultado esperado (Output)
    df_out = df_in.copy()
    df_out['consumo_por_km'] = df_out['litros_consumidos'] / df_out['distancia_km']
    df_out = df_out[df_out['consumo_por_km'] > umbral].copy()
    
    if not df_out.empty:
        # Calculamos el exceso y ordenamos (como pide el ejercicio)
        df_out['exceso'] = (df_out['consumo_por_km'] - umbral) * df_out['distancia_km'] * 5.0
        df_out = df_out.sort_values(by='exceso', ascending=False).reset_index(drop=True)
    
    # --- LO QUE TE FALTABA: EL RETURN ---
    # Debes devolver una tupla con el diccionario de entrada y el objeto de salida
    return {"df": df_in, "umbral_consumo": umbral}, df_out
    # Invocamos la función para obtener el par input/output
entrada, salida = generar_caso_de_uso_analizar_eficiencia_rutas()

print("--- DICCIONARIO DE ENTRADA (INPUT) ---")
print(entrada)

print("\n--- DATAFRAME RESULTANTE (OUTPUT) ---")
print(salida)
