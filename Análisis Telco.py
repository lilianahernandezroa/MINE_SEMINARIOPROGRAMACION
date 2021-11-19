#!/usr/bin/env python
# coding: utf-8

# ## ¿Existe relación alguna entre el total de minutos usados con la compañía y el ingreso total de los clientes?
# 
# ### LILIANA PATRICIA HERNANDEZ
# 
# En el desarrollo de este caso introduciremos las librerías pandas, numpy y matplotlib para el preprocesamiento, visualización de un conjunto de datos y el desarrollo de algunas medidas estadísticas descriptivas.
# 
# 
# 
# ##  Introducción 
# 
# La revisión del comportamiento de los clientes en cualquier empresa es de vital importancia para el desarrollo de estrategias  tanto de mejoramiento de productos como de publicidad y toma de decisiones. Evaluaremos la información obtenida de un conjunto de registro obtenidos de una empresa de telecomunicaciones que cuenta con la revisión de las siguientes variables:
# 
# 1. totrev: Ingresos del cliente
# 2. totmou: Total de minutos usados por el cliente
# 3. area: Área geográfica
# 4. creditcd: Indicador de tarjeta de crédito
# 5. eqpdays: Número de días (antigüedad) del equipo actual
# 
# Es importante mencionar que la empresa contiene una gran cantidad de clientes y hacer el análisis uno a uno no es lo  óptimo. Con ayuda de la programación y el análisis de datos, se logrará llegar a conclusiones rápidas y acertadas para encontrar relaciones que a simple vista no son tenidas en cuenta.
# 
# ### ¿Qué se quiere identificar? 
# 
# Teniendo en cuenta la información de la base de datos se quiere identificar si hay una relación entre el total de minutos usados por el cliente con la compañía y el ingreso total de los clientes, es decir, Será posible afirmar que cuando una persona
# tiene un mayor ingreso mayor entonces es mayor la utilización de minutos o todo lo contrario?
# 
# 
# ####  Insumos para tratar este problema
# 
# 
# Teniendo en cuenta que la compañía tenia estándares para la entrega de la información, se dispone de un  conjunto de tablas en formato CSV ordenado de la siguiente manera:
# La información de este conjunto de datos puede encontrase en [aquí](https://www.kaggle.com/abhinav89/telecom-customer?select=Telecom_customer+churn.csv)
# 
# ### Objetivos
# 
# En este caso usted tendrá que cargar varias bases de datos, hará una exploración básica sobre la información y fusionará las distintas bases para tener una visión general del problema. La idea es que desarrolle las siguientes habilidades:
# 
# 1. Manejo de la librería pandas de Python para cargar y leer datos; 
# 2. Ideas elementales para una útil transformación de los datos;
# 3. Construcción y presentación de argumentos válidos que le brindarán una solución para la pregunta expresada más arriba y llegar a una conclusión. 
# 4. Visualización de gráficas elementales que le permitirá entender mejor la información contenida en los datos.
# 
# #### Importación de paquetes
# 
# 
# Una de las mejores opciones para trabajar con datos tabulares en Python es usar el módulo pandas. La librería `pandas` provee estructuras de datos, genera gráficos de alta calidad con `matplotlib` y se integra de buena forma con otras librerías que usan arrays de `numpy`.
# 
# Debemos revisar si la librería se encuentra en nuestro sistema usando el comando 
# 
# ```python
# !pip show librería
# ```
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# ### Carga de información en `pandas`
# 
# Para nuestro  ejercicio usaremos los siguientes conjuntos de datos:
# 
# 1. NEW ENGLAND AREA.csv
# 2. ATLANTIC SOUTH AREA.csv
# 3. NEW YORK CITY AREA.csv
# 4. CHICAGO AREA.csv
# 5. NORTH FLORIDA AREA.csv
# 6. DC-MARYLAND-VIRGINIA AREA.csv
# 7. GREAT LAKES AREA.csv
# 8. NORTHWEST-ROCKY MOUNTAIN AREA.csv
# 9. MIDWEST AREA.csv
# 10. SOUTHWEST AREA.csv
# 11. LOS ANGELES AREA.csv
# 12. HOUSTON AREA.csv
# 13. CALIFORNIA NORTH AREA.csv
# 14. CENTRAL-SOUTH TEXAS AREA.csv
# 15. DALLAS AREA.csv
# 16. PHILADELPHIA AREA.csv
# 17. TENNESSEE AREA.csv
# 18. OHIO AREA.csv
# 19. SOUTH FLORIDA AREA.csv
# 
# Cada uno de estos conjuntos de datos contiene la información de:
# 
# 1. *mou_Mean:* Número medio de minutos de uso mensuales
# 2. *custcare_Mean:* Número medio de llamadas de atención al cliente
# 3. *area:*  Área geografica
# 4. *creditcd:* Indicador de tarjeta de crédito
# 5. *eqpdays:* Número de días (antigüedad) del equipo actual
# 
# Además, se incluye _Credito_dias.csv_ con la información de 2 variables adicionales para los registros las cuales son:
# 
# 1. _creditcd:_ Indicador de tarjeta de crédito
# 2. _eqpdays:_ Número de días (antigüedad) del equipo actual
# 
# Revisaremos inicialmente los datos contenidos en _Credito_dias.csv_ para revisar algunas funciones interesantes de `pandas`, usaremos el comando 
# ```python
# pd.read_csv("archivo.csv")
# ```
# Podemos definir el número de registros a imprimir usando
# ```python
# pd.options.display.min_rows=10
# ````

# In[2]:


df=pd.read_csv("Bases/Credito_dias.csv", sep=",",index_col="Customer_ID")


# El conjunto de datos se encuentra en el `DataFrame` `df`
# 
# sobre el objeto creado podemos usar  algunas funciones  para darnos una idea del comportamiento de la información:
# ```python
# df.head(n)  # imprime los primeros n registros del DataFrame
# df.tail(n)  # imprime los últimos n registros del DataFrame 
# df.shape    # imprime el numero de columnas y filas del DataFrame
# df.columns  # imprime el nombre de las columnas del DataFrame
# df.index    # imprime el indice de los registros del DataFrame
# df.dtypes   # imprime el tipo de cada una de las columnnas del DataFrame
# df.sample(n)# imprime una muestra aleatoria de n registros en el DataFrame
# ```

# In[3]:


display("primeros 3 registros",df.head(3))
display("3 últimos registros",df.tail(3))
display("Columnas:",df.columns)
display("Índices:",df.index)
display("Tipos de registros en el DataFrame",df.dtypes)
display("Muestra aleatoria de 3 registros",df.sample(3))
display("dimensión",df.shape)


# ### Agregar información de múltiples tablas
# 
# Hemos desarrollado un breve resumen estadístico solamente usando la base `Credito_dias.csv`. Realizaremos la combinación de las 19 áreas que nos reportan en los archivos csv. Una forma de lograr esta tarea de agregación es usar el método pd.concat() de pandas. Una entrada en este método puede ser una lista de DataFrames que quiera concatenar. Usaremos un ciclo  `for` sobre cada uno de los archivos de áreas para 
# 

# In[ ]:


df.columns
df.dtypes


# ### Ejercicio 1
# Determinar los percentiles 25, 50 y 75 para las columnas ttomou, totrev, eqpdays

# In[6]:


df.describe(include='all')


# In[4]:


print("Definición de los símbolos de las acciones")
areas = ['ATLANTIC SOUTH AREA',
 'CALIFORNIA NORTH AREA',
 'CENTRAL-SOUTH TEXAS AREA',
 'CHICAGO AREA',
 'DALLAS AREA',
 'DC-MARYLAND-VIRGINIA AREA',
 'GREAT LAKES AREA',
 'HOUSTON AREA',
 'LOS ANGELES AREA',
 'MIDWEST AREA',
 'NEW ENGLAND AREA',
 'NEW YORK CITY AREA',
 'NORTH FLORIDA AREA',
 'NORTHWEST-ROCKY MOUNTAIN AREA',
 'OHIO AREA',
 'PHILADELPHIA AREA',
 'SOUTH FLORIDA AREA',
 'SOUTHWEST AREA',
 'TENNESSEE AREA']
lista_de_df = []
# Bucle sobre los símbolos
print(" --- Inicie el bucle sobre los símbolos --- ")
for i in areas:
    print("Procesando el símbolo: " + i)
    temp_df = pd.read_csv("Bases/" + i + ".csv",index_col="Customer_ID")
    temp_df["area"] = i
    lista_de_df.append(temp_df)
    # Usando un salto de línea al final de esta cadena de caracteres por estética
    print(" --- Bucle completo sobre los símbolos --- \n")
    # Combinando en un solo DataFrame usando el concat
print("Agregando los datos")
agr_df = pd.concat(lista_de_df, axis=0)
print(agr_df.shape)
print("Cabeza del DataFrame agr_df: ")
agr_df.head()


# In[5]:


agr_df.sort_index(axis=0,inplace=True)
agr_df


# In[10]:


df3=df.merge(agr_df,left_index=True,right_index=True,how="inner")


# In[11]:


display("Estructura del dataframe df3",df3.shape)
display("Estructura del dataframe df",df.shape)


# ### Ejercicio 2  
# ¿Cuáles son los 3 registros que no se incluyen en df3 ?
# 

# In[14]:


sin_registros=df.index.isin(df3.index)
df.iloc[~sin_registros,]


# ### Ejercicio 3
# 
# Realice una agrupación por la variable creditcd_x y encuentre el valor de la desviación estándar

# In[16]:


round(df3.groupby("creditcd_x").mean(),2)


# In[18]:


pencentiles50 = df3.groupby("area")["totrev"].quantile(0.5)


# In[19]:


# Loop a través de los símbolos
areas = ['ATLANTIC SOUTH AREA',
 'CALIFORNIA NORTH AREA',
 'CENTRAL-SOUTH TEXAS AREA',
 'CHICAGO AREA',
 'DALLAS AREA',
 'DC-MARYLAND-VIRGINIA AREA',
 'GREAT LAKES AREA',
 'HOUSTON AREA',
 'LOS ANGELES AREA',
 'MIDWEST AREA',
 'NEW ENGLAND AREA',
 'NEW YORK CITY AREA',
 'NORTH FLORIDA AREA',
 'NORTHWEST-ROCKY MOUNTAIN AREA',
 'OHIO AREA',
 'PHILADELPHIA AREA',
 'SOUTH FLORIDA AREA',
 'SOUTHWEST AREA',
 'TENNESSEE AREA'] # registro de las áreas
lista_df = []
# ciclo sobre todos los símbolos
for i in areas:
    print("Etiqueta por área: " + i)
    temp_df = df3[df3["area"] == i] .copy()
    umbral_punto = pencentiles50.loc[i]
    temp_df["Nivel_totrev"] = np.where(temp_df["totrev"] < umbral_punto, "Bajo", "Alto") 
    lista_df.append(temp_df)
df_con_etiquetas = pd.concat(lista_df)


# Ahora podemos hacer una evaluaciónd de como es el comportamiento de los minutos gastados y el nivel de ingresos de los clientes

# ### ¿Existe relación alguna entre el total de minutos usados con la compañía y el ingreso total de los clientes?
# 
# Para explorar la relación entre el nivel de total de ingresos y el número promedio de llamadas, agrupemos por
# Nivel_totrev y miremos ingreso total promedio por cada +area geográfica.
# 
# 

# In[20]:


round(df_con_etiquetas.groupby(['area','Nivel_totrev'])[['totmou']].mean(),2)


# ### Ejercicio 4
# 
# 
# Escriba el código para categorizar  el total de ingresos  baja, media y alta volatilidad, donde:
# 
# `
# si totrev > (percentil 75 de totrev para el área dada):
# Nivel_totrev = 'Alto'
# o si VolStat > (percentil 25 de totrev para el área dada):
# Nivel_totrev  = 'Medio'
# de lo contrario:
# Nivel_totrev  = 'Bajo'`

# In[21]:


pencentiles25 = df3.groupby("area")["totrev"].quantile(0.25) # percentil 50
pencentiles75 = df3.groupby("area")["totrev"].quantile(0.75)


# In[22]:


#areas


# In[23]:


lista_df = []
# ciclo sobre todos los símbolos
for i in areas:
    print("Etiqueta por área: " + i)
    temp_df = df3[df3["area"] == i] .copy()
    umbral_punto1 = pencentiles25.loc[i]
    umbral_punto2 = pencentiles75.loc[i]
    lv=[]
    for i in temp_df['totrev']:
        if i<umbral_punto1:
            lv.append('Bajo')
        elif i<umbral_punto2:
            lv.append('Medio')
        else:
            lv.append('Alto')
    temp_df['Nivel']=lv
    lista_df.append(temp_df)
df_con_etiquetas = pd.concat(lista_df)
# realice el ejercicio en este espacio


# In[24]:


round(df_con_etiquetas.groupby(['area','Nivel'])[['totmou']].mean(),2)


# ### Visualización de total de llamadas y total de ingresos
# 
# Ya hemos respondido satisfactoriamente a nuestra pregunta original. Sin embargo, no es necesario solamente
# analizar los datos en formato tabular. Python contiene una funcionalidad que le permite analizar sus datos
# visualmente también.
# 
# Usaremos la funcionalidad de pandas sobre la librería estándar de graficación de Python, `matplotlib`. Vamos
# a importar la librería e instruir a Jupyter que muestre los gráficos en línea (es decir, mostrar los gráficos en
# la pantalla del cuaderno para que podamos verlos mientras ejecutamos el código):
# 
# 

# In[25]:


modules = dir()
print(modules)


# In[26]:


import matplotlib.pyplot as plt
# Graficar en el cuaderno
get_ipython().run_line_magic('matplotlib', 'inline')


# #### Histograma

# In[28]:


plt.style.use('ggplot')
plt.hist(df3["totrev"],bins=13,color="green")
plt.title('Histograma de ingresos del cliente (totrev)')
plt.xlabel("totrev");plt.ylabel("Frecuencia")
plt.show()


# #### Boxplot

# In[30]:


plt.style.use('ggplot')
plt.boxplot(df3["totrev"])
plt.title('Boxplot de ingresos del cliente(totrev)')
plt.show()


# #### Gráficas a partir de `groupby`

# In[31]:


df4=round(df_con_etiquetas.groupby(['area','Nivel'])[['totmou']].mean(),2)


# In[32]:


df4.plot(kind='barh',figsize=(10,8),color='purple')
plt.show()


# In[33]:


df3["creditcd_x"].value_counts().plot(kind="pie", label =' Tiene Tarjeta de Credito?')
plt.show()


# *Revisando la relación entre las dos variables `totrev` y `totmou`*

# In[34]:


df3.plot(kind="scatter",x='totrev',y='totmou',c='purple')


# ### `Seaborn`

# In[35]:


import seaborn as sns
sns.boxplot(df3["totrev"],orient='v')
plt.title('Boxplot Ingresos del cliente (totrev)')
plt.show()


# ### Gráficas de parcela 

# In[36]:


plt.figure(figsize=(116,4))
sns.pairplot(data=df3, hue='creditcd_x', vars=['totrev','totmou','eqpdays'])
plt.title("Parcelas")
plt.show()


# ### Ejercicio 5
# 
# Realice un  boxplot para la variable totmou segmentado por las variable  credict_x y Nivel_totrev

# In[44]:


df_con_etiquetas.info()


# In[48]:


df5=round(df_con_etiquetas.groupby(['creditcd_x','Nivel'])[['totmou']].sum(),2)
df5


# In[49]:


plt.style.use('ggplot')
plt.boxplot(df5["totmou"])
plt.title('Boxplot de uso en minutos por cliente (totmou)')
plt.show()

