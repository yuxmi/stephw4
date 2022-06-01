print(main())
print(small())

def main():
    pages = {}
    links = {}

    with open('data/pages.txt') as f:
        for data in f.read().splitlines():
            page = data.split('\t')
        # page[0]: id, page[1]: title
            pages[page[0]] = page[1]

    with open('data/links.txt') as f:
        for data in f.read().splitlines():
            link = data.split('\t')
        # link[0]: id (from), links[1]: id (to)
            if link[0] in links:
                links[link[0]].add(link[1])
            else:
                links[link[0]] = {link[1]}

    for k, v in pages.items():
        if v == 'Google':
            # Determines start node
            start = k
    
    for k, v in pages.items():
        if v == '渋谷':
            # Determines target node
            end = k

    visited = []
    path = DFS(start, end, visited, links, pages)
    final_path = []
    # Converts nodes into page names
    for node in path:
        final_path.append(pages[node])
    return final_path


def DFS(start, target, visited, links, pages):
    visited.append(start)
    # Iterates through every link from the current node until target found
    for node in links[start]:

        # Base case
        if node == target:
            visited.append(target)
            return visited
    
        if isLegal(node, links, visited):
            # Recursive backtracking
            potential = DFS(node, target, visited, links, pages)
            if potential != None:
                return potential


# Checks if a path is possible from node without recursion (reduces runtime)
def isLegal(node, links, visited):
    if (node in links) and (node not in visited) and (links[node] != {node}):
        return True
    else: return False

    
    
def small():
    pages = {}
    links = {}

    with open('data/pages_small.txt') as f:
        for data in f.read().splitlines():
            page = data.split('\t')
        # page[0]: id, page[1]: title
            pages[page[0]] = page[1]

    with open('data/links_small.txt') as f:
        for data in f.read().splitlines():
            link = data.split('\t')
        # link[0]: id (from), links[1]: id (to)
            if link[0] in links:
                links[link[0]].add(link[1])
            else:
                links[link[0]] = {link[1]}

    for k, v in pages.items():
        if v == 'Google':
            # Determines start node
            start = k
    
    for k, v in pages.items():
        if v == '渋谷':
            # Determines target node
            end = k

    visited = []
    path = DFS(start, end, visited, links, pages)
    final_path = []
    # Converts nodes into page names
    for node in path:
        final_path.append(pages[node])
    return final_path
