import numpy as np

edges = {}

n = int(input())

sick = np.ones(n+2)
visited = np.ones(n+2)

for i in range(n):
    edge = input()
    l, r = edge.split()

    sick[int(l)] = 0
    sick[int(r)] = 0
    visited[int(l)] = 0
    visited[int(r)] = 0
    
    try:
        edges[int(l)].add(int(r))
    except KeyError:
        edges[int(l)] = {int(r)}
    
    try:
        edges[int(r)].add(int(l))
    except KeyError:
        edges[int(r)] = {int(l)}

sick_flag = 1

neighbours = np.zeros(n+2)

for key in edges.keys():
    neighbours[key] = len(edges[key])
    if len(edges[key]) == 1:
        sick[key] = 1
    
neighbours_copy = np.copy(neighbours)
cur_ver_max = np.argmax(neighbours)
    
while(not(np.all(visited > 0))):
    n_sick_counter = 0
    for n in edges[cur_ver_max]:
        if sick[n] == 1:
            n_sick_counter += 1
        if n_sick_counter == 2:
            break
            
    if n_sick_counter != 2:
        sick[cur_ver_max] = 1
    neighbours_copy[cur_ver_max] = 0
    visited[cur_ver_max] = 1
    cur_ver_max = np.argmax(neighbours_copy)
    
answer = []
count = 0
for key in edges.keys():
    if sick[key] == 1:
        count += 1
        answer.append(key)
        
print(count)
for v in answer:
    print(v, end=' ')
print()