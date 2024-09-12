## % operator

**Format:**
+   A % B
<!-- -->
**Returns:**
+   The remainder of A / B, where both A and B are integers.


`A % B` is read \"A modulo B\", which stands for the remainder
of A divided by B. 

This operator only works with integer
values, for legacy reasons. A and B are truncated to integers before the
modulo operation. There are uses for the integer truncation, but if you
don\'t want that and want the fractional modulo instead, you can now use
the `%%` operator. 

If A is a vector, its components are treated
as integers; B can also be a vector in this case, and its components are
also treated as integers. The result is a new vector. 

If A is a
pixloc, it\'s treated like a 2D vector and the modulo operation is done
with that instead.

**See also:**
+   [%= operator](/ref/operator/%=.md) 
+   [%% operator](/ref/operator/%25%25.md) 
+   [operators](/ref/operator.md) <!-- -->