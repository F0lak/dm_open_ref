
## newlist (proc)

**Format:**
+   newlist(A,B,C,...)

**Arguments:**
+   Arbitrary number of types to be created in the list.

**Returns:**
+   A list of new objects, just as though you had done .
***

```dm

mob/contents = newlist(/obj/scroll/readme)

```


This causes new mobs to be created with a readme scroll in their inventory.

It is possible to make simple initializations when you want variables to have values other than the default for the particular type you are creating.


```dm

mob/contents = newlist(
   /obj/scroll/readme {
      name = "Introduction"
      desc = "The fate of Bracolia depends on you ..."
   }
)

```


This is the most common use of "modified types", but it is not specific to the newlist instruction. Anywhere a type value may be used in DM, it may be followed by a list of initializations. The general syntax for a modified types is:

<em>path</em> {<em>var1</em> = <em>val1</em>; <em>var2</em> = <em>val2</em>}

The semicolon is necessary if you put several variable assignments on the same line. The braces are necessary, even though they are generally optional in DM (since the compiler looks at your indentation). The reason is that the path + initializations must be parsed as a single expression, which is a different context from the usual use of braces in DM when you are defining a true type. Also, indentation inside of an argument list is always ignored anyway.
***
**Related Pages:**
+    [list proc](/ref/proc/list)
+    [new proc](/ref/proc/new)
