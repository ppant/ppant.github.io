---
id: 1477
title: apache lucy search examples
date: 2015-10-13T20:46:38+05:30
author: Pradeep Pant
layout: post
guid: /?p=1477
permalink: /2015/10/13/apache-lucy-search-test/
dsq_thread_id:
  - "4221391787"
---
Investigating search engines and this time [apache Lucy](/2011/10/apache-lucy-search-engine/) 0.4.2. I am showing a basic indexer and a small search application. See below code for indexer (This will take documents one by one and then index them). Search module will take arugument as STDIN and then will show the search result.

This is pure command line utility just to show how basic indexing and searching works using apache lucy.

**indexer.pl**  
`<br />
<!--?prettify linenums=true?--></p>
<pre class="prettyprint">#!/usr/local/bin/perl

use strict;
use warnings;
use Lucy::Simple;

#
# Ensure the index directory is both available and empty.
#
my $index = "/ppant/LucyTest/index";
system( "rm", "-rf", $index );
system( "mkdir", "-p", $index );
# Create the helper...a new Lucy::Simple object
my $lucy = Lucy::Simple new( path = $index, language = 'en', );

# Add the first "document". (We are mainly adding meta data of the document)
my %one = ( title ="This is a title of first article" , body ="some text inside the body we need to test the implementaion of lucy", id =1 );
$lucy-add_doc( \%one );

# Add the second "document".
my %two = ( title ="This is another article" , body ="I am putting some basic content, using some words which are also in first document like implementation", id =2 );
$lucy add_doc( \%two );
</pre>
<p># Both the documents are now indexed in path</p>
<p>One indexing of the documents is done we'll make a small search script.</p>
<p><strong>search.cgi</strong></p>
<p>

<!--?prettify linenums=true?--></p>
<pre class="prettyprint">#!/usr/local/bin/perl

use strict;
use warnings;

use Lucy::Search::IndexSearcher;

my $term = shift || die "Usage: $0 search-term";

my $searcher = Lucy::Search::IndexSearcher new( index ='/ppant/LucyTest/index');
# A basic search command line which will look for indexed items based on STDIN and will show that in which document query string is found and no of hits
my $hits = $searcher hits( query =$term );
while ( my $hit = $hits next ) {
print "Title: $hit {title} - ID: $hit {id}\n";
}
# End of search.cgi
</pre>
<p>`

  
\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\***\*****

If you want to explore more check Full Code on [GitHub](https://github.com/ppant/apache-lucy-search-examples)