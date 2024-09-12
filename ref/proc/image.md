## image proc
**See also:**
+   [\<\< operator](/ref/operator/%3c%3c.md) 
+   [del proc](/ref/proc/del.md) 
+   [icon](/ref/icon.md) 
+   [image objects](/ref/image.md) 
+   [images var (client)](/ref/client/var/images.md) 
+   [overlays var (atom)](/ref/atom/var/overlays.md) 
<!-- -->
**Format:**
+   image(icon,loc,icon_state,layer,dir)
+   [(supports [named arguments](/ref/proc/arguments/named.md) )]{.small}
<!-- -->
**Returns:**
+   An image reference on success; 0 on failure.
<!-- -->
**Args:**
+   icon: An icon, icon_state, object prototype, object instance, or
    other image.
+   loc: The location at which to display the image.
+   icon_state: The icon state to use.
+   layer: The drawing layer to use.
+   dir: The direction to orient the image.


Images are \"virtual\" objects, which have a purely visual
effect. Once created, they can be made to appear to selected players.
The image() instruction is simply a short-hand for new/image().


The image remains attached to the location specified by
`loc`{.variable}. For example, if `loc`{.variable} is a mob, the image
will appear above the mob until it is destroyed. 

The `icon`
argument can be anything that can be interpreted as an appearance, i.e.
anything you might add to an overlays list. If this argument is
interpreted as an appearance, it will be used *instead of* the
appearance of the image type. A null value will use the image type\'s
own default appearance. An icon value will use the default appearance
but change the icon. A text string will be interpreted as the
`icon_state` argument if one is not present, but otherwise will be
interpreted as an appearance. 

The arguments
`icon_state`{.variable}, `layer`{.variable}, and `dir`{.variable} may be
used to override the settings associated with the icon or object used to
create the image. For example, the default drawing layer for an plain
icon is FLY_LAYER (above all other objects), but you could change this
to OBJ_LAYER to make it appear under mobs on the map.
### Example:

```
 var/Box Box = image (\'highlight.dmi\', usr) usr \<\< Box
\... del(Box) //when done, remove image 
```
 

Another
common use of images is in making an overlay: 
```
 overlays +=
image(\'pants.dmi\',icon_state = \"red\") 
```
 

Since the
`loc` argument could never be a text string, the above statement can be
further shortened: 
```
 overlays += image(\'pants.dmi\',\"red\")

```
 

This is much preferable to achieving the same effect
with `icon('pants.dmi',"red")`, since that involves the overhead of
creating a new icon file, which should only be done when it is really
necessary. 

Note: The fact that `image` is essentially a wrapper
for `new/image()` means that the arguments in
[image/New()](/ref/datum/proc/New.md) are always treated the same way
as defined in this article. This applies even to subtypes, like
`/image/thing`. If you create a user-defined subtype like
`new/image/thing()` it will still use the arguments the same way as in
`image()`. You can\'t meaningfully customize the arguments in `New()`
for images.