---
id: 1469
title: implementing mapper attachment in elasticsearch
date: 2015-09-16T17:03:21+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2015/09/1468-revision-v1/
permalink: /2015/09/16/1468-revision-v1/
---
<table class="highlight tab-size js-file-line-container" data-tab-size="8">
  <tr>
    <td id="LC1" class="blob-code blob-code-inner js-file-line">
      //Mapping
    </td>
  </tr>
  
  <tr>
    <td id="L2" class="blob-num js-line-number" data-line-number="2">
    </td>
    
    <td id="LC2" class="blob-code blob-code-inner js-file-line">
      curl -X DELETE &#8220;192.168.0.37:9200/test&#8221;
    </td>
  </tr>
  
  <tr>
    <td id="L3" class="blob-num js-line-number" data-line-number="3">
    </td>
    
    <td id="LC3" class="blob-code blob-code-inner js-file-line">
      curl -X PUT &#8220;192.168.0.37:9200/test&#8221; -d &#8216;{
    </td>
  </tr>
  
  <tr>
    <td id="L4" class="blob-num js-line-number" data-line-number="4">
    </td>
    
    <td id="LC4" class="blob-code blob-code-inner js-file-line">
      &#8220;settings&#8221; : { &#8220;index&#8221; : { &#8220;number_of_shards&#8221; : 1, &#8220;number_of_replicas&#8221; : 0 }}
    </td>
  </tr>
  
  <tr>
    <td id="L5" class="blob-num js-line-number" data-line-number="5">
    </td>
    
    <td id="LC5" class="blob-code blob-code-inner js-file-line">
      }&#8217;
    </td>
  </tr>
  
  <tr>
    <td id="L6" class="blob-num js-line-number" data-line-number="6">
    </td>
    
    <td id="LC6" class="blob-code blob-code-inner js-file-line">
    </td>
  </tr>
  
  <tr>
    <td id="L7" class="blob-num js-line-number" data-line-number="7">
    </td>
    
    <td id="LC7" class="blob-code blob-code-inner js-file-line">
      //Mapping attachement type
    </td>
  </tr>
  
  <tr>
    <td id="L8" class="blob-num js-line-number" data-line-number="8">
    </td>
    
    <td id="LC8" class="blob-code blob-code-inner js-file-line">
      curl -X PUT &#8220;192.168.0.37:9200/test/attachment/_mapping&#8221; -d &#8216;{
    </td>
  </tr>
  
  <tr>
    <td id="L9" class="blob-num js-line-number" data-line-number="9">
    </td>
    
    <td id="LC9" class="blob-code blob-code-inner js-file-line">
      &#8220;attachment&#8221; : {
    </td>
  </tr>
  
  <tr>
    <td id="L10" class="blob-num js-line-number" data-line-number="10">
    </td>
    
    <td id="LC10" class="blob-code blob-code-inner js-file-line">
      &#8220;properties&#8221; : {
    </td>
  </tr>
  
  <tr>
    <td id="L11" class="blob-num js-line-number" data-line-number="11">
    </td>
    
    <td id="LC11" class="blob-code blob-code-inner js-file-line">
      &#8220;file&#8221; : {
    </td>
  </tr>
  
  <tr>
    <td id="L12" class="blob-num js-line-number" data-line-number="12">
    </td>
    
    <td id="LC12" class="blob-code blob-code-inner js-file-line">
      &#8220;type&#8221; : &#8220;attachment&#8221;,
    </td>
  </tr>
  
  <tr>
    <td id="L13" class="blob-num js-line-number" data-line-number="13">
    </td>
    
    <td id="LC13" class="blob-code blob-code-inner js-file-line">
      &#8220;fields&#8221; : {
    </td>
  </tr>
  
  <tr>
    <td id="L14" class="blob-num js-line-number" data-line-number="14">
    </td>
    
    <td id="LC14" class="blob-code blob-code-inner js-file-line">
      &#8220;title&#8221; : { &#8220;store&#8221; : &#8220;yes&#8221; },
    </td>
  </tr>
  
  <tr>
    <td id="L15" class="blob-num js-line-number" data-line-number="15">
    </td>
    
    <td id="LC15" class="blob-code blob-code-inner js-file-line">
      &#8220;file&#8221; : { &#8220;term_vector&#8221;:&#8221;with_positions_offsets&#8221;, &#8220;store&#8221;:&#8221;yes&#8221; }
    </td>
  </tr>
  
  <tr>
    <td id="L16" class="blob-num js-line-number" data-line-number="16">
    </td>
    
    <td id="LC16" class="blob-code blob-code-inner js-file-line">
      }
    </td>
  </tr>
  
  <tr>
    <td id="L17" class="blob-num js-line-number" data-line-number="17">
    </td>
    
    <td id="LC17" class="blob-code blob-code-inner js-file-line">
      }
    </td>
  </tr>
  
  <tr>
    <td id="L18" class="blob-num js-line-number" data-line-number="18">
    </td>
    
    <td id="LC18" class="blob-code blob-code-inner js-file-line">
      }
    </td>
  </tr>
  
  <tr>
    <td id="L19" class="blob-num js-line-number" data-line-number="19">
    </td>
    
    <td id="LC19" class="blob-code blob-code-inner js-file-line">
      }
    </td>
  </tr>
  
  <tr>
    <td id="L20" class="blob-num js-line-number" data-line-number="20">
    </td>
    
    <td id="LC20" class="blob-code blob-code-inner js-file-line">
      }&#8217;
    </td>
  </tr>
  
  <tr>
    <td id="L21" class="blob-num js-line-number" data-line-number="21">
    </td>
    
    <td id="LC21" class="blob-code blob-code-inner js-file-line">
    </td>
  </tr>
  
  <tr>
    <td id="L22" class="blob-num js-line-number" data-line-number="22">
    </td>
    
    <td id="LC22" class="blob-code blob-code-inner js-file-line">
      shell script to index data
    </td>
  </tr>
  
  <tr>
    <td id="L23" class="blob-num js-line-number" data-line-number="23">
    </td>
    
    <td id="LC23" class="blob-code blob-code-inner js-file-line">
      #!/bin/sh
    </td>
  </tr>
  
  <tr>
    <td id="L24" class="blob-num js-line-number" data-line-number="24">
    </td>
    
    <td id="LC24" class="blob-code blob-code-inner js-file-line">
    </td>
  </tr>
  
  <tr>
    <td id="L25" class="blob-num js-line-number" data-line-number="25">
    </td>
    
    <td id="LC25" class="blob-code blob-code-inner js-file-line">
      coded=`cat TestPDF.pdf | perl -MMIME::Base64 -ne &#8216;print encode_base64($_)&#8217;`
    </td>
  </tr>
  
  <tr>
    <td id="L26" class="blob-num js-line-number" data-line-number="26">
    </td>
    
    <td id="LC26" class="blob-code blob-code-inner js-file-line">
      json=&#8221;{\&#8221;file\&#8221;:\&#8221;${coded}\&#8221;}&#8221;
    </td>
  </tr>
  
  <tr>
    <td id="L27" class="blob-num js-line-number" data-line-number="27">
    </td>
    
    <td id="LC27" class="blob-code blob-code-inner js-file-line">
      echo &#8220;$json&#8221; > json.file
    </td>
  </tr>
  
  <tr>
    <td id="L28" class="blob-num js-line-number" data-line-number="28">
    </td>
    
    <td id="LC28" class="blob-code blob-code-inner js-file-line">
      curl -X POST &#8220;192.168.0.37:9200/test/attachment/&#8221; -d @json.file
    </td>
  </tr>
  
  <tr>
    <td id="L29" class="blob-num js-line-number" data-line-number="29">
    </td>
    
    <td id="LC29" class="blob-code blob-code-inner js-file-line">
    </td>
  </tr>
  
  <tr>
    <td id="L30" class="blob-num js-line-number" data-line-number="30">
    </td>
    
    <td id="LC30" class="blob-code blob-code-inner js-file-line">
      //Search for Highlighted results
    </td>
  </tr>
  
  <tr>
    <td id="L31" class="blob-num js-line-number" data-line-number="31">
    </td>
    
    <td id="LC31" class="blob-code blob-code-inner js-file-line">
      curl &#8220;192.168.0.37:9200/_search?pretty=true&#8221; -d &#8216;{
    </td>
  </tr>
  
  <tr>
    <td id="L32" class="blob-num js-line-number" data-line-number="32">
    </td>
    
    <td id="LC32" class="blob-code blob-code-inner js-file-line">
      &#8220;fields&#8221; : [&#8220;title&#8221;],
    </td>
  </tr>
  
  <tr>
    <td id="L33" class="blob-num js-line-number" data-line-number="33">
    </td>
    
    <td id="LC33" class="blob-code blob-code-inner js-file-line">
      &#8220;query&#8221; : {
    </td>
  </tr>
  
  <tr>
    <td id="L34" class="blob-num js-line-number" data-line-number="34">
    </td>
    
    <td id="LC34" class="blob-code blob-code-inner js-file-line">
      &#8220;query_string&#8221; : {
    </td>
  </tr>
  
  <tr>
    <td id="L35" class="blob-num js-line-number" data-line-number="35">
    </td>
    
    <td id="LC35" class="blob-code blob-code-inner js-file-line">
      &#8220;query&#8221; : &#8220;Cycling tips&#8221;
    </td>
  </tr>
  
  <tr>
    <td id="L36" class="blob-num js-line-number" data-line-number="36">
    </td>
    
    <td id="LC36" class="blob-code blob-code-inner js-file-line">
      }
    </td>
  </tr>
  
  <tr>
    <td id="L37" class="blob-num js-line-number" data-line-number="37">
    </td>
    
    <td id="LC37" class="blob-code blob-code-inner js-file-line">
      },
    </td>
  </tr>
  
  <tr>
    <td id="L38" class="blob-num js-line-number" data-line-number="38">
    </td>
    
    <td id="LC38" class="blob-code blob-code-inner js-file-line">
      &#8220;highlight&#8221; : {
    </td>
  </tr>
  
  <tr>
    <td id="L39" class="blob-num js-line-number" data-line-number="39">
    </td>
    
    <td id="LC39" class="blob-code blob-code-inner js-file-line">
      &#8220;fields&#8221; : {
    </td>
  </tr>
  
  <tr>
    <td id="L40" class="blob-num js-line-number" data-line-number="40">
    </td>
    
    <td id="LC40" class="blob-code blob-code-inner js-file-line">
      &#8220;file&#8221; : {}
    </td>
  </tr>
  
  <tr>
    <td id="L41" class="blob-num js-line-number" data-line-number="41">
    </td>
    
    <td id="LC41" class="blob-code blob-code-inner js-file-line">
      }
    </td>
  </tr>
  
  <tr>
    <td id="L42" class="blob-num js-line-number" data-line-number="42">
    </td>
    
    <td id="LC42" class="blob-code blob-code-inner js-file-line">
      }
    </td>
  </tr>
  
  <tr>
    <td id="L43" class="blob-num js-line-number" data-line-number="43">
    </td>
    
    <td id="LC43" class="blob-code blob-code-inner js-file-line">
      }&#8217;
    </td>
  </tr>
</table>