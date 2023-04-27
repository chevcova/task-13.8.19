n_Tickets = int(input("Введите желаемое количество билетов: "))
list_age = []
for i in range(0, n_Tickets):
    value = int(input(f"Введите возраст участника №{i + 1}: "))
    list_age.append(value)
    def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390
    cost = sum(map(price, list_age))
discount = int(cost * 0.9)
if n_Tickets > 3:
    print("Стоимость билетов с учетом скидки:",discount,"руб.")
else:
    print("Стоимость билетов:",cost,"руб.")
