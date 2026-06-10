
## RenderIcon (proc)

**Format:**
+   RenderIcon(object)

**Arguments:**
+   object: An atom or appearance to render.

**Returns:**
+   A single-image icon file in which the object is rendered with all its
overlays, visual contents, etc.
***
Use this proc to render an atom or an appearance as a single icon. This is a client proc because the server is not capable of rendering anything on its own.

Any overlays, image objects known to this client that are attached to the object, visual contents, maptext, and so on will be included in the render. The returned icon is sized to fit all of the above, and to include room for any expansion due to filter effects.


```dm

mob/proc/GetFlatIcon()
    return client?.RenderIcon(src)

```


Important notes regarding this proc:
***
**Related Pages:**
+    [vis_contents](/ref/atom/var/vis_contents)
+    [Filter effects](/ref/{notes}/filters)
