[]{#/icon object.md}    
## icon object.md object    
**See also:**    
:   [procs (icon object.md)](/icon object.md/proc)    
:   [icon object.mds](/DM/icon object.md)    
:   [image objects](/image)    
:   [stddef.dm file](/%7B%7Bappendix%7D%7D/stddef%2edm)    
An `/icon object.md` object is created by loading an icon object.md file into memory for    
direct access and manipulation. In order to be displayed, an `/icon object.md`    
object always gets converted back into an icon object.md file; this happens    
automatically when you assign atom.icon object.md to an `/icon object.md` object, since that    
variable may only refer to a static icon object.md file, rather than a dynamic    
memory object.    
To create an `/icon object.md` object, simply use `new/icon object.md()`, or the short-cut    
`icon object.md()` proc. The following example loads an icon object.md file, reddens it, and    
then assigns it back to the player\'s icon object.md, which implicitly creates a    
new icon object.md file.    
### Example:    
mob/verb/test() var/icon object.md/I = new(\'player.dmi\') I.Blend(rgb(40,0,0))    
usr.icon object.md = I    
Note that merely displaying different icon object.md states or directions can    
generally be achieved without any icon object.md manipulation, which saves quite a    
bit of overhead. For example, the variables `atom.icon object.md_state` and    
`atom.dir` can be used to control how `atom.icon object.md` is displayed, without    
any need for generating a new icon object.md file.    
Many things that used to require icon object.md manipulation may not need you to    
do so anymore, as DM has evolved new capabilities.    
  ---------------------------------------------------------------------------------------------------------------------------------    
  Operation                `/icon object.md` proc                                      New method    
  ------------------------ ------------------------------------------------- ------------------------------------------------------    
  Multiplying by color     [`Blend`](/icon object.md/proc/Blend){.code} or            [color](/atom/var/color){.code} var    
                           [SetIntensity](/icon object.md/proc/SetIntensity){.code}       
                           procs                                                 
  Adding color             [Blend](/icon object.md/proc/Blend){.code} proc            [color](/atom/var/color){.code} var (using [color    
                                                                             matrix](/%7Bnotes%7D/color-matrix))    
  Applying color matrix    [MapColors](/icon object.md/proc/MapColors){.code} proc        
  Rotation                 [Turn](/icon object.md/proc/Turn){.code} proc              [transform](/atom/var/transform){.code} var    
  Flipping                 [Flip](/icon object.md/proc/Flip){.code} proc                  
  horizontal/vertical                                                            
  Scaling                  [Scale](/icon object.md/proc/Scale){.code} proc                
  Overlaying/underlaying   [Blend](/icon object.md/proc/Blend){.code} proc +          Overlay/underlay +    
  another icon object.md             `ICON_OVERLAY`                                    [KEEP_TOGETHER](/atom/var/appearance_flags){.code}\    
                                                                             [Layering filter](/%7Bnotes%7D/filters/layer)    
  ---------------------------------------------------------------------------------------------------------------------------------    
Note: Anything you can do with an atom var instead of using icon object.md    
manipulation procs will usually perform much better. Games that use the    
new methods use fewer resources, use less memory, and also usually look    
better too.  