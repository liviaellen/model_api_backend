from fastapi import FastAPI
from repurchase import *

app = FastAPI()
app.state.model= load_model()
app.state.prep_scaler= load_prep()
@app.get("/")
def read_root():
    return {"test": "This is for code testing ,please check the docs for more info"}

 #input is a string
 #output is only builtin python data type
@app.get("/prep")
def prep(nb_past_orders, avg_basket, total_purchase_cost, avg_quantity, total_quantity, avg_nb_unique_products, total_nb_codes):
    value_to_predict=[nb_past_orders, avg_basket, total_purchase_cost, avg_quantity, total_quantity, avg_nb_unique_products, total_nb_codes]
    scaler = app.state.prep_scaler
    prep_value=scaler.transform([value_to_predict])[0]
    return {'prep_value': list(prep_value)}

@app.get("/predict")
def predict(nb_past_orders, avg_basket, total_purchase_cost, avg_quantity, total_quantity, avg_nb_unique_products, total_nb_codes):
    value_to_predict=[nb_past_orders, avg_basket, total_purchase_cost, avg_quantity, total_quantity, avg_nb_unique_products, total_nb_codes]
    model = app.state.model
    pred=model.predict([value_to_predict])[0]
    return {'prediction': int(pred)}


@app.get("/preppredict")
def prep_and_predict(nb_past_orders, avg_basket, total_purchase_cost, avg_quantity, total_quantity, avg_nb_unique_products, total_nb_codes):
    value_to_predict=[nb_past_orders, avg_basket, total_purchase_cost, avg_quantity, total_quantity, avg_nb_unique_products, total_nb_codes]
    scaler = app.state.prep_scaler
    value_to_predict=scaler.transform([value_to_predict])
    model = app.state.model
    pred=model.predict(value_to_predict)[0]
    return {'prediction': int(pred)}
