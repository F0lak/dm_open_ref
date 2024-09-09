[]{#/{skin}/param/is-fullscreen}
  ## is-fullscreen parameter (skin) {#is-fullscreen-parameter-skin byondver="515"}
  **See also:**
  :   [can-resize parameter](ref/%7Bskin%7D/param/can-resize)
  :   [titlebar parameter](ref/%7Bskin%7D/param/titlebar)
  :   [is-maximized parameter](ref/%7Bskin%7D/param/is-maximized)
  :   [is-minimized parameter](ref/%7Bskin%7D/param/is-minimized)
  :   [size parameter](ref/%7Bskin%7D/param/size)
  :   [outer-size parameter](ref/%7Bskin%7D/param/outer-size)
  :   [screen-pos parameter](ref/%7Bskin%7D/param/screen-pos)
  :   [screen-size parameter](ref/%7Bskin%7D/param/screen-size)
  <!-- -->
  **Applies to:**
  :   [Main](ref/%7Bskin%7D/control/main) (window only)
  <!-- -->
  **Format:**
  :   true/false
  <!-- -->
  **Default value:**
  :   false
  True if the window should be in fullscreen mode. This suppresses
  `can-resize`, `titlebar`, `is-maximized`, and `is-minimized`. They will
  continue to return the values that would apply if fullscreen mode were
  turned off.