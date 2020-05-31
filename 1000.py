three = 0
five = 0
chipo = 0
for i in range(1000):
    if (i % 3 == 0):
        three += i
    if (i % 5 == 0):
        five += i
    if (i % 15 == 0):
        chipo += i
sum = three + five - chipo
print(sum)