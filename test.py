from main import model_pred

new_data = {'Present_Price': 1.309818,
            'Fuel_Type': 2,
            'Seller_Type': 2,
            'Transmission': 2,
            'Owner': 0,
            'logAge': 0.079181,
            'logKMSDriven': 0.016381,
            'PrecenPriceyLogAge': 0.103713,
            'PrecentPriceyFuel': 2.619636,
            }


def test_predict():
    prediction = model_pred(new_data)
    assert prediction == 1