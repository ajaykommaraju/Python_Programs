#this program reverses the key & value in a dictinary
dict1 = {'ajay' : 1, 'vijay' : 2 , 'Aarav' : 3}
dict2 = {}
dict2={v:k for k,v in dict1.items()}
print(dict2)
