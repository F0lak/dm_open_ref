## group list var (mob)

**Default value:**
+   (empty list)


This is a list of mobs in the same group. By default, a mob
will swap positions with another mob in its group if bumped. It is also
possible to make verbs that are accessible only to members of the group.


The following example handles addition of somebody else to your
group.
### Example:

```
 mob/verb/join(mob/M) usr.group.Add(M) // add M to usr\'s
group view() \<\< \"\[usr\] joins \[M\].\" mob/verb/disband(mob/M)
usr.group.Remove(M) // remove M from group view() \<\< \"\[usr\]
disbands \[M\].\" 
```
 

Note that group lists may be
asymmetric. Mob A may have mob B in his group list, but mob B may or may
not. It is up to you to define whether mobs are added into both lists or
not. 

Here is an example of a verb accessible to a group:
### Example:

```
 mob/verb/summon() set src in usr.group loc = usr.loc view()
\<\< \"\[usr\] summons \[src\].\" 
```


**See also:**
+   [Bump proc (movable atom)](/ref/atom/movable/proc/Bump.md) 
+   [list](/ref/list.md) <!-- -->