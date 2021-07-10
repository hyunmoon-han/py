from os import pipe
import cmenu
a=cmenu.Menu()

# while True:
#     a.getMenu()
#     if a.menuname!='':
#         a.addMenu(a.menuname,a.price)
#     else:
#         break
# a.printlist()

# name=input("메뉴명:")
# while name!='':
#     price=input("가격:")
#     a.addMenu(name,price)
#     name=input("메뉴명:")
# a.printlist()
# a.saveList()
# a.readList()

with open("c:/testpy/menu.txt","r")as file: 
    for line in file:
        to,tos=line.split(",")
        a.addMenu(to,tos)
a.printlist()
name=input("추가메뉴:")
while name !='':
    if name in a.menulist:
        print("메뉴가 존재합니다.")
        break
    price=input("가격:")
    a.addMenu(name,price)
    name=input("추가 메뉴:")
a.saveList()
if name not in a.menulist:
    a.readList()
#print(a.menulist)

# file=open("c:/testpy/menu.txt","r")
# line=file.readline()
# while line:
#     name,price=line.split(",")
#     # lst=line.split(",")->[name,price]
#     # price=price.split(",")
#     # self.addMenu(name,price)
#     line=file.readline()
# a.printlist()

# name=input("메뉴명:")
# while name:
#     price=input("가격:")
#     a.addMenu(name,price)
#     name=input("메뉴명:")
# a.saveList()
# a.printlist()
    
