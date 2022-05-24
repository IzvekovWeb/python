import copy
from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile
from pprint import pprint 


tree = mkdir('/', [
    mkdir('etc', [
        mkfile('bashrc'),
        mkfile('consul.cfg'),
    ]),
    mkfile('hexletrc'),
    mkdir('bin', [
        mkfile('ls'),
        mkfile('cat'),
    ]),
])

# В реализации используем рекурсивный процесс,
# чтобы добраться до самого дна дерева.
def get_nodes_count(node):
    if is_file(node):
        # Возвращаем 1 для учёта текущего файла
        return 1
    # Если узел — директория, получаем его детей
    children = get_children(node)
    # Самая сложная часть
    # Считаем количество потомков для каждого из детей,
    # вызывая рекурсивно нашу функцию get_nodes_count
    pprint(children)
    descendant_counts = list(map(get_nodes_count, children))
    # Возвращаем 1 (текущая директория) + общее количество потомков
    print(descendant_counts)
    return 1 + sum(descendant_counts)

print(get_nodes_count(tree))