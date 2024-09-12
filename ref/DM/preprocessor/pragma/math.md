## #pragma math directive 
###### BYOND Version 516
**See also:**
*   [#pragma directive](/ref/DM/preprocessor/pragma.md) 
*   [sin proc](/ref/proc/sin.md) 
*   [cos proc](/ref/proc/cos.md) 
*   [tan proc](/ref/proc/tan.md) <!-- -->
**Format:**
*   #pragma math [\<]{.faded}fast[\|]{.faded}accurate[\>]{.faded}


Chooses old-style fast math procs, or newer more accurate ones
that sacrifice a small amount of speed. This appplies to
[`sin()`](/proc/sin), [`cos()`](/proc/cos), and
[`tan()`](/proc/tan). 

The reason this is necessary is
because BYOND uses degrees for its angles, but converting to radians
(for the underlying math libraries) can\'t be done with precision for
many angles such as 90°, which is π/2 in radians. When the result of the
trig function is small, the angle being slightly off from what the user
intended will produce a small error in the result as well. 

The
more-accurate procs use trigonometric identities to reduce the angle to
a more manageable range of 0 to 45° (π/4 radians).
### Example:

```
 var/angle = 90 #pragma math fast usr \<\< cos(angle) //
6.12323e-17 #pragma math accurate usr \<\< cos(angle) // 0 
```



Using [`#pragma compatibility
515`](/DM/preprocessor/pragma/compatibility) will also force the
fast math version. 

Note* For consistency, built-in compiler
math for constant values uses the same calculations that would be used
for non-constant values runtime, so `cos(90)` compiles as 6.12323e-17
with fast math and as 0 for accurate math.