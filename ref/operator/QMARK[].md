## ?\[\] operator 
###### BYOND Version 514


This is the null-conditional list index operator. It is used to
access an element of a list, IF that list is not null. If the list is
null, then the access will not happen and the index expression inside
the brackets won\'t be evaluated. If this is the left-hand side of an
assignment operator, such as `list?[index] = rhs`, then `rhs` is also
not evaluated when the list is null.
### Example:

```
 var/list/good = list(5,6,7) var/list/bad var/idx = 1 //
prints null because bad is null; idx is not changed world \<\<
json_encode(bad?\[idx++\]) // prints 5 because good is not null, and
good\[1\] is 5; idx changes to 2 world \<\< json_encode(good?\[1\]) idx
= 1 // reset idx // bad is null, so idx does not advance and myproc() is
not called bad?\[idx++\] = myproc() // good is not null, so idx advances
after read, and myproc() is called good?\[idx++\] = myproc() 
```



This operator cannot be overloaded, but overloads to the `[]`
operator will apply to this operator as well. 



**See also:**
+   [list](/ref/list.md) 
+   [operators](/ref/operator.md) 
+   [\[\] operator](/ref/operator/%5B%5D.md) 
+   [?. operator](/ref/operator/%3f%2e.md) 
+   [?: operator](/ref/operator/%3f:.md) 