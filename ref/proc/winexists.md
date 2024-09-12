## winexists proc

**Format:**
+   winexists(player, control_id)
<!-- -->
**Args:**
+   player: A mob or client.
+   control_id: The unique ID of a control in the player\'s skin.


Tells if a control exists and if so, what type it is. The
return value is an empty string if the control does not exist, but
otherwise it is the type of control. 

This proc will not tell
you if a control has been defined in the skin file but is not in use
yet. 

Because the client must be contacted to get this
information, winexists() will sleep the current proc.

> [!TIP] 
> **See also:**
> +   [winclone proc](/ref/proc/winclone.md) 
> +   [winget proc](/ref/proc/winget.md) 
> +   [winset proc](/ref/proc/winset.md) 
> +   [winshow proc](/ref/proc/winshow.md) 
> +   [User interface skins](/ref/%7Bskin%7D.md) 
> +   [type parameter (skin)](/ref/%7Bskin%7D/param/type.md) <!-- -->