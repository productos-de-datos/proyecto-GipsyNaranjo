def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    import pickle
    import pandas as pd
    
    pickled_model = pickle.load(open('models/precios-diarios.pickle', 'rb'))
    df = pd.DataFrame(pickled_model)
    #print(pickled_model)
    #pickled_model.predict(X_test)

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
