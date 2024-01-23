import sys

sys.stdin = open("input.txt", "r")

def make_tree(nodes):
    tree = {i: [] for i in range (1,N+1)}
    tree[1].append(0)
    for node in range(N-1):
        parent = int(nodes[node*2])
        child = int(nodes[node * 2 +1])

        # Add at the 0th index to go back up
        tree[child] = [parent] + tree[child]
        tree[parent].append(child)
    return tree

def get_lowest_tree(tree):
    first_stack = []
    second_stack = []
    first_it , second_it = first,second

    while True:
        first_it = tree[first_it][0]
        first_stack.append(first_it)
        if first_it == 1:
            break
        
    
    while True:
        second_it = tree[second_it][0]
        second_stack.append(second_it)
        if second_it == 1:
            break
        
    parent_node = 0
    
    if len(first_stack) >= len(second_stack):
        first_set = set(first_stack)
        for stack in second_stack:
            if stack in first_set:
                parent_node = stack
                break
    
    else:
        second_set = set(second_stack)
        for stack in first_stack:
            if stack in second_set:
                parent_node = stack
                break
    
    return parent_node

def get_subtree_size(tree,parent):
    right_size, left_size = 0,0
    if len(tree[parent]) == 1:
        return 1
    elif len(tree[parent]) == 2: 
        right_size = get_subtree_size(tree, tree[parent][1])
    else:
        right_size = get_subtree_size(tree, tree[parent][1])
        left_size = get_subtree_size(tree, tree[parent][2])

    return 1+right_size + left_size


T = int(input())

for test_case in range(1, T + 1):
    N, E, first, second = map(int, input().split()) 
    nodes = input().split()

    tree = make_tree(nodes)
    lowest_parent = get_lowest_tree(tree)
    size = get_subtree_size(tree,lowest_parent)
    
    print(f"#{test_case} {lowest_parent} {size}")
