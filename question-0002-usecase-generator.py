import pandas as pd
import numpy as np

def generar_caso_de_uso_priorizar_reabastecimiento():
    # Componente aleatorio para el tamaño y valores
    n_filas = np.random.randint(5, 10)
    stock_umbral = np.random.randint(10, 20)
    demanda_umbral = np.random.randint(30, 50)
    
    productos = [f"Prod_{i}" for i in range(n_filas)]
    stock = np.random.randint(5, 30, size=n_filas)
    demanda = np.random.randint(20, 70, size=n_filas)
    
    df_input = pd.DataFrame({
        'producto': productos,
        'stock_actual': stock,
        'demanda_mensual': demanda
    })
    
    # Lógica para generar el output esperado
    df_res = df_input[(df_input['stock_actual'] < stock_umbral) & 
                      (df_input['demanda_mensual'] > demanda_umbral)].copy()
    
    if not df_res.empty:
        df_res['indice_prioridad'] = (df_res['demanda_mensual'] - df_res['stock_actual']) / df_res['demanda_mensual']
        df_res = df_res.sort_values(by='indice_prioridad', ascending=False).reset_index(drop=True)
    else:
        df_res = pd.DataFrame(columns=['producto', 'stock_actual', 'demanda_mensual', 'indice_prioridad'])

    return {
        "df": df_input,
        "stock_umbral": stock_umbral,
        "demanda_umbral": demanda_umbral
    }, df_res

# Comprobación
inputs, output = generar_caso_de_uso_priorizar_reabastecimiento()
print("Inputs Aleatorios:", inputs)
print("Output Esperado:\n", output)
