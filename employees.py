import streamlit as st
import pandas as pd
import numpy as np

st.title('Empleados')

@st.cache
def cargarDatos(nrows):
    data = pd.read_csv('Employees.csv', nrows=nrows)
    return data

df = cargarDatos(500)
