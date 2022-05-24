from hexlet.fs import get_children, is_file, mkdir, mkfile, is_directory, get_name
from operator import itemgetter

def du(node):
    children = get_children(node)
    res = list(map(
        lambda child: (get_name(child), get_direcrory_size(child)),
        children
        ))
    return sorted(res, key=itemgetter(1), reverse=True)

def get_direcrory_size(node):
    if is_file(node):
        return node['meta']['size']
    size = list(map(get_direcrory_size, get_children(node)))
    return sum(size)






# tree = mkdir('/', [
#     mkdir('etc', [
#         mkdir('apache'),
#         mkdir('nginx', [
#             mkfile('nginx.conf', {'size': 800}),
#         ]),
#         mkdir('consul', [
#             mkfile('.config.json', {'size': 1200}),
#             mkfile('data', {'size': 8200}),
#             mkfile('raft', {'size': 80}),
#         ]),
#     ]),
#     mkfile('hosts', {'size': 3500}),
#     mkfile('resolve', {'size': 1000}),
# ])

# [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]


tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('nginx.conf', {'size': 800}),
            ]),
            mkdir('consul', [
                mkfile('.config.json', {'size': 1200}),
                mkfile('data', {'size': 8200}),
                mkfile('raft', {'size': 80}),
            ]),
        ]),
        mkfile('hosts', {'size': 3500}),
        mkfile('resolve', {'size': 1000}),
    ])

print(du(get_children(tree)[0]))  

#  [('consul', 9480), ('nginx', 800), ('apache', 0)]
 