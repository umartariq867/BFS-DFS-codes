graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue
# function that takes three parameters
def bfs(visited, graph, node):
  # it append the visted nodes in the list of visited(visited)
  visited.append(node)
  # add the visited node in queue
  queue.append(node)

  while queue:
    # dequeue the first element of the queue n saved it in the variable
    s = queue.pop(0)
    # print that on screen
    print (s, end = " ")
    # now check neighbour
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
# Driver Code
bfs(visited, graph, 'A')