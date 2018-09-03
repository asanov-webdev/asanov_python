# задание 1
def f(x):
    if x>0: y=1
    if x==0: y=1
    if x<0: y=-1
    print(y)

# задание 2 (max)
def max(*args):
    m = args[0]
    for e in args:
        if e > m:
            m = e
    return(m)

# задание 3 (summator)
def sum(*args):
    s = 0
    for e in args:
        s = s + e
    return s

# задание 5 (date)
def print_date(day = 1, month = 9, year = 2018):
    print("Today is day %s of month %s of year %s." % (day, month, year))

# задание 2 - другие варианты
lst = max([int(elem) for elem in input.split(' ')])
# или
def max2(x, y):
    return x if x>y else y
max = reduce(max2, lst)
# если лень объявлять функцию, можно использовать лямбда-выражение:
max = reduce(lambda x,y: x if x>y else y, lst)
# можно вообще в одну строчку с вводом данных
max = reduce(lambda x,y: x if x>y else y,
             lst = [int(elem) for elem in input.split(' ')])

#lst.append(x) - adding x to list

    
