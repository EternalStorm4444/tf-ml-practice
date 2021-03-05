#Kiersten Campbell
#9/19/2020
#Artificial Intelligence
#DFS Algorithm

#the graph
#each node in the graph has connecting nodes as members
undirected = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'C'],
    'C' : ['B', 'D', 'E'],
    'D' : ['B', 'C', 'E', 'F'],
    'E' : ['C', 'D', 'F'],
    'F' : ['D', 'E']
    }


#a list to keep track of visited nodes
visited = []
    
#the depth first search function performs a DFS search given a start node
def depth_search(start):
    if start not in visited:
        visited.append(start)

        for neighbor in undirected[start]:
            depth_search(neighbor)

        

#call to DFS function
depth_search('A')

#correct output should be ['A', 'B', 'D', 'E', 'F']
print(visited)


