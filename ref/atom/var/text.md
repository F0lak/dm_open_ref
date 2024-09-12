# text var (atom)
**Default value:**
+   The first letter of the object\'s name.


This is the character used to represent the object on text
clients. 

Entering several characters produces a text movie (the
state of the art!). In that case, each character is displayed for a 10th
of a second. 

HTML tags in the text can be used to modify the
colors of the text characters. As a convenience, the \<font\> tag may
include a `bgcolor` attribute, so you don\'t have to do a CSS style
setting to accomplish the same thing.
### Example:

```
 world maxx = 10 maxy = 10 area text = \" \" turf text =
\"\...\...\" 
```
 

The example above produces a map with a
blue background (from the area) and turfs (depicted by \".\") that flash
from bright red to a shorter span of light red. 

Note that in
order to see text icons, the user must switch to the text map in Dream
Seeker. If your DM code never does anything with the icon variable, then
this is the default configuration. Such applications are known as
*advanced* iconic text games:)

> [!TIP] 
> 