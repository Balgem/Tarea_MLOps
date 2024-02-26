from main import model_pred

new_data = {'TV': 100.3,
            }


def test_predict():
    prediction = model_pred(new_data)
