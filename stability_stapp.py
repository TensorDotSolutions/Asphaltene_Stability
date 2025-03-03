import streamlit as st
import pandas as pd
import joblib

# Loading the trained model
model = joblib.load('optimized_extra_tree_model.pkl')  # Ensuring correct file path

def predict(resins, asphaltenes):
    """Predicting stability based on resin and asphaltene values."""
    # Creating a DataFrame for prediction
    df = pd.DataFrame({'Resins': [resins], 'Asphaltenes': [asphaltenes]})

    # Making prediction
    prediction = model.predict(df)  # Returning an array

    # Displaying prediction
    stability = prediction[0]  # Extracting single value from array
    st.success(f"**{stability.upper()}**")

def main():
    st.title("Asphaltene Stability Predictor\n(in Crude Oil)")

    # Adding input fields using sliders
    resins = st.slider("Selecting Resins (0.01 - 25.0)", min_value=0.01, max_value=25.0, value=1.0, step=0.01)
    asphaltenes = st.slider("Selecting Asphaltenes (0.01 - 25.0)", min_value=0.01, max_value=25.0, value=0.1, step=0.01)

    # Handling prediction on button click
    if st.button("Predicting Stability"):
        predict(resins, asphaltenes)

if __name__ == "__main__":
    main()
