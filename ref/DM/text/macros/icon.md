
## icon (info)
***
The \icon macro is used to treat the following embedded expression (in []'s) as an icon rather than as text. An object, for example, would be replaced by its icon rather than by its name.


```dm

usr << "You look like this: \icon[usr]!"

```


The <code>\icon</code> macro expands internally to the &lt;IMG&gt; tag. The above example, could be rewritten like this:


```dm

usr << "You look like this: \
  !"

```


Note that the current icon state of the object is automatically used. Also note that the image belongs to a class called <code>icon</code>. That allows you to configure the way icons are displayed by using a style sheet. The following default style rule causes icons to be shrunk to 16 by 16 pixels so they fit in better with surrounding text:


```dm

IMG.icon {width: 16px; height: 16px}

```


You could override this setting globally in your own style sheet. You could even define rules to allow individual icons to be formatted differently from the rest.


```dm

BIG IMG.icon {width: 32px; height: 32px}
SMALL IMG.icon {width: 16px; height: 16px}

```


With those rules in place, you could output a full sized icon by using the &lt;BIG&gt; tag:


```dm

usr << "You look like this: \icon[usr]!"

```


The one time that one might want to use the &lt;IMG&gt; tag directly is to specify the ALT text to be displayed on clients which don't support graphical icons.

Specific states, directions, and frames of an icon can be displayed in lieu of the default through use of the following tags:


```dm

usr << "You look like this: \
  !"

```


Note that the \icon macro does not work in the mini-browser; it is only for text output. To make icons appear in an HTML document, use <a href="#/proc/browse_rsc">browse_rsc()</a> to send an icon to the client before using <a href="#/proc/browse">browse()</a> to display it.
***
**Related Pages:**
+    [icon_state](/ref/atom/var/icon_state)
+    [macros (text)](/ref/DM/text/macros)
+    [style sheets](/ref/DM/text/style)
+    [tags (text)](/ref/DM/text/tags)
