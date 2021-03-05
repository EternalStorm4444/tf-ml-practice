#Kiersten Campbell
#9/8/2020
#Artificial Intelligence

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

#a queue of nodes to visit
the_queue = []




#the visit function visits a node and adds adjacent nodes to the queue
def visit(curr_node):
    visited.append(curr_node)
    
    #if a neighboring node is not in the queue it is added
    for neighbor in undirected[curr_node]:
        if (neighbor in the_queue) == False:
            the_queue.append(neighbor)   

#the breadth_search function performs a BFS search given a start character
def breadth_search(start):
    the_queue.append(start)
    
    #visit the current node
    for curr_node in the_queue:
        visit(curr_node)

    print(visited)

#call to BFS function
breadth_search('A')

