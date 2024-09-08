[]{#/atom/var/pixel_z}
## pixel_z var (atom)
**See also:**
:   [animate_movement var (movable
    atoms)](#/atom/movable/var/animate_movement)
:   [glide_size var (movable atoms)](#/atom/movable/var/glide_size)
:   [pixel_x var (atom)](#/atom/var/pixel_x)
:   [pixel_y var (atom)](#/atom/var/pixel_y)
:   [pixel_w var (atom)](#/atom/var/pixel_w)
:   [icon_size var (world)](#/world/var/icon_size)
:   [map_format var (world)](#/world/var/map_format)
<!-- -->
**Default value:**
:   0
This displaces the object\'s icon vertically by the specified number of
pixels. This is meant to be used in situations where world.map_format is
used to display something other than a top-down form, for instance in an
isometric or side-view display. In a top-down mode pixel_z behaves the
same as pixel_y, except that it does not rotate with changes to
client.dir.
This effect is purely visual and does not influence such things as
movement bumping or view() range calculations.