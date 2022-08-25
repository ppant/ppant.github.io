---
id: 1734
title: Data Structures and Algorithms in Python – Graphs
date: 2018-05-16T22:10:06+05:30
author: Pradeep Pant
layout: post
guid: /?p=1734
permalink: /2018/05/16/data-structures-and-algorithms-in-python-graphs/
---
### Graph Implementation &#8211; Adjacency list

  * We&#8217;ve used dictionaries to implement the adjacency list in Python which is the easiest way.
  * To implement Graph ADT we&#8217;ll create two classes, Graph, which holds the master list of vertices, and Vertex, which will represent each vertex in the graph.
  * Each Vertex uses a dictionary to keep track of the vertices to which it is connected, and the weight of each edge. This dictionary is called connectedTo.

<div class="highlight highlight-source-python">
  <pre><code>&lt;span class="pl-c"># Create six vertices numbered 0 through 5. &lt;/span>
&lt;span class="pl-c"># Display the vertex dictionary&lt;/span>
g &lt;span class="pl-k">=&lt;/span> Graph()
&lt;span class="pl-k">for&lt;/span> i &lt;span class="pl-k">in&lt;/span> &lt;span class="pl-c1">range&lt;/span>(&lt;span class="pl-c1">6&lt;/span>):
    g.addVertex(i)
&lt;span class="pl-c1">print&lt;/span>(g.vertList)

&lt;span class="pl-c"># Add the edges that connect the vertices together&lt;/span>
g.addEdge(&lt;span class="pl-c1">0&lt;/span>,&lt;span class="pl-c1">1&lt;/span>,&lt;span class="pl-c1">5&lt;/span>)
g.addEdge(&lt;span class="pl-c1">0&lt;/span>,&lt;span class="pl-c1">5&lt;/span>,&lt;span class="pl-c1">2&lt;/span>)
g.addEdge(&lt;span class="pl-c1">1&lt;/span>,&lt;span class="pl-c1">2&lt;/span>,&lt;span class="pl-c1">4&lt;/span>)
g.addEdge(&lt;span class="pl-c1">2&lt;/span>,&lt;span class="pl-c1">3&lt;/span>,&lt;span class="pl-c1">9&lt;/span>)
g.addEdge(&lt;span class="pl-c1">3&lt;/span>,&lt;span class="pl-c1">4&lt;/span>,&lt;span class="pl-c1">7&lt;/span>)
g.addEdge(&lt;span class="pl-c1">3&lt;/span>,&lt;span class="pl-c1">5&lt;/span>,&lt;span class="pl-c1">3&lt;/span>)
g.addEdge(&lt;span class="pl-c1">4&lt;/span>,&lt;span class="pl-c1">0&lt;/span>,&lt;span class="pl-c1">1&lt;/span>)
g.addEdge(&lt;span class="pl-c1">5&lt;/span>,&lt;span class="pl-c1">4&lt;/span>,&lt;span class="pl-c1">8&lt;/span>)
g.addEdge(&lt;span class="pl-c1">5&lt;/span>,&lt;span class="pl-c1">2&lt;/span>,&lt;span class="pl-c1">1&lt;/span>)
&lt;span class="pl-c"># Nested loop verifies that each edge in the graph is properly stored. &lt;/span>
&lt;span class="pl-k">for&lt;/span> v &lt;span class="pl-k">in&lt;/span> g:
   &lt;span class="pl-k">for&lt;/span> w &lt;span class="pl-k">in&lt;/span> v.getConnections():
       &lt;span class="pl-c1">print&lt;/span>(&lt;span class="pl-s">&lt;span class="pl-pds">"&lt;/span>( &lt;span class="pl-c1">%s&lt;/span> , &lt;span class="pl-c1">%s&lt;/span> )&lt;span class="pl-pds">"&lt;/span>&lt;/span> &lt;span class="pl-k">%&lt;/span> (v.getId(), w.getId()))</code></pre>
</div>

### <a id="user-content-graph-implementation---solving-word-ladder-problem-using-breadth-first-search-bfs" class="anchor" href="https://github.com/ppant/DS-Algos-Python#graph-implementation---solving-word-ladder-problem-using-breadth-first-search-bfs" aria-hidden="true"></a>Graph Implementation &#8211; Solving Word Ladder Problem using Breadth First Search (BFS)</h1> 

let’s consider the following puzzle called a word ladder. Transform the word “FOOL” into the word “SAGE”. In a word ladder puzzle you must make the change occur gradually by changing one letter at a time. At each step you must transform one word into another word, you are not allowed to transform a word into a non-word. The following sequence of words shows one possible solution to the problem posed above.

  * FOOL
  * POOL
  * POLL
  * POLE
  * PALE
  * SALE
  * SAGE

This is implemented using dictionary

<div class="highlight highlight-source-python">
  <pre><code>&lt;span class="pl-c"># The Graph class, contains a dictionary that maps vertex names to vertex objects.&lt;/span>
&lt;span class="pl-c"># Graph() creates a new, empty graph.&lt;/span>
Graph()   

buildGraph()

&lt;span class="pl-c">#BFS begins at the starting vertex s and colors start gray to show that &lt;/span>
&lt;span class="pl-c">#it is currently being explored. Two other values, the distance and the &lt;/span>
&lt;span class="pl-c">#predecessor, are initialized to 0 and None respectively for the starting&lt;/span>
&lt;span class="pl-c">#vertex. Finally, start is placed on a Queue. The next step is to begin &lt;/span>
&lt;span class="pl-c">#to systematically explore vertices at the front of the queue. We explore &lt;/span>
&lt;span class="pl-c">#each new node at the front of the queue by iterating over its adjacency &lt;/span>
&lt;span class="pl-c">#list. As each node on the adjacency list is examined its color is &lt;/span>
&lt;span class="pl-c">#checked. If it is white, the vertex is unexplored, and four things happen:&lt;/span>
&lt;span class="pl-c">#	* The new, unexplored vertex nbr, is colored gray.&lt;/span>
&lt;span class="pl-c">#	* The predecessor of nbr is set to the current node currentVert&lt;/span>
&lt;span class="pl-c">#The distance to nbr is set to the distance to currentVert + 1&lt;/span>
&lt;span class="pl-c">#nbr is added to the end of a queue. Adding nbr to the end of the queue &lt;/span>
&lt;span class="pl-c">#effectively schedules this node for further exploration, but not until all the &lt;/span>
&lt;span class="pl-c">#other vertices on the adjacency list of currentVert have been explored.&lt;/span>

bfs()</code></pre>
</div>

### <a id="user-content-graph-implementation---solving-knight-tour-problem-using-depth-first-search-dfs" class="anchor" href="https://github.com/ppant/DS-Algos-Python#graph-implementation---solving-knight-tour-problem-using-depth-first-search-dfs" aria-hidden="true"></a>Graph Implementation &#8211; Solving Knight tour problem using Depth First Search (DFS)</h1> 

The knight’s tour puzzle is played on a chess board with a single chess piece, the knight. The object of the puzzle is to find a sequence of moves that allow the knight to visit every square on the board exactly once. One such sequence is called a “tour.”  
we will solve the problem using two main steps: Represent the legal moves of a knight on a chessboard as a graph. Use a graph algorithm to find a path of length rows×columns−1rows×columns−1 where every vertex on the graph is visited exactly once. To represent the knight’s tour problem as a graph we will use the following two ideas: Each square on the chessboard can be represented as a node in the graph. Each legal move by the knight can be represented as an edge in the graph.

<div class="highlight highlight-source-python">
  <pre><code>&lt;span class="pl-c"># The Graph class, contains a dictionary that maps vertex names to vertex objects.&lt;/span>
&lt;span class="pl-c"># Graph() creates a new, empty graph.&lt;/span>
Graph()

&lt;span class="pl-c"># To represent the knight’s tour problem as a graph we will use the &lt;/span>
&lt;span class="pl-c"># following two ideas: Each square on the chessboard can be represented &lt;/span>
&lt;span class="pl-c"># as a node in the graph. Each legal move by the knight can be represented&lt;/span>
&lt;span class="pl-c"># as an edge in the graph. &lt;/span>

knightGraph()

&lt;span class="pl-c"># The genLegalMoves function takes the position of the knight on the &lt;/span>
&lt;span class="pl-c"># board and generates each of the eight possible moves. The legalCoord &lt;/span>
&lt;span class="pl-c"># helper function makes sure that a particular move that is generated is &lt;/span>
&lt;span class="pl-c"># still on the board.&lt;/span>
genLegalMoves()

&lt;span class="pl-c"># DFS implementation&lt;/span>
        
&lt;span class="pl-c"># we will look at two algorithms that implement a depth first search. &lt;/span>
&lt;span class="pl-c"># The first algorithm we will look at directly solves the knight’s tour &lt;/span>
&lt;span class="pl-c"># problem by explicitly forbidding a node to be visited more than once. &lt;/span>
&lt;span class="pl-c"># The second implementation is more general, but allows nodes to be visited &lt;/span>
&lt;span class="pl-c"># more than once as the tree is constructed. The second version is used in &lt;/span>
&lt;span class="pl-c"># subsequent sections to develop additional graph algorithms.&lt;/span>

&lt;span class="pl-c"># The depth first exploration of the graph is exactly what we need in &lt;/span>
&lt;span class="pl-c"># order to find a path that has exactly 63 edges. We will see that when &lt;/span>
&lt;span class="pl-c"># the depth first search algorithm finds a dead end (a place in the graph &lt;/span>
&lt;span class="pl-c"># where there are no more moves possible) it backs up the tree to the next&lt;/span>
&lt;span class="pl-c"># deepest vertex that allows it to make a legal move.&lt;/span>
        
&lt;span class="pl-c"># The knightTour function takes four parameters: n, the current depth in &lt;/span>
&lt;span class="pl-c"># the search tree; path, a list of vertices visited up to this point; u, &lt;/span>
&lt;span class="pl-c"># the vertex in the graph we wish to explore; and limit the number of nodes &lt;/span>
&lt;span class="pl-c"># in the path. The knightTour function is recursive. When the knightTour &lt;/span>
&lt;span class="pl-c"># function is called, it first checks the base case condition. If we have &lt;/span>
&lt;span class="pl-c"># a path that contains 64 vertices, we return from knightTour with a status &lt;/span>
&lt;span class="pl-c"># of True, indicating that we have found a successful tour. If the path is not &lt;/span>
&lt;span class="pl-c"># long enough we continue to explore one level deeper by choosing a new vertex &lt;/span>
&lt;span class="pl-c"># to explore and calling knightTour recursively for that vertex.&lt;/span>

&lt;span class="pl-c"># DFS also uses colors to keep track of which vertices in the graph have been visited. &lt;/span>
&lt;span class="pl-c"># Unvisited vertices are colored white, and visited vertices are colored gray. &lt;/span>
&lt;span class="pl-c"># If all neighbors of a particular vertex have been explored and we have not yet reached &lt;/span>
&lt;span class="pl-c"># our goal length of 64 vertices, we have reached a dead end. When we reach a dead end we &lt;/span>
&lt;span class="pl-c"># must backtrack. Backtracking happens when we return from knightTour with a status of False. &lt;/span>
&lt;span class="pl-c"># In the breadth first search we used a queue to keep track of which vertex to visit next. &lt;/span>
&lt;span class="pl-c"># Since depth first search is recursive, we are implicitly using a stack to help us with &lt;/span>
&lt;span class="pl-c"># our backtracking. When we return from a call to knightTour with a status of False, in line 11, &lt;/span>
&lt;span class="pl-c"># we remain inside the while loop and look at the next vertex in nbrList.&lt;/span>

knightTour()

</code></pre>
  
  <p>
    Please check <a href="https://github.com/ppant/DS-Algos-Python">GitHub</a> for the full working code.
  </p>
  
  <p>
    I will keep adding more problems/solutions.
  </p>
  
  <p>
    Stay tuned!
  </p>
  
  <p>
    <strong>Ref: </strong> The inspiration of implementing DS in Python is from <a href="http://interactivepython.org/runestone/static/pythonds/index.html">this</a> course
  </p>
</div>