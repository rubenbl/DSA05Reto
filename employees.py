import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
    df_tmp = df_empleados.query(' (Education_Level == @texto ) ') 
    return df_tmp

@st.cache
def buscarEmpleadoPorHometownCaseSensitive(texto):
    df_tmp = df_empleados.query(' (Hometown == @texto ) ') 
    return df_tmp

@st.cache
def buscarEmpleadoPorUnitCaseSensitive(texto):
    df_tmp = df_empleados.query(' (Unit == @texto ) ') 
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
   st.write("\n10. En el sidebar incluir un control selectedbox que permita filtrar los empleados por su nivel educativo, mostrar el dataframe filtrado y total de empleados. Nota: Usar funciones con cache.")
   st.write(f"\nTotal de empleados identificados : {contador}")
   st.dataframe(df_filtroEmpleadosEducationLevel)
   
# Sección - Búsqueda por Hometown (selectedbox)
selectedboxHometown = st.sidebar.selectbox("Seleccionar Hometown", df_empleados['Hometown'].unique())
btnBuscarEmpleadoHometownPorSelectedBox = st.sidebar.button('Buscar empleado por "Hometown"')

if (btnBuscarEmpleadoHometownPorSelectedBox):
   df_filtroEmpleadosHometown = buscarEmpleadoPorHometownCaseSensitive(selectedboxHometown)
   contador = df_filtroEmpleadosHometown.shape[0]  
   st.write("\n11. En el sidebar crear un control selectedbox con las ciudades que participaron en el estudio, mostrar los empleados por ciudad en un dataframe filtrado y total de empleados. Nota: Usar funciones con cache.")
   st.write(f"\nTotal de empleados identificados : {contador}")
   st.dataframe(df_filtroEmpleadosHometown)

# Sección - Búsqueda por Unit (selectedbox)
selectedboxUnit = st.sidebar.selectbox("Seleccionar Unit", df_empleados['Unit'].unique())
btnBuscarEmpleadoUnitPorSelectedBox = st.sidebar.button('Buscar empleado por "Unit"')

if (btnBuscarEmpleadoUnitPorSelectedBox):
   df_filtroEmpleadosUnit = buscarEmpleadoPorUnitCaseSensitive(selectedboxUnit) 
   contador = df_filtroEmpleadosUnit.shape[0]  
   st.write("\n12. Crear un selectedbox para filtrar por la unidad funcional (Unit) a la que pertenece. Nota: Usar funciones con cache.")
   st.write(f"Total de empleados identificados : {contador}")
   st.dataframe(df_filtroEmpleadosUnit)

# Sección - Mostrar/ocultar histograma
if st.sidebar.checkbox('Mostrar/ocultar histograma'):
    st.subheader('Histograma')
    st.write("\n13. Crear un histograma de los empleados agrupados por edad. ")
    # Grafico: Seaborn
    grafico = plt.figure(figsize=(10, 5))
    sns.histplot(x=df_empleados['Age'])
    st.pyplot(grafico)

# Sección - Mostrar/ocultar histograma
if st.sidebar.checkbox('Mostrar/ocultar grafica de frecuencias'):
    st.subheader('Grafica de frecuencias')
    st.write("\n14. Crear una gráfica de frecuencias para las unidades funcionales (Unit) para conocer cuántos empleados hay en cada Unidad. ")
    # Grafico: Seaborn
    grafico = plt.figure(figsize=(10, 5))
    sns.countplot(y='Unit', data=df_empleados, order=df_empleados['Unit'].value_counts().index)
    plt.xticks(rotation=90)
    st.pyplot(grafico)
    # Tabla resumen
    #df_empleadosResumen = df_empleados[['Employee_ID','Unit']].groupby(['Unit']).count()
    #df_empleadosResumen.sort_values('Employee_ID', ascending=False)
    #st.dataframe(df_empleadosResumen)
    
# Sección - Mostrar/ocultar gráfico mayor índice de deserción
if st.sidebar.checkbox('Mostrar/ocultar gráfico índice de deserción'):
    st.subheader('Grafico')
    st.write("\n15. Analizar los datos con una gráfica que nos permita visualizar las ciudades (Hometown) que tienen el mayor índice de deserción. ")
    # Grafico: 
    df_empleadosResumen = df_empleados.groupby(['Hometown']).mean()
    df_empleadosResumen = df_empleadosResumen.sort_values('Hometown', ascending=True)['Attrition_rate']
    st.line_chart(df_empleadosResumen)
    st.dataframe(df_empleadosResumen)
    
    
