def cost(size):
    flavour = input("Pizza Çeşidi: ")
    if flavour == "margerita":
        if size == "Büyük":
            print("borcunuz: 20 usd")
        elif size == "Küçük":
            print("borcunuz: 10 usd")
        elif size == "Orta":
            print("borcunuz 15 usd")
        else:
            print("Yanlış Boy Seçimi Yapılmış")

    elif flavour == "sebzeli":
        if size == "Büyük":
            print("borcunuz: 20 usd")
        elif size == "Küçük":
            print("borcunuz: 10 usd")
        elif size == "Orta":
            print("borcunuz 15 usd")
        else:
            print("Yanlış Boy Seçimi Yapılmış")

    elif flavour == "sucuklu":
        if size == "Büyük":
            print("borcunuz: 30 usd")
        elif size == "Küçük":
            print("borcunuz: 15 usd")
        elif size == "Orta":
            print("borcunuz 22 usd")
        else:
            print("Yanlış Boy Seçimi Yapılmış")

    elif flavour == "sosisli":
        if size == "Büyük":
            print("borcunuz: 30 usd")
        elif size == "Küçük":
            print("borcunuz: 15 usd")
        elif size == "Orta":
            print("borcunuz 22 usd")
        else:
            print("Yanlış Boy Seçimi Yapılmış")

    elif flavour == "karışık":
        if size == "Büyük":
            print("borcunuz: 40 usd")
        elif size == "Küçük":
            print("borcunuz: 25 usd")
        elif size == "Orta":
            print("borcunuz 32 usd")
        else:
            print("Yanlış Boy Seçimi Yapılmış")

    else:
        print("Öyle bir çeşidimiz yok:(çeşitler)")
        print("1-margerita",'\n'+"2-sebzeli"+'\n'+"3-sucuklu"+'\n'+"4-sosisli"+'\n'+"5-karışık")

pizza = input("Hangi Boy Pizza İstersiniz: ")
cost(pizza)
