from functools import wraps


def memoizing(max_):
    def wrapper(f):
        temp = {}
        memory = {'key': None, 'value': None}
        count = [0]

        @wraps(f)
        def inner(*args, **kwargs):
            x = args[0]
            if temp.get(x) is None:
                if count[0] < 3:
                    temp[x] = f(x)
                    if count[0] == 0:
                        memory['key'] = x
                        memory['value'] = temp[x]
                    count[0] += 1
                    return temp.get(x)
                else:
                    res = f(x)
                    del temp[memory['key']]
                    temp[x] = res
                    memory['key'] = x
                    memory['value'] = res
                    count[0] = 0
                    return res
            return temp.get(x)

        return inner

    return wrapper


@memoizing(3)
def f(x):
    print()
    print('Calculating...')
    return x * 10


print(f(1))
# => Calculating...
# 10
print(f(1))  # будет "вспомнено"
# 10
print(f(2))
# => Calculating...
# 20
print(f(3))
# => Calculating...
# 30
print(f(4))  # вытеснит запомненный результат для "1"
# => Calculating...
# 40
print(f(1))  # будет перевычислено
# => Calculating...
# 10
