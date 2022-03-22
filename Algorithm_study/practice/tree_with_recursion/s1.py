import sys
sys.stdin = open('input.txt')

def recursion(node, ancestors, generations):
    if node in tree:
        for i, child in enumerate(tree[node], start=1):
            recursion(child, ancestors + [node], generations + [i])
    else:
        ancestors += [node]
        rtn = f'[{str(ancestors[0]).zfill(3)}]' if not printed else ''
        for i, ancestor in enumerate(ancestors[1:], start=1):
            if ancestor in printed:
                rtn += '        |   '
            else:
                sibling_count = len(tree[ancestors[i-1]])
                sibling_ranking = generations[i]
                number = str(ancestor).zfill(3)

                if sibling_count == 1:
                    rtn += f' ----- [{number}]'
                elif sibling_ranking == 1:
                    rtn += f' --+-- [{number}]'
                elif sibling_count == sibling_ranking:
                    rtn += f'        L-- [{number}]'
                else:
                    rtn += f'        +-- [{number}]'
                printed.add(ancestor)
        print(rtn)



tree = {}
edge = list(map(int, input().split()))
for i in range(0, len(edge) - 1, 2):
    tree[edge[i]] = tree.get(edge[i], []) + [edge[i+1]]

printed = set()
recursion(edge[0], [], [1])