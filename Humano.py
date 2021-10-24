#!/usr/bin/env python
# coding: utf-8

# In[9]:


import time
from datetime import date
from datetime import datetime


# In[2]:


class Humano(): #Creamos la clase Humano
    def __init__(self, edad, nombre, ocupacion,horas_laboradas,peso, estatura, fecha_nac): #Definimos el parámetro edad , nombre y ocupación
        self.edad = edad # Definimos que el atributo edad, sera la edad asignada
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asig
        self.ocupacion = ocupacion #DEFINIMOS EL ATRIBUTO DE INSTANCIA OCUPACIÓN
        self.horas=horas_laboradas
        self.peso= peso 
        self.estatura= estatura
        self.fecha_nac = fecha_nac
        self.dia=0 #Iniciamos en el día 0
        
        #Creación de un nuevo método
    def presentar(self):
        presentacion = ("Hola soy {name}, mi edad es {age} y mi ocupación es {ocu}") #Mensaje
        print(presentacion.format(name=self.nombre, age=self.edad, ocu=self.ocupacion)) #Usamos FORMAT
        
    def dias_transcurridos(self,n):
        if self.ocupacion!= 'Desocupado':
            self.dia=self.dia+n
            self.horas=self.horas+n*8
            print('Has trabajado',self.horas,'horas')
        else:
            self.dia=self.dia+n
            print('Desde el día 0, han transcurrido',self.dia,'días' )
        
        #Creamos un nuevo método para cambiar la ocupación:
        #En caso que esta persona sea contratada
        
    def contratar(self, puesto): #añadimos un nuevo parámetro en el método
        self.puesto = puesto
        print ("{name} ha sido contratado como {vac}".format(name=self.nombre, vac=self.puesto))
        self.ocupacion = puesto#Ahora cambiamos el atributo ocupación
    
    def cumplio_anios(self):
        hoy = date.today()
        fecha_hoy = format(hoy.month)+'-'+format(hoy.day)
        fec_cum = fecha_nac[5:]
        if fecha_hoy == fec_cum:
            self.edad=self.edad+1
            print("Feliz cumpleaños te deseamos a ti, {name}".format(name=self.nombre))
        else:
            print("Aún no es tu cumpleaños, {name}".format(name=self.nombre)) 
            #print(fec_cum)

    def caminar(self, tiempo):  #añadimos un nuevo parametro para el tiempo que el humano va a caminar
        self.tiempo = tiempo
        caminata = ("{name} va a empezar a caminar, por {tiempo} segundos") # Mensaje
        print(caminata.format(name=self.nombre, tiempo=self.tiempo)) #Usamos FORMAT
        recorrido = ''
        finCaminata=("{name} ha terminado su caminata")
        i=0
        while i<tiempo:            
            i=i+1
            recorrido=recorrido + ' _'
            time.sleep(tiempo)
        print(recorrido)
        print(finCaminata.format(name=self.nombre))
        
    def correr(self, tiempo):  #añadimos un nuevo parametro para el tiempo que el humano va a caminar
        self.tiempo = tiempo
        corrida = ("{name} va a empezar a correr, por {tiempo} segundos") # Mensaje
        print(corrida.format(name=self.nombre, tiempo=self.tiempo)) #Usamos FORMAT
        recorrido1 = ''
        fincorrida=("{name} ha terminado su carrera")
        i=0
        while i<tiempo:            
            i=i+1
            recorrido1=recorrido1 + ' _ _'
            time.sleep(tiempo)
        print(recorrido1)
        print(fincorrida.format(name=self.nombre))

    def imc(self):
        indice = peso/(estatura**2)
        if indice < 18.5:
            mensaje=("{name} su indice de masa corporal es muy bajo, por favor consulte a su médico!")
        elif indice < 24.9:
            mensaje=("Felicitaciones {name} su indice de masa corporal está en el rango adecuado!")
        elif indice < 29.9:
            mensaje=("{name} su indice de masa corporal indica sobrepeso, consuma una dieta saludable e inicie una rutina de ejercicios diario")
        else:
            mensaje=("{name} su indice de masa corporal indica obesidad, consulte a su medico!")
        print(mensaje)
    


# In[3]:


Liliana= Humano(35, "Liliana", "Ingeniera", 300, 54, 1.59,"1986-03-12") #Instancia
#(self, edad, nombre, ocupacion,horas_laboradas,peso, estatura, genero):


# In[4]:


Liliana.presentar()


# In[5]:


Liliana.dias_transcurridos(40)


# In[6]:


Liliana.contratar('Experto en BI')


# In[7]:


Liliana.imc()


# In[ ]:


Francisco=Humano(20,"Francisco","Desempleado",20,90,1.7,"1995-10-24")


# In[ ]:


Francisco.cumplio_anios()


# In[8]:


Liliana.correr()
Francisco.caminar()


# In[ ]:




