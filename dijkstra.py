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
            # Determines start node number
            start = k

    for k, v in pages.items():
        if v == '渋谷':
            # Determines target node number
            target = k

    path = dijkstra(start, target, links)
    final_path = []
    # Converts page numbers into names
    for node in path:
        final_path.append(pages[node])
    return final_path

def dijkstra(start, target, links):

    # Setup
    inf = float('inf')
    # Adding all pages with links to unvisited (queue)
    unvisited = set()
    for k,v in links.items():
        unvisited.add(k)
    # All nodes except start is labelled as inf since we do not know what the smallest distance is
    dist = {}
    for val in unvisited:
        dist[val] = inf
    dist[start] = 0
    # Parents dict used to trace back path
    parents = {}

    # Loops until hitting base case (target found)
    while len(unvisited) > 0:
        minDist = inf
        for item in unvisited:
            if dist[item] <= minDist:
                minDist = dist[item]
                node = item
        
        # Base Case
        if node == target:
            final = [node]
            while start not in final:
                final.append(parents[node])
                node = parents[node]
            final = final[::-1]
            return final

        unvisited.remove(node)
        
        # Iterates through all links from the page (node)
        for neighbor in links[node]:
            # Weight to another page is 1
            newDist = dist[node] + 1
            # Skips if the neighbor doesn't have links
            if neighbor not in dist:
                continue
            # Runs if the newDist is less than current: either inf or a value if neighbor has been run before
            if newDist < dist[neighbor]:
                dist[neighbor] = newDist
                parents[neighbor] = node
                

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
            # Determines start node number
            start = k

    for k, v in pages.items():
        if v == '渋谷':
            # Determines target node number
            target = k

    path = dijkstra(start, target, links)
    final_path = []
    # Converts page numbers into names
    for node in path:
        final_path.append(pages[node])
    return final_path
