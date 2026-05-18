import pandas

stdata={
    'id':[1,2,3,4,5],
    'name':['sanket','nirav','darshan','gopal','mitesh'],
    'city':['rajkot','ahmedabad','baroda','surat','navsari']
}

#print(stdata)

dt=pandas.DataFrame(stdata)
print(dt)
