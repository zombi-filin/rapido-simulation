# -*- coding: utf-8 -*-
import random

TICKET_PRICE = 25
TRY_PERIOD = 100

prize = {
    25: [25, 50, 100, 150, 175, 250, 500, 25000],
    50: [50, 100, 250, 400, 600, 1500, 5000, 50000],
    1000: [1000, 2000, 4000, 7000, 20000, 50000, 200000, 1500000],
    2100: [2100, 2100, 2100, 5600, 14000, 35000, 175000, 1500000]
}

selected_lst = list(range(1, 21))
selected_sub_lst = list(range(1, 5))

random.shuffle(selected_lst)
random.shuffle(selected_sub_lst)

generate_lst = list(range(1, 21))
generate_sub_lst = list(range(1, 5))

cash = TICKET_PRICE * TRY_PERIOD

for i in range(TRY_PERIOD):
    # Вычит стоимости юилета
    cash -= TICKET_PRICE
    # Генерация
    random.shuffle(generate_lst)
    random.shuffle(generate_sub_lst)
    # Сброс счетчиков
    matches_count = 0
    # Сравнение первой части
    for j in range(8):
        for g in range(8):
            matches_count += 1 if selected_lst[j] == generate_lst[g] else 0
    # Сравнение доп части
    matches_sub_count = 1 if selected_sub_lst[0] == generate_sub_lst[0] else 0
    # Выигрыш
    if matches_count == 8 and matches_sub_count == 1:
        cash += 999999999
    elif matches_count == 8 and matches_sub_count == 0:
        cash += prize[TICKET_PRICE][7]
    elif matches_count == 7 and matches_sub_count == 1:
        cash += prize[TICKET_PRICE][6]
    elif matches_count == 7 and matches_sub_count == 0:
        cash += prize[TICKET_PRICE][5]
    elif matches_count == 6 and matches_sub_count == 1:
        cash += prize[TICKET_PRICE][4]
    elif matches_count == 6 and matches_sub_count == 0:
        cash += prize[TICKET_PRICE][3]
    elif matches_count == 5 and matches_sub_count == 1:
        cash += prize[TICKET_PRICE][2]
    elif matches_count == 5 and matches_sub_count == 0:
        cash += prize[TICKET_PRICE][1]
    elif matches_count == 4 and matches_sub_count == 1:
        cash += prize[TICKET_PRICE][0]

print(f"{cash} ({cash-(TICKET_PRICE * TRY_PERIOD)})")