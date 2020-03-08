---
id: 2264
title: 'Adding core and custom properties in Microsoft Word (doc), XLS, PPT file using Apache POI through Perl wrapper: Example'
date: 2019-12-31T23:00:00+05:30
author: Pradeep Pant
layout: post
---
Apache POI is the set of Java APIs to manipulate MS Office documents. You can read more about Apache POI [here](https://poi.apache.org/).
In this post, I am showing a fully working example to push core and custom properties in Microsoft Word (.doc) file.

**Env:**
 *  *CentOS 6x*
 *  *Java 1.8*
 *  *POI 3.17*
 *  *[Inline](https://metacpan.org/pod/Inline) - Write Perl Subroutines in Other Programming Languages* 
 *  *[Inline::Java](https://metacpan.org/pod/Inline::Java) - Write Perl classes in Java.*
 *  *Perl 5.12*

**Perl script:**

````perl
#!/usr/local/bin/perl    
	use POI;	
	# Make sure to give full path of the doc file
	my $path = "doc_test_file.doc";
	# Make a POI object
	my $poi_obj = POI->new();
	# Call push properties routine which is inside POI.pm and written in Java
	my $docname = $poi_obj->PushProperties($path,"Test_doc_file","Test file doc type extension","2.0","ppant");	
````

**Perl module with Java code:**

````perl
package POI;
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
 ````
 ````java
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
} //end of public POI
````

**Command to run/stop/restart JVM**

JVM to be run the first time and each time you make changes to module file.

For more info on POI env setting please check my [previous post](/2019/12/07/apache-poi-env-setting-in-centos-6-and-perl/)

* % perl -MInline::Java::Server=start
 
* % perl -MInline::Java::Server=stop
 
* % perl -MInline::Java::Server=restart
 

**Full code and sample files on my Github:**


<https://github.com/ppant/apache-poi-examples-in-perl>  


In case of issues please mention in comments.

Happy coding!

**Note:** The same routine can be used to push variables in XLS and PPT type.  
In another post, I will share an example with the Microsoft Word DOCX file which also uses different sets of POI APIs. 
