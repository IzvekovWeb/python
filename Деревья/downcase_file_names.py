import copy
from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile
from pprint import pprint 

def downcase_file_names(node):
    '''Рекурсивный обход дерева

     Принимает на вход директорию (объект-дерево), 
     приводит имена всех файлов в этой и во всех вложенных директориях к нижнему регистру. 
     Результат в виде обработанной директории возвращается наружу
    '''
    name = get_name(node)
    new_meta = copy.deepcopy(get_meta(node))

    if is_file(node):
        return mkfile(name.lower(), new_meta)
    
    children = get_children(node)
    new_children = list(map(lambda cild: downcase_file_names(cild), children))

    return mkdir(name, new_children, new_meta)

 


tree = mkdir('/', [
    mkdir('eTc', [
        mkdir('NgiNx', [], {'size': 4000}),
        mkdir(
            'CONSUL',
            [mkfile('config.JSON', {'uid': 0})],
        ),
    ]),
    mkfile('HOSTS'),
])

new_tree = downcase_file_names(tree)
new_file = get_children(new_tree)[1]
pprint(get_name(new_file))  # hosts