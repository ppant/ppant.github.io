---
id: 1718
title: 'Data Structures and Algorithms in Python &#8211; Sorting'
date: 2018-05-15T22:01:48+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=1718
permalink: /2018/05/15/data-structures-and-algorithms-in-python-sorting/
twitter_share:
  - 'a:1:{s:8:"hashtags";a:1:{i:0;s:18:"python #algorithms";}}'
---
##### Bubble Sort Implementation

The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs.

  * Regardless of how the items are arranged in the initial list, n−1 passes will be made to sort a list of size n, so 1 pass n-1 comparisons, 2 pass n-2 comparions and n-1 is 1 comparions.
  * A bubble sort is often considered the most inefficient sorting method since it must exchange items before the final location is known. These “wasted” exchange operations are very costly. However, because the bubble sort makes passes through the entire unsorted portion of the list, it has the capability to do something most sorting algorithms cannot. In particular, if during a pass there are no exchanges, then we know that the list must be sorted. A bubble sort can be modified to stop early if it finds that the list has become sorted. This means that for lists that require just a few passes, a bubble sort may have an advantage in that it will recognize the sorted list and stop.
  * Performance: &#8211; Worst case: O(n2) n-square &#8211; Best case: O(n) &#8211; Average case: O(n2) n-square

<div class="highlight highlight-source-python">
  <pre><code>arr &lt;span class="pl-k">=&lt;/span> [&lt;span class="pl-c1">2&lt;/span>,&lt;span class="pl-c1">7&lt;/span>,&lt;span class="pl-c1">1&lt;/span>,&lt;span class="pl-c1">8&lt;/span>,&lt;span class="pl-c1">5&lt;/span>,&lt;span class="pl-c1">9&lt;/span>,&lt;span class="pl-c1">11&lt;/span>,&lt;span class="pl-c1">35&lt;/span>,&lt;span class="pl-c1">25&lt;/span>]
bubble_sort(arr)
&lt;span class="pl-c1">print&lt;/span> (arr)
[&lt;span class="pl-c1">1&lt;/span>, &lt;span class="pl-c1">2&lt;/span>, &lt;span class="pl-c1">5&lt;/span>, &lt;span class="pl-c1">7&lt;/span>, &lt;span class="pl-c1">8&lt;/span>, &lt;span class="pl-c1">11&lt;/span>, &lt;span class="pl-c1">25&lt;/span>, &lt;span class="pl-c1">35&lt;/span>]</code></pre>
  
  <h5>
    Selection Sort Implementation
  </h5>
  
  <ul>
    <li>
      Selection sort is a in-place algorithm
    </li>
    <li>
      It works well with small files
    </li>
    <li>
      It is used for sorting the files with large values and small keys this is due to the fact that selection is based on keys and swaps are made only when required
    </li>
    <li>
      The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location. As with a bubble sort, after the first pass, the largest item is in the correct place. After the second pass, the next largest is in place. This process continues and requires n−1 passes to sort n items, since the final item must be in place after the (n−1) st pass
    </li>
    <li>
      Performance: &#8211; Worst case: O(n2) n-square &#8211; Best case: O(n) &#8211; Average case: O(n2) n-square &#8211; worst case space complexity: O(1)
    </li>
  </ul>
  
  <div class="highlight highlight-source-python">
    <pre><code>arr &lt;span class="pl-k">=&lt;/span> [&lt;span class="pl-c1">2&lt;/span>,&lt;span class="pl-c1">7&lt;/span>,&lt;span class="pl-c1">1&lt;/span>,&lt;span class="pl-c1">8&lt;/span>,&lt;span class="pl-c1">5&lt;/span>,&lt;span class="pl-c1">9&lt;/span>,&lt;span class="pl-c1">11&lt;/span>,&lt;span class="pl-c1">35&lt;/span>,&lt;span class="pl-c1">25&lt;/span>]
selection_sort(arr)
&lt;span class="pl-c1">print&lt;/span> (arr)
[&lt;span class="pl-c1">1&lt;/span>, &lt;span class="pl-c1">2&lt;/span>, &lt;span class="pl-c1">5&lt;/span>, &lt;span class="pl-c1">7&lt;/span>, &lt;span class="pl-c1">8&lt;/span>, &lt;span class="pl-c1">11&lt;/span>, &lt;span class="pl-c1">25&lt;/span>, &lt;span class="pl-c1">35&lt;/span>]</code></pre>
    
    <p>
      &nbsp;
    </p>
  </div>
  
  <h5>
    <a id="user-content-insertion-sort-implementation" class="anchor" href="https://github.com/ppant/DS-Algos-Python#insertion-sort-implementation" aria-hidden="true"></a>Insertion Sort Implementation
  </h5>
  
  <p>
    Insertion sort always maintains a sorted sub list in the lower portion of the list Each new item is then &#8220;inserted&#8221; back into the previous sublist such that the sorted sub list is one item larger complexity O(n2) square
  </p>
  
  <div class="highlight highlight-source-python">
    <pre><code>arr &lt;span class="pl-k">=&lt;/span> [&lt;span class="pl-c1">2&lt;/span>,&lt;span class="pl-c1">7&lt;/span>,&lt;span class="pl-c1">1&lt;/span>,&lt;span class="pl-c1">8&lt;/span>,&lt;span class="pl-c1">5&lt;/span>,&lt;span class="pl-c1">9&lt;/span>,&lt;span class="pl-c1">11&lt;/span>,&lt;span class="pl-c1">35&lt;/span>,&lt;span class="pl-c1">25&lt;/span>]
insertion_sort(arr)
&lt;span class="pl-c1">print&lt;/span> (arr)
[&lt;span class="pl-c1">1&lt;/span>, &lt;span class="pl-c1">2&lt;/span>, &lt;span class="pl-c1">5&lt;/span>, &lt;span class="pl-c1">7&lt;/span>, &lt;span class="pl-c1">8&lt;/span>, &lt;span class="pl-c1">11&lt;/span>, &lt;span class="pl-c1">25&lt;/span>, &lt;span class="pl-c1">35&lt;/span>]</code></pre>
    
    <p>
      &nbsp;
    </p>
  </div>
  
  <h5>
    <a id="user-content-merge-sort-implementation" class="anchor" href="https://github.com/ppant/DS-Algos-Python#merge-sort-implementation" aria-hidden="true"></a>Merge Sort Implementation
  </h5>
  
  <p>
    Merge sort is a recursive algorithm (example of divide and conquer) that continually splits a list in half.
  </p>
  
  <ul>
    <li>
      If the list is empty or has one item, it is sorted by definition (the base case).
    </li>
    <li>
      If the list has more than one item, we split the list and recursively invoke a
    </li>
    <li>
      Merge sort on both halves.
    </li>
    <li>
      Once the two halves are sorted, the fundamental operation, called a merge, is performed.
    </li>
    <li>
      Merging is the process of taking two smaller sorted lists and combining them
    </li>
    <li>
      together into a single, sorted, new list.
    </li>
    <li>
      This algorithm is used to sort a linked list
    </li>
    <li>
      Performance: &#8211; Worst case: O(nlog n) &#8211; Best case: O(nlog n) &#8211; Average case: O(nlog n)
    </li>
  </ul>
  
  <div class="highlight highlight-source-python">
    <pre><code>arr &lt;span class="pl-k">=&lt;/span> [&lt;span class="pl-c1">11&lt;/span>,&lt;span class="pl-c1">2&lt;/span>,&lt;span class="pl-c1">5&lt;/span>,&lt;span class="pl-c1">4&lt;/span>,&lt;span class="pl-c1">7&lt;/span>,&lt;span class="pl-c1">6&lt;/span>,&lt;span class="pl-c1">8&lt;/span>,&lt;span class="pl-c1">1&lt;/span>,&lt;span class="pl-c1">23&lt;/span>]
merge_sort(arr)
&lt;span class="pl-c1">print&lt;/span> (arr)
[&lt;span class="pl-c1">1&lt;/span>, &lt;span class="pl-c1">2&lt;/span>, &lt;span class="pl-c1">4&lt;/span>, &lt;span class="pl-c1">5&lt;/span>, &lt;span class="pl-c1">6&lt;/span>, &lt;span class="pl-c1">7&lt;/span>, &lt;span class="pl-c1">8&lt;/span>, &lt;span class="pl-c1">11&lt;/span>, &lt;span class="pl-c1">23&lt;/span>]</code></pre>
    
    <p>
      &nbsp;
    </p>
  </div>
  
  <h5>
    <a id="user-content-quick-sort-implementation" class="anchor" href="https://github.com/ppant/DS-Algos-Python#quick-sort-implementation" aria-hidden="true"></a>Quick Sort Implementation
  </h5>
  
  <p>
    The quick sort uses divide and conquer to gain the same advantages as the merge sort, while not using additional storage also known as &#8220;partition exchange sort&#8221;.
  </p>
  
  <ul>
    <li>
      As a trade-off, however, it is possible that the list may not be divided in half.
    </li>
    <li>
      When this happens, we will see that performance is diminished.
    </li>
    <li>
      A quick sort first selects a value, which is called the pivot value.
    </li>
    <li>
      The role of the pivot value is to assist with splitting the list.
    </li>
    <li>
      The actual position where the pivot value belongs in the final sorted list, commonly called the split point, will<br /> be used to divide the list for subsequent calls to the quick sort.
    </li>
    <li>
      Performance: <ul>
        <li>
          Worst case: O(n square)
        </li>
        <li>
          Best case: O(nlog n)
        </li>
        <li>
          Average case: O(nlog n)
        </li>
      </ul>
    </li>
  </ul>
  
  <div class="highlight highlight-source-python">
    <pre><code>arr &lt;span class="pl-k">=&lt;/span> [&lt;span class="pl-c1">2&lt;/span>,&lt;span class="pl-c1">7&lt;/span>,&lt;span class="pl-c1">1&lt;/span>,&lt;span class="pl-c1">8&lt;/span>,&lt;span class="pl-c1">5&lt;/span>,&lt;span class="pl-c1">9&lt;/span>,&lt;span class="pl-c1">11&lt;/span>,&lt;span class="pl-c1">35&lt;/span>,&lt;span class="pl-c1">25&lt;/span>]
quick_sort(arr)
&lt;span class="pl-c1">print&lt;/span> (arr)
[&lt;span class="pl-c1">1&lt;/span>, &lt;span class="pl-c1">2&lt;/span>, &lt;span class="pl-c1">5&lt;/span>, &lt;span class="pl-c1">7&lt;/span>, &lt;span class="pl-c1">8&lt;/span>, &lt;span class="pl-c1">11&lt;/span>, &lt;span class="pl-c1">25&lt;/span>, &lt;span class="pl-c1">35&lt;/span>]</code></pre>
    
    <p>
      &nbsp;
    </p>
  </div>
  
  <h5>
    <a id="user-content-shell-sort-implementation" class="anchor" href="https://github.com/ppant/DS-Algos-Python#shell-sort-implementation" aria-hidden="true"></a>Shell Sort Implementation
  </h5>
  
  <p>
    This is also called diminishing incremental sort
  </p>
  
  <ul>
    <li>
      The shell sort improves on insertion sort by breaking the original list into a number of smaller sublists.
    </li>
    <li>
      The unique way these sun lists are chosen is the key to the shell sort
    </li>
    <li>
      Instead of breaking the list into sublists of contiguous items, the shell sort uses an increment ”i” to create a sublist by choosing all items that are ”i” items apart.
    </li>
    <li>
      Shell sort is efficient for medium size lists
    </li>
    <li>
      Complexity somewhere between O(n) and O(n2) square
    </li>
  </ul>
  
  <div class="highlight highlight-source-python">
    <pre><code>arr &lt;span class="pl-k">=&lt;/span> [&lt;span class="pl-c1">45&lt;/span>,&lt;span class="pl-c1">67&lt;/span>,&lt;span class="pl-c1">23&lt;/span>,&lt;span class="pl-c1">45&lt;/span>,&lt;span class="pl-c1">21&lt;/span>,&lt;span class="pl-c1">24&lt;/span>,&lt;span class="pl-c1">7&lt;/span>,&lt;span class="pl-c1">2&lt;/span>,&lt;span class="pl-c1">6&lt;/span>,&lt;span class="pl-c1">4&lt;/span>,&lt;span class="pl-c1">90&lt;/span>]
shell_sort(arr)
&lt;span class="pl-c1">print&lt;/span> (arr)
[&lt;span class="pl-c1">2&lt;/span>, &lt;span class="pl-c1">4&lt;/span>, &lt;span class="pl-c1">6&lt;/span>, &lt;span class="pl-c1">7&lt;/span>, &lt;span class="pl-c1">21&lt;/span>, &lt;span class="pl-c1">23&lt;/span>, &lt;span class="pl-c1">24&lt;/span>, &lt;span class="pl-c1">45&lt;/span>, &lt;span class="pl-c1">45&lt;/span>, &lt;span class="pl-c1">67&lt;/span>, &lt;span class="pl-c1">90&lt;/span>]</code></pre>
    
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
      <strong>Ref: </strong> The inspiration of implementing DS in Python is from <a href="http://interactivepython.org/runestone/static/pythonds/index.html">this</a> course
    </p>
  </div>
</div>