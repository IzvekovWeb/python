import copy
from hexlet import fs
from pprint import pprint 

def change_owner(node, owner):
    '''Рекурсивный обход дерева

    Базовый алгоритм обхода графа.
    В данном примере меняет метаданные владельца
    '''
    name = fs.get_name(node)
    new_meta = copy.deepcopy(fs.get_meta(node))

    new_meta['owner'] = owner

    children = fs.get_children(node)
    if fs.is_file(node):
        return fs.mkfile(name, new_meta)


    new_children = list(map(lambda cild: change_owner(cild, owner), children))

    return fs.mkdir(name, new_children, new_meta)


tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkfile('bashrc'),
        fs.mkfile('consul.cfg'),
    ]),
    fs.mkfile('hexletrc'),
    fs.mkdir('bin', [
        fs.mkfile('ls'),
        fs.mkfile('cat'),
    ]),
])
#pprint(tree)
pprint(change_owner(tree, 'Alex'))