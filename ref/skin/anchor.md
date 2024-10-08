## anchor1, anchor2 parameters (skin)


**Applies to:**
+   [All](/ref/skin/control.md)  (except
    [Main](/ref/skin/control/main.md) 

**Format:**
+   none
+   *x*,*y*

**Default value:**
+   none


Anchors the control within the window or pane. If the anchor is
not `none`, it is expressed as pecentages of the container\'s width and
height. For example, an anchor of 100,100 means that the X and Y
position are tied to the lower right of the container, and 50,0 is tied
to the top center. 

Setting only `anchor1` will control the
position of the control but won\'t affect its size. 

Setting
`anchor2` as well will allow you to stretch the control as the
container\'s size changes. You can think of this `anchor1` controlling
the top left corner, and `anchor2` the bottom right corner.

> [!TIP] 
> **See also:**
> +   [pos parameter](/ref/skin/param/pos.md) 
> +   [size parameter](/ref/skin/param/size.md) 