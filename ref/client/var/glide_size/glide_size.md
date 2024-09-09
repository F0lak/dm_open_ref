[]{#/client/var/glide_size}
  ## glide_size var (client) {#glide_size-var-client byondver="490"}
  **See also:**
  :   [eye var (client)](ref/client/var/eye)
  :   [glide_size var (movable atoms)](ref/atom/movable/var/glide_size)
  <!-- -->
  **Default value:**
  :   0
  Note: The way this setting is used depends on
  [world.movement_mode](ref/world/var/movement_mode). See
  [Gliding](ref/%7Bnotes%7D/gliding) for more details.
  This controls the number of pixels the map is moved in each step during
  scrolling of the map. The default value of 0 chooses automated control
  over this value, which generally results in a minimum step of 4 pixels
  that is increased when necessary to keep up with motion of the map.
  Be careful about using small step sizes. Icons with high contrast
  pixel-level detail can look pretty ugly when displaced by short
  distances.
  This was renamed from `pixel_step_size`.