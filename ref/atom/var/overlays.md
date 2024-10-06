## overlays var (atom)

<!-- -->
**Default value:**
+   empty list

> [!IMPORTANT]
> Overlays are relatively static and cannot be altered on the
fly, only replaced. They\'re your best-performing option for very simple
things that won\'t change often. If you need something that allows
dynamic changes you may prefer to look into [image objects](/ref/image.md) 
(which can also be selectively shown to only certain players) or [visual
contents](/ref/atom/var/vis_contents.md)  which are more versatile.


This is a list of simple icons which are displayed on top of
the object\'s main icon. 

The individual items in the list may
not be directly accessed, since they are stored in a [special internal
format](/ref/atom/var/appearance.md)  However, the list operators `+=`, `-=`,
and the procedures `Add`, `Remove`, and `Cut` work normally.

### Example:

```dm
turf/verb/AddOverlay(I as icon)
	overlays += I

turf/verb/RemoveOverlay(I as icon)
	overlays -= I 
```

The
data types that may be used as overlays are icons, icon states (text
strings), objects, and object types. When an icon state is used, the
corresponding image in the object\'s icon is displayed. When another
object is used as an overlay, a static "snapshot" of the object is
taken at the time when the overlay is created. Future changes to the
object will not change the appearance of the overlay, except that in
some cases the overlay may inherit things from the base object like its
icon (if left empty), direction, and moving state. 

Overlays
have their own independent drawing layer. It is normally the special
value FLOAT_LAYER, which makes them float above the base object. If the
overlay is a snapshot of another object, the drawing layer of that
object is used (and in that case, the overlay can appear beneath the
object if its layer is lower). The important advantage of using
FLOAT_LAYER is that if the layer of the base object changes, the
overlays will move with it into the new layer. 

Any negative
number may be used in place of FLOAT_LAYER (which happens to be -1).
They all cause the same "floating" behavior. However, the overlays are
ordered amongst themselves according to their own relative layer values
(-2 below -1 and so on). This may be useful if you have several classes
of overlays that should always appear in a certain order, because you
would not have to worry about the order in which you add them to the
list.
### Example:

```dm
var/const
	ARMOR_LAYER = FLOAT_LAYER-1
	CLOTHES_LAYER = FLOAT_LAYER-2
	
obj/overlay
	armor
		icon = 'armor.dmi'
		layer = ARMOR_LAYER
	clothes
		icon = 'clothes.dmi'
		layer = CLOTHES_LAYER
		
mob/verb
	wear_clothes()
		overlays += /obj/overlay/clothes
	wear_armor()
		overlays += /obj/overlay/armor
	remove_clothes()
		overlays -= /obj/overlay/clothes
	remove_armor()
		overlays -= /obj/overlay/armor 
```
 

That
example used object types, but you can use instances of objects as well.
Rather than using different "float" layers, you can also just make
your own list of overlays with the order you want and assign that to the
actual overlays list.

### Example:

```dm
mob/var
	boots
	clothes
	armor
	
mob/proc
	ShowOverlays()
		var/L[0]
		if(boots)
			L += boots
		if(clothes)
			L += clothes
		if(armor)
			L += armor
		overlays = L 
```


> [!TIP] 
> **See also:**
> +   [underlays var (atom)](/ref/atom/var/underlays.md) 
> +   [icon var (atom)](/ref/atom/var/icon.md) 
> +   [layer var (atom)](/ref/atom/var/layer.md) 
> +   [list](/ref/list.md) 
> +   [image objects](/ref/image.md) 
> +   [vis_contents var (atom)](/ref/atom/var/vis_contents.md) 
> +   [Understanding the renderer](/ref/notes/renderer.md) 