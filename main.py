s = 0

print("Введите необходимое количество билетов:")

ticket = int(input())  # получаем строку

for i in range(1, ticket + 1):
    print(f"Введите возраст {i} посетителя:")
    age = int(input())  # возраст посетителя
    if age < 18:
        s += 0
    elif 18 <= age < 25:
        s += 990
    else:
        s += 1390


def discount():
    if ticket >= 3:
        return s * 0.9
    else:
        return s


print(f"Общая сумма покупки составляет: ", discount(), "рубля")
