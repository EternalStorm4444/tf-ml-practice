# BFS-DFS-Search of Undirected Graph
An illustration of a BFS and DFS search through an undirected graph.

This code explores a given undirected graph using a basic BFS search or DFS search. 

## Background

![Image of DFS vs BFS searches] (https://miro.medium.com/max/3648/1*VM84VPcCQe0gSy44l9S5yA.jpeg)


### - Depth First Search

The depth first search is called this because it focuses on going "deep" into a graph. 
Depth first searches can be used simply to search through an entire graph or they can
be used to find if a specific path exists between two nodes such as [A, F] which represents
a theoretical path between node A and node F in a graph.




### - Breadth First Search

Breadth first search is an upgraded and more advanced type of search algorithm. Unlike Depth First, 
BFS needs to track both visited nodes and queue of nodes it plans to visit. The BFS essentially 
follows a pattern of: start node, children nodes, grandchildren nodes etc. BFS moves layer by layer
or generation by generation down a graph. One of the major advantages BFS has over DFS is that it
doesn't go on long "wild goose chases" deep into a graph. In many BFS can save both time and 
the amount of nodes that need to be visited if you are searching for a specific node. 

## How to Run
Ensure that a Python 3 editor is installed on your computer to run this code. 
- idle for Python 3 may be downloaded here: https://www.python.org/downloads/
- run the code in IDLE and read the comments to learn how it works!

## Future Releases and Contribution
For future releases of this program I hope to be able to have users input graphs. 
I may also consider moving the program into a class/object form but for now with the current level of simplicity I feel this is overkill.

Contributions are welcome!

## Project Status
Saving further releases on this project for a rainy day.

## Licensing

MIT License

Copyright (c) [2020] [Kiersten Campbell]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



