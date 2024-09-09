[]{#/world/var/view}
  ## view var (world)
  **See also:**
  :   [lazy_eye var (client)](ref/client/var/lazy_eye)
  :   [show_map var (client)](ref/client/var/show_map)
  :   [view proc](ref/proc/view)
  :   [view var (client)](ref/client/var/view)
  <!-- -->
  **Default value:**
  :   5
  <!-- -->
  **Possible values:**
  :   -1 to 34 or \"WIDTHxHEIGHT\"
  This is the default map viewport range. The default value of 5 produces
  an 11x11 viewport. A value of -1 turns off the map display altogether.
  The client may automatically scale down icons in order to conveniently
  fit the map on the player\'s screen.
  For non-square views, you can assign this to a text string of the form
  \"WIDTHxHEIGHT\". For example, \"11x11\" is equivalent to a view depth
  of 5, but you could make it wider like this: \"13x11\".
  This setting also affects the default range of the `view()`, `oview()`,
  `range()`, and `orange()` procedures.
  If the entire map is small enough to fit on one screen (arbitrarily
  defined to be 21x21 or less), the default `view` is automatically
  adjusted to fit the map. In this case, `client.lazy_eye` is also
  automatically turned on by default, since you probably don\'t want the
  map to scroll around.