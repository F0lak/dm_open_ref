[]{#/atom/var/maptext}
## maptext var (atom) {#maptext-var-atom byondver="494"}
**See also:**
:   [maptext_width var (atom)](#/atom/var/maptext_width)
:   [maptext_height var (atom)](#/atom/var/maptext_height)
:   [maptext_x var (atom)](#/atom/var/maptext_x)
:   [maptext_y var (atom)](#/atom/var/maptext_y)
:   [overlays var (atom)](#/atom/var/overlays)
:   [image objects](#/image)
:   [pixel_x var (atom)](#/atom/var/pixel_x)
:   [pixel_y var (atom)](#/atom/var/pixel_y)
:   [pixel_w var (atom)](#/atom/var/pixel_w)
:   [pixel_z var (atom)](#/atom/var/pixel_z)
<!-- -->
**Default value:**
:   null
This is optional text that will be displayed in the same position as the
atom. If an atom has both an icon and maptext, the text will be
displayed in front of the icon. Usually however, this is something that
would be added to an overlay or image object, which can then be
positioned with pixel offsets.
Map text is constrained to the bounds set by maptext_width and
maptext_height, which default to a single icon in size. It can be offset
by maptext_x and maptext_y.
Text can use HTML and CSS, mostly the same limited subset supported by
regular text output, and different styles can be used in the same block
of text. In addition, alpha colors can also be used, by specifying a
color as #rrggbbaa instead of just #rrggbb. (Alpha transparency will be
ignored when the map is drawn without hardware rendering, so anything
below 50% opacity is not displayed in those cases.)
Maptext supports links with the `<a>` tag. Left-clicking on a link will
follow the link, but also generate other events such as `MouseDown` or
`Click`.