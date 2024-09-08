[]{#/icon/proc/Flip}
## Flip proc (icon)
**See also:**
:   [Turn proc (icon)](#/icon/proc/Turn)
:   [dir var (atom)](#/atom/var/dir)
:   [icon](#/icon)
:   [procs (icon)](#/icon/proc)
<!-- -->
**Format:**
:   Flip(dir)
<!-- -->
**Args:**
:   dir: direction in which to flip over the icon
This flips the icon over in the specified direction. For example,
Flip(NORTH) would be like turning the icon upside down by grabbing the
bottom edge and flipping it up over the top edge. You would get the same
result by doing Flip(SOUTH). In general, this is not the same as turning
the icon by 180 degrees, because it produces a mirror image.
If an icon is square, it may be flipped diagonally.