'''
Se toma el archivo de "precios-diarios.csv" ubicado en data_lake/business y se realiza un gráfico de líneas con la librería matplotlib
donde en el eje x se ubica la fecha y en el eje y se ubica el precio, finalmente, se guarda en la ruta data_lake/business/reports/figures/
con el nombre "daily_prices.png".
'''

def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    import pandas as pd
    import matplotlib.pyplot as plt

    precios_diarios = pd.read_csv('data_lake/business/precios-diarios.csv', sep=',', header=0, index_col=None)
    precios_diarios['fecha'] = pd.to_datetime(precios_diarios["fecha"])
    x = precios_diarios.fecha
    y = precios_diarios.precio
    plt.plot(x, y, 'c')
    plt.title('Promedio de Precios Diarios')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(rotation='vertical')
    plt.savefig("data_lake/business/reports/figures/daily_prices.png")

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    make_daily_prices_plot()

    doctest.testmod()
    
