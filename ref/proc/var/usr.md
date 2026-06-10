
## usr (var)
***
This is a mob variable (var/mob/usr) containing the mob of the player who executed the current verb, or whose action ultimately called the current proc.


```dm

obj/bread
  verb/eat()
    world << "[usr] eats [src]"

```


If a player named "Bob" calls "eat bread", the output will be "Bob eats the bread."

Essentially, `usr` is an implicit parameter that is passed to every proc or verb. Each procedure inherits the value from its caller. While it can simplify your code in some situations, it can also lead to subtle problems if you are assuming that `usr` is automatically assigned the value of `src` when you call a verb programmatically. It is not.

The only time `usr` is assigned for you is when a player executes a verb, clicks something with the mouse, clicks a link (see <a class="code" href="#/client/proc/Topic">Topic</a>), or any other such action.


> [!TIP]
> Note: **A good rule of thumb is to never put usr in a proc, only verbs.** Typically `usr` in a proc is an unsafe programming practice. If `src` would not be the correct choice, it is better to send another argument to your proc with the information it needs.

Certain built-in procs such as <a class="code" href="#/atom/proc/Click">atom/Click()</a> are called automatically by a client counterpart like <a class="code" href="#/client/proc/Click">client/Click()</a>; usually <a class="code" href="#/atom/proc/Click">atom/Stat()</a> is called by <a class="code" href="#/client/proc/Click">client/Stat()</a>; and so on. It is mostly safe to apply `usr` as directed in those situations, because these procs are pseudo-verbs. It is mostly <em>not</em> safe to apply `usr` in a movement proc such as <a class="code" href="#/atom/movable/proc/Move">Move()</a> or <a class="code" href="#/atom/proc/Enter">Enter()</a>, because objs and non-player mobs may move autonomously without setting `usr`.

Although `usr` is often set in <a href="#/mob/proc/Login">mob/Login()</a> when a client first connects, you should not assume it is valid if `Login()` is called any other way. Common cases occur when creating a new character, loading a player's mob from a savefile; or explicitly when setting a mob's key or changing the value of <a class="code" href="#/client/var/mob">client.mob</a>. It is safest to use `src` in `mob/Login()`, which is always correct, rather than `usr`.

`usr` is the default point of reference for several procs like <a class="code" href="#/proc/view">view()</a> and <a class="code" href="#/proc/range">range()</a>, because of their common use in verbs. It is also the default recipient for <a class="code" href="#/proc/input">input()</a> and <a class="code" href="#/proc/alert">alert()</a> messages. When using these in procs, be aware of that so you can change the default reference value to something more appropriate.
***
**Related Pages:**
+    [src var (proc)](/ref/proc/var/src)
+    [verbs](/ref/verb)
+    [Topic proc (client)](/ref/client/proc/Topic)
+    [range proc](/ref/proc/range)
+    [view proc](/ref/proc/view)
+    [alert proc](/ref/proc/alert)
+    [input proc](/ref/proc/input)
