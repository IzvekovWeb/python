def my_map(f, xs):
    for el in xs:
        yield f(el)


def my_filter(f, xs):
    for el in xs:
        if f(el):
            yield el


def replicate_each(n, xs):
    for el in xs:
        i = 0
        while i < n:
            yield el
            i += 1
            





print(list(my_map(abs, [-1, 2, -3])))
# [1, 2, 3]

print(list(my_filter(lambda x: x % 2 == 1, range(10))))
# [1, 3, 5, 7, 9]

print(list(replicate_each(1, [1, 'a'])))  # [1, 'a']
print(list(replicate_each(3, [1, 'a'])))  # [1, 1, 1, 'a', 'a', 'a']
print(list(replicate_each(0, [1, 'a'])))  # []
