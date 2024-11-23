## Understanding SendMaps

To efficiently build multiplayer games in BYOND, it helps to understand how
map updates are sent to clients.

Every server tick, SendMaps determines what visual information needs to be sent to
each client. It interfaces with BYOND's appearance system to track changes to
icon, icon_state, overlays, underlays, vis_contents, and other visual properties.
It doesn't send the entire map every tick - instead, it tracks what has changed
and only sends updates for those changes.

The update process happens in several stages, each building on the previous one:

### Client Movement and Bounds
When a client's mob moves or map boundaries change, that information is sent immediately. This includes changes to:
- view range.
- screen_loc.
- map boundaries.
- current position.

### Turf Updates
The server then looks at turfs in the client's view range:
- Full list (if the client hasn't moved).
- Partial list (if the client has moved).
- No update (if nothing has changed).
- Individual turf appearances changes including vis_contents and overlays / underlays.

### Movable Processing
After turfs are handled, the system processes all movable atoms in view range:
- New movables that entered view.
- Old movables that left view.
- Movement changes.
- Appearance changes (icon, overlays, vis_contents, etc.).
- Invisibility changes.

### Visual Content Resolution
Finally, the system does a recursive scan of:
- vis_contents for all visible objects.
- overlays and underlays.
- screen objects (HUD elements).
- maptext and filters.
- image objects.

> [!Note]
> With a typical update cycle, the data sent might look like this:
> + Movement data.
> + Changed turfs and their appearances.
> + Changed movables and their visual states.
> + Visual contents updates including nested vis_contents.
> 
> This can get more complex when dealing with nested contents.
> For example, if a movable contains other objects:
> + Movement data
> + Changed turfs
> + Movable #1
>   + vis children of movable
>   + overlays and visual effects
> + Movable #2
>   + vis children of movable
>   + overlays and visual effects
> + Visual contents updates

### Threading
The scanning process used to be entirely serial, but now it can be broken into threads using cfg/daemon.txt.
This dramatically reduces the performance impact of these regular scans.

> [!TIP] 
> **See also:**
> +   [view var (client)](/ref/client/var/view.md)
> +   [screen var (client)](/ref/client/var/screen.md)
> +   [appearance var (atom)](/ref/atom/var/appearance.md)
> +   [vis_contents var (atom)](/ref/atom/var/vis_contents.md)
> +   [Server Ticks](/ref/notes/server-ticks.dm)
> +   [Understanding the renderer](/ref/notes/renderer.md)
