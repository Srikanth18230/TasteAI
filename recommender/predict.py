import joblib

model, le_time, le_order, le_rec = joblib.load("model.pkl")

def predict_food(time, budget, previous_order):
    time_encoded = le_time.transform([time])[0]
    order_encoded = le_order.transform([previous_order])[0]

    prediction = model.predict([[time_encoded, budget, order_encoded]])
    result = le_rec.inverse_transform(prediction)

    return result[0]
print(predict_food("night",300,"biryani"))