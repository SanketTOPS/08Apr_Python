class master:
    def header(self):
        print("This is Header")
    
    def footer(self):
        print("This is footer")

class home(master):
    def header(self):
        return super().header()
    def footer(self):
        return super().footer()

class about(master):
    def header(self):
        return super().header()
    def footer(self):
        return super().footer()
   