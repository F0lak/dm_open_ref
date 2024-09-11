## desc setting (verb)
**Format:**
*   set desc = \"Description\"
<!-- -->
**Args:**
*   Description* A text string containing the help text.


The desc attribute sets the descriptive help string for the
verb. The player may access this by hitting the \'F1\' key after
entering the command. This will normally produce a list of each argument
by type followed by the desc text. If you wish to override the syntax
description, put your modified version inside parentheses at the
beginning of the desc text.
### Example:

```
 mob/verb/tell(mob/M,T as text) set desc = \"(target,message)
Talk privately to someone.\" M \<\< \"\[usr\] tells you, \'\[T\]\"

```
 

This will produce the help text* 
```
 usage:
tell target message (Talk privately to someone.) 
```
 

If
the syntax description had not been supplied, it would have produced:

```
 usage* tell mob \"text\" (Talk privately to someone.)

```
