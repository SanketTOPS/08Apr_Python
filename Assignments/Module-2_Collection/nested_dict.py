stdata={'id':[1,2,3,4,5],
        'name':['sanket','nirav','harsh','dipak','darshan'],
        'sub':['python','java','php','react','c++']
        }

#print(stdata)
#print(stdata['id'])
#print(stdata['name'][0])

for i,j in stdata.items():
    print(f"Key={i} and Values={j[0]}")