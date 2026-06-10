
## ref (info)
***
The <code>\ref</code> text macro inserts a unique identification number or text string for the following embedded object (inside []'s).

In older versions of BYOND, if an object had a tag, that was used instead. However this has often proved to be problematic, so anything compiled from version 512 onward should expect to output a reference number. If you want to use the tag, which stands a better chance of still being valid if the object is deleted and recreated (like in a world reboot), you can output the object's tag explicitly.

The primary use for object references embedded in text is in topic links. This allows you to encode a reference to an object in the href value of a hyperlink. (Just make sure the object does not get deleted before the user executes the link. See <a href="#/DM/garbage">garbage collection</a>.)

Topic links that contain a parameter "src" assigned to an object reference are treated somewhat specially. Unless you override client.Topic() to do otherwise, the default behavior is to call the referenced object's own Topic() procedure.


```dm

mob/verb/test()
   usr << "Click here!"
mob/Topic(href,href_list[])
   switch(href_list["action"])
      if("start")
         usr << "Starting the game..."
      else
         return ..()

```


The above example uses an embedded reference to the player's own mob to create a link to a topic handled by that mob's Topic() proc. The <code>href_list</code> parameter is simply the result of <code>params2list(href)</code>.

In that example, the embedded reference was automatically converted back into an object (dereferenced) for you. If you embed references to additional objects in the href data, you would have to dereference those yourself using the locate() instruction.

In output for browser controls, you can use `\ref[object]` as the src parameter for an &lt;img&gt; tag. The object can be an <a href="#/atom/var/appearance">appearance</a>, an icon, or an atom or image.

If the ref string is for an icon, you can add an HTML query string after the icon reference.


```dm

player << browse({"
    
    
    "})

```


The query string can include any of the following (separated by &amp; characters):
***
**Related Pages:**
+    [Topic proc (client)](/ref/client/proc/Topic)
+    [icon text macro](/ref/DM/text/macros/icon)
+    [locate proc](/ref/proc/locate)
+    [macros (text)](/ref/DM/text/macros)
+    [tag](/ref/datum/var/tag)
