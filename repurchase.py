import joblib

def load_prep():
    return joblib.load('model/scaler_prep.joblib')

def load_model():
    return joblib.load('model/model.joblib')
