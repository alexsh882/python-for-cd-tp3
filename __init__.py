import pandas as pd

data: list[int] = [
    19,
    29,
    19,
    22,
    23,
    19,
    30,
    19,
    19,
    19,
    20,
    20,
    20,
    18,
    22,
    19,
    34,
    34,
    21,
    21,
    22,
    28,
    29,
    19,
    20,
    19,
    25,
    28,
    21,
    22,
]


def analisis_estadistico(data: list[int]) -> pd.DataFrame:
    """
    Función que realiza el análisis estadístico
    que recibe como parámetro el DataFrame y el nombre de la columna
    que contiene los datos a analizar.
    """
    # Verifico que los valores de la lista sean de tipo numérico.
    assert all(
        isinstance(x, int) for x in data
    ), "No todos los valores de la lista no son numéricos"

    # Creo un DataFrame vacío.
    list_data_frame = pd.DataFrame(data, columns=["ages"])
    data_frame = pd.DataFrame()

    # Agrego los valores únicos en la columna x.
    data_frame["x"] = list_data_frame["ages"].sort_values().unique()
    # calculo el fi: Frecuencia absoluta de cada valor en la lista.
    data_frame["fi"] = list_data_frame["ages"].groupby(list_data_frame["ages"]).size().values
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

    # retorno el dataFrame con el análisis estadístico.
    return data_frame


print(analisis_estadistico(data))
