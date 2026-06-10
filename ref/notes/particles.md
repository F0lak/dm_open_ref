
## particles (info)
***
A particle set is a special effect, whose computations are handled entirely on the client, that spawns and tracks multiple pixels or icons with a temporary lifespan. Examples of this might be confetti, sparks, rocket exhaust, or rain or snow. Particles are rendered on a special surface and that gets attached to an obj or a mob like an overlay.

Particles can exist in 3 dimensions instead of the usual 2, so a particle's position, velocity, and other values may have a z coordinate. To make use of this z coordinate, you can use a <a href="#/{notes}/projection-matrix">projection matrix</a>. (The value of the z coordinate must be between -100 and 100 after projection. Otherwise it's not guaranteed the particle will be displayed.)

To create a particle set, use `new` to create a new `/particles` datum, and then you can set the datum's vars. The vars can be set to constant values, or generator functions that will allow the client to choose from a range of values when spawning those particles. (The easiest way to handle this is to create your own type that inherits from `/particles`, and set up the parameters you'll want at compile-time.)

After the datum is created, it can be assigned to an obj or mob using their `particles` var. The particles will appear on the map wherever that obj or mob appears.


```dm

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


These are the vars that can be used in a particle set. "Tick" refers to a BYOND standard tick of 0.1s.
***