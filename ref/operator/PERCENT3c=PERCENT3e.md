## \<=\> operator 
###### BYOND Version 516
**See also:**
*   [\< operator](/operator/%3c)
*   [\> operator](/operator/%3e)
*   [\<= operator](/operator/%3c=)
*   [\>= operator](/operator/%3e=)
*   [== operator](/operator/==)
*   [operators](/operator)
*   [sorttextEx proc](/proc/sorttextEx)
<!-- -->
**Format:**
*   A \<=\> B
<!-- -->
**Returns:**
*   -1 if A is less B; 1 if A is greater than B; 0 otherwise.


If A and B are text strings, a case sensitive comparison is
performed (like sorttextEx()). 

If either value is the special
number NaN (not a number), the result is currently 0 but should be
considered ambiguous.