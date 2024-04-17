import pandas as pd

data = pd.read_csv("./assets/edades-30Alumnos.csv")

""" 
    Defino la función que realiza el análisis estadístico
    que recibe como parámetro el DataFrame y el nombre de la columna
    que contiene los datos a analizar.
"""
def analisis_estadistico(data: pd.DataFrame, col: str) -> pd.DataFrame:


    # Verifico que el parámetro data sea de tipo DataFrame.
    assert isinstance(data, pd.DataFrame), "El DataFrame no es de tipo DataFrame"    
    # Verifico que la columna exista en el DataFrame.
    assert col in data.columns, f"La columna {col} no existe en el DataFrame"
    # Verifico que la columna sea de tipo numérico.
    assert data[col].dtype in [
        "int64",
        "float64",
    ], f"El tipo de dato de la columna {col} no es numérico"    

    # Creo un DataFrame vacío.
    data_frame = pd.DataFrame()

    # Agrego los valores únicos en la columna x.
    data_frame["x"] = data[col].sort_values().unique()
    # calculo el fi: Frecuencia absoluta de cada valor en la lista.
    data_frame["fi"] = data[col].groupby(data[col]).size().values
    # calculo el Fi: Frecuencia acumulada.
    data_frame["Fi"] = data_frame["fi"].cumsum()

    # calculo el  ri: Frecuencia relativa, que se calcula dividiendo 
    # la frecuencia absoluta de cada valor entre el tamaño total de la muestra.
    data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()
    # Ri: Frecuencia relativa acumulada, la suma acumulada de las frecuencias relativas.
    data_frame["Ri"] = data_frame["ri"].cumsum()

    # pi: Probabilidad, que se obtiene dividiendo la frecuencia absoluta 
    # de cada valor entre el tamaño total de la muestra.
    data_frame["pi%"] = (data_frame["ri"] * 100).round(2)

    # Pi: Probabilidad acumulada, la suma acumulada de las probabilidades.
    data_frame["Pi%"] = (data_frame["Ri"] * 100).round(2)

    #retorno el dataFrame con el análisis estadístico como diccionario.
    return data_frame.to_dict()


print(analisis_estadistico(data, "edad"))
