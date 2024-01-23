import sys

sys.stdin = open("input.txt", "r")


def make_tree(N,nodes):
    tree = {i:{'parent': None, 'children':[]} for i in range(1,N+1)}

    for node in range(0,len(nodes),2):
        parent, child = int(nodes[node]), int(nodes[node+1])
        tree[child]['parent'] = parent
        tree[parent]['children'].append(child)
    return tree

def get_lowest_tree(tree, first, second):
    ancestor = set()
    while first:
        ancestor.add(first)
        first = tree[first]['parent']
    while second not in ancestor:
        second = tree[second]['parent']
    
    return second

def get_subtree_size(tree,parent):
    right_size, left_size = 0,0
    if len(tree[parent]['children']) == 0:
        return 1
    elif len(tree[parent]['children']) == 1: 
        right_size = get_subtree_size(tree, tree[parent]['children'][0])
    else:
        right_size = get_subtree_size(tree, tree[parent]['children'][0])
        left_size = get_subtree_size(tree, tree[parent]['children'][1])

    return 1+right_size + left_size

T = int(input())

for test_case in range(1, T + 1):
    N, E, first, second = map(int, input().split()) 
    nodes = input().split()

    tree = make_tree(N, nodes)
    # print(tree)
    lowest_parent = get_lowest_tree(tree, first, second)
    # print(lowest_parent)
    size = get_subtree_size(tree,lowest_parent)
    # print(size) 
    print(f"#{test_case} {lowest_parent} {size}")