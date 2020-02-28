---
id: 2208
title: 'Decoupled Content Management Systems: Some thoughts'
date: 2019-12-17T21:47:37+05:30
author: Pradeep Pant
layout: post
guid: /?p=2208
permalink: /2019/12/17/decoupled-content-management-systems-some-thoughts/
---
<div class="wp-block-group">
  <div class="wp-block-group__inner-container">
    <p>
      If we look into existing CMS like Drupal, WordPress, etc there we see that they are still on an old way of delivering the content e.g.; HTML/ CSS to build the page and content storage which is coupled with the UI (maybe they are already in process?).
    </p>
    
    <p>
      In the new approach, we decouple the content source from UI and use a newer JavaScript framework and API to fetch the data using an excellent <a href="https://graphql.org/">GraphQL</a> query. The JavaScript framework to be used like <a href="https://reactjs.org/">ReactJS</a>, <a href="https://angularjs.org/">AngularJS</a> etc. One can use the components to make the dynamic elements as well. 
    </p>
  </div>
</div>

In a decoupled way, content resides separately and one can use API to fetch the data on-demand. so as a software developer mostly APIs will be developed And GraphQL type of language is used to querying the data. If you look into GraphQL, this is different than [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) architecture which takes the get request and in response fetches the full object irrespective if used or not whereas with GraphQL one can fetch an attribute of the data/object which helps hugely in reducing the client-server data and speed up things. 

Though decoupled way looks very promising probably not fits for all types of applications. So it advisable first to check out a few things before trying a switch. Below are a few which I can think of&#8230;

  1. If the API way of working will be beneficial for your application?
  2. What will be the backend technologies? 
  3. How this will affect the user interface like Tiny WYSIWYG etc. for online editing?
  4. The expertise of resources in the team developing the app (If you have good JS developers then a good idea to explore this route)  
  
  
    _`I am working on creating a static site using a decoupled implementation <a href="https://www.gatsbyjs.org/">gasbyjs</a>  (gas-bee) which uses API based model using reactJS and GraphQL`_.

<!--EndFragment-->