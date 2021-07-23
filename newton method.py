#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt
import numpy as np


hor=np.arange(0,10,1.1) #x array
ver=np.random.randint(-1000,1000,len(hor)) #y array
c=0
p=0
def newton():
    #x=float(input("introduzir  x"))
    #y=float(input("introduzir  y"))
    #hor.append(x)
    #ver.append(y)
    #dec=input("s para continuar, n para parar")
    #if dec == "s":
        #newton()
    #elif dec == "n":  
            p=0
            for l in range(0, len(hor)):
                p=p+1
            number_of_lists = p 
            empty_lists = [[] for i in range(number_of_lists)]  #criar uma lista para cada passo 
            for i in ver:
                empty_lists[0].append(i)           
            for i in range(0, len(hor)):        #ordenar x em ordem de crescente x
                for  j in range(i+1, len(hor)):  
                    if(hor[i] > hor[j]):  
                        temp = hor[i]  
                        yemp = empty_lists[0][i]
                        hor[i] = hor[j]
                        ver[i] = empty_lists[0][i]
                        hor[j] = temp
                        empty_lists[0][i] = yemp 
            numero=int(len(hor))-1
            for u in range(0,numero):                   #each newton step calc
                nlistainterior=len(empty_lists[u])-1    
                for j in range(0,nlistainterior):     
                    numerador = empty_lists[u][j+1] - empty_lists[u][j]
                    denominador = hor[j+1+u]-hor[j]
                    resultado = numerador/denominador
                    empty_lists[u+1].append(resultado) #certo
            t=int(empty_lists[0][0])
            x = np.arange(0,10,0.01)
            total=t
    
            for u in range(1,numero+1):   #polynomial creation
                tu=empty_lists[u][0]
                m=1
                for j in range(0,u):
                    parent=x-hor[j]
                    m=np.multiply(parent,m)
                tu=np.multiply(m,tu)    
                total= total + tu
            plt.plot(x, total)
            plt.scatter(hor, ver)
            plt.ylim((-3000,3000))
            plt.show() 


newton()


# In[ ]:





# In[ ]:





# In[ ]:




