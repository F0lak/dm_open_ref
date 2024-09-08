[]{#/proc/alert}
## alert proc
**See also:**
:   [input proc](#/proc/input)
<!-- -->
**Format:**
:   alert(Usr=usr,Message,Title,Button1=\"Ok\",Button2,Button3)
<!-- -->
**Returns:**
:   Selected button
This sleeps the current proc until the user clicks one of the named
buttons. As with input(), the first argument may be entirely left out.
### Example:
mob/verb/self_destruct() alert(\"Prepare to die.\") del usr
A slightly more complicated example provides the user with a choice in
the matter:
### Example:
mob/verb/self_destruct() switch(alert(\"Would you like to
die?\",,\"Yes\",\"No\",\"Maybe\")) if(\"Yes\") del usr if(\"No\") usr
\<\< \"You have second thoughts.\" if(\"Maybe\") usr \<\< \"You flip a
coin\...\" if(rand(0,1)) usr \<\< \"Heads \-- you lose.\" del usr else
usr \<\< \"Tails \-- you win!\"