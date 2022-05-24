import copy
from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def get_hidden_files_count(node):
    name = get_name(node)
    if is_file(node) and name.startswith('.'):
        print(name)
        return 1
    children = get_children(node)
    count_list = list(map(get_hidden_files_count, children))
    return sum(count_list)

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('.nginx.conf', {'size': 800}),
        ]),
        mkdir('.consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('.hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
print(get_hidden_files_count(tree))  # 3