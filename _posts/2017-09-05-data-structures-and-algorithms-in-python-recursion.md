---
id: 1696
title: 'Data Structures and Algorithms in Python Recursion'
date: 2017-09-05T18:26:16+05:30
author: Pradeep Pant
layout: post
---
## Computes the cumulative sum : Recursion

Aim is to write a recursive function which takes an integer and computes the cumulative sum of to that integer. For example, if n=4 , return 4+3+2+1+0, which is 10. We always should take car of the base case. In this case, we have a base case of n =0 (Note, you could have also designed the cut off to be 1). In this case, we have: n + (n-1) + (n-2) + ... + 0. 

#### Example:

```python
print (recursion_cululative_sum(5))
Result = 15
```

## Sum of digits : Recursion
Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1 

#### Example:

```python
print (recursion_sum_digits(12))
Result = 9+8+5+4 = 25
```

## Word split : Recursion

Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable. Example:

#### Example:
```python
print (word_split('themanran',['the','ran','man']))
['the', 'man', 'ran']
```



## Reverse a string : Recursion

Implement a recursive reverse. 

#### Example:
```python
print(reverse_str('hello world'))
'dlrow olleh'
```



## List all the permutation of a string : Recursion

Given a string, write a function that uses recursion to output a list of all the possible permutations of that string. For example, given s='abc' the function should return
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']. This way of doing permutaion is for learning in realscenerios better to use excellant Python library *ltertools* with current approach there are n! permutations, so the it looks that algorithm will take O(n*n!)time 

#### Example:

```python
print(permute('abc'))
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```



## Implement fibonacci sequence with simple iteration
We'll try to find the 9th no in the fibonacci sequence which is 34

#### Example:

```python
print (fibonacci_itertaive(9))
34
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

The recursive solution is exponential time Big-O , with O(n).

## Implement fibonacci sequence Recursion

Our function will accept a number n and return the nth number of the fibonacci sequence Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21, ... ; starts off with a base case checking to see if n = 0 or 1, then it returns 1. Else it returns fib(n-1)+fib(n+2).

#### Example:

We'll try to find the 9th no in the fibnacci sequence which is 34

```python
print (fibonacci_recursion(9))
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

The recursive solution is exponential time Big-O , with O(2^n). However, its a very simple and basic implementation to consider.

The recursive solution is exponential time Big-O , with O(2^n). However, its a very simple and basic implementation to consider.

## Implement fibonacci sequence Dynamic programming

Implement the function using dynamic programming by using a cache to store results (memoization). memoization + recursion = dynamic programming

#### Example:
We'll try to find the 9th no in the fibnacci sequence which is 34

```python
print (fibonacci_dynamic(9))
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

The recursive-memoization solution is exponential time Big-O , with O(n)

The recursive-memoization solution is exponential time Big-O , with O(n)

## Implement coin change problem Recursion

Given a target amount n and a list (array) of distinct coin values, what&#8217;s the fewest coins needed to make the change amount. 1+1+1+1+1+1+1+1+1+1 
5 + 1+1+1+1+1 
5+5 
10 With 1 coin being the minimum amount.

#### Example:

```python
print (coin_change_recursion(8,[1,5]))
4
```

**Note:**
The problem with this approach is that it is very inefficient! It can take many, 
many recursive calls to finish this problem and its also inaccurate for non 
standard coin values (coin values that are not 1,5,10, etc.)

## Implement coin change problem Dynamic programming

Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.

Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the
change amount.
1+1+1+1+1+1+1+1+1+1
5 + 1+1+1+1+1
5+5
10
With 1 coin being the minimum amount.

#### Example:
Caching

```python
target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)

print (coin_change_dynamic(target,coins,known_results))
print (coin_change_dynamic(8,[1,5]))
2
```



------


Check **[GitHub](https://github.com/ppant/DS-Algos-Python)** for the full working code.

I will keep adding more problems/solutions.

Stay tuned!

**Refernce:**  The inspiration of implementing DS in Python is from **[this](http://interactivepython.org/runestone/static/pythonds/index.html)** course