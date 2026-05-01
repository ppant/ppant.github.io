---
id: 186
title: Working With AJAX and Perl with example
date: 2010-11-17T12:27:22+05:30
layout: post
categories: [tech]
guid: http://ppant.wordpress.com/?p=186
permalink: /2010/11/17/ajax-imple-in-perl-example/
jabber_published:
  - "1289977046"
dsq_thread_id:
  - "780495575"
---
<p style="padding-left:30px;">
  Hello,


<p style="text-align:left;padding-left:30px;">
  While doing Ajax Perl application development, I came across an interesting article on the following <a href="http://code.activestate.com/recipes/502299-simple-example-demonstrating-ajax-implementation-u/?in=user-4040865">link</a>.


<p style="padding-left:30px;">
  The article demonstrate with an example how Ajax can be used with Perl.  In the example given, there is table containing Student names and Marks. Every row has an Edit button, by which user can edit the information for that row. THE DB used is Microsoft Access to keep things simple. In order to run the below example code you will have to create a table by the name “Student” in MS Access”. It should have the following columns.


<p style="padding-left:30px;">
  <span style="color:#008000;">Column Name Data type Sl_No(Primary Key) Number Name Text Marks Number</span>


<p style="padding-left:30px;">
  Also you need to create a DSN by the name “mydsn” pointing to the Access DB.


<p style="padding-left:30px;">
  The basic logic here used in the example is that we have two separate rows for View and Edit (for every Student). Initially we hide the Edit row (by using style="display:none") and display the View Row(by using style="display:block"). When the user clicks on the “Edit” button, the View row becomes hidden and the Edit row is displayed. We have used JavaScript to toggle between the rows. Below is the code snippet used in files <span style="color:#993300;">(AjaxExample.pl and student.js)</span>.


<p style="padding-left:30px;">
  <span style="color:#993300;">============================================================</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"><strong>AjaxExample.pl</strong></span>


<p style="padding-left:30px;">
  <span style="color:#993300;">============================================================</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">#!perl</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">use DBI qw(:sql_types);</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">use CGI;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">use CGI qw/:standard/;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">use CGI::Ajax;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">my $cgi = new CGI();</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">#——————————————————————–</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># Mapping the Perl subroutine to the triggering function</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">#——————————————————————–</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">my $ajax = new CGI::Ajax( 'saveStudInfo_JScript' => &saveStudInfo_PerlScript );</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$cgi->header(-charset=>'US-ASCII');</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">print $ajax->build_html($cgi,&generateHTML);</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">#——————————————————————–</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># Subroutine which generates the HTML</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">#——————————————————————–</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">sub generateHTML {</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># Hash which contains existing data</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">%Students = get_Student_Info();</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$cnt = 1;</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># Write the html code in the form of a string</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  "n<HTML>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  "n<HEAD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  "n<TITLE>Student Information</TITLE>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  "<SCRIPT language="javascript" src="/javascript/student.js" type="text/javascript"></SCRIPT>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  "n</HEAD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  "n<BODY bgColor="#ffffff">";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  "<FORM  method="POST" enctype="multipart/form-data" name="StudentForm">";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<BR>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<BR>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<TABLE cellspacing="0&#8243; cellpadding="0&#8243; align="center">";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<TR><TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<TABLE width="100%" align="center" border="1&#8243; cellpadding="3&#8243; cellspacing="1&#8243; id= "StudentInfoTable">";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<TR>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<TD align="center" >SL No</TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<TD align="center"  nowrap>Name  </TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<TD align="center" nowrap>Marks  </TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<TD align="center" >&nbsp;</TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n</TR >";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">foreach $key (sort { $a <=> $b }(keys %Students)) {</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">#View row</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .=  "n<INPUT type="hidden" name="SerialNo" id="SerialNo_$key" value="$key">";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<TR style="display:block">";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .="n<TD align="center" >$key</TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .="n<TD align="center"  nowrap><Div id="Div_Name_$key">". (($Students{$key}->{Name}) ? $Students{$key}->{Name} : "&nbsp;")."</DIV></TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .="n<TD align="center"  nowrap><Div id="Div_Marks_$key">". (($Students{$key}->{Name}) ? $Students{$key}->{Marks} : "&nbsp;")."</DIV></TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<TD  align="center"><INPUT type="button" name="EditButton" value="Edit" style="cursor: hand; width: 40px" onClick="makeRowEditable($cnt,'StudentInfoTable')"></TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n</TR >";</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">#Edit row</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<TR style="display:none">";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .="n<TD align="center"  nowrap>$key</TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .="n<TD align="center"  nowrap><INPUT type="text" size="30&#8243; id="Student_Name_$key" value="$Students{$key}->{Name}"  style="text-align: center"></TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .="n<TD align="center"  nowrap><INPUT type="text" size="10&#8243; id="Student_Marks_$key" value="$Students{$key}->{Marks}"  style="text-align: center"></TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n<TD  align="center"><INPUT type="button" name="SaveButton" value="Save" style="cursor: hand; width: 40px" onClick="saveStudInfo_JScript(['Student_Name_$key','Student_Marks_$key','SerialNo_$key','NO_CACHE'],['Div_Name_$key','Div_Marks_$key'],'POST');makeRowViewable($cnt,'StudentInfoTable')"></TD>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n</TR >";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$cnt += 2;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n</TABLE>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n</TD></TR>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$returnHTML .= "n</Table>";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">#——————————————————————–</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># Perl Subroutine which is called aschronously</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">#——————————————————————–</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">sub saveStudInfo_PerlScript {</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># Accept Input</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">my $Name = shift;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">my $Marks = shift;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">my $SerialNo = shift;</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># Call subroutine which does database update</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">update_Student_Info($SerialNo,$Name,$Marks);</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># Return Output</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">return (@Return, ($Name ne "") ? $Name : "&nbsp;",($Marks ne "") ? $Marks : "&nbsp;");</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">#——————————————————————–</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># Subroutine which fetches the data</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">#——————————————————————–</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">sub get_Student_Info {</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">my %Details;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">my ($sql, $sth, $row);</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># DSN with the name "mydsn"  points to the Db</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$DB = "mydsn";</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># User name and password if any need to be specified. Currently no user name and pwd set.";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$DB_USER = "";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$DB_PASS= "";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$dbh = DBI->connect("dbi:ODBC:$DB", $DB_USER, $DB_PASS);</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$sql = "SELECT * FROM Student";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$sth = $dbh->prepare($sql);</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$sth->execute;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$cnt = 1;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">while ($row = $sth->fetchrow_hashref) {</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$Details{$cnt++} = $row;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$sth->finish();</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">return %Details;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">#——————————————————————–</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># Subroutine which updates the Student Table in DB</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">#——————————————————————–</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">sub update_Student_Info   {</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">my $SerialNo = shift;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">my $Name = shift;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">my $Marks = shift;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">my ($sql, $sth,$row);</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># DSN with the name "mydsn"  points to the Db</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$DB = "mydsn";</span>


<p style="padding-left:30px;">
  <span style="color:#993300;"># User name and password if any need to be specified. Currently no user name and pwd set.</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$DB_USER = "";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$DB_PASS= "";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$dbh = DBI->connect("dbi:ODBC:$DB", $DB_USER, $DB_PASS);</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$sql  = "Update Student set Name = '$Name',Marks = $Marks where Sl_No = $SerialNo ";</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$sth = $dbh->prepare($sql);</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$sth->execute;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">$sth->finish();</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">return $sql;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">============================================================</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">student.js</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">============================================================</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">/*</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">* Toggles the rows from EDIT mode to VIEW mode.</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">* Invoked on clicking the 'SAVE' button in last column.</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">*/</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">function makeRowViewable(rowNumber,id) {</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">var table = document.all ? document.all[id]  : document.getElementById ? document.getElementById(id) : null;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">var editableRowNumber = rowNumber + 1 ;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">var nonEditableRowNumber = editableRowNumber -1 ;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">table.rows[editableRowNumber].style.display = "none" ;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">table.rows[nonEditableRowNumber].style.display = "block" ;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">/*</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">* Toggles the rows from view mode to edit mode.</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">* Invoked on clicking the 'EDIT' button in last column.</span>


<p style="padding-left:30px;">
  <span style="color:#993300;">*/</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">function makeRowEditable(rowNumber,id) {</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">var table = document.all ? document.all[id]  : document.getElementById ? document.getElementById(id) : null;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">var editableRowNumber = rowNumber + 1 ;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">var nonEditableRowNumber = editableRowNumber -1 ;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">table.rows[editableRowNumber].style.display = "block" ;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">table.rows[nonEditableRowNumber].style.display = "none" ;</span>


<p style="padding-left:30px;">
  <span style="color:#008000;">}</span>


<p style="padding-left:30px;">
  <span style="color:#008000;"><br /> </span>


<p style="padding-left:30px;">
  As we know, the term <a href="http://en.wikipedia.org/wiki/Ajax_(programming)">Ajax</a> stands for ‘Asynchronous JavaScript And XML’. It is not a technology but a set of technologies being used together in a particular way. With effective use of existing technologies like HTML, DHTML, DOM, CSS, JavaScript one can make web pages more dynamic and interactive.


<p style="padding-left:30px;">
  Using JavaScript, Ajax makes an asynchronous call to the server and fetches an XML document from a server-side component. Upon completion of the request, JavaScript may be used to update or modify the Document Object Model (DOM) of the HTML page. Only the necessary portions of the HTML DOM are re-rendered in the HTML page. In short Ajax techniques let you update parts of your web page without reloading the whole page.


<p style="padding-left:30px;">
  The general benefit here is that an asynchronous operation executes in a separate thread. So when an operation is triggered asynchronously by the application, it can continue executing while the asynchronous method performs its task. Moreover only the data that needs to be updated or inserted can be sent instead of sending the entire form data. <a href="http://ajaxpatterns.org/Perl_Ajax_Frameworks">Perl Ajax framework</a> are also available for faster development and test.


<p style="padding-left:30px;">
  Popular web applications like  Gmail, Amazon, Orkut etc are using Ajax.


<p style="padding-left:30px;">
  <p style="padding-left:30px;">
    <span style="color:#993300;"><strong>References and more links:</strong></span>
  
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;"><a href="http://code.activestate.com/recipes/502299-simple-example-demonstrating-ajax-implementation-u/">Simple Example demonstrating Ajax Implementation using Perl « Perl recipes « ActiveState Code</a>.</span>
  
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;"><a href="http://www.perl.com/pub/2006/03/02/ajax_and_perl.html">http://www.perl.com/pub/2006/03/02/ajax_and_perl.html</a></span>
  
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;"><a href="http://perl.about.com/b/2006/03/17/using-ajax-from-perl.htm">http://perl.about.com/b/2006/03/17/using-ajax-from-perl.htm</a></span>
  
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;"><a href="http://ajaxpatterns.org/Perl_Ajax_Frameworks">http://ajaxpatterns.org/Perl_Ajax_Frameworks</a></span>
  
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;"><a href="http://search.cpan.org/~bpederse/CGI-Ajax-0.707/">http://search.cpan.org/~bpederse/CGI-Ajax-0.707/</a></span>
  
  
  <p style="padding-left:30px;">
    <span style="color:#0000ff;"><br /> </span>
  
  
  <p style="padding-left:30px;">
    Enjoy using Ajax from Perl.
  
  
  <p style="padding-left:60px;">
    <span style="color:#993300;"><br /> </span>
  