# IsByondMember proc (client)
**Format:**
+   IsByondMember()
<!-- -->
**Args:**
+   None.


This built-in procedure checks to see if the user is a BYOND
Member. Use it to give special in-game rewards to those who support
BYOND. 

If the user is a Member, the result is the number of
days left (rounded up) on their Membership, or -1 for lifetime Members.
### Example:

```
 mob/var special_features mob/Login()
if(client.IsByondMember()) special_features = 1 else src \<\< \"For
special features, [become a BYOND Member](\){'http:=""
members.byond.com="" '=""}!\" return ..() 
```
