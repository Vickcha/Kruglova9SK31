temperature = int(input("Какая сейчас температура? "))
is_rainy = input("Идёт дождь? (да/нет): ")
is_raining_heavily = "нет"
if is_rainy == "да":
    is_raining_heavily = input("Дождь сильный? (да/нет): ")
if temperature <= 0:
    print("Пуховик")
else:
    if temperature <= 20:
        if is_rainy == "да":
            if is_raining_heavily == "да":
                print("Пальто, резиновые сапоги и зонт")
            else:
                print("Пальто и дождевик")
        else:
            print("Пальто")
    else:
        if temperature < 30:
            if is_rainy == "да":
                print("Футболку, шорты и дождевик")
            else:
                print("Футболку и шорты")
        else:
            if is_rainy == "да":
                if is_raining_heavily == "да":
                    print("Пальто, резиновые сапоги и зонт")
                else:
                    print("Футболку, шорты и дождевик")
            else:
                print("Футболку и шорты")