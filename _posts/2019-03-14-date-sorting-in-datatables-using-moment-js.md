---
id: 1852
title: date sorting in datatables using moment js
date: 2019-03-14T21:22:11+05:30
author: Pradeep Pant
layout: post
guid: http://pradeeppant.com/?p=1852
permalink: /2019/03/14/date-sorting-in-datatables-using-moment-js/
twitter_share:
  - 'a:1:{s:8:"hashtags";a:1:{i:0;s:68:"programming #datatables #jquery #javascipt #datetimesorting #sorting";}}'
---
Sorting dates could be tricky because of various date and time format used. Fortunately there is awsome js lib called [moment.js](https://momentjs.com/) library avaliable, this is free and open source. I have made a small demo of how moment.js is used with datatables. for date sorting. First let have a look into how many date time types which moment.js supports.

### Format Dates

<pre class="wp-block-code"><code>moment().format('MMMM Do YYYY, h:mm:ss a'); // March 12th 2019, 6:46:42 pm
moment().format('dddd');                    // Tuesday
moment().format("MMM Do YY");               // Mar 12th 19
moment().format('YYYY [escaped] YYYY');     // 2019 escaped 2019
moment().format();                          // 2019-03-12T18:46:42+05:30
                                            // undefined</code></pre>

### Relative Time

<pre class="wp-block-code"><code>moment("20111031", "YYYYMMDD").fromNow(); // 7 years ago
moment("20120620", "YYYYMMDD").fromNow(); // 7 years ago
moment().startOf('day').fromNow();        // 19 hours ago
moment().endOf('day').fromNow();          // in 5 hours
moment().startOf('hour').fromNow();       // an hour ago
                                          // undefined</code></pre>

### Calendar Time

<pre class="wp-block-code"><code>moment().subtract(10, 'days').calendar(); // 03/02/2019
moment().subtract(6, 'days').calendar();  // Last Wednesday at 6:46 PM
moment().subtract(3, 'days').calendar();  // Last Saturday at 6:46 PM
moment().subtract(1, 'days').calendar();  // Yesterday at 6:46 PM
moment().calendar();                      // Today at 6:46 PM
moment().add(1, 'days').calendar();       // Tomorrow at 6:46 PM
moment().add(3, 'days').calendar();       // Friday at 6:46 PM
moment().add(10, 'days').calendar();      // 03/22/2019
                                          // undefined</code></pre>

### Multiple Locale Support

<pre class="wp-block-code"><code>moment.locale();         // en
moment().format('LT');   // 6:46 PM
moment().format('LTS');  // 6:46:42 PM
moment().format('L');    // 03/12/2019
moment().format('l');    // 3/12/2019
moment().format('LL');   // March 12, 2019
moment().format('ll');   // Mar 12, 2019
moment().format('LLL');  // March 12, 2019 6:46 PM
moment().format('lll');  // Mar 12, 2019 6:46 PM
moment().format('LLLL'); // Tuesday, March 12, 2019 6:46 PM
moment().format('llll'); // Tue, Mar 12, 2019 6:46 PM
                        

</code></pre>

I have used the following libs to make this demo:

  * jquery
  * data table
  * moment.js 
  * datetime-moment.js



## HTML source

<pre class="wp-block-code"><code>
&lt;h3 class="ui_title">Employee joining data&lt;/h3>
&lt;div class="ui_block">
&lt;table id="myTable1" class="ui_table">
&lt;thead id="table_head">
&lt;tr>
&lt;th style="width:150px;">Name&lt;/th>
&lt;th style="width:50px;">Designation&lt;/th>
&lt;th>Joining date&lt;/th>
&lt;/tr>
&lt;/thead>
&lt;tbody>
&lt;tr>
	&lt;td>Ram&lt;/td>	
	&lt;td>Engineer&lt;/td>
	&lt;td>18/10/2015&lt;/td>	
&lt;/tr>
&lt;tr>
	&lt;td>Shyam&lt;/td>	
	&lt;td>Engineer&lt;/td>
	&lt;td>05/01/2012&lt;/td>	
&lt;/tr>
&lt;tr>
	&lt;td>Suresh&lt;/td>	
	&lt;td>Sr. Engineer&lt;/td>
	&lt;td>22/06/2010&lt;/td>	
&lt;/tr>
&lt;tr>
	&lt;td>Ahmed&lt;/td>	
	&lt;td>Manager&lt;/td>
	&lt;td>02/02/2002&lt;/td>	
&lt;/tr>
&lt;tr>
	&lt;td>Leena&lt;/td>	
	&lt;td>Sr. Manager&lt;/td>
	&lt;td>01/01/2018&lt;/td>	
&lt;/tr>
&lt;tr>
	&lt;td>Pradeep&lt;/td>	
	&lt;td>Architect&lt;/td>
	&lt;td>21/05/2012&lt;/td>	
&lt;/tr>
&lt;/tbody>
&lt;/table>
&lt;/div>
</code></pre>

## jQuery

<pre class="wp-block-code"><code>jQuery(document).ready(function() {
$.fn.dataTableExt.oPagination.iFullNumbersShowPages = 3;
$.fn.dataTable.moment('DD/MM/YYYY');
		$("#myTable1").DataTable({	
		"autoWidth": false,
		"destroy": true,
		"order": [[2, 'desc']],
		"pageLength": 15,
		"lengthMenu": [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
		"pagingType": "full_numbers"
});
});	</code></pre>

## CSS

<pre class="wp-block-code"><code>/* 1. GENERAL */
* {
	font-family: /* 'Roboto', */ Verdana, Arial, Helvetica, sans-serif;
	font-size: 13px;
	box-sizing: border-box;
}

body {
	font-family: /* 'Roboto', */ Verdana, Arial, sans-serif;
	background: #f8f8f8; /* e2dbc5; */
	margin: 1em;
}

.ui_title {
	font-family: /* 'Open Sans', */ Verdana, sans-serif;
	color: #2A3F54;
	font-weight: 400;
	font-size: 24px;
	line-height:26.4px;
	border-bottom: 1px solid  #2A3F54;
}

.ui_title i {
	font-size: 24px;
}

/* BLOCKS */
.ui_block {
	min-width: 20px;
	background: white;
	border: 0; /* 1px solid #ebebeb;*/
	padding: 1em 1em;
	margin-bottom: 2em;
	box-shadow: 0 4px 6px 0 hsla(0,0%,0%,0.2);
}

.ui_block h3,
.ui_block h3 i {
	font-family: /* 'Open Sans', */ Verdana, sans-serif;
	border-bottom: 2px solid rgb(230,233,237);
	color: rgb(115,135,156);
	font-weight: 400;
	font-size: 16px;
	line-height: 18.7px;
	padding: 0;
	margin: 1em 0 0.5em 0;
}
.ui_block h3:first-child {
	margin: 0.5em 0 0.5em 0;
}

/* 3. TABLE */
.ui_table {
	border: 1px solid black;
	border-collapse: collapse;
	width:100%;
	margin-bottom: 1em;
}
.ui_table th {
	text-align: left;
	background: lightgray;
}
.ui_table td,
.ui_table th {
	border: 1px solid gray;
	padding: 3px 5px;
	font-size: 10pt;
	font-weight: 400;
}
</code></pre>

## Demo 

**jsFiddle**  
h[ttps://jsfiddle.net/ppant/efL3pvq2/3/](https://jsfiddle.net/ppant/efL3pvq2/3/)  
**Github**  
<https://github.com/ppant/jshacks/blob/master/data-table-date-sorting.html> 

## References:

  


  * **momentjs lib:**  
    [h](https://momentjs.com/)t[tps://momentjs.com/](https://momentjs.com/)
  * **Datetable moment plugin:**  
    <https://datatables.net/plug-ins/sorting/datetime-moment>