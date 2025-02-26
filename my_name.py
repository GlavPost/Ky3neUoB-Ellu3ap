def pass(word):
    match word:
        case "1111":
            print("Не совсем")

match input("Кто ты, воин?"):
    case "password":
        input("Ну и какой пэссворд?")
    case "pucbka":
        print("tbI pucbka")
    case "писька":
        print("tbI pucbka")
    case _:
        print("НЕ ГОВОРИ ТАК!", "НЕ ГОВОРИИИИ ТАААК!!", sep='\n')
