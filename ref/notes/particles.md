## Particle effects 
###### BYOND Version 514



A particle set is a special effect, whose computations are
handled entirely on the client, that spawns and tracks multiple pixels
or icons with a temporary lifespan. Examples of this might be confetti,
sparks, rocket exhaust, or rain or snow. Particles are rendered on a
special surface and that gets attached to an obj or a mob like an
overlay. 

Particles can exist in 3 dimensions instead of the
usual 2, so a particle\'s position, velocity, and other values may have
a z coordinate. To make use of this z coordinate, you can use a
[projection matrix](/ref/notes/projection-matrix.md) . (The value of the
z coordinate must be between -100 and 100 after projection. Otherwise
it\'s not guaranteed the particle will be displayed.) 

To create
a particle set, use `new` to create a new `/particles` datum, and then
you can set the datum\'s vars. The vars can be set to constant values,
or generator functions that will allow the client to choose from a range
of values when spawning those particles. (The easiest way to handle this
is to create your own type that inherits from `/particles`, and set up
the parameters you\'ll want at compile-time.) 

After the datum
is created, it can be assigned to an obj or mob using their `particles`
var. The particles will appear on the map wherever that obj or mob
appears.
### Example:

``` dm
particles/snow
    width = 500     // 500 x 500 image to cover a moderately sized map
    height = 500
    count = 2500    // 2500 particles
    spawning = 12    // 12 new particles per 0.1s
    bound1 = vector(-1000, -300, -1000)   // end particles at Y=-300
    lifespan = 600  // live for 60s max
    fade = 50       // fade out over the last 5s if still on screen
    // spawn within a certain x,y,z space
    position = generator("box", vector(-300,250,0), vector(300,300,50))
    // control how the snow falls
    gravity = vector(0, -1)
    friction = 0.3  // shed 30% of velocity and drift every 0.1s
    drift = generator("sphere", 0, 2)
obj/snow
    screen_loc = "CENTER"
    particles = new/particles/snow

mob
    proc/CreateSnow()
        client?.screen += new/obj/snow
```
 

> [!IMPORTANT]
> These are the vars
that can be used in a particle set.\
> "Tick" refers to a BYOND standard
tick of 0.1s.\
> 
> The following vars are ignored if no `icon` is specified:
> - grow
> - spin

  ### Particle vars that affect the entire set (generators are not allowed for these)                                                  
  | Var | Type | Description |
  | --- | --- | --- |
  | width | num | Size of particle canvas in pixels.  Particles will not render outside this canvas |
  | height | num | Size of particle canvas in pixels.  Particles will not render outside this canvas |
  | count | num | Maximum particle count |
  | spawning | num |  Number of particles to spawn per tick (can be fractional) |
  | bound1 | vector | Minimum particle position in x,y,z space; defaults to list(-1000,-1000,-1000) |
  | bound2 | vector | Maximum particle position in x,y,z space; defaults to list(1000,1000,1000) |
  | gravity | vector | Constant acceleration applied to all particles in this set (pixels per squared tick) |
  | gradient | [color gradient](/ref/notes/color-gradient.md) | Color gradient used, if any |
  | transform  | [matrix](/ref/notes/projection-matrix.md) | Transform done to all particles, if any (can be higher than 2D) |

  ### Vars that apply when a particle spawns
  | Var | Type | Description |
  | --- | --- | --- |                                                     
  | lifespan | num | Maximum life of the particle, in ticks |
  | fade | num | Fade-out time at end of lifespan, in ticks |
  | fadein | num | Fade-in time, in ticks |
  | icon | icon | Icon to use, if any; no icon means this particle will be a dot<br> Can be assigned a weighted list of icon files, to choose an icon at random |
  | icon_state | text | Icon state to use, if any <br>Can be assigned a weighted list of strings, to choose an icon at random |
  | color | num or color | Particle color (not a color matrix); can be a number if a gradient is |
  | color_change | num | Color change per tick; only applies if gradient is used |
  | position | num | x,y,z position, from center in pixels |
  | velocity | num | x,y,z velocity, in pixels |
  | scale | vector (2D) | Scale applied to icon, if used; defaults to list(1,1) |
  | grow | num | Change in scale per tick; defaults to list(0,0) |
  | rotation | num | Angle of rotation (clockwise); applies only if using an icon |
  | spin | num | Change in rotation per tick |
  | friction | num | Amount of velocity to shed (0 to 1) per tick, also applied to acceleration from drift |

  ### Vars that are evalulated every tick   
  | Var | Type | Description |
  | --- | --- | --- |                                                     
  | drift | vector | Added acceleration every tick; e.g. a circle or sphere generator can be applied to produce snow or ember effects |

The `icon` and `icon_state` values are special in that they
can\'t be assigned a generator, but they can be assigned a constant icon
or string, respectively, or a list of possible values to choose from
like so: 
``` dm
icon = list('confetti.dmi'=5, 'coin.dmi'=1)
```

The list used can either be a simple
list, or it can contain weights as shown above. 

Changing a var
on a particle datum will make changes to future particles. For instance,
you can set the datum\'s `spawning` var to 0 to make it stop creating
new particles. (Note: If you are changing a vector or color matrix, such
as `gravity`, you need to assign a new value. You can\'t for instance
set `particles.gravity[2] = 0` because it won\'t do anything to update
the particle stream.) 

The same particle datum can be assigned
to more than one movable atom. However the particles displayed by each
atom will be different.

> [!TIP] 
> **See also:**
> +   [particles (movable atom var)](/ref/atom/movable/var/particles.md) 
> +   [Generators](/ref/notes/generators.md) 
> +   [generator proc](/ref/proc/generator.md) 
> +   [Projection matrix](/ref/notes/projection-matrix.md) 
> +   [stddef.dm file](/ref/appendix/stddef%2edm.md) 
