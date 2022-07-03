from src.features.make_features import make_features

def test_make_features():
    archi = make_features()
    assert  archi == True 