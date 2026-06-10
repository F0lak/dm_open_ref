
## syntax (info)

**Format:**
+   #pragma syntax CDM forswitch
***
Changes the syntax used to parse certain statements. This can be more natural for users who prefer non-DM style, and can sometimes do things that regular DM syntax can't do.

Changing the <a href="#/proc/for/loop">`for()` loop</a> syntax to C will use semicolons to separate the Init, Test, Inc sections instead of commas. That means commas can be used to chain multiple statements together instead.

In <a class="code" href="#/proc/switch">switch()</a>, C syntax changes the if/else statements to use C's `case` and/or `default` keywords, followed by a colon, and the <a href="#/proc/break">`break` statement</a> is required to skip to the end of the switch unless you want to fall through to the next case. Fall-through behavior isn't possible in the default DM syntax.


```dm

#pragma push
#pragma syntax C switch

switch(thing)
    case 1:
        usr << "This is case 1!"
        break
    case 2, 3:
        usr << "This is case 2 or 3."
        // no break, fall through
    case 4 to 6:
        usr << "This is case 4 through 6 (or maybe 2 or 3)."
        break
    default:
        usr << "This is a different case.

#pragma pop

```

***
**Related Pages:**
+    [#pragma directive](/ref/DM/preprocessor/pragma)
+    [for loop proc](/ref/proc/for/loop)
+    [switch proc](/ref/proc/switch)
