## \|\| operator

**Format:**
+   A \|\| B
<!-- -->
**Returns:**
+   First true value of either A or B; last false value otherwise
The only false values in DM are the number 0, an empty text string, or
null. All other values are considered true. 

The first true
value from left to right completes the evaluation (a practice known as
short-circuiting)), meaning that any expressions after the first true
value are skipped. The return value is equal to the last operand to be
evaluated.
### Example:

``` dm
mob/verb/Fly() if(swimming \|\| IsStuck()) src << "You
can\'t fly right now!" return 
```
 

In this example, the
`IsStuck()` call is not performed if `swimming` is true.


Although logical short-circuit operators are used most often in
blocks such as `if` or `while`, they can be used elsewhere.
### Example:

``` dm
 // if current_target is null, pick a new one var/target =
current_target \|\| PickTarget() 
```


> [!TIP] 
> **See also:**
> +   [! operator](/ref/operator/!.md) 
> +   [&& operator](/ref/operator/&&.md) 
> +   [\|\|= operator](/ref/operator/%7C%7C=.md) 
> +   [operators](/ref/operator.md) <!-- -->