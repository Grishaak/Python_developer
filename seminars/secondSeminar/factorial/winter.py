# Уставшие от необычно теплой зимы,
#  жители решили узнать, действительно
# ли это самая длинная оттепель за всю
# историю наблюдений за погодой. Они обратились
# к синоптикам, а те, в свою очередь,
# занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько
# дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который
# среднесуточная температура ежедневно
# превышала 0 градусов Цельсия. Напишите
# программу, помогающую синоптикам в работе.
import random
season = 10
total = 0
temp = 0
season_list = []
for i in range(0, season):
    rnd = random.randrange(-10, 10)
    season_list.append(rnd)
    