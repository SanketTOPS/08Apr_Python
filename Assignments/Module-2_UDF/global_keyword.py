a=10
print("A:",a)

def getval():
    global a
    a+=1
    print("A:",a)

getval()