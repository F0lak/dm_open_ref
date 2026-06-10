
## IsByondMember (proc)

**Format:**
+   IsByondMember()

**Arguments:**
+   None.
***
This built-in procedure checks to see if the user is a BYOND Member. Use it to give special in-game rewards to those who support BYOND.

If the user is a Member, the result is the number of days left (rounded up) on their Membership, or -1 for lifetime Members.


```dm

mob/var
   special_features

mob/Login()
   if(client.IsByondMember())
      special_features = 1
   else
      src << "For special features, become a BYOND Member!"
   return ..()

```

***