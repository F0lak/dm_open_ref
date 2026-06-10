
## break (proc)

**Format:**
+   break
+   break Label
***
Terminate the loop with the given label. If no label is specified, the innermost loop containing the <code>break</code> statement is assumed.


```dm

obj/zapper
  verb/use()
    var/mob/M

    for(M in view())
      if(!M.key) break

    if(!M) M = usr
    M << "ZAP!"
    del(M)

```


The zapper object kills the first mob it finds that doesn't belong to a player. If none can be found, it kills the user. Be careful! Note how this code takes advantage of the fact that the loop variable `M` will be <code>null</code> if the loop terminates normally.

For an example of how to use labeled loops, see the reference section for the <code>continue</code> statement.

The `break` statement can also be used inside of a <a href="#/proc/switch">`switch()` proc</a> when using <a href="#/DM/preprocessor/pragma/syntax">C-like syntax</a>, where it breaks out of a `case` block to the end of the switch. See <a href="#/proc/switch">switch proc</a> for more details.
***
**Related Pages:**
+    [continue statement](/ref/proc/continue)
+    [do proc](/ref/proc/do)
+    [for loop proc](/ref/proc/for/loop)
+    [while proc](/ref/proc/while)
+    [switch proc](/ref/proc/switch)
+    [#pragma syntax directive](/ref/DM/preprocessor/pragma/syntax)
