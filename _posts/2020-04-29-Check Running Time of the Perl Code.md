---
title: 'Check Running Time of the Perl Code'
date: 2020-04-29
author: Pradeep Pant
layout: post
---

Timing functions during a program run is really helpful and crucial in debugging. Below is the quick intro on ````timediff()```` using Perl's Benchmark module. 

````perl
use Benchmark;
$t0 = Benchmark->new;
# ... your code here ...
$t1 = Benchmark->new;
$td = timediff($t1, $t0);
print "the code took:",timestr($td),"\n";
````

For more functions, you can use excellent module [Benchmark on CPAN](https://metacpan.org/pod/Benchmark)


If somehow you don't have access to [CPAN](https://www.cpan.org/) then you can just use basic 
```` time() ```` 
function

Example:

````perl
sub time_taken {
     my $start_time = time();
     print "Start time\n";
     print $start_time;
     print "\n";

## Code goes here ######

     my $end_time = time();
     print "End time\n";
     print $end_time;
     print "\n";
     my $diff_time = $end_time - $start_time;
     print "Total time taken\n";
     print $diff_time;
     print "\n";
     } # end of time_taken
	 
````

Happy debugging!