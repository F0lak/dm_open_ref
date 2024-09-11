## pick proc
**See also:**
*   [prob proc](/ref/proc/prob.md) -m<!-- -->
**Format:**
*   pick(Val1,Val2,\...)
*   pick(List)
<!-- -->
**Returns:**
*   One of the given values randomly chosen.


Randomly chooses an item from a list or from the arguments
provided. If only one argument is included and it is a list, then the
item is chosen from that list. 

When not using the list form,
you can make a particular value more or less likely to be chosen by
providing a relative probability like this* 
```
 prob(P); Val Or
P; Val 
```
 

A value for P of 200 makes it twice as likely
as the norm, 50 half as likely, and so on.
### Example:

```
 obj/food verb/eat() usr \<\< pick ( \"\[usr\] eats \\a
\[src\].\", prob(50) \"\[usr\] devours \\a \[src\].\", prob(25)
\"\[usr\] wolfs down \\a \[src\].\" ) del(src) 
```
 

There
is no analogous weighted format for the list version of this proc.