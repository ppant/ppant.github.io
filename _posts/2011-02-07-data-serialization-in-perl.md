---
id: 297
title: Data Serialization in Perl
date: 2011-02-07T13:34:42+05:30
author: Pradeep Pant
layout: post
guid: /?p=297
permalink: /2011/02/07/data-serialization-in-perl/
jabber_published:
  - "1297066413"
dsq_thread_id:
  - "781201471"
---
<span style="color:#008080;">Before I dig more into details let&#8217;s try to understand some basic facts about Serialization :</span>

 <span style="color:#008080;"></span><span style="color:#008080;"><strong>What exactly Serialization is?</strong></span>

<span style="color:#008080;">Serialization is the process of converting a data structure or object into a format that can be stored (for example, in a file or memory buffer, or transmitted across a network connection link) and &#8220;resurrected&#8221; later in the same or another computer environment. When the resulting series of bits is reread according to the serialization format, it can be used to create a semantically identical clone of the original object.</span>

<span style="color:#008080;"><strong>Serialization in Perl:</strong></span>

<span style="color:#008080;">In Perl, the data which is represented as key-value pairs can be stored in a file. This gives persistence to such data so that the data can be retrieved and manipulated by many independent, but possibly related, programs. However, if the structure of the data is more complex,  associative arrays or hashes do not provide adequate representation. For example, if the data item is an anonymous array of arrays, or a hash of hashes, or an object belonging to a certain class, it is not enough to be able to tie a file to a hash in order to be able to save the data to a file. So, we need to perform serialization in such cases which involves converting the contents of any complex data structure into a string following a certain well-designed algorithm.</span>

<span style="color:#008080;">The string produced by the serialization algorithm can then be deserialized later in the program when and if necessary. The serialized data structure can be sent over socket connections or used in remote procedure calls as long as the receiving end deserializes it using an appropriate algorithm. The serialized string can be stored to a text file, or a DBM file if it can be somehow associated with a key, or can be stored in a database. The only requirement that before using again, the string should be deserialized. There are several Perl modules that provide for serialization and de-serialization facilities. These include </span><a href="http://search.cpan.org/dist/FreezeThaw/" target="_blank"><span style="color:#008080;">FreezeThaw.pm</span></a><span style="color:#008080;">, </span><a href="http://search.cpan.org/~ams/Storable-2.25/Storable.pm" target="_blank"><span style="color:#008080;">Storable.pm</span></a><span style="color:#008080;">, </span><a href="http://search.cpan.org/~smueller/Data-Dumper-2.128/Dumper.pm" target="_blank"><span style="color:#008080;">Data::Dumper.pm</span></a><span style="color:#008080;">, </span><a href="http://search.cpan.org/~ingy/Data-Denter-0.15/" target="_blank"><span style="color:#008080;">Data::Denter.pm</span></a> <a href="http://search.cpan.org/~mikewong/XML-Dumper-0.81/" target="_blank"><span style="color:#008080;">XML::Dumper</span></a><span style="color:#008080;">, <a href="http://search.cpan.org/~mlehmann/JSON-XS-2.3/XS.pm">JSON::XS</a></span>  
 <span style="color:#008080;">etc. A module called </span>[<span style="color:#008080;">Data::Serializer.pm</span>](http://search.cpan.org/~neely/Data-Serializer-0.57/) <span style="color:#008080;">provides a common interface to some of the serialization modules. The default module used by </span><a href="http://search.cpan.org/~neely/Data-Serializer-0.57/" target="_blank"><span style="color:#008080;">Data::Serializer.pm</span></a> <span style="color:#008080;">is </span>[<span style="color:#008080;">Data::Dumper.pm</span>](http://search.cpan.org/~smueller/Data-Dumper-2.128/Dumper.pm)<span style="color:#008080;">.</span>

<span style="color:#993300;">In my next post I will try to show some examples.</span>