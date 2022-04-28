mydict = {
    "window": 78000,
    "door": 60000
}


def menu_cycle(my_input=""):
    while True:
        print('Menü: \n1 : Hozzáadás/Módosítás\n2 : Törlés\n3 : Kilépés')
        my_input = input('Válasszon menüpontot: ')
        match my_input:
            case '1':
                new_key = input('Termék neve: ')
                new_value = int(input('Termék értéke: '))
                mydict[new_key] = new_value
                print(mydict)
            case '2':
                key_to_delete = input('Törlendő termék neve: ')
                mydict.pop(key_to_delete)
                print(mydict)
            case '3':
                break


menu_cycle()


