---
id: 1694
title: 'Implemeting Data Structures and Algorithms in Python: Problems and solutions Contd..'
date: 2017-07-22T13:25:22+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2017/07/1688-revision-v1/
permalink: /2017/07/22/1688-revision-v1/
---
# Contd.. from last post

# Array Pair SumArray Pair Sum

Given an integer array, output all the unique pairs that sum up to a specific value k. So the input:

    sum_arr_uniq_pairs([1,2,2,3,4,1,1,3,2,1,3,1,2,2,4,0],5) 

would return 2 pairs:  
(2,3)  (1,4)

# Find a missing element in an array/list

Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array. Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.  
Input:

     find_missing_ele([1,2,3,4,5,6,7],[3,7,2,1,4,6]) 

Output:5 is the missing numberStack class implementation

# Implement basic stack operations (LIFO)

push() &#8211; Push an element in a stack pop()- POP an element from top of the stackpeek() &#8211; Just peek into top element of the stack (don&#8217;t perform any operation)Queue class implementation

# Implement basic Queue operations (FIFO)

enqueue &#8211; adding a element to the queue dequeue &#8211; removing an element from the queueDeque (DECK) class implementation

# Implement basic operation in deque (Add and remove elements both at front and rear)

    addFront()

Add an element at the front

    addRear()

Add an element at the rear

    removeFront()

Remove from front

    removeRear()

Remove from rear

# Balance parentheses using stack/list

Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: () square brackets: [] curly brackets: {}. Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not. Algo will take a string as the input string and will return boolean (TRUE/FALSE) Examples:

    print (check_parentheses_match('([])'))
    print (check_parentheses_match('[](){([[[]]])'))
    

&nbsp;

# Queue with 2 stack implementation

This is a classic problem. We need to use the basic characteristics of the stack (popping out elements in reverse order) will make a queue. Example:

    # Create a object of the class
    qObj = QueueWith2Stack()
    # Add an element 
    qObj.enqueue(1)
    # Add another element
    qObj.enqueue(2)
    # Add more element
    qObj.enqueue(4)
    # Add more element
    qObj.enqueue(8)
    # Remove item
    print (qObj.dequeue())
    # Remove item 
    print (qObj.dequeue())
    # Remove item
    print (qObj.dequeue())
    # Remove item 
    print (qObj.dequeue())
    

&nbsp;

# Singly Linked List class implementation

Implement basic skeleton for a Singly Linked List Example:

    # Added node
    a = LinkedListNode(1)
    b = LinkedListNode(2)
    c = LinkedListNode(3)        
    # Set the pointers
    a.nextnode = bb.nextnode = c
    print (a.value)
    print (b.value)
    print (c.value)
    # Print using class 
    print (a.nextnode.value)

# Doubly Linked List class implementation

    

Implement basic skeleton for a Doubly Linked List Example:

    

    
    # Added node
    a = DoublyLinkedListNode(1)
    b = DoublyLinkedListNode(2)
    c = DoublyLinkedListNode(3)        
    # Set the pointers
    # setting b after a (a before b)
    b.prev_node = a
    a.next_node = b
    # Setting c after a
    b.next_node = c
    c.prev_node = b
    print (a.value)
    print (b.value)
    print (c.value)
    # Print using class 
    print (a.next_node.value)
    print (b.next_node.value)
    print (b.prev_node.value)
    print (c.prev_node.value)
    

    

&nbsp;

    

# Reverse a linked list implementation

The aim is to write a function to reverse a Linked List in place. The function will take in the head of the list as input and return the new head of the list. Example:

    
    # Create a Linked List 
    a = LinkedListNode(1)
    b = LinkedListNode(2)
    c = LinkedListNode(3)
    d = LinkedListNode(4)
    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    print (a.nextnode.value)
    print (b.nextnode.value)
    print (c.nextnode.value)
    # Call the reverse()
    LinkedListNode().reverse(a)
    print (d.nextnode.value)
    print (c.nextnode.value)
    print (b.nextnode.value)
    

&nbsp;

# Linked list Nth to the last node

The aim is a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. Example:

    
    # Create a Linked List 
    a = LinkedListNode(1)
    b = LinkedListNode(2)
    c = LinkedListNode(3)
    d = LinkedListNode(4)
    e = LinkedListNode(5)
    
    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    d.nextnode = e
    
    print (a.nextnode.value)
    print (b.nextnode.value)
    print (c.nextnode.value)
    print (d.nextnode.value)
    
    # This would return the node d with a value of 4, because its the 2nd to last node.
    target_node = LinkedListNode().nth_to_last_node(2, a) 
    print (target_node.value)
    # Ans: d=4
    
    
    

<div id="page" class="site">
  <div class="site-inner">
    <div id="content" class="site-content">
      <div id="primary" class="content-area">
        <article id="post-1667" class="post-1667 post type-post status-publish format-standard hentry category-data-strcuctures-and-algorithms category-programming category-python tag-data-structures tag-programming-2 tag-python"> 
        
        <div class="entry-content">
          <p>
            Check <a href="https://github.com/ppant/DS-Algos-Python">GitHub</a> for the full working code.
          </p>
          
          <p>
            I will keep adding more problems/solutions.
          </p>
          
          <p>
            Stay tuned!
          </p>
          
          <p>
            Ref:  The inspiration of implementing DS in Python is from <a href="http://interactivepython.org/runestone/static/pythonds/index.html">this</a> course<span style="font-family: Inconsolata, monospace; white-space: pre-wrap;"></span>
          </p>
        </div></article>
      </div>
    </div>
  </div>
</div>