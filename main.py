# -*- coding: utf-8 -*-
import random

TICKET_PRICE = 150
TRY_PERIOD = 5

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
    matches_sub_count = 0
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
        cash += 2000000
    elif matches_count == 7 and matches_sub_count == 1:
        cash += 200000
    elif matches_count == 7 and matches_sub_count == 0:
        cash += 50000
    elif matches_count == 6 and matches_sub_count == 1:
        cash += 20000
    elif matches_count == 6 and matches_sub_count == 0:
        cash += 7000
    elif matches_count == 5 and matches_sub_count == 1:
        cash += 4000
    elif matches_count == 5 and matches_sub_count == 0:
        cash += 2000
    elif matches_count == 4 and matches_sub_count == 1:
        cash += 1000

print(f"{cash} ({cash-(TICKET_PRICE * TRY_PERIOD)})")