class Studinfo:
    stid=101
    stnm="Sanket"
    
    def myfunc(self):
        print("This is my function")

#Object
st=Studinfo()
print("ID:",st.stid)
print("Name:",st.stnm)
st.myfunc()