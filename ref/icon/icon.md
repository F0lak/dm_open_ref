## icon object
**See also:**
*   [procs (icon)](/ref/icon/proc.md) -m
*   [icons](/ref/DM/icon.md) -m
*   [image objects](/ref/image.md) -m
*   [stddef.dm file](/ref/%7B%7Bappendix%7D%7D/stddef%2edm.md) -m


An `/icon` object is created by loading an icon file into
memory for direct access and manipulation. In order to be displayed, an
`/icon` object always gets converted back into an icon file; this
happens automatically when you assign atom.icon to an `/icon` object,
since that variable may only refer to a static icon file, rather than a
dynamic memory object. 

To create an `/icon` object, simply use
`new/icon()`, or the short-cut `icon()` proc. The following example
loads an icon file, reddens it, and then assigns it back to the
player\'s icon, which implicitly creates a new icon file.
### Example:

```
 mob/verb/test() var/icon/I = new(\'player.dmi\')
I.Blend(rgb(40,0,0)) usr.icon = I 
```
 

Note that merely
displaying different icon states or directions can generally be achieved
without any icon manipulation, which saves quite a bit of overhead. For
example, the variables `atom.icon_state` and `atom.dir` can be used to
control how `atom.icon` is displayed, without any need for generating a
new icon file. 

Many things that used to require icon
manipulation may not need you to do so anymore, as DM has evolved new
capabilities.
  ---------------------------------------------------------------------------------------------------------------------------------
  Operation                `/icon` proc                                      New method
  ------------------------ ------------------------------------------------- ------------------------------------------------------
  Multiplying by color     [`Blend`](/ref/icon/proc/Blend.md) -m{.code} or            [color](/ref/atom/var/color.md) -m{.code} var
                           [SetIntensity](/ref/icon/proc/SetIntensity.md) -m{.code}   
                           procs                                             
  Adding color             [Blend](/ref/icon/proc/Blend.md) -m{.code} proc            [color](/ref/atom/var/color.md) -m{.code} var (using [color
                                                                             matrix](/ref/%7Bnotes%7D/color-matrix.md) -m)
  Applying color matrix    [MapColors](/ref/icon/proc/MapColors.md) -m{.code} proc    
  Rotation                 [Turn](/ref/icon/proc/Turn.md) -m{.code} proc              [transform](/ref/atom/var/transform.md) -m{.code} var
  Flipping                 [Flip](/ref/icon/proc/Flip.md) -m{.code} proc              
  horizontal/vertical                                                        
  Scaling                  [Scale](/ref/icon/proc/Scale.md) -m{.code} proc            
  Overlaying/underlaying   [Blend](/ref/icon/proc/Blend.md) -m{.code} proc +          Overlay/underlay +
  another icon             `ICON_OVERLAY`                                    [KEEP_TOGETHER](/ref/atom/var/appearance_flags.md) -m{.code}\
                                                                             [Layering filter](/ref/%7Bnotes%7D/filters/layer.md) -m  ---------------------------------------------------------------------------------------------------------------------------------
Note* Anything you can do with an atom var instead of using icon
manipulation procs will usually perform much better. Games that use the
new methods use fewer resources, use less memory, and also usually look
better too.