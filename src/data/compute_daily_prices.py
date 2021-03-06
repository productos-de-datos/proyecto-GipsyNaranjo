"""
Tome el archivo procesado "precios-horarios.csv" con pandas, porteriormente, con un group byde fecha, calcule el 
promedio de los precios de las horas por dia y adicional exporte a data_lake/business/
"""

def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional

    """
    import pandas as pd

    df = pd.read_csv("data_lake/cleansed/precios-horarios.csv",index_col=None,header=0)
    df =  df[["fecha", "precio"]]
    preciosdiarios = df.groupby("fecha").mean({"precio"})
    df.to_csv("data_lake/business/precios-diarios.csv",index=None, header=True)
    return


    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    compute_daily_prices()
    doctest.testmod()
