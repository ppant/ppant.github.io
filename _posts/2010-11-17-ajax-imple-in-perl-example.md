---
id: 186
title: Working With AJAX and Perl with example
date: 2010-11-17T12:27:22+05:30
author: Pradeep Pant
layout: post
guid: http://ppant.wordpress.com/?p=186
permalink: /2010/11/17/ajax-imple-in-perl-example/
jabber_published:
  - "1289977046"
dsq_thread_id:
  - "780495575"
---
<p style="padding-left:30px;">
  Hello,
</p>

<p style="text-align:left;padding-left:30px;">
  While doing Ajax Perl application development, I came across an interesting article on the following <a href="http://code.activestate.com/recipes/502299-simple-example-demonstrating-ajax-implementation-u/?in=user-4040865">link</a>.
</p>

<p style="padding-left:30px;">
  The article demonstrate with an example how Ajax can be used with Perl.  In the example given, there is table containing Student names and Marks. Every row has an Edit button, by which user can edit the information for that row. THE DB used is Microsoft Access to keep things simple. In order to run the below example code you will have to create a table by the name “Student” in MS Access”. It should have the following columns.
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">Column Name Data type Sl_No(Primary Key) Number Name Text Marks Number</span>
</p>

<p style="padding-left:30px;">
  Also you need to create a DSN by the name “mydsn” pointing to the Access DB.
</p>

<p style="padding-left:30px;">
  The basic logic here used in the example is that we have two separate rows for View and Edit (for every Student). Initially we hide the Edit row (by using style=&#8221;display:none&#8221;) and display the View Row(by using style=&#8221;display:block&#8221;). When the user clicks on the “Edit” button, the View row becomes hidden and the Edit row is displayed. We have used JavaScript to toggle between the rows. Below is the code snippet used in files <span style="color:#993300;">(AjaxExample.pl and student.js)</span>.
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">============================================================</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"><strong>AjaxExample.pl</strong></span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">============================================================</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">#!perl</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">use DBI qw(:sql_types);</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">use CGI;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">use CGI qw/:standard/;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">use CGI::Ajax;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">my $cgi = new CGI();</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">#&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># Mapping the Perl subroutine to the triggering function</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">#&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">my $ajax = new CGI::Ajax( &#8216;saveStudInfo_JScript&#8217; => &saveStudInfo_PerlScript );</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$cgi->header(-charset=>&#8217;US-ASCII&#8217;);</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">print $ajax->build_html($cgi,&generateHTML);</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">#&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># Subroutine which generates the HTML</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">#&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">sub generateHTML {</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># Hash which contains existing data</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">%Students = get_Student_Info();</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$cnt = 1;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># Write the html code in the form of a string</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  &#8220;n<HTML>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  &#8220;n<HEAD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  &#8220;n<TITLE>Student Information</TITLE>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  &#8220;<SCRIPT language=&#8221;javascript&#8221; src=&#8221;/javascript/student.js&#8221; type=&#8221;text/javascript&#8221;></SCRIPT>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  &#8220;n</HEAD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  &#8220;n<BODY bgColor=&#8221;#ffffff&#8221;>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  &#8220;<FORM  method=&#8221;POST&#8221; enctype=&#8221;multipart/form-data&#8221; name=&#8221;StudentForm&#8221;>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<BR>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<BR>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<TABLE cellspacing=&#8221;0&#8243; cellpadding=&#8221;0&#8243; align=&#8221;center&#8221;>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<TR><TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<TABLE width=&#8221;100%&#8221; align=&#8221;center&#8221; border=&#8221;1&#8243; cellpadding=&#8221;3&#8243; cellspacing=&#8221;1&#8243; id= &#8220;StudentInfoTable&#8221;>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<TR>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<TD align=&#8221;center&#8221; >SL No</TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<TD align=&#8221;center&#8221;  nowrap>Name  </TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<TD align=&#8221;center&#8221; nowrap>Marks  </TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<TD align=&#8221;center&#8221; >&nbsp;</TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n</TR >&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">foreach $key (sort { $a <=> $b }(keys %Students)) {</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">#View row</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  &#8220;n<INPUT type=&#8221;hidden&#8221; name=&#8221;SerialNo&#8221; id=&#8221;SerialNo_$key&#8221; value=&#8221;$key&#8221;>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<TR style=&#8221;display:block&#8221;>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=&#8221;n<TD align=&#8221;center&#8221; >$key</TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=&#8221;n<TD align=&#8221;center&#8221;  nowrap><Div id=&#8221;Div_Name_$key&#8221;>&#8221;. (($Students{$key}->{Name}) ? $Students{$key}->{Name} : &#8220;&nbsp;&#8221;).&#8221;</DIV></TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=&#8221;n<TD align=&#8221;center&#8221;  nowrap><Div id=&#8221;Div_Marks_$key&#8221;>&#8221;. (($Students{$key}->{Name}) ? $Students{$key}->{Marks} : &#8220;&nbsp;&#8221;).&#8221;</DIV></TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<TD  align=&#8221;center&#8221;><INPUT type=&#8221;button&#8221; name=&#8221;EditButton&#8221; value=&#8221;Edit&#8221; style=&#8221;cursor: hand; width: 40px&#8221; onClick=&#8221;makeRowEditable($cnt,&#8217;StudentInfoTable&#8217;)&#8221;></TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n</TR >&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">#Edit row</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<TR style=&#8221;display:none&#8221;>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=&#8221;n<TD align=&#8221;center&#8221;  nowrap>$key</TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=&#8221;n<TD align=&#8221;center&#8221;  nowrap><INPUT type=&#8221;text&#8221; size=&#8221;30&#8243; id=&#8221;Student_Name_$key&#8221; value=&#8221;$Students{$key}->{Name}&#8221;  style=&#8221;text-align: center&#8221;></TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=&#8221;n<TD align=&#8221;center&#8221;  nowrap><INPUT type=&#8221;text&#8221; size=&#8221;10&#8243; id=&#8221;Student_Marks_$key&#8221; value=&#8221;$Students{$key}->{Marks}&#8221;  style=&#8221;text-align: center&#8221;></TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n<TD  align=&#8221;center&#8221;><INPUT type=&#8221;button&#8221; name=&#8221;SaveButton&#8221; value=&#8221;Save&#8221; style=&#8221;cursor: hand; width: 40px&#8221; onClick=&#8221;saveStudInfo_JScript([&#8216;Student_Name_$key&#8217;,&#8217;Student_Marks_$key&#8217;,&#8217;SerialNo_$key&#8217;,&#8217;NO_CACHE&#8217;],[&#8216;Div_Name_$key&#8217;,&#8217;Div_Marks_$key&#8217;],&#8217;POST&#8217;);makeRowViewable($cnt,&#8217;StudentInfoTable&#8217;)&#8221;></TD>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n</TR >&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$cnt += 2;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n</TABLE>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n</TD></TR>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= &#8220;n</Table>&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">#&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># Perl Subroutine which is called aschronously</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">#&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">sub saveStudInfo_PerlScript {</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># Accept Input</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">my $Name = shift;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">my $Marks = shift;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">my $SerialNo = shift;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># Call subroutine which does database update</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">update_Student_Info($SerialNo,$Name,$Marks);</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># Return Output</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">return (@Return, ($Name ne &#8220;&#8221;) ? $Name : &#8220;&nbsp;&#8221;,($Marks ne &#8220;&#8221;) ? $Marks : &#8220;&nbsp;&#8221;);</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">#&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># Subroutine which fetches the data</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">#&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">sub get_Student_Info {</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">my %Details;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">my ($sql, $sth, $row);</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># DSN with the name &#8220;mydsn&#8221;  points to the Db</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$DB = &#8220;mydsn&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># User name and password if any need to be specified. Currently no user name and pwd set.&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$DB_USER = &#8220;&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$DB_PASS= &#8220;&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$dbh = DBI->connect(&#8220;dbi:ODBC:$DB&#8221;, $DB_USER, $DB_PASS);</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$sql = &#8220;SELECT * FROM Student&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$sth = $dbh->prepare($sql);</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$sth->execute;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$cnt = 1;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">while ($row = $sth->fetchrow_hashref) {</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$Details{$cnt++} = $row;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$sth->finish();</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">return %Details;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">#&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># Subroutine which updates the Student Table in DB</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">#&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">sub update_Student_Info   {</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">my $SerialNo = shift;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">my $Name = shift;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">my $Marks = shift;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">my ($sql, $sth,$row);</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># DSN with the name &#8220;mydsn&#8221;  points to the Db</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$DB = &#8220;mydsn&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;"># User name and password if any need to be specified. Currently no user name and pwd set.</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$DB_USER = &#8220;&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$DB_PASS= &#8220;&#8221;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$dbh = DBI->connect(&#8220;dbi:ODBC:$DB&#8221;, $DB_USER, $DB_PASS);</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$sql  = &#8220;Update Student set Name = &#8216;$Name&#8217;,Marks = $Marks where Sl_No = $SerialNo &#8220;;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$sth = $dbh->prepare($sql);</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$sth->execute;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">$sth->finish();</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">return $sql;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">============================================================</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">student.js</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">============================================================</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">/*</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">* Toggles the rows from EDIT mode to VIEW mode.</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">* Invoked on clicking the &#8216;SAVE&#8217; button in last column.</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">*/</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">function makeRowViewable(rowNumber,id) {</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">var table = document.all ? document.all[id]  : document.getElementById ? document.getElementById(id) : null;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">var editableRowNumber = rowNumber + 1 ;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">var nonEditableRowNumber = editableRowNumber -1 ;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">table.rows[editableRowNumber].style.display = &#8220;none&#8221; ;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">table.rows[nonEditableRowNumber].style.display = &#8220;block&#8221; ;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">/*</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">* Toggles the rows from view mode to edit mode.</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">* Invoked on clicking the &#8216;EDIT&#8217; button in last column.</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#993300;">*/</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">function makeRowEditable(rowNumber,id) {</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">var table = document.all ? document.all[id]  : document.getElementById ? document.getElementById(id) : null;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">var editableRowNumber = rowNumber + 1 ;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">var nonEditableRowNumber = editableRowNumber -1 ;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">table.rows[editableRowNumber].style.display = &#8220;block&#8221; ;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">table.rows[nonEditableRowNumber].style.display = &#8220;none&#8221; ;</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>
</p>

<p style="padding-left:30px;">
  <span style="color:#008000;"><br /> </span>
</p>

<p style="padding-left:30px;">
  As we know, the term <a href="http://en.wikipedia.org/wiki/Ajax_(programming)">Ajax</a> stands for ‘Asynchronous JavaScript And XML’. It is not a technology but a set of technologies being used together in a particular way. With effective use of existing technologies like HTML, DHTML, DOM, CSS, JavaScript one can make web pages more dynamic and interactive.
</p>

<p style="padding-left:30px;">
  Using JavaScript, Ajax makes an asynchronous call to the server and fetches an XML document from a server-side component. Upon completion of the request, JavaScript may be used to update or modify the Document Object Model (DOM) of the HTML page. Only the necessary portions of the HTML DOM are re-rendered in the HTML page. In short Ajax techniques let you update parts of your web page without reloading the whole page.
</p>

<p style="padding-left:30px;">
  The general benefit here is that an asynchronous operation executes in a separate thread. So when an operation is triggered asynchronously by the application, it can continue executing while the asynchronous method performs its task. Moreover only the data that needs to be updated or inserted can be sent instead of sending the entire form data. <a href="http://ajaxpatterns.org/Perl_Ajax_Frameworks">Perl Ajax framework</a> are also available for faster development and test.
</p>

<p style="padding-left:30px;">
  Popular web applications like  Gmail, Amazon, Orkut etc are using Ajax.
</p>

<p style="padding-left:30px;">
  <p style="padding-left:30px;">
    <span style="color:#993300;"><strong>References and more links:</strong></span>
  </p>
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;"><a href="http://code.activestate.com/recipes/502299-simple-example-demonstrating-ajax-implementation-u/">Simple Example demonstrating Ajax Implementation using Perl « Perl recipes « ActiveState Code</a>.</span>
  </p>
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;"><a href="http://www.perl.com/pub/2006/03/02/ajax_and_perl.html">http://www.perl.com/pub/2006/03/02/ajax_and_perl.html</a></span>
  </p>
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;"><a href="http://perl.about.com/b/2006/03/17/using-ajax-from-perl.htm">http://perl.about.com/b/2006/03/17/using-ajax-from-perl.htm</a></span>
  </p>
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;"><a href="http://ajaxpatterns.org/Perl_Ajax_Frameworks">http://ajaxpatterns.org/Perl_Ajax_Frameworks</a></span>
  </p>
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;"><a href="http://search.cpan.org/~bpederse/CGI-Ajax-0.707/">http://search.cpan.org/~bpederse/CGI-Ajax-0.707/</a></span>
  </p>
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;"><br /> </span>
  </p>
  
  <p style="padding-left:30px;">
    Enjoy using Ajax from Perl.
  </p>
  
  <p style="padding-left:60px;">
    <span style="color:#993300;"><br /> </span>
  </p>