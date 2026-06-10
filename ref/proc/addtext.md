
## addtext (proc)

**Format:**
+   addtext(Arg1,Arg2,...)

**Arguments:**
+   Any number of text strings.

**Returns:**
+   A text string with the arguments concatenated.
***
This instruction returns text containing the first argument followed by the second, followed by the third, etc. The arguments may be constants or variables containing text.


```dm

var/T
T = "1"
T = addtext(T,"*1 = ",T)  // T = "1*1 = 1"
world << "The answer is: [T]"

```


This instruction exists primarily for backwards-compatibility. You can accomplish the same thing with the + operator or by using embedded expressions.
***
**Related Pages:**
+    [+ operator](/ref/operator/+)
