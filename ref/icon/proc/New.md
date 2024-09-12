## New proc (icon)
**See also:**
+   [icon](/ref/icon.md) 
+   [procs (icon)](/ref/icon/proc.md) 
+   [image proc](/ref/proc/image.md) 
+   [new proc](/ref/proc/new.md) 
<!-- -->
**Format:**
+   New(icon,icon_state,dir,frame,moving)
+   [(supports [named arguments](/ref/proc/arguments/named.md) ]{.small}
<!-- -->
**Args:**
+   icon: an icon file or /icon object
+   icon_state: an optional text string, specifying a single icon state
    to load
+   dir: an optional direction to extract
+   frame: an optional animation frame to extract
+   moving: Non-zero to extract only movement states, 0 for non-movement
    states, or null (default) for both


You generally don\'t call this directly but via new(). The
specified icon file is loaded into memory for direct access and
manipulation. 

If the icon state is not specified, all icon
states are loaded. Ditto for the direction, animation frame, or
preference for movement states. Animation frames are numbered from 1 and
up, so frame=4 is the 4th frame. 

(Movement states are special
versions of an existing icon_state with the same name, but appear in the
Dream Maker editor with an \"M\" indicator. These states are used for
animation when the atom using the icon_state moves from one tile to the
next; otherwise only the normal non-moving state is displayed.)


The following contrived example, loads the EAST facing default
icon state \"\" from the user\'s icon file, rotates that a bit, and then
creates a new icon file for the user.
### Example:

```
 mob/verb/test() var/icon/I = new(usr.icon,icon_state =
\"\",dir = EAST) I.Turn(90) //rotate clockwise 90 degrees usr.icon = I

```
 

Note that merely displaying different icon states or
directions can generally be achieved without any icon manipulation,
which is good, because it saves quite a bit of overhead. For example,
the variables atom.icon_state and atom.dir can be used to control how
atom.icon is displayed, without any need for generating a new icon file.