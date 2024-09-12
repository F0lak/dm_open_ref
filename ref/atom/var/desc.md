# desc var (atom)
**Default value:**
+   null


This is the description of the object.
### Example:

```
 mob/verb/look(atom/O in view()) if(O.desc) usr \<\< O.desc
else usr \<\< \"It\'s just \\an \[O\].\" 
```
