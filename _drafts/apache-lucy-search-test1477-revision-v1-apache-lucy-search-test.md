---
id: 1484
title: apache lucy search test
date: 2015-10-13T20:46:38+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2015/10/1477-revision-v1/
permalink: /2015/10/13/1477-revision-v1/
---
Investigating search engines and this time [apache Lucy](http://pradeeppant.com/2011/10/apache-lucy-search-engine/) 0.4.2. I am showing a basic indexer and a small search application. See below code for indexer (This will take documents one by one and then index them). Search module will take arugument as STDIN and then will show the search result.

This is pure command line utility just to show how basic indexing and searching works using apache lucy.

**indexer.pl**  
`<br />
#!/usr/local/bin/perl`

use strict;  
use warnings;  
use Lucy::Simple;

#  
\# Ensure the index directory is both available and empty.  
#  
my $index = &#8220;/ppant/LucyTest/index&#8221;;  
system( &#8220;rm&#8221;, &#8220;-rf&#8221;, $index );  
system( &#8220;mkdir&#8221;, &#8220;-p&#8221;, $index );  
\# Create the helper&#8230;a new Lucy::Simple object  
my $lucy = Lucy::Simple->new( path => $index, language => &#8216;en&#8217;, );

\# Add the first &#8220;document&#8221;. (We are mainly adding meta data of the document)  
my %one = ( title => &#8220;This is a title of first article&#8221; , body => &#8220;some text inside the body we need to test the implementaion of lucy&#8221;, id => 1 );  
$lucy->add_doc( \%one );

\# Add the second &#8220;document&#8221;.  
my %two = ( title => &#8220;This is another article&#8221; , body => &#8220;I am putting some basic content, using some words which are also in first document like implementation&#8221;, id => 2 );  
$lucy->add_doc( \%two );  
</code>  
\# Both the documents are now indexed in path

One indexing of the documents is done we&#8217;ll make a small search script.

**search.cgi**  
`<br />
#!/usr/local/bin/perl</p>
<p>use strict;<br />
use warnings;</p>
<p>use Lucy::Search::IndexSearcher;</p>
<p>my $term = shift || die "Usage: $0 search-term";</p>
<p>my $searcher = Lucy::Search::IndexSearcher->new( index => '/ppant/LucyTest/index');<br />
# A basic search command line which will look for indexed items based on STDIN and will show that in which document query string is found and no of hits<br />
my $hits = $searcher->hits( query => $term );<br />
while ( my $hit = $hits->next ) {<br />
print "Title: $hit->{title} - ID: $hit->{id}\n";<br />
}<br />
# End of search.cgi<br />
` 

\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\*****

If you want to explore more check Full Code on [GitHub](https://github.com/ppant/apache-lucy-search-examples)