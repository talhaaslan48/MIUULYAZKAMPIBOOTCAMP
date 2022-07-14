 ###### NUMPY #######

 ####### 1-Neden NUMPY #######

 import numpy as np
 a = [1 , 2, 3 ,4]
 b = [2 , 3, 4, 5]

ab = []

for i in range(0,len(a)):
    ab.append(a[i] * b[i])

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
a*b


###### 2-NumPy Array'i Oluşturmak #####

import numpy as np
np.array([1,2,3,4,5])
type(np.array([1,2,3,4,5]))

np.zeros(10,dtype=int)

np.random.randint(0,10,size=10)
np.random.normal(10 , 4 , (3,4))

###### 3-NumPy Array Özellikleri
#ndim : boyut sayısı
#shape : boyut bilgisi
#size : toplam eleman sayısı
#dtype : array veri tipi

a = np.random.randint(10,size=5)
a.ndim
a.shape
a.size
a.dtype


###### 4- Yeniden Şekillendirme
 np.random.randint(1,10,size=9)
 np.random.randint(1, 10, size=9).reshape(3,3)
 ar =  np.random.randint(1,10,size=9)
 ar.reshape(3,3)



 ###### 5-Index Seçimi

a= np.random.randint(10,size=10)
a[0]
a[0:5]
a[0] = 999

m = np.random.randint(10,size=(3,5))

m[1][2]
m[2][3]

m[2][3] = 23

m[2][3] = 2.9

m[:,2]
m[1,:]

m[0:2 , 0:3]

###### 6- Fancy Index

v = np.arange(0,30,3)
v[1]

catch = [1,2,3]

v[catch]

##### 7 - NumPy Koşullu İşlemler

v = np.array([1,2,3,4,5])

#Klasik Döngü İle
 ab = []

for i in v:
    print(i)

 for i in v:
     if i < 3 :
         ab.append(i)

##### NumPy İle
v < 3

v[v != 3]
v[v == 3]


##### 8-Matematisel İşlemler

v = np.array([1,2,3,4,5])

v/5
v * 5 / 10
v ** 2
v ** 3
v ** 4

v - 1

np.subtract(v,1)  # V den 1'i çıkar
np.add(v,1) # V ' ye 1 ekle
np.mean(v # V 'nin ortalaması)
np.sum(v) # V deki elemanları topla
np.min(v) # En Küçük Eleman
np.max(v) # En Büyük Eleman
np.var(v) #V'nin Varyansı

v = np.subtract(v,1)

# NumPy ile 2 bilinmeyenli denklem çözümü

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5 ,1] , [1 ,3]])
b=  np.array([12, 10])

np.linalg.solve(a , b)
