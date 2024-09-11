## \<\< shift operator
**See also:**
*   [\>\> operator](/ref/operator/%3e%3e.md) -m
*   [\<\<= operator](/ref/operator/%3c%3c=.md) -m
*   [operators](/ref/operator.md) -m<!-- -->
**Format:**
*   A \<\< B
<!-- -->
**Returns:**
*   The bits of A shifted left B times.


A and B must be between 0 and 2\*\*24 - 1, giving an effective
width of 24 bits. 

Bits shifted beyond the 24 low bits are lost.