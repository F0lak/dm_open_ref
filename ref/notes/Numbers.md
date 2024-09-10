[]{#/Numbers.md}/numbers}    
## Numbers    
In DM, all numbers are stored in floating point format. Specifically,    
single-precision (32-bit) floating point. This is important to know if    
you think you will be working with large numbers or decimal values a    
lot, because the accuracy of the numbers is limited.    
32-bit floating point numbers can represent integers from -16777216 to    
16777216 (2^24^). Non-integer values can get about as small as 2^-126^    
and as large as 2^127^.    
Floating point numbers do not handle most decimal values precisely. For    
instance, 0.1 is not exactly 0.1, because floating point numbers are    
stored in a binary format and in binary, 1/10 is a fraction that repeats    
forever---the same way 1/3 repeats as 0.33333\... in decimal numbers. It    
ends up being rounded off, either a little higher or a littler lower    
than its true value. This means that the following loop won\'t work like    
you might expect:    
### Example:    
for(i = 0, i \< 100, i += 0.1) world \<\< i    
You might expect that code to loop exactly 1000 times, with `i` going    
from 0 up to 99.9 before stopping. The truth is more complicated,    
because 0.1 stored in floating point is actually greater than the exact    
value of 0.1. Other values might be more or less than their exact    
numbers, and as you add these numbers together repeatedly you\'ll    
introduce more and more rounding error.    
Even more insidious, if you add 0.1 a bunch of times starting from 0,    
and then subtract it out again the same number of times, the result you    
get may not be 0. This is counterintuitive, because you might expect    
rounding errors to reverse themselves in the same order they crept in.    
Unfortunately it doesn\'t work that way.    
You can correct for rounding error somewhat by using the [`round`    
proc](/proc/round) to adjust the loop var each time, although for    
performance reasons it might be preferable to find another alternative.    
for(i = 0, i \< 100, i = round(i + 0.1, 0.1)) world \<\< i    
Only fractions whose denominators are powers of 2 are immune to this    
rounding error, so 0.5 is in fact stored as an exact value.    
Another place floating point may lose accuracy is when you try to add    
numbers of very different sizes. For instance as stated above, the upper    
limit for accurate integers is 16777216. If you try to use a number such    
as 100 million it will only be approximate, so adding 1 to that number    
won\'t actually change it because the 1 is so much smaller, it will be    
gobbled up by rounding error.    
Also for the same reasons stated above, division will cost you accuracy.    
Again you can divide by powers of 2 easily enough, and you can divide an    
integer by any of its factors (like dividing 9 by 3) without a problem,    
but a fraction like 1/3 will repeat forever so it gets rounded to as    
much precision as floating point can manage.    
In decimal, floating point numbers have at least six decimal digits of    
precision. Since they\'re actually stored in binary, their true    
precision is exactly 24 bits.  