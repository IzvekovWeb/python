import itertools


# BEGIN (write your solution here)
# 2 варианта реализации
def remove_first_level2(tree):
    tree_res = []
    for node in tree:
        if isinstance(node, list):
            tree_res.extend([i for i in node])
    return tree_res

def remove_first_level(tree):
    tree_res = []
    tree_res.extend(i for node in filter(lambda x: isinstance(x, list), tree) for i in node )
    return tree_res
     
    

# END

tree1 = [[5], 1, [3, 4]]
print(remove_first_level(tree1))  # [5, 3, 4]

tree2 = [1, 2, [3, 5], [[4, 3], 2]]
print(remove_first_level(tree2))  # [3, 5, [4, 3], 2]
