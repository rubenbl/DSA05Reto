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

@st.cache
def buscarEmpleadoPorID(texto):
    df_tmp = df_empleados[df_empleados['Employee_ID'].str.upper().str.contains(texto)]
    return df_tmp

@st.cache
def buscarEmpleadoPorHometown(texto):
    df_tmp = df_empleados[df_empleados['Hometown'].str.upper().str.contains(texto)]
    return df_tmp

@st.cache
def buscarEmpleadoPorUnit(texto):
    df_tmp = df_empleados[df_empleados['Unit'].str.upper().str.contains(texto)]
    return df_tmp

@st.cache
def buscarEmpleadoPorEducationLevelCaseSensitive(texto):
    
    df_tmp = df_empleados.query(' (Education_Level == ',int(text),' )') 
    #df_tmp = df_empleados[df_empleados['Education_Level'].str.contains(texto)]
    return df_tmp

@st.cache
def buscarEmpleadoPorUnitCaseSensitive(texto):
    df_tmp = df_empleados[df_empleados['Unit'].str.contains(texto)]
    return df_tmp

# ###############################################
# Main 
# ###############################################

# Sección - Pre-carga de datos.
df_empleados = cargarDatos(500)

# Sección - Mostrar/ocultar dataframe
if st.sidebar.checkbox('Mostrar/ocultar el dataframe'):
    st.subheader('dataframe (employees)')
    st.write(df_empleados)

# Sección - Búsqueda por ID (cada de texto)
inputEmpleadoID = st.sidebar.text_input('Busqueda por "Employee_ID" : ')
btnBuscarEmpleadoID = st.sidebar.button('Buscar ID')

if (btnBuscarEmpleadoID):
   df_filtroEmpleadosID = buscarEmpleadoPorID(inputEmpleadoID.upper())
   contador = df_filtroEmpleadosID.shape[0] 
   st.write(f"Total de empleados identificados : {contador}")
   st.write(df_filtroEmpleadosID)

# Sección - Búsqueda por Hometown (cada de texto)
inputEmpleadoHometown = st.sidebar.text_input('Busqueda por "Hometown" : ')
btnBuscarEmpleadoHometown = st.sidebar.button('Buscar Hometown')

if (btnBuscarEmpleadoHometown):
   df_filtroEmpleadosHometown = buscarEmpleadoPorHometown(inputEmpleadoHometown.upper())
   contador = df_filtroEmpleadosHometown.shape[0] 
   st.write(f"Total de empleados identificados : {contador}")
   st.write(df_filtroEmpleadosHometown)

# Sección - Búsqueda por Unit (cada de texto)
inputEmpleadoUnit = st.sidebar.text_input('Busqueda por "Unit" : ')
btnBuscarEmpleadoUnit = st.sidebar.button('Buscar Unit')

if (btnBuscarEmpleadoUnit):
   df_filtroEmpleadosUnit = buscarEmpleadoPorUnit(inputEmpleadoUnit.upper())
   contador = df_filtroEmpleadosUnit.shape[0] 
   st.write(f"Total de empleados identificados : {contador}")
   st.write(df_filtroEmpleadosUnit)

# Sección - Búsqueda por Education_Level (selectedbox)
selectedboxEducationLevel = st.sidebar.selectbox("Seleccionar Education_Level", df_empleados['Education_Level'].unique())
btnBuscarEmpleadoEducationLevelPorSelectedBox = st.sidebar.button('Buscar empleado por "Education_Level"')

if (btnBuscarEmpleadoEducationLevelPorSelectedBox):
   df_filtroEmpleadosEducationLevel = buscarEmpleadoPorEducationLevelCaseSensitive(selectedboxEducationLevel)
   contador = df_filtroEmpleadosEducationLevel.shape[0]  
   st.write(f"Total de empleados identificados : {contador}")
   st.dataframe(df_filtroEmpleadosEducationLevel)
   
# Sección - Búsqueda por Unit (selectedbox)
selectedboxUnit = st.sidebar.selectbox("Seleccionar Unit", df_empleados['Unit'].unique())
btnBuscarEmpleadoUnitPorSelectedBox = st.sidebar.button('Buscar empleado por "Unit"')

if (btnBuscarEmpleadoUnitPorSelectedBox):
   df_filtroEmpleadosUnit = buscarEmpleadoPorUnitCaseSensitive(selectedboxUnit)
   contador = df_filtroEmpleadosUnit.shape[0]  
   st.write(f"Total de empleados identificados : {contador}")
   st.dataframe(df_filtroEmpleadosUnit)
