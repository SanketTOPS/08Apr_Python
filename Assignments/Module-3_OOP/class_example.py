class Studinfo:
    stid=101
    stnm="Sanket"
    
    def myfunc(self):
        print("This is member function!")
    
#Object of class
st=Studinfo() #object
print("ID:",st.stid)
print("Name:",st.stnm)

st.myfunc()