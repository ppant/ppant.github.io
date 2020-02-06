---
id: 1689
date: 2017-07-22T12:38:58+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2017/07/1688-revision-v1/
permalink: /2017/07/22/1688-revision-v1/
---
## Array Pair Sum

Given an integer array, output all the unique pairs that sum up to a specific value k. So the input:

<div class="highlight highlight-source-python">
  <pre>sum_arr_uniq_pairs([<span class="pl-c1">1</span>,<span class="pl-c1">2</span>,<span class="pl-c1">2</span>,<span class="pl-c1">3</span>,<span class="pl-c1">4</span>,<span class="pl-c1">1</span>,<span class="pl-c1">1</span>,<span class="pl-c1">3</span>,<span class="pl-c1">2</span>,<span class="pl-c1">1</span>,<span class="pl-c1">3</span>,<span class="pl-c1">1</span>,<span class="pl-c1">2</span>,<span class="pl-c1">2</span>,<span class="pl-c1">4</span>,<span class="pl-c1"></span>],<span class="pl-c1">5</span>)
would <span class="pl-k">return</span> <span class="pl-c1">2</span> pairs:

 	(<span class="pl-c1">2</span>,<span class="pl-c1">3</span>)
 	(<span class="pl-c1">1</span>,<span class="pl-c1">4</span>)</pre>
</div>

## <a id="user-content-find-a-missing-element-in-an-arraylist" class="anchor" href="https://github.com/ppant/DS-Algos-Python#find-a-missing-element-in-an-arraylist" aria-hidden="true"></a>Find a missing element in an array/list

Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array. Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

<div class="highlight highlight-source-python">
  <pre>Input:
find_missing_ele([<span class="pl-c1">1</span>,<span class="pl-c1">2</span>,<span class="pl-c1">3</span>,<span class="pl-c1">4</span>,<span class="pl-c1">5</span>,<span class="pl-c1">6</span>,<span class="pl-c1">7</span>],[<span class="pl-c1">3</span>,<span class="pl-c1">7</span>,<span class="pl-c1">2</span>,<span class="pl-c1">1</span>,<span class="pl-c1">4</span>,<span class="pl-c1">6</span>])
Output:
<span class="pl-c1">5</span> <span class="pl-k">is</span> the missing number</pre>
</div>

## <a id="user-content-stack-class-implementation" class="anchor" href="https://github.com/ppant/DS-Algos-Python#stack-class-implementation" aria-hidden="true"></a>Stack class implementation

Implement basic stack operations (LIFO)

<div class="highlight highlight-source-python">
  <pre>push() <span class="pl-k">-</span> Push an element <span class="pl-k">in</span> a stack 
pop()<span class="pl-k">-</span> <span class="pl-c1">POP</span> an element <span class="pl-k">from</span> top of the stack
peek() <span class="pl-k">-</span> Just peek into top element of the stack (don<span class="pl-s"><span class="pl-pds">'</span>t perform any operation)</span></pre>
</div>

## <a id="user-content-queue-class-implementation" class="anchor" href="https://github.com/ppant/DS-Algos-Python#queue-class-implementation" aria-hidden="true"></a>Queue class implementation

Implement basic Queue operations (FIFO)

<div class="highlight highlight-source-python">
  <pre>enqueue <span class="pl-k">-</span> adding a element to the queue 
dequeue <span class="pl-k">-</span> removing an element <span class="pl-k">from</span> the queue</pre>
</div>

## <a id="user-content-deque-deck-class-implementation" class="anchor" href="https://github.com/ppant/DS-Algos-Python#deque-deck-class-implementation" aria-hidden="true"></a>Deque (DECK) class implementation

Implement basic operation in deque (Add and remove elements both at front and rear)

<div class="highlight highlight-source-python">
  <pre>addFront() <span class="pl-k">-</span> Add an element at the front
addRear() <span class="pl-k">-</span> Add an element at the rear
removeFront() <span class="pl-k">-</span> Remove <span class="pl-k">from</span> front
removeRear() <span class="pl-k">-</span> Remove <span class="pl-k">from</span> rear</pre>
</div>

# <a id="user-content-balance-parenthelss-using-stacklist" class="anchor" href="https://github.com/ppant/DS-Algos-Python#balance-parenthelss-using-stacklist" aria-hidden="true"></a>Balance parentheses using stack/list

Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: () square brackets: [] curly brackets: {}. Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not. Algo will take a string as the inut string and will return boolean (TRUE/FALSE) Examples:

<div class="highlight highlight-source-python">
  <pre><span class="pl-c1">print</span> (check_parentheses_match(<span class="pl-s"><span class="pl-pds">'</span>([])<span class="pl-pds">'</span></span>))
<span class="pl-c1">print</span> (check_parentheses_match(<span class="pl-s"><span class="pl-pds">'</span>[](){([[[]]])<span class="pl-pds">'</span></span>))</pre>
</div>

# <a id="user-content-queue-with-2-stack-implementation" class="anchor" href="https://github.com/ppant/DS-Algos-Python#queue-with-2-stack-implementation" aria-hidden="true"></a>Queue with 2 stack implementation

This is a classic problem. We need to use the basic characteristics of the stack (popping out elements in reverse order) will make a queue. Example:

<div class="highlight highlight-source-python">
  <pre><span class="pl-c"># Create a object of the class</span>
qObj <span class="pl-k">=</span> QueueWith2Stack()
<span class="pl-c"># Add an element </span>
qObj.enqueue(<span class="pl-c1">1</span>)
<span class="pl-c"># Add another element</span>
qObj.enqueue(<span class="pl-c1">2</span>)
<span class="pl-c"># Add more element</span>
qObj.enqueue(<span class="pl-c1">4</span>)
<span class="pl-c"># Add more element</span>
qObj.enqueue(<span class="pl-c1">8</span>)
<span class="pl-c"># Remove item</span>
<span class="pl-c1">print</span> (qObj.dequeue())
<span class="pl-c"># Remove item </span>
<span class="pl-c1">print</span> (qObj.dequeue())
<span class="pl-c"># Remove item</span>
<span class="pl-c1">print</span> (qObj.dequeue())
<span class="pl-c"># Remove item </span>
<span class="pl-c1">print</span> (qObj.dequeue())</pre>
</div>

# <a id="user-content-singly-linked-list-class-implementation" class="anchor" href="https://github.com/ppant/DS-Algos-Python#singly-linked-list-class-implementation" aria-hidden="true"></a>Singly Linked List class implementation

Implement basic skeleton for a Singly Linked List Example:

<div class="highlight highlight-source-python">
  <pre><span class="pl-c"># Added node</span>
a <span class="pl-k">=</span> LinkedListNode(<span class="pl-c1">1</span>)
b <span class="pl-k">=</span> LinkedListNode(<span class="pl-c1">2</span>)
c <span class="pl-k">=</span> LinkedListNode(<span class="pl-c1">3</span>)        
<span class="pl-c"># Set the pointers</span>
a.nextnode <span class="pl-k">=</span> b
b.nextnode <span class="pl-k">=</span> c

<span class="pl-c1">print</span> (a.value)
<span class="pl-c1">print</span> (b.value)
<span class="pl-c1">print</span> (c.value)

<span class="pl-c"># Print using class </span>
<span class="pl-c1">print</span> (a.nextnode.value)</pre>
</div>

# <a id="user-content-doubly-linked-list-class-implementation" class="anchor" href="https://github.com/ppant/DS-Algos-Python#doubly-linked-list-class-implementation" aria-hidden="true"></a>Doubly Linked List class implementation

Implement basic skeleton for a Doubly Linked List Example:

<div class="highlight highlight-source-python">
  <pre><span class="pl-c"># Added node</span>
a <span class="pl-k">=</span> DoublyLinkedListNode(<span class="pl-c1">1</span>)
b <span class="pl-k">=</span> DoublyLinkedListNode(<span class="pl-c1">2</span>)
c <span class="pl-k">=</span> DoublyLinkedListNode(<span class="pl-c1">3</span>)        
<span class="pl-c"># Set the pointers</span>
<span class="pl-c"># setting b after a (a before b)</span>
b.prev_node <span class="pl-k">=</span> a
a.next_node <span class="pl-k">=</span> b

<span class="pl-c"># Setting c after a</span>
b.next_node <span class="pl-k">=</span> c
c.prev_node <span class="pl-k">=</span> b

<span class="pl-c1">print</span> (a.value)
<span class="pl-c1">print</span> (b.value)
<span class="pl-c1">print</span> (c.value)

<span class="pl-c"># Print using class </span>
<span class="pl-c1">print</span> (a.next_node.value)
<span class="pl-c1">print</span> (b.next_node.value)
<span class="pl-c1">print</span> (b.prev_node.value)
<span class="pl-c1">print</span> (c.prev_node.value)</pre>
</div>

# <a id="user-content-reverse-a-linked-list-implementation" class="anchor" href="https://github.com/ppant/DS-Algos-Python#reverse-a-linked-list-implementation" aria-hidden="true"></a>Reverse a linked list implementation

The aim is to write a function to reverse a Linked List in place. The function will take in the head of the list as input and return the new head of the list. Example:

<div class="highlight highlight-source-python">
  <pre><span class="pl-c"># Create a Linked List </span>
a <span class="pl-k">=</span> LinkedListNode(<span class="pl-c1">1</span>)
b <span class="pl-k">=</span> LinkedListNode(<span class="pl-c1">2</span>)
c <span class="pl-k">=</span> LinkedListNode(<span class="pl-c1">3</span>)
d <span class="pl-k">=</span> LinkedListNode(<span class="pl-c1">4</span>)

a.nextnode <span class="pl-k">=</span> b
b.nextnode <span class="pl-k">=</span> c
c.nextnode <span class="pl-k">=</span> d

<span class="pl-c1">print</span> (a.nextnode.value)
<span class="pl-c1">print</span> (b.nextnode.value)
<span class="pl-c1">print</span> (c.nextnode.value)

<span class="pl-c"># Call the reverse()</span>
LinkedListNode().reverse(a)
<span class="pl-c1">print</span> (d.nextnode.value)
<span class="pl-c1">print</span> (c.nextnode.value)
<span class="pl-c1">print</span> (b.nextnode.value)</pre>
</div>

# <a id="user-content-linked-list-nth-to-last-node" class="anchor" href="https://github.com/ppant/DS-Algos-Python#linked-list-nth-to-last-node" aria-hidden="true"></a>Linked list Nth to the last node

The aim is a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. Example:

<div class="highlight highlight-source-python">
  <pre><span class="pl-c"># Create a Linked List </span>
a <span class="pl-k">=</span> LinkedListNode(<span class="pl-c1">1</span>)
b <span class="pl-k">=</span> LinkedListNode(<span class="pl-c1">2</span>)
c <span class="pl-k">=</span> LinkedListNode(<span class="pl-c1">3</span>)
d <span class="pl-k">=</span> LinkedListNode(<span class="pl-c1">4</span>)
e <span class="pl-k">=</span> LinkedListNode(<span class="pl-c1">5</span>)

a.nextnode <span class="pl-k">=</span> b
b.nextnode <span class="pl-k">=</span> c
c.nextnode <span class="pl-k">=</span> d
d.nextnode <span class="pl-k">=</span> e

<span class="pl-c1">print</span> (a.nextnode.value)
<span class="pl-c1">print</span> (b.nextnode.value)
<span class="pl-c1">print</span> (c.nextnode.value)
<span class="pl-c1">print</span> (d.nextnode.value)

<span class="pl-c"># This would return the node d with a value of 4, because its the 2nd to last node.</span>
target_node <span class="pl-k">=</span> LinkedListNode().nth_to_last_node(<span class="pl-c1">2</span>, a) 
<span class="pl-c1">print</span> (target_node.value)
<span class="pl-c"># Ans: d=4</span></pre>
</div>