import numpy as np
import collections

def activarRegadera(regadera,alcance,array, begin, end):
  #Evaluar regaderas de la izquierda
  print("Izquierda")
  for i in range(regadera-alcance,regadera):
    print(i)
    if i == regadera-alcance and i!=0 and i >= begin:
      print("Enrr")
      activarRegadera(i,alcance,array,begin,end)
    elif i==regadera-1:
      array[i]=1
    elif i<regadera and array[i]!=1:
      array[i]=-1
  #array[regadera]=1
  #Evaluar regaderas de la derecha
  print("Derecha")
  for y in range(regadera+1,(regadera+alcance+1)):
    print(y)
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
      print(aux)
      end=0
      if begin==-1 and aux[i]==0 and parcela[i]==maximo:
        begin=i
        print(begin)
        if i==len(parcela)-1:
          end=1
      else:
        if i==len(parcela)-1 and begin != -1 and parcela[i]==maximo:
          end=1
        else:
          if begin != -1 and finish ==-1 and aux[i-1]==0:
            if parcela[i-1]!= parcela[i]:
              end=1
            elif aux[i] == -1:
              end=1     
      if end==1:
        finish=i-1
        if begin==finish:
            activarRegadera(begin,maximo,aux,begin,finish)
            print(begin,maximo,begin,finish)
        elif end-begin+1!=2:
          activarRegadera(int((begin+finish)/2),maximo,aux,begin,finish)
          print('or',int((begin+finish)/2),maximo,begin,finish) 
        elif end-begin+1==2:
          activarRegadera(begin,maximo,aux,begin,finish)
          print('ri',begin,maximo,begin,finish)     
        begin=-1
        finish=-1
        end=0
    print('maximo:'+str(maximo))
    maximo=maximo-1
    
  total_regaderas_minimas= collections.Counter(aux)[1]
  print("Para regar la parcela se necesitarán como mínimo "+str(total_regaderas_minimas)+" regaderas que deben ser ubicadas en la posición donde el arregle siguiente coloque 1:")
  print(aux)

#parcela=[1,1,1,0,2,1,0,0,2,0,0,0,1]
parcela=[3,3,3,3,3,3,3,1,0,0,0,1]
#parcela=[1,1,1,0,2,1,0,0,2,0,1,0]
regadorasMin(parcela)