def enter(word):
    while(True):
        match word:
            case "1111":
                print("Не совсем")
            case "pucbka":
                print("Правильно")
                return print("Пока!")

match input("Кто ты, воин?"):
    case "password":
        enter(input("Ну и какой пэссворд?"))
    case "pucbka":
        print("tbI pucbka")
    case "писька":
        print("tbI pucbka")
    case _:
        print("НЕ ГОВОРИ ТАК!", "НЕ ГОВОРИИИИ ТАААК!!", sep='\n')
