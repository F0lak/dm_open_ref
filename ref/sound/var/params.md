
## params (var)

**Default Value:**
+   null
***
Used to set client skin information related to this sound. This can be set to an <a href="#/list/associations">associative list</a> or a parameter string such as you would get from <a class="code" href="#/proc/list2params">list2params()</a>.

These are the parameters currently defined:


```dm

mob/proc/PlayIntro()
    var/sound/S = sound('intro.ogg')
    S.params = list("on-end" = ".intro-ended")
    src << S

mob/verb/_Intro_Ended()
    set name = ".intro-ended"
    src << "The intro has concluded."

```

***
**Related Pages:**
+    [vars (sound)](/ref/sound/var)
