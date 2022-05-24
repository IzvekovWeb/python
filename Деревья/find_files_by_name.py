import os

from hexlet.fs import flatten, get_children, get_name, is_file, mkdir, mkfile

def find_files_by_name(node, substr):
    
    def walk(node, substr, ancestry=os.path.join):
        children = get_children(node)
        if substr in get_name(node) and is_file(node):
            return ancestry

        if len(children) == 0:
            return []

        res = list(map(
            lambda child: walk(child, substr, os.path.join(ancestry, get_name(child))),
            children
        ))
        return flatten(res)

    return walk(node, substr, get_name(node))




tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkfile('data'),
            mkfile('raft'),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
print(find_files_by_name(tree, 'co'))
# ['/etc/nginx/nginx.conf', '/etc/consul/config.json']
