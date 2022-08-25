---
title: 'JSX in ReactJS: a quick intro with examples'
date: 2019-11-27T21:55:47+05:30
author: Pradeep Pant
layout: post
---
**What is JSX file **

  * A JSX file can have HTML code in a JavaScript file. 
  * JSX elements are treated as JavaScript expressions. 
  * JSX element looks exactly like HTML, this can be put in a JS file instead of an HTML file. 
  * JSX element can be saved a variable, can be passed in a function or can also be stored in an object or an array.
  * JSX is not a JavaScript, so browsers can't read it.
  * A JSX compiler is needed, to compile to JSX to covert to native JS
  * We can give attribute in JSX elements just like HTML  
    e.g.; 
	````html 
	<p id="test"></p>
	````
  * Use parentheses to wrap multi-line JSX expressions  
    ````html 
	(<br>  <hr>Test</h1>              
	 <br> )
	````

  * JSX outer element should be exactly one, if not wrap all the code in a ````html <div> </div>````
  * ````ReactDOM```` is the JSX renderer.
  * ````ReactDOM.render()````is the most common way to render JSX. It takes a JSX expression, creates a corresponding tree of DOM nodes, and adds that tree to the DOM. 
  * The first argument to `ReactDOM.render` is a JSX element or a variable having the JSX expression, the second argument is the target.
  * One special thing about ````ReactDOM.render()```` is that it *only updates DOM elements that have changed*.  This is significant! Only updating the necessary DOM elements is a large part of what makes React so successful. React does this by something called *Virtual DOM*

**More JSX**

  * JSX and HTML grammar are mostly the same except class attribute, in JSX you will have to use ````ClassName````, this is because JSX is get converted to native JS and ````class```` is reserved there 
  * Self-closing tags One has to add a mandatory slash (/) e.g.; ````html <br />```` in HTML slash is optional.
  * We can also write native JavaScript inside a JSX file
  * Curly braces are used to embed the JS code inside JSX expression, any JS code inside the curly braces will be executed.  
  
Examples:

**HTML inside JSX -> output: 2 + 3**
	```` import React from 'react';
	import ReactDOM from 'react-dom';
	ReactDOM.render(<h1>2 + 3</h1>,document.getElementById('app'));````

**JS inside JSX-> output: 5**  
	````import React from 'react';    
	import ReactDOM from 'react-dom';    
	ReactDOM.render(<h1>{2 + 3}</h1>,document.getElementById('app'));````  


More about JSX and React on my next post.  
  
Keep learning!