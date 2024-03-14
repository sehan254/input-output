#!/usr/bin/env python
# coding: utf-8

# In[ ]:


bil1 = input('isikan bilangan 1')
bil2 = input('isikan bilangan 2')
hasil = int(bil1) + int(bil2)
print("hasil",bil1,"+",bil2,"=",hasil)


# 

# In[2]:


print("A","B","C","D",sep= '\n',end="^_^")


# In[3]:


num_1 = 8
num_2 = 10

#hasil dari 8 modulus 10=8
#str.format()

print('Hasil dari {} modulus {}={}'.format(num_1,num_2,num_1%num_2))


# In[6]:


fname ="rudi"
mname = "hartono"
iname = "darmawan"

print('Nama Anda {2} {0} {1}'.format (fname,mname,iname))


# In[7]:


print('nama anda {nama},nilai anda {nilai}'.format(nama='andri',nilai=70))


# In[8]:


univ = "Universitas Nusa Putra"

print("karakter pertama : ",univ[0])
print("karakter terakhir : ",univ[-1])
#Universitas
print(univ[0:11])
print(univ[-5:-1])
print(univ[17:])
print(univ[::-1])



# In[13]:


f_name ='Rudi'
l_name ='Andri'

print(f'Nama Saya {f_name} {l_name}')
first = 100
second = 20
print(f' Hasil penjumlahan {first} + {second} = {first+second}')


# In[ ]:


nama = "Andri,Budi,Cika"
nama2 = "Andri Budi Cika"
#split -> memisahkan string kedalam kumpulan karakter
print(nama2.split())
print(nama.split(','))

#join ->menggabungkan string kedalam kumpulan karakter
print('@'.join(nama.split(',')))


#input tgl lahir -> 18/oktober/2010
#input nama -> Bill Gate
#output:
#tgl : 18,Bulan:Oktober, Tahun :2010
#Nama Inisial : BG

tgl = input ("masukan tanggal lahir : ")
nama = input("masukan nama : ")
pemisah = tgl.split("/")
print("output ;")
print (f"tgl : {pemisah[o]}, Bulan: {pemisah[1]}, Tahun : {pemisah[2]}")
pemisah2 = nama.split()
nama_pertama = pemisah2[0]
nama_terakhir = pemisah2[1]
print(f"Nama inisial : {nama_pertama[0]+nama_terakhir[0]}")


# In[ ]:




