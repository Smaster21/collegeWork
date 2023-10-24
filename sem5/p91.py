def dfs(graph, start_node, path): 
  visited = set()

  if start_node in visited:
    return

  visited.add(start_node)
  path.append(start_node)

  for neighbor in graph[start_node]:
    dfs(graph, neighbor, path)

  if len(path) == len(graph):
    print(path)


def main():
  graph = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f"],
    "d": [],
    "e": [],
    "f": []
  }

  start_node = "a"
  path = []
  dfs(graph, start_node, path)

if __name__ == "__main__":
      main()
