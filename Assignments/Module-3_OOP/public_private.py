class Studinfo:
    #Private
    __stid=101
    __stnm="Sanket"

    #Private
    def __getdata(self):
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    
    def printdata(self):
        self.__getdata()
        
    def getsum(self,a,b):
        print("Sum:",a+b)

st=Studinfo()
st.printdata()
st.getsum(23,45)

    
    