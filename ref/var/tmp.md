
## tmp (var)
***
The tmp type modifier indicates that an object variable should not be automatically written to the save file. This could mean that the variable is transient—that is, it is calculated at run-time and need not be saved. It could also indicated that the designer will handle saving of that variable specially and wishes to bypass the automated routine.

It is especially important to use tmp when you have references to external objects that should not be saved along with the object. For example, suppose players have a `leader` variable which indicates who or what they are following. You would not necessarily want the leader to be saved in the player's savefile. Therefore, you would need to use <code>tmp</code> when defining the variable.


```dm

mob
   var/tmp
      leader
   verb
      follow(mob/M)
         leader = M

```


Accidentally saving another mob in your savefile can be disastrous. This can happen if you save a turf that the mob is standing on, or if you save an obj with a non-tmp var that points to that mob, and many other ways.

The reason this is a problem is that another player's mob will have the `key` var set already. When that mob is loaded, if they are already logged into the game they will be immediately reassigned to that just-loaded, older mob with a `Login()` call, while the mob they're supposed to be using will have `Logout()` called. Thus they'll appear to "rollback" to an earlier state.

If your game accidentally falls into this trap, don't panic! You can look at your savefiles via <a class="code" href="#/savefile/ImportText">ImportText()</a> or in an editor to see which var is the problem. Once you change that var to `/tmp`, you can override <a class="code" href="#/datum/proc/Read">Read()</a> so if that var is present, you can remove it before calling `..()` to finish loading.
***
**Related Pages:**
+    [savefile](/ref/savefile)
+    [vars](/ref/var)
