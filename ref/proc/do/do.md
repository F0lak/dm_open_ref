[]{#/proc/do}
## do proc
**See also:**
:   [break statement](#/proc/break)
:   [continue statement](#/proc/continue)
:   [for loop proc](#/proc/for/loop)
:   [while proc](#/proc/while)
<!-- -->
**Format:**
:   do Statement while( E )
Execute Statement. If E is true (non-zero) do it over again. Continue
until E is false (zero).
Statement may be a block of code or a single statement.
### Example:
var/i = 3 do world \<\< i\-- while(i)
This outputs: 3 2 1