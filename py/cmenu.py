class Menu:
    def __init__(self):
        self.menulist=[]
        self.pricelist=[]        
        # self.menuname=''
        # self.price=''
        # file=open("c:/testpy/menu.txt","r")
        # line=file.readline()
        # while line:
        #     name,price=line.split(",")
        #     # lst=line.split(",")->[name,price]
        #     # price=price.split(",")
        #     # self.addMenu(name,price)
        #     line=file.readline()
        # self.printlist()

    def getMenu(self):
       self.menuname=input("메뉴명:")
       if self.menuname!='':
            self.price=input("가격:")

    def addMenu(self,menuname,price):
        self.menulist.append(menuname)     
        self.pricelist.append(price)    
    
    def printlist(self): 
        if __name__=="__main__":
            for i in range(len(self.menulist)):
                print(self.menulist[i],self.pricelist[i])

    def saveList(self):
        with open("c:/testpy/menu.txt","w")as file:
            for i in range(len(self.menulist)):
                names=self.menulist[i]
                prices=self.pricelist[i]
                file.write("{},{}".format(names,prices))
                file.write("\n")
                #file.write(names+','+prices)

    def readList(self):
        with open("c:/testpy/menu.txt","r")as file:
            c=file.read()
            return c

    # def join(self):
    #     for i in range(len(self.menulist)):
    #         namet=self.menulist[i]
    #         pricet=self.pricelist[i]
    #         return namet,pricet      
    # def saveTest(self,n,m):
    #     with open("c:/testpy/menu.txt","r")as file:
    #         file.write("{},{}".format(n,m))             
    
    
        

