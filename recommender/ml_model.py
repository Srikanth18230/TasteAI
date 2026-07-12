import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("food_recommender/food_data.csv")

le_time = LabelEncoder()
le_order = LabelEncoder()
le_rec = LabelEncoder()

df['time'] = le_time.fit_transform(df['time'])
df['previous_order'] = le_order.fit_transform(df['previous_order'])
df['recommendation'] = le_rec.fit_transform(df['recommendation'])

X = df[['time', 'budget', 'previous_order']]
y = df['recommendation']

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump((model, le_time, le_order, le_rec), "model.pkl")

print("Model created")