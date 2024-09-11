## \|= operator
**See also:**
*   [&= operator](/ref/operator/&=.md) -m
*   [operators](/ref/operator.md) -m
*   [\| operator](/ref/operator/%7C.md) -m<!-- -->
**Format:**
*   A \|= B


Set A equal to A \| B. It is shorthand for A = A \| B.


This is commonly used to turn on certain bitfields in a word.
### Example:

```
 usr.sight \|= BLIND // turn on the blind bit 
```



If A and B are lists, any items in B that are not already in A
are added to A. 

If A is an /icon or /matrix datum, the datum
will be changed rather than creating a new one and re-assigning it to A.