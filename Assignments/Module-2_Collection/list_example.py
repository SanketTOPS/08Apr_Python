data=['python','java','php','react','angular']

"""print(data)
print(data[0])
print(data[-1])
print(data[0:3]) #range
print(data[2:])
print(data[:3])"""

# ------------------- #
"""print(data)
print(len(data))"""
# ------------------- #

"""print(data)
data[1]="android"
print(data)"""

# ------------------- #

"""print(data)

for i in data:
    print(i)
    
print(data.index("react"))"""

# ------------------- #
#print(data)
"""for i in data:
    print(i)"""
    
"""for i in data:
    print(f"{data.index(i)} - {i}")"""
    
# ------------------- #
"""if 'JAVA' in data:
    print("Yes...")
else:
    print("Noo")"""

# ------------------- #

print(data)
#data.append("node")
#data.insert(2,'c++')
#data.pop()
#data.pop(0)
#data.remove('java')
#del data[0]
#del data
#data.clear()
#data.reverse()
#data.sort()
#print(data)

#newdata=data.copy()
#print(newdata)

# ------------------- #
newdata=['c','c++','ds']
print(newdata)

#print(data+newdata)
data.extend(newdata)
print(data)