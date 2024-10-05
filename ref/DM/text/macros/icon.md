## icon text macro

The \\icon macro is used to treat the following embedded
expression (in []\'s) as an icon rather than as text. An object, for
example, would be replaced by its icon rather than by its name.
### Example:

``` dm
usr << "You look like this: \icon[usr]!"
```

The `\icon` macro expands internally to the <IMG> tag. The
above example, could be rewritten like this: 
``` dm
usr << "You look like this: \
  <IMG CLASS=icon SRC=\ref[usr.icon] ICONSTATE='[usr.icon_state]'>!"
```
 
> [!NOTE] 
> The current icon state of the object is automatically used. Also note that
the image belongs to a class called `icon`. That allows you to configure
the way icons are displayed by using a style sheet. The following
default style rule causes icons to be shrunk to 16 by 16 pixels so they
fit in better with surrounding text: 
``` dm
IMG.icon {width: 16px; height: 16px}
```

You could override this setting
globally in your own style sheet. You could even define rules to allow
individual icons to be formatted differently from the rest.
### Example:
``` dm
BIG IMG.icon {width: 32px; height: 32px}
SMALL IMG.icon {width: 16px; height: 16px}
```
 
With those rules in
place, you could output a full sized icon by using the \<BIG> tag:

``` dm
usr << "You look like this: <BIG>\icon[usr]</BIG>!"
```

The one time that one might want to use the <IMG> tag
directly is to specify the ALT text to be displayed on clients which
don\'t support graphical icons. 

Specific states, directions,
and frames of an icon can be displayed in lieu of the default through
use of the following tags:
-   ICONSTATE=\'[state]\'
-   ICONDIR=[dir], where dir is one of NORTH, SOUTH, EAST, WEST,
    NORTHEAST, NORTHWEST, SOUTHEAST, SOUTHWEST
-   ICONFRAME=[frame], where frame is the animation frame, starting
    with 1
### Example:

``` dm
usr << "You look like this: \
  <IMG CLASS=icon SRC=\ref[usr.icon] ICONSTATE='glowing' ICONDIR=NORTH ICONFRAME=2>!"
```
 
> [!NOTE] 
> The \\icon macro does not work in the mini-browser; it is only for text output. To make icons
appear in an HTML document, use [browse_rsc()](/ref/proc/browse_rsc.md)  to
send an icon to the client before using [browse()](/ref/proc/browse.md) to
display it.

> [!TIP] 
> **See also:**
> +   [icon_state var (atom)](/ref/atom/var/icon_state.md) 
> +   [macros (text)](/ref/DM/text/macros.md) 
> +   [style sheets](/ref/DM/text/style.md) 
> +   [tags (text)](/ref/DM/text/tags.md) 
