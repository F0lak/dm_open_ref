
## renderer (info)
***
To get the most out of BYOND's visual effects, it helps to understand how the map is displayed.

Every atom has an <a href="#/atom/var/appearance">appearance</a> that holds all of its visual info (and sometimes a little non-visual info). This appearance has to be turned into sprites in order to be rendered.

Although many atoms need little more than a simple <a class="code" href="#/atom/var/icon">icon</a> and <a class="code" href="#/atom/var/icon_state">icon_state</a> and produce only a single sprite, some are more complex with overlays, underlays, maptext, etc. Also there may be <a href="#/image">image objects</a> and <a href="#/atom/var/vis_contents">visual contents</a> involved, although they're not part of the atom's appearance.

For a simple `icon` and `icon_state`, just one sprite is generated. The client looks up the icon it's given. Then it looks up an icon state, which may be influenced by whether the atom is moving or not since you can have moving and non-moving icon states. Then it determines which <a href="#/atom/var/dir">direction</a> to draw and which frame of the icon's animation (if any) to use.

So with several simple icons, and not worrying about layers for now, a list of sprites lays out like this:

Now let's consider what happens when an appearance has overlays.

The <a class="code" href="#/atom/var/underlays">underlays</a> list is processed first, then <a class="code" href="#/atom/var/overlays">overlays</a>. These lists contain appearances themselves, rather than actual atoms. This means that overlays are recursive: an overlay can have overlays itself. To picture how that works, just replace one of the overlays above with another list.

Any atom can have an <a href="#/image">image object</a> attached, which can be shown to only specific players. Most atoms, and image objects, can have <a href="#/atom/var/vis_contents">visual contents</a> that display other atoms as if they're overlays.

As you see this is very similar to overlays. Just like overlays, image objects and visual contents have appearances of their own (and may also have their own images or visual contents), so this may be recursive as they add new overlays, etc.

A couple of things to keep in mind:

Any appearance may have <a class="code" href="#/atom/var/maptext">maptext</a> attached. That maptext draws above the icon but is grouped with it. That grouping will be discussed further below.

Particle effects also get grouped with the main icon in a similar way to maptext.

For simplicity, from this point forward the diagram will just treat underlays, overlays, image objects, and visual contents as overlays.

An appearance's <a class="code" href="#/atom/var/color">color</a> and <a class="code" href="#/atom/var/alpha">alpha</a> vars (from here forwarded they'll just be referred to by `color`) and <a class="code" href="#/atom/var/transform">transform</a> are inherited by any overlays, which also includes images and visual contents. You can avoid that inheritance by giving those overlays special <a class="code" href="#/atom/var/appearance_flags">appearance_flags</a>: `RESET_COLOR`, `RESET_ALPHA`, and `RESET_TRANSFORM`.

The appearance's filters are only applied to the main icon.

When `color` and `transform` are inherited, they "stack". The inherited color and transform values are applied after those of the overlays.

There are times it's desirable for an appearance and all its overlays to be treated as a single unit so any colors or filters can be applied all at once. One simple example is if the appearance has an `alpha` of 128 to make it translucent, you probably want to draw the whole atom faded instead of drawing each sprite faded, one on top of the other.

By using the `KEEP_TOGETHER` value in <a class="code" href="#/atom/var/appearance_flags">appearance_flags</a> (called KT for short), an appearance will group all of its underlays and overlays together. If this is an atom with image objects and visual contents, those will be grouped with it as well.

With `KEEP_TOGETHER` all of these sprites are rendered to a temporary drawing surface, and then the main appearance's `color`, `transform`, and `filters` are all applied to the combined drawing. This comes with a trade-off, since you can no longer use flags such as `RESET_COLOR` to opt out of inheritance.

If an overlay doesn't want to be part of a KT group, it can use the `KEEP_APART` flag (KA for short). If there are multiple nested KT groups, KA will only escape the innermost group.

If an overlay inside a KT group has a different <a class="code" href="#/atom/var/plane">plane</a> than the group's owner, it will be separated as if it defined `KEEP_APART`, except it can escape multiple nested groups.

Any appearance can have a <a class="code" href="#/atom/var/layer">layer</a> or <a class="code" href="#/atom/var/plane">plane</a>, and these influence how it gets sorted. (There's also a concept called a "sub-plane" that's influenced by whether an atom is a <a href="#/{notes}/HUD">HUD/screen object</a> or special layers like <a class="code" href="#/{notes}/BACKGROUND_LAYER">BACKGROUND_LAYER</a>.)

If a sprite is created with `FLOAT_LAYER` (any negative value counts as a floating layer) its layer has to be resolved, or "unfloated". The main sprite for an atom can never float; it has to have a real layer. Its overlays and underlays with floating layers will reorder themselves in numerical order, then look for the next closest sprites in the rendering list that has a non-negative layer.

A similar process happens with `FLOAT_PLANE`. Planes can have negative values but `FLOAT_PLANE` and the values close to it are special. Sprites with floating planes have to resolve those as well.

Once all atoms that will appear on the map are assembled into a rendering list of sprites, the order in which they're rendered on the map is determined in this order:

In a typical topdown map, `layer` is basically all that matters after the plane and subplane are taken into account. There is a legacy concept called micro-layers that helps break ties between sprites with the same layer; for instance if an atom is moving it's usually desirable to draw it above other atoms with the same layer; this applies only to topdown maps.

Sometimes it's helpful to group multiple sprites on one plane as if the plane itself were a KT group. For this, <a class="code" href="#/atom/var/appearance_flags">appearance_flags</a> has a value called `PLANE_MASTER`. An object with this flag will act as a "parent" for everything else on the plane. All other sprites on the plane will be grouped together and rendered on a temporary drawing surface, and then the plane master's `color`, `transform`, and `filters` will be applied.

A plane master does not, however, get an icon or maptext of its own; they're simply ignored. It can have overlays added to the group.

There are other topics not covered in this article, such as <a href="#/atom/var/render_target">render targets</a> and special map formats. Any details on how those features impact rendering are discussed in their own articles.
***