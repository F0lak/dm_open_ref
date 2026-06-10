
## pointer (info)

**Format:**
+   &A

**Returns:**
+   A pointer to the var or list item A.
***

> [!TIP]
> This operator is also called the reference operator, since it creates a reference to a var that you can use elsewhere.)

Sometimes it is desirable to have easy access to a var without knowing its name, or send multiple items back from a proc. To do this, you can create a pointer to that var. A pointer is basically a way to look up and access a var without needing to know anything else about it, like its name or which object it might belong to. You can pass the pointer like any other piece of data, and use the <a href="#/operator/*/pointer">`*` operator</a> to read or write the var's value.


```dm

var/a=3, b=4
var/p = &a
world << *p   // same as world << a
*p = 5    // same as a = 5

var/list/L = list(1, 2, 3)
var/list/pl = &L[2]
*pl *= 10 // same as L[2] *= 10

```


If you want the compiler to recognize that the item in your pointer var should be a certain type, you can give the pointer var that same type. Hence in the example above, `pl` is defined as a `/list`.

Unlike in some languages, pointers in DM are *not* literal memory addresses. Instead, a pointer is a shortcut indicating the type of var (e.g., global, object var, list index), and information needed to look it up. A pointer is an object, which is reference counted. It also holds references to the objects it needs, so for instance `&amp;thing.name` has a reference to `thing`, or `&amp;mylist[quest]` has references to `mylist` and `quest`.

You can also call procs this way. You can either wrap the pointer and the `*` operator in paretheses, like `(*p).MyProc()`, or you can skip the operator and just call `p.MyProc()` directly.

The same also applies to the list index operator `[]`. If `p = &amp;list` then you can use `(*p)[index]` or `p[index]` interchangeably.

Pointers can be made for any of these kinds of vars:

One advantage of pointers is that you can use them to alter a value in a suspended (sleeping) proc.

Note: When <a class="code" href="#/proc/spawn">spawn()</a> is used, the current proc is forked, where one keeps running and a copy is scheduled to run later. If any pointers to proc vars were created, they belong to the original proc (the one that keeps running), not to the fork.
***
**Related Pages:**
+    [* operator (pointers)](/ref/operator/*/pointer)
+    [operators](/ref/operator)
+    [ispointer proc](/ref/proc/ispointer)
