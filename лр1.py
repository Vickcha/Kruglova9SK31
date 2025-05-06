def clothing():
    t_20_30 = input("Температура выше 20 и меньше 30? (да/нет): ")

    if t_20_30 == "да":
        osadki = input("Есть ли осадки? (да/нет): ")
        if osadki == "да":
            return "Футболку, шорты и дождевик"
        else:
            return "Футболку и шорты"
    else:
        t_0 = input("Температура выше 0 градусов? (да/нет): ")
        if t_0 == "нет":
            return "Пуховик"
        else:
            osadki = input("Есть ли осадки? (да/нет): ")
            if osadki == "нет":
                return "Пальто"
            else:
                S_osadki = input("Осадки сильные? (да/нет): ")
                if S_osadki == "да":
                    return "Пальто, резиновые сапоги и зонт"
                else:
                    return "Пальто и дождевик"
print("Что надеть?")
recom = clothing()
print(recom)
