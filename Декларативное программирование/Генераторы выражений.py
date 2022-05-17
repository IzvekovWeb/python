def each2d(test, matrix):
    m = (i for el in matrix for i in el)
    for el in m:
        if not test(el):
            return False
    return True


def some2d(test, matrix):
    m = (i for el in matrix for i in el)
    for el in m:
        if test(el):
            return True
    return False


def sum2d(test, matrix):
    return sum(list(filter(test, [i for el in matrix for i in el])))




def is_int(x):
    return isinstance(x, int)
 
print(each2d(is_int, [[1, 2], [3, 4]]))
# True
print(each2d(is_int, [[1, None], [3, 4]]))
# False
# В пустой матрице нет ни одного элемента, который бы завалил тест
print(each2d(is_int, []))
# True

print()

print(some2d(is_int, [[None, "foo"], [(), {}]]))
# False
print(some2d(is_int, [[None, "foo"], [0, {}]]))
# True
# В пустой матрице нет ни одного элемента, который бы прошёл тест
print(some2d(is_int, []))
# False

print()
      
print(sum2d(is_int, [[1, "Foo", 100], [False, 10, None]]))
# 111
print(sum2d(is_int, [[-1, 2, -3], [4, -5, 6]]))
# 12

