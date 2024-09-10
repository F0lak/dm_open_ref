[]{#/switch proc.md}    
## switch proc    
**See also:**    
:   [if proc](/proc/if)    
:   [#pragma syntax directive](/DM/preprocessor/pragma/syntax)    
**Format:**    
switch(E)    
:   if(A1,A2,\...) Statement1    
:   if(B1,B2,\...) Statement1    
:   else Statement3    
The \"switch\" instruction is a compact notation for a lengthy    
\"else-if\" chain. The expression E is compared to the values A1, A2,    
B1, B2, etc. When a match is found, the following statement (or code    
block) is executed. An optional \"else\" statement is run if no match is    
found. Once a matching switch condition is found, no further conditions    
will be tested.    
The values A1, A2, etc. must be constants. As a convenience, a range of    
values may be specified in the form: A1 to An.    
The switch instruction is MUCH more efficient than a lengthy \"else-if\"    
chain, because the expression E is evaluated only once. The conditional    
values may be any constant expression, such as a number or text string.    
### Example:    
switch (2) if(1) world \<\< \"ONE\" if(4) world \<\< \"FOUR\" if(2,3)    
world \<\< \"TWO or THREE\" if(5 to 10) world \<\< \"FIVE to TEN\" else    
world \<\< \"not ONE to TEN\"    
This outputs: TWO or THREE    
Note: Currently the compiler does not throw a warning or error if there    
is a conflict between two different `if` blocks in a `switch`, e.g. when    
you define `if(1 to 10)` and `if(5 to 20)` which overlap from 5 to 10.    
If two different blocks could handle a given value, the choice of which    
block takes over is not defined.    
### C-like syntax    
Using the [`#pragma syntax` directive](/DM/preprocessor/pragma/syntax)    
you can change `switch()` to be more like other languages such as C.    
This replaces the if/else instructions with `case `*`value`* and    
`default` with a trailing colon. If you don\'t use the [`break`    
statement](/proc/break) at the end of a block, it will fall through to    
the next block.    
### Example:    
// make this syntax change temporary #pragma push #pragma syntax C    
switch mob/proc/Greeting(friend) switch(roll(6)) case 4: friend \<\<    
\"I\'m \[name\]. \\\...\" // fall through to cases 1 and 2 case 1,2:    
friend \<\< \"Hi!\" break case 3: friend \<\< \"Hello there!\" default:    
friend \<\< \"Yo.\" break #pragma pop    
Multiple cases can be put together with either commas between the    
values, or separate `case` statements. The *`A`*` to `*`B`* syntax is    
still allowed also.  