---
id: 2271
title: adding custom properties in doc and xls files using Apache POI through Perl wrapper example
date: 2019-12-31T13:48:07+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2019/12/31/2264-revision-v1/
permalink: /2019/12/31/2264-revision-v1/
---
Apache POI are the set of Java API&#8217;s to manipulate MS Office documents. You can read more about Apache POI [here](https://poi.apache.org/).

In this post, I am showing a fully working example to push core and custom properties in Microsoft Word (.doc) file.

<p style="color:#0477a8" class="has-text-color">
  <strong>Env:</strong>
</p>

  * CentOS 6x
  * Java 1.8
  * POI 3.17
  * Perl Inline module
  * Perl Inline::Java module
  * Perl 5.12

<p style="color:#0375a6" class="has-text-color">
  <strong>Perl script:</strong>
</p>

<pre class="wp-block-code"><code>#!/usr/local/bin/perl    
	use POI;
	# Call to push custom info in word documents	
	# Handle DOC, XLS  and PPT extension 
	# Todo
	#my $content_type;
    #if (defined($content_type) && ($content_type eq "application/x-msword" || $content_type eq "application/vnd.ms-excel" || $content_type eq "application/vnd.ms-powerpoint") ) {
	# Make sure to give full path of the doc file
	my $path = "doc_test_file.doc";
	# Make a POI object
	my $alu = POI->new();
	# Time to call push properties routine which is inside POI.pm and written in Java
	my $docname = $alu->PushProperties($path,"Test_doc_file","Test file doc type extension","2.0","ppant");	
	
	
	
	
	
	
</code></pre>

<p style="color:#0373a3" class="has-text-color">
  <strong>Perl module with Java code:</strong>
</p>

<pre class="wp-block-code"><code>package POI;
use strict; 
use warnings;
use Inline Java => "DATA", SHARED_JVM => 1;

### CONSTRUCTOR
###############################################################
# new()
###############################################################     
sub new {
        my $class    = shift;
        my $proto = shift;        
        return POI::POI->new();
    }
 1;
    __DATA__
    __Java__

//Import POI classes
import org.apache.poi.hpsf.CustomProperties;
import org.apache.poi.hpsf.DocumentSummaryInformation;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Date;
import org.apache.poi.hpsf.PropertySet;
import org.apache.poi.hpsf.PropertySetFactory;
import org.apache.poi.hpsf.SummaryInformation;
import org.apache.poi.poifs.filesystem.DirectoryEntry;
import org.apache.poi.poifs.filesystem.DocumentEntry;
import org.apache.poi.poifs.filesystem.DocumentInputStream;
import org.apache.poi.poifs.filesystem.POIFSFileSystem; 


class POI {
    public POI(){
}
/* function for pushing custom variables */

public String PushProperties(String filename, String docname, String doctitle, String revision, String author) {
	  try {
		File poiFilesystem = new File(filename);
     /* Open the POI filesystem. */
        InputStream is = new FileInputStream(poiFilesystem);
        POIFSFileSystem poifs = new POIFSFileSystem(is);
        is.close();

     /* Read the summary information. */
        DirectoryEntry dir = poifs.getRoot();
		SummaryInformation si;
            
        try {
            DocumentEntry siEntry = (DocumentEntry)
                dir.getEntry(SummaryInformation.DEFAULT_STREAM_NAME);
            DocumentInputStream dis = new DocumentInputStream(siEntry);
            PropertySet ps = new PropertySet(dis);
            dis.close();
            si = new SummaryInformation(ps);
        }
        catch (FileNotFoundException ex) {
            /* There is no summary information yet. We have to create a new
             * one. */
            si = PropertySetFactory.newSummaryInformation();
        }

        /* Change the author to "Pradeep Pant". Any former author value will
         * be lost. If there has been no author yet, it will be created. */
        si.setAuthor("Pradeep Pant");
		si.setTitle(doctitle);
		si.setSubject("Car parts manual");
		si.setComments("Testing manual for making car parts");
		si.setKeywords("automobiles");
		si.setRevNumber("2.0");
		System.out.println("Author changed to " + si.getAuthor() + ".");
		
        /* Read the document summary information. */
        DocumentSummaryInformation dsi;
        try {
            DocumentEntry dsiEntry = (DocumentEntry)
			dir.getEntry(DocumentSummaryInformation.DEFAULT_STREAM_NAME);
            DocumentInputStream dis = new DocumentInputStream(dsiEntry);
            PropertySet ps = new PropertySet(dis);
            dis.close();
            dsi = new DocumentSummaryInformation(ps);
        }
        catch (FileNotFoundException ex) {
            /* There is no document summary information yet. We have to create a
             * new one. */
            dsi = PropertySetFactory.newDocumentSummaryInformation();
        }
        dsi.setCategory("Quality Manual");  
		dsi.setCompany("PRADEEPPANT.COM");
		dsi.setManager("PK PANT");
		//Pushing Custom properties
        CustomProperties cp = dsi.getCustomProperties();
	if (cp == null)        
		cp = new CustomProperties();
		cp.put("Document Name",docname);
		cp.put ("Document Title",doctitle);
		cp.put("Revision number",revision);
		cp.put("Author",author);
		cp.put("Date", new Date());
    
     /* Write the custom properties back to the document summary information. */
		dsi.setCustomProperties(cp);
		si.write(dir, SummaryInformation.DEFAULT_STREAM_NAME);
		dsi.write(dir, DocumentSummaryInformation.DEFAULT_STREAM_NAME);
	/* Write the POI filesystem back to the original file. Please note that
         * in production code you should never write directly to the origin
         * file! In case of a writing error everything would be lost. */
        OutputStream out = new FileOutputStream(poiFilesystem);
        poifs.writeFilesystem(out);
        out.close();
    
   } // end of try
   catch( Exception e ) {
     e.printStackTrace();
   }   
   return docname;
  } // end of PushProperties
} //end of public POI</code></pre>

<p style="color:#0373a3" class="has-text-color">
  <strong>Command to run/stop/restart JVM</strong>
</p><figure class="wp-block-pullquote">

> % perl -MInline::Java::Server=start&nbsp; &nbsp;
> 
> % perl -MInline::Java::Server=stop&nbsp; &nbsp;
> 
> % perl -MInline::Java::Server=restart
> 
> <cite>Command to start and stop jvm</cite></figure> 

Full code and sample files: <https://github.com/ppant/apache-poi-examples-in-perl>  


<div class="wp-block-group">
  <div class="wp-block-group__inner-container">
    <div class="wp-block-group">
      <div class="wp-block-group__inner-container">
        <p style="color:#03868f" class="has-text-color">
          <strong>References:</strong>
        </p>
      </div>
    </div>
  </div>
</div>

<div class="wp-block-group">
  <div class="wp-block-group__inner-container">
    <p>
      Apache POI <a href="https://poi.apache.org/">https://poi.apache.org/</a>
    </p>
    
    <p>
      Perl Inline module: <a href="https://metacpan.org/pod/Inline">https://metacpan.org/pod/Inline</a>
    </p>
    
    <p>
      Perl Inline::Java module: <a href="https://metacpan.org/pod/Inline::Java">https://metacpan.org/pod/Inline::Java</a>
    </p>
  </div>
</div>