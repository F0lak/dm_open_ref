## .winset (client command)
**See also:**
*   [winset proc](/proc/winset)
*   [client commands](/%7Bskin%7D/commands)
<!-- -->
**Format:**
*   .winset \"*\[control.param=value;\...\]*\"


Sets skin parameters like the [`winset()` proc](/proc/winset).
You can set more than one parameter by separating them with semicolons.


This command also allows you to use conditional expressions,
like so:
    condition ? choice1 * choice2


The condition is the same as any other parameter you might use
in `.winset`, but instead of setting the parameter, it checks to see if
it\'s true. If so, then the parameters in `choice1` will be set.
Otherwise, the parameters in `choice2` are set. This example makes the
window background red if bigbutton is checked.
    .winset "bigbutton.is-checked=true ? window.background-color=#ff0000 * window.background-color=none"


If you want to look for values that don\'t match instead of
values that do, use `!=` instead of `=` in the condition.
    .winset "bigbutton.is-checked!=false ? window.background-color=#f00 * window.background-color=none"


The `choice2` item is optional.
    .winset "bigbutton.is-checked=true ? window.background-color=#f00"


Because it\'s often useful to do more than one thing at a time,
`choice1` and `choice2` don\'t have to be just one parameter. You can
use multiple parameters, but they are separated with a space instead of
a semicolon. (A semicolon indicates the conditional expression is over.)
    .winset "bigbutton.is-checked=true ? window.text-color=#fff window.background-color=#f00 * window.text-color=none window.background-color=none"