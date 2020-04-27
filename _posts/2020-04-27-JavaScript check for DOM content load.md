---
title: 'JavaScript DOM content load check'
date: 2020-04-27
author: Pradeep Pant
layout: post
---
DOM loading is an important event, sometimes you have some logic which takes DOM into consideration so knowing exactly when DOM has been loaded fully is the crucial info. DOM corresponds to Document Object Model.

we all know that anything which is put onside the 
````js
<script></script>
```` 
tags will be executed instantly as soon as the script is downloaded to browser. So any logic which is based on not fully loaded DOM will go result in a crash or wrong outcome.
So to resolve this its better to wait until the DOM tree is fully ready.

So, to wait on the DOM event, add an event listener to the document object. The
name of the event is 
````js
DOMContentLoaded
````
The event listener will make sure that all we have to make sure DOM tree is loaded fully into the memory so that any logic accessing DOM items will not results in any kind of error. 

 ````js
DOMContentLoaded
```` 
event fires when HTML content has been loaded completely without loading the CSS files, referred images etc which takes a major chunk of loading time for a page. 


Basic usage:
````js
window.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');
});
````

Example:
````js
<html>
<head>
<script type="text/javascript">
function DOMReadyCheck() {
alert("DOM is ready");
}
document.addEventListener("DOMContentLoaded", DOMReadyCheck);
</script>
</head>
</html>
````

Happy Coding!

You may check Web APIs at [Mozilla Developer Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event)

