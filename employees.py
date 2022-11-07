import streamlit as st
import pandas as pd
import numpy as np

st.title('Empleados')

# ###############################################
# Definición de funciones
# ###############################################
@st.cache
def cargarDatos(nrows):
    data = pd.read_csv('Employees.csv', nrows=nrows)
    return data

def buscarEmpleadoPorID(texto):
    df_tmp = data[data['Employee_ID'].str.upper().str.contains(texto)]
    return df_tmp

# ###############################################
# Main 
# ###############################################

df_empleados = cargarDatos(500)

if st.sidebar.checkbox('Mostrar/ocultar el dataframe'):
    st.subheader('dataframe (employees)')
    st.write(df_empleados)

inputEmpleadoID = st.sidebar.text_input('Busqueda por "Employee_ID" : ')
btnBuscarEmpleadoID = st.sidebar.button('Buscar')

if (btnBuscarEmpleadoID):
   df_filtroEmpleadosID = buscarEmpleadoPorID(inputEmpleadoID.upper())
   contador = df_filtroEmpleadosID.shape[0] 
   st.write(f"Total de empleados identificados : {contador}")
   st.write(df_filtroEmpleadosID)
    
   
