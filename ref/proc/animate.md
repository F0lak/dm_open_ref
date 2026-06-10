
## animate (proc)

**Format:**
+   animate(Object, var1=new_value1, var2=new_value2, ..., time, loop, easing, flags, delay, tag, command)
+   animate(Object, appearance=new_appearance, time, loop, easing, flags, delay, tag, command)
+   animate(Object)

**Arguments:**
+   Object: The atom, image, or client to animate; omit to add another step to the same sequence as the last  call
+   var1=new_value1, var2=new_value2, ...: Vars to change in the animation step
+   var_list: An associative list of vars to change
+   appearance: New appearance to use instead of multiple var changes (must be a ) [named arguments (proc)](/ref/proc/arguments/named)
+   time: Time of this step, in 1/10s (may be a ) [named arguments (proc)](/ref/proc/arguments/named)
+   loop: Number of times to run this sequence, or -1 to loop forever (may be a named argument)
+   easing: The "curve" followed by this animation step (may be a ) [named arguments (proc)](/ref/proc/arguments/named)
+   flags: Flags that impact how the animation acts (may be a ) [named arguments (proc)](/ref/proc/arguments/named)
+   delay: Delay time for starting the first step in a sequence (may be negative; may be a ) [named arguments (proc)](/ref/proc/arguments/named)
+   tag: Optional name for a new animation sequence (must be a ) [named arguments (proc)](/ref/proc/arguments/named)
+   command: Optional  to run at the end of this step [Client commands](/ref/{skin}/commands)
***
**Step:** A piece of an animation that transitions from the old appearance to a new appearance, in a given time.

**Sequence:** One or more steps in an animation. A sequence may loop a certain number of times, but requires more than one step for the loop to be meaningful.

**Parallel:** Multiple sequences can run concurrently if they are flagged as parallel. A parallel animation animates only the relative changes from the appearance that started the sequence.

**Supersede:** If a new animation sequence is not flagged as parallel, it will freeze the previous animation at its current point and animate any changes from there. The previous sequences are superseded, and will eventually be discarded.

This proc creates an **animation step**, which may be the start of a **sequence** of multiple steps, that will be displayed to players. Starting with an atom or image, you can change one or more vars that affect its apprearance. This change will take place immediately, but will be displayed to users as a gradual change over a period of time. The actual interpolation between frames is all done on the client.

If the `Object` argument is left out, a new animation step will be created for the previously used animation seqeunce. If all other arguments besides the object are left out, the animation is stopped completely.


```dm

mob/proc/GrowAndFade()
    // expand (scale by 2x2) and fade out over 1/2s
    animate(src, transform = matrix()*2, alpha = 0, time = 5)

obj/spell/proc/Spin()
    // cast a spell on a monster: make the icon spin
    // this animation takes 3s total (6 ticks * 5)
    animate(src, transform = turn(matrix(), 120), time = 2, loop = 5)
    animate(transform = turn(matrix(), 240), time = 2)
    animate(transform = null, time = 2)

```


The following vars will animate smoothly:

These vars can be changed, but will change immediately on each step rather than smoothly:

Other vars may apply:

For convenience, you can use an <a href="#/list/associations">associative list</a>, appearance, or <a href="#/mutable_appearance">mutable appearance</a> in place of the appearance vars. You can use `appearance` itself as a name for this argument, or leave the argument unnamed.

An animation step doesn't have to be strictly linear. Some changes look much better if they follow a curve. A cubic curve, for instance, will start slow, accelerate very quickly in the middle, and slow down again at the end. A sine curve could be used with a flip transformation to make a coin appear to spin. A text bubble can jump into place and bounce a little before it settles. The choice of curve you use is called easing, and you have several good choices to pick from. <script> function easing(t,ease,doubled) { var _in=(ease&64), _out=(ease&128), b; ease &= 63; t = Math.max(0,Math.min(1,t)); // clamp t if(!ease) return t; // linear case, simplest of all if(!_in && !_out) { // default case switch(ease) { case 4: case 5: case 8: _out = true; break; // bounce, elastic, jump default: _in = _out = true; break; // all other cases } } if(_in && _out) { if(ease == 8) return t <= 0.5 ? 0 : 1; // jump is a special case return ((t <= 0.5) ? easing(t*2,ease|64,true) : easing(t*2-1,ease|128,true)+1) / 2; } if(_in) return 1-easing(1-t,ease|128,doubled); switch(ease) { // all out cases case 1: // sine return Math.sin(t*Math.PI/2); case 2: // circular t = 1-t; return Math.sqrt(1 - t*t); case 3: // cubic t = 1-t; return 1 - t*t*t; case 4: // bounce b = t*2.75; if(b<1) return b*b; // 1st arc if(b<2) {b-=1.5; return b*b + 0.75;} // bounce #1 if(b<2.5) {b-=2.25; return b*b + 0.9375;} // bounce #2 b-=2.625; return b*b + 0.984375; // final bounce case 5: // elastic return 1 - Math.pow(2,-10*t) * Math.cos(t*Math.PI/0.15); case 6: // back b = doubled ? 2.59491 : 1.70158; t = 1-t; return 1 - t*t*((b+1)*t - b); case 7: // quad t = 1-t; return 1 - t*t; case 8: // jump return (t<1) ? 0 : 1; default: return t; } } function drawEasing() { var canvas = document.querySelector('#easing_canvas'); var ease = document.querySelector('#easing_type').value; if(document.querySelector('#ease_in').checked) ease |= 64; if(document.querySelector('#ease_out').checked) ease |= 128; var ctx=canvas.getContext("2d"), t, y, w=ctx.canvas.width, h=ctx.canvas.height, margin=5, miny=0, maxy=1, s; ctx.fillStyle = 'white'; ctx.fillRect(0,0,w,h); ctx.fillStyle = 'transparent'; w -= margin*2+1; h -= margin*2+1; for(x=0,y=[]; x<=w; ++x) { y[x] = easing(x/w,ease); if(y[x] < miny) miny = y[x]; else if(y[x] > maxy) maxy = y[x]; } s = h / (maxy-miny); ctx.beginPath(); ctx.setLineDash([3,3]); ctx.strokeStyle = 'rgba(0,128,0,0.5)'; ctx.strokeWidth = 1; ctx.moveTo(margin, margin+h+miny*s); ctx.lineTo(margin+w, margin+h+miny*s); ctx.stroke(); ctx.beginPath(); ctx.strokeStyle = 'rgba(0,128,255,0.5)'; ctx.moveTo(margin, margin+(maxy-1)*s); ctx.lineTo(margin+w, margin+(maxy-1)*s); ctx.stroke(); ctx.beginPath(); ctx.setLineDash([]); ctx.strokeStyle = 'black'; ctx.moveTo(margin, margin+h+miny*s); for(x=1; x<=w; ++x) ctx.lineTo(margin+x, margin+h+(miny-y[x])*s); ctx.stroke(); } </script>

In this play area, you can test different easing functions to see how they work.

The horizontal axis from left to right represents the time of the animation from beginning to end. The vertical axis, from bottom to top, is how the animation will be interpolated; the lower green line represents the starting appearance, and the upper blue line is the ending appearance.

These can be combined with `EASE_IN` or `EASE_OUT` using the `|` operator, to use just the first or last part of the curve.


```dm

obj/coin/proc/Spin()
    var/matrix/M = matrix()
    M.Scale(-1, 1)  // flip horizontally
    animate(src, transform = M, time = 5, loop = 5, easing = SINE_EASING)
    animate(transform = null, time = 5, easing = SINE_EASING)

obj/speech_bubble/New(newloc, msg)
    icon = 'bubble.dmi'

    var/obj/O = new
    O.maptext = msg
    O.maptext_width = width
    O.maptext_height = height
    overlays = O

    // start below final position and jump into place
    pixel_z = -100
    alpha = 0
    animate(src, pixel_z = 0, alpha = 255, time = 10, easing = ELASTIC_EASING)

```


Some easing functions may overshoot one line or the other, so it's fully possible to have a `pixel_w` value, for instance, animate from 0 to 100 but actually end up briefly outside of that range during the animation.

Any combination of these flags may be used for animation (use `+` or `|` to combine them):

<a href="#/{notes}/filters">Filters</a> can be animated too. If you want to animate a filter, you need to specify the filter to be animated. If the last call to `animate()` used the same object as this filter, or a different filter for that object, then this will be treated as a new step in the same animation sequece. Likewise, if the last `animate()` call was to a filter, and this call is for the object that filter belonged to, again it will be treated as a continuation of the sequence.


```dm
atom/proc/BlurFade()
    filters += filter(type = "blur", size = 0)
    // Animating a filter of src
    animate(filters[filters.len], size = 5, time = 10)
    // Switching back to src to animate the next step
    animate(src, alpha = 0, time = 2.5)

```


The `tag` argument allows you to refer to an animation sequence by name. This is useful for being able to replace or stop a previous animation sequence with the same name, but leaving other parallel sequences alone.

The `ANIMATION_PARALLEL` flag is always implied when using a named sequence. However, a named sequence will always supersede an earlier sequence with the same name, so you can't have two sequences with the same name running concurrently.

Stopping a named sequence is as simple as calling `animate(Object, tag=name)` with no other arguments.

If the `command` argument is present, a command will run on the client when this step ends. If this is part of a looping sequence, it will run each time. (If for any reason an entire loop runs in between client ticks, those loops will be ignored.)

The purpose of this is to synchronize events on the client, such as the <a class="code" href="#/{skin}/commands/%2esound">.sound</a> command, that otherwise couldn't be matched to the animation.

Using `[[*]]` in the command will expand it to a reference to the object being animated. (If this is a filter, it references the object that owns the filter.) The reference will be in the same format output by <a class="code" href="#/proc/ref">ref()</a>, without quotes.


```dm

obj/bouncing_ball/New()
    // this is only here to ensure the sound is included in resources
    var/static/bounce = 'bounce.ogg'
    var/sound_command = @".sound 'bounce.ogg' atom=[[*]] transform=1,0,0,0,0.707,0.707,0,0,0 falloff=10"

    animate(src, pixel_z=16, easing=QUAD_EASING|EASE_OUT, time=5, loop=-1)
    animate(pixel_z=0, command=sound_command, easing=QUAD_EASING|EASE_IN, time=5)

```

***
**Related Pages:**
+    [vars (atom)](/ref/atom/var)
