import numpy as np
import collections



def activarRegadera(regadera,alcance,array, begin, end):
  #Evaluar regaderas de la izquierda
  for i in range(regadera-alcance,regadera):
        if i == regadera-alcance and i!=0 and i >= begin:  
          activarRegadera(i,alcance,array,begin,end)
        elif i>=0 and array[i]!=1:
          array[i]=-1
  array[regadera]=1
  #Evaluar regaderas de la derecha
  for y in range(regadera+1,(regadera+alcance+1)):   
      if y == (regadera+alcance) and y<len(array) and y<=end:
        activarRegadera(y,alcance,array,y,y)
      elif y<len(array) and  array[y]!=1:
        array[y]=-1

    


def regadorasMin(parcela):
  maximo=max(parcela)
  groups=list()
  aux=np.zeros(len(parcela))
  while maximo >= 0:
    begin=-1
    finish=-1
    for i in range(len(parcela)):
      if i< len(parcela)-1 and begin==-1 and parcela[i] == maximo and  parcela[i+1]==maximo and aux[i]==0:
        begin=i
      elif i< len(parcela)-1 and begin==-1 and  parcela[i] == maximo and parcela[i+1]!=maximo  and aux[i]==0:
        begin=finish=i
        activarRegadera(begin,maximo,aux,begin,finish)
        begin=-1
        finish=-1
      elif i== len(parcela)-1 and begin==-1 and parcela[i] == maximo  and aux[i]==0:
        begin=finish=i
        activarRegadera(begin,maximo,aux,begin,finish)
        begin=-1
        finish=-1
      if begin != -1 and (parcela[i] == maximo and parcela[i+1]!=maximo) and aux[i]==0:
        finish=i
        activarRegadera(int((begin+finish)/2),maximo,aux,begin,finish)
        begin=-1
        finish=-1       
    maximo=maximo-1
    total_regaderas_minimas= collections.Counter(aux)[1]
  print("Para regar la parcela se necesitarán como mínimo "+str(total_regaderas_minimas)+" regaderas que deben ser ubicadas en la posición donde el arregle siguiente coloque 1:")
  print(aux)

parcela=[3,3,3,3,3,3,3,1,0,0,0,1]
print(parcela)
regadorasMin(parcela)