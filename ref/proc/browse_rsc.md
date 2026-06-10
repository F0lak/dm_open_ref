
## browse_rsc (proc)

**Format:**
+   usr << browse_rsc(File,FileName)

**Arguments:**
+   File: a resource file (such as an image)
+   FileName: name of file (if different from source file)
***
This sends the specified resource file to usr (or anybody else) and stores it in their <code>cache</code> directory with the specified name. In subsequent <code>browse()</code> output, you can then refer to that file.

If your world is always running on the internet, you can save yourself the trouble and simply link to the image files through a web server. However, if it may be played offline, you can compile in the resource files and manually send them to players with <code>browse_rsc()</code>.

Note that no data is transmitted if it already exists in the user's cache, so there is little overhead in calling this every time you are about to use <code>browse()</code>.


```dm

area
   var
      room_graphic = 'cozy_room.jpg'
   Enter(O)
      . = ..() //do default checks
      if(.)    //if we got clearance to enter
         O << browse_rsc(room_graphic,"room.jpg")
         O << browse("[desc]")

```


<img src="room.jpg"/>
***
**Related Pages:**
+    [browse proc](/ref/proc/browse)
