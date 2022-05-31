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
            print('Google', k)
            start = k

    for k, v in pages.items():
        if v == '渋谷':
            print('渋谷', k)
            target = k

    path = dijkstra(start, target, links)
    final_path = []
    for node in path:
        final_path.append(pages[node])
    return final_path


def dijkstra(start, target, links):

    # Setup
    inf = float('inf')
    unvisited = set()
    for k,v in links.items():
        unvisited.add(k)
    dist = {}
    for val in unvisited:
        dist[val] = inf
    dist[start] = 0
    parents = {}

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
        
        for neighbor in links[node]:
            newDist = dist[node] + 1
            if neighbor not in dist:
                continue
            if newDist < dist[neighbor]:
                dist[neighbor] = newDist
                parents[neighbor] = node

if __name__ == '__main__':
    main()
