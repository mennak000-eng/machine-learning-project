import streamlit as st
import joblib
import numpy as np
model = joblib.load('best_random_forest_model.pkl')
st.title("Protein Structure Prediction App")
st.write("Enter the protein structure features below:")
matthews = st.number_input("Matthews Coefficient")
solvent = st.number_input("Percent Solvent Content")
ph = st.number_input("pH")
temp = st.number_input("Temperature (K)")
molecular_weight = st.number_input("Molecular Weight")
sequence_length = st.number_input("Polymer Entity Sequence Length")
ligand_mw = st.number_input("Ligand MW")
residues = st.number_input("Number of Residues")
chains = st.number_input("Number of Chains")
helix = st.number_input("Helix")
sheet = st.number_input("Sheet")
coil = st.number_input("Coil")
structure_complexity = helix + sheet + coil
input_data = np.array([[
    matthews,
    solvent,
    ph,
    temp,
    molecular_weight,
    sequence_length,
    ligand_mw,
    residues,
    chains,
    helix,
    sheet,
    coil,
    structure_complexity
]])
if st.button("Predict Average B Factor"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Average B Factor: {prediction[0]:.2f}")