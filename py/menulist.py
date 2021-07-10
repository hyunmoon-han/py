from cmenu import Menu

menu = Menu()

#메뉴 가격 입력
while True:
    menu.getMenu()
    menu.addMenu(menu.menuname,menu.price)
    if(menu.menuname==''):
        break
menu.printlist()

print(menu.total)
# menu.getMenu()
# menu.addMenus(menu.menuname,menu.price)
# menu.printlists()
