import sys

sys.stdin = open("input.txt", "r")


def solve_arith(Nodes, node):
    if len(Nodes[node]) == 1:
        return int(Nodes[node][0])
    else:
        if Nodes[node][0] == "+":
            return solve_arith(Nodes, int(Nodes[node][1])) + solve_arith(
                Nodes, int(Nodes[node][2])
            )
        if Nodes[node][0] == "-":
            return solve_arith(Nodes, int(Nodes[node][1])) - solve_arith(
                Nodes, int(Nodes[node][2])
            )
        if Nodes[node][0] == "/":
            return solve_arith(Nodes, int(Nodes[node][1])) / solve_arith(
                Nodes, int(Nodes[node][2])
            )
        if Nodes[node][0] == "*":
            return solve_arith(Nodes, int(Nodes[node][1])) * solve_arith(
                Nodes, int(Nodes[node][2])
            )

    return None


T = int(input)

for test_case in range(1, T + 1):
    N, E, first, second = int(input().split())
    parent_node, size = 0, 0

    print(f"#{test_case} {parent_node} {size}")
