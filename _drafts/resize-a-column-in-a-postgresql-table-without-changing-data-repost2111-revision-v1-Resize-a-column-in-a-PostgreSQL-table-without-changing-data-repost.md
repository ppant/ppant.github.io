---
id: 2112
title: 'Resize a column in a PostgreSQL table without changing data: repost'
date: 2019-10-15T16:02:43+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2019/10/2111-revision-v1/
permalink: /2019/10/15/2111-revision-v1/
---
This morning I realized that one of the columns in the table I have recently created is running out of space. It is varchar(10) and I want to make it varchar(20). I want to do this without losing any data which got filled in the last couple of days. I found this awesome post on Resize a column in a PostgreSQL table without changing data. As this an almost 10 yrs old post so reposting in case lost.

<pre class="wp-block-preformatted">You use Post­greSQL. You find that a col­umn you have in a table is of a smaller length than you now wish. In my case, this was a&nbsp;<code>varchar(20)</code>&nbsp;that I now wished to make&nbsp;<code>varchar(35)</code>. Noth­ing else. I just want to change the size, keep­ing the data intact.</pre>

<pre class="wp-block-preformatted">The&nbsp;<code>ALTER TABLE ...ALTER COLUMN...TYPE...</code>&nbsp;com­mand is use­ful only if you want to alter the data some­how, or change the data type. Oth­er­wise, it'll be an aeon before this fin­ishes even inside a trans­ac­tion on a data­base of any mean­ing­ful&nbsp;size.</pre>

<pre class="wp-block-preformatted">Until now, I was not famil­iar with any sen­si­ble mech­a­nism to sim­ply change the size in PG. But yes­ter­day, Tom Lane him­self sug­gested some­thing uber­cool in the&nbsp;list.</pre>

<pre class="wp-block-preformatted">Let's assume for the sake of sim­plic­ity that your table is called "<code>TABLE1</code>" and your col­umn is "COL1". You can find the size of your "<code>COL1</code>" col­umn by issu­ing the fol­low­ing query on the sys­tem tables:</pre>

<table class="wp-block-table">
  <tr>
    <td>
      <strong>SELECT</strong> atttypmod <strong>FROM</strong> pg_attribute <strong>WHERE</strong> attrelid = &#8216;TABLE1&#8217;::regclass <strong>AND</strong> attname = &#8216;COL1&#8217;; &nbsp; atttypmod <em>&#8212;&#8212;&#8212;&#8211;</em> 24 (1 <strong>ROW</strong>)
    </td>
  </tr>
</table>

<pre class="wp-block-preformatted">This means that the size is 20 (4 is added for legacy rea­sons, we're told). You can now con­ve­niently change this to a&nbsp;<code>varchar(35)</code>&nbsp;size by issu­ing this command:</pre>

<table class="wp-block-table">
  <tr>
    <td>
      <strong>UPDATE</strong> pg_attribute <strong>SET</strong> atttypmod = 35+4 <strong>WHERE</strong> attrelid = &#8216;TABLE1&#8217;::regclass <strong>AND</strong> attname = &#8216;COL1&#8217;; &nbsp; <strong>UPDATE</strong> 1
    </td>
  </tr>
</table>

<pre class="wp-block-preformatted">Note that I man­u­ally added the 4 to the desired size of 35..again, for some legacy rea­sons inside PG. Done. That's it. Should we&nbsp;check?</pre>

<table class="wp-block-table">
  <tr>
    <td>
      d TABLE1 &nbsp; <strong>TABLE</strong> &#8220;public.TABLE1&#8221; <strong>COLUMN</strong> | <strong>TYPE</strong> | Modifiers <em>&#8212;&#8212;&#8211;+&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;+&#8212;&#8212;&#8212;&#8211;</em> COL1 | <strong>CHARACTER</strong> <strong>VARYING</strong>(35) |
    </td>
  </tr>
</table>

<pre class="wp-block-preformatted">Such a sim­ple yet effec­tive trick. Of course it'd be nicer if this is some­how included in a more proper way in the data­base, but this does the&nbsp;job.</pre>

  * 

Check below post