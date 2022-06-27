"""
Se lee el archivo creado en el python compute_daily_prices.py y se escribe nuevamente en la ruta indicada.
"""

def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
    import pandas as pd

    df_caract = pd.read_csv(r'data_lake/business/precios-diarios.csv',index_col=None,header=0)
    df_caract["fecha"] = pd.to_datetime(df_caract["fecha"]).dt.strftime('%Y-%m-%d')
    df_caract.to_csv("data_lake/business/features/precios-diarios.csv",index=None, header=True)
    return
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
