import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

# Load the model
model = load_model('Stability new')  # Replace with your model path

def predict(resins, asphaltenes):
    """Predicts stability based on resin and asphaltene values."""
    # Create a DataFrame for prediction
    data = {'Resins': [resins], 'Asphaltenes': [asphaltenes]}
    df = pd.DataFrame(data)

    # Make prediction
    prediction = predict_model(model, data=df)

    # Display prediction in bold
    stability = prediction['prediction_label'][0]
    st.success(f"**{stability.upper()}**")

def main():
    st.title("Asphaltene Stability Predictor\n(in Crude Oil)")

    flag:bool = True
    while flag:
        resins = st.number_input("Resins (1.0 - 25.0)", min_value=1.0, max_value=25.0, step=0.1)
        # Input validation
        if not (1 <= resins <= 25):
            st.error("Resin value must be between 1. and 25.")
            flag = False
        else:
            break

    flag:bool = True
    while flag:
        asphaltenes = st.number_input("Asphaltenes (0.1 - 25.0)", min_value=0.1, max_value=25.0, step=0.1)
        if not (0.1 <= asphaltenes <= 25):
            st.error("Asphaltene value must be between 0.1 and 25.")
            flag = False
        else:
            break
        
    if st.button("Predict"):
        predict(resins, asphaltenes)
        
if __name__ == "__main__":
    main()