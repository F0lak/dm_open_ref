
## hub (var)
***
This is a registered <a href="http://www.byond.com/hub/">BYOND hub</a> path. The default value of null is for unregistered games. Registered games (don't worry, it's free!) have their own hub page showing a brief description of the game, the author, an optional installation package, and links to online games. The hub path is a string of the form "YourName.GameName" and can be found in your <a href="https://secure.byond.com/members/?command=edit_hub">hub console</a>.

Even unregistered games show up in the hub when they are live (that is online with people connected). It just doesn't show any of the extra info like a description, and there is no way for people to find out about it when nobody is logged in.

If you do not want your game to show up in the hub (like while you are in the initial stages of development), just compile with <code>visibility=0</code>. Either that, or turn off your pager or your BYOND locator when you are connected to it.

You (or the players) might also wish to turn off the notice of a live game in the hub when there is no longer any room for new players or if it is too late in the game for new people to join. At such times, you can simply set the visibility to 0.


```dm

world
   hub = "Dan.PipeStock"   //registered hub path

mob/verb/start_game()
   world.visibility = 0
   //...

```


If you configure your hub page to require a hub password, you must also specify <code>world.hub_password</code>.
***