[]{#/world/var/hub}
  ## hub var (world)
  **See also:**
  :   [hub_password var (world)](ref/world/var/hub_password)
  :   [name var (world)](ref/world/var/name)
  :   [status var (world)](ref/world/var/status)
  :   [game_state var (world)](ref/world/var/game_state)
  :   [version var (world)](ref/world/var/version)
  :   [visibility var (world)](ref/world/var/visibility)
  <!-- -->
  **Default value:**
  :   null
  This is a registered [BYOND hub](http://www.byond.com/hub/) path. The
  default value of null is for unregistered games. Registered games
  (don\'t worry, it\'s free!) have their own hub page showing a brief
  description of the game, the author, an optional installation package,
  and links to online games. The hub path is a string of the form
  \"YourName.GameName\" and can be found in your [hub
  console](https://secure.byond.com/members/?command=edit_hub).
  Even unregistered games show up in the hub when they are live (that is
  online with people connected). It just doesn\'t show any of the extra
  info like a description, and there is no way for people to find out
  about it when nobody is logged in.
  If you do not want your game to show up in the hub (like while you are
  in the initial stages of development), just compile with `visibility=0`.
  Either that, or turn off your pager or your BYOND locator when you are
  connected to it.
  You (or the players) might also wish to turn off the notice of a live
  game in the hub when there is no longer any room for new players or if
  it is too late in the game for new people to join. At such times, you
  can simply set the visibility to 0.
  ### Example:
  world hub = \"Dan.PipeStock\" //registered hub path
  mob/verb/start_game() world.visibility = 0 //\...
  If you configure your hub page to require a hub password, you must also
  specify `world.hub_password`.