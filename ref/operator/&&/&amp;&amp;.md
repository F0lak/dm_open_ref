[]{#/operator/&&}
## && operator
**See also:**
:   [! operator](#/operator/!)
:   [operators](#/operator)
:   [\|\| operator](#/operator/%7C%7C)
:   [&&= operator](#/operator/&&=)
<!-- -->
**Format:**
:   A && B
<!-- -->
**Returns:**
:   First false value of either A or B; last true value otherwise
The only false values in DM are the number 0, an empty text string, or
null. All other values are considered true.
The first false value from left to right completes the evaluation (a
practice known as short-circuiting), meaning that any expressions after
the first false value are skipped. The return value is equal to the last
operand to be evaluated.
### Example:
if(jumping && CanDoubleJump()) DoubleJump()
In this example, the `CanDoubleJump()` call is not performed if
`jumping` is false.
Although logical short-circuit operators are used most often in blocks
such as `if` or `while`, they can be used elsewhere.
### Example:
// check if current target is valid, if it exists at all // but don\'t
call the proc if we don\'t have to var/target = current_target &&
TargetIsValid(current_target)