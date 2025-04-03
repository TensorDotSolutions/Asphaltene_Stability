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
    st.title("Imran-Tariq Asphaltene Stability Predictor\n(in Crude Oil)")

    # Handling input validation with a loop
    flag: bool = True
    while flag:
        resins = st.number_input("Entering Resins", min_value=1.0, max_value=25.0, step=0.1)
        if not (1.0 <= resins <= 25.0):  # Checking if value is out of range
            st.error("Displaying error: Resin value must be between 1.0 and 25.0.")
            flag = False
        else:
            break  # Exiting loop if input is valid

    flag: bool = True
    while flag:
        asphaltenes = st.number_input("Entering Asphaltenes", min_value=0.1, max_value=25.0, step=0.1)
        if not (0.1 <= asphaltenes <= 25.0):  # Checking if value is out of range
            st.error("Displaying error: Asphaltene value must be between 0.1 and 25.0.")
            flag = False
        else:
            break  # Exiting loop if input is valid

    # Handling prediction on button click
    if st.button("Predicting Stability"):
        predict(resins, asphaltenes)

if __name__ == "__main__":
    main()
