
## GetScores (proc)

**Format:**
+   number

**Arguments:**
+   x: Horiztonal direction and period of wave
+   y: Vertical direction and period of wave
+   size: Maximum distortion in pixels (defaults to 1)
+   offset: Phase of wave, in periods (e.g., 0 to 1)
+   flags: Defaults to 0; see below for other flags

**Returns:**
+   The key, if the scores were successfully updated; null otherwise.

**Called When:**
+   Called when a message is received from another server by using
    world.Export().  If a file is expected, world.Import() may be called to
    get it.  The return value of Topic() will be passed back to the remote
    server.

**Default Action:**
+   The topic "ping" returns a true value (number of players plus one),
     which may be useful for telling if a server is alive.  The topics
     "Reboot" and "Del" will call world.Reboot() and world.Del()
     respectively if the message was sent by the master server.

**Default Value:**
+   normal
***
Retrieves information about scores that is kept on the BYOND hub.

This proc will return null if there was no way to reach the hub. Use isnull() to check for a null value. Contacting the hub may take a few moments, so it is a good idea to use spawn() to avoid holding up the rest of the game.

In this form, you can get information about individual scores. This is the most common way to use GetScores().

The key is an arbitrary text value. Usually a player's key is a good choice, but you can also use the name of their character, or anything else you like, as long as it is unique. The key is case-insensitive.

Scores and stats use data fields, which might be things like "Score", "Level", "Class", etc. To retrieve all the fields associated with a key, leave the fields argument blank. To retrieve only certain fields, you can send a separated list like "Score;Level" which is in the same format returned by list2params().

If you leave the key argument blank, you will get a complete list of keys that have scores and stats associated with them.


```dm

mob/var/scores_found
mob/var/score = 0

mob/Login()
  ..()
  spawn()
    var/scores = world.GetScores(key)
    scores_found = !isnull(scores)
    if(scores)
      var/list/params = params2list(scores)
      if(params["Score"])
        score = text2num(params["Score"])
        src << "You have [score] point\s!"

```


In this form, the proc gets a list of the top scores for a certain field, and gives you the keys and scores in order. To get the top 10 players by level, for instance, you would use GetScores(10,"level"). This returns a parameter list with the top keys and scores, so it might be in a form like "Bob=100;Anita=80;David=20;Charlie=5".

The count and skip arguments are always numbers, not text. The count is the number of scores to retrieve, and skip is the number to skip over to get to them. So count=10 and skip=0 is the top 10, while count=10 and skip=5 is #6 through #15. If you leave out skip, it's a 0.

The way you set up your hub entry is how the top scores are determined. If you told the hub that the "score" field is always sorted from highest number to lowest, then that's what you'll get. If "birthplace" is set up to use an alphabetical order, that's the order that GetScores() will use. If a field cannot be sorted, this form of GetScores() will return an empty text string.

If you don't specify a field, your hub entry may have a default field to use. For instance if your hub page displays "Score", then "Level", then the "Score" field is the default.


```dm

mob/var/scores_found

mob/Login()
  ..()
  spawn()
    var/top_scores = world.GetScores(10, "Booty")
    scores_found = !isnull(scores)
    if(scores)
      var/list/params = params2list(scores)
      src << "Top Buccaneers:"
      for(var/i=1, i
Note: You can specify a different hub path and hub_password
by adding these as extra arguments, but this is not recommended for security
reasons. If you use this feature, it should only be on games that cannot be
downloaded by the public.



Import proc (world)




Example:

//sending the file
mob/proc/Export(Addr)
  var/savefile/F = new()
  F.Write(src)
  world.Export(Addr,F)

//receiving the file
world/Topic()
  var/savefile/F = new(world.Import())
  F.Read() //read the mob

This example defines a mob proc called Export() which writes the mob to a
savefile and sends it to another server (specified by Addr).  The remote
server opens it as a savefile and creates the mob (if the same mob type is
defined on both servers and mob.Read() is compatible with the sending
server's mob.Write()).

Note that another method of transferring player mobs is to use the key
savefile (accessed by client.Export() and client.Import()).  Direct server
to server communication on the other hand could transfer data (like
non-players) without the need for player involvement at all.

Savefiles are the most common type of file to transfer, but world.Import()
simply returns a reference to an item in the world's .rsc file, which could be
any type of file.  This particular example demonstrates how to open such a
file as a temporary savefile.  (It gets dumped from the cache into a separate
temporary file, which is then opened as a savefile.)  Other types of files
would be handled differently.  For example, you could use fcopy() to dump the
cached item to its own separate file.



IsBanned proc (world)




By default, this procedure checks the "ban" configuration file.  If an
entry is found for the current world (based on the value of world.hub), the
parameter text is converted into a list (using params2list()), and the result
is returned.  Otherwise, null is returned.

A ban that applies to all worlds on the host's computer will not call
IsBanned(). The connection will simply be denied.

This procedure is called internally whenever a new user connects (before
client/New() is called).  If the result is true, access is denied.  If you
want to ban a user but still allow them to log in (perhaps with reduced
functionality), you can put "Login=1" in the parameter text.  If you want to
display an explanation to the user about why they are banned, you can also put
"message=X" in the parameter text, where X is the message to display to the user.
A reason for the ban can be added with a "reason=X" field.  Of course, you can
also override IsBanned() and insert these values directly into the list that is
returned.

Example

world/IsBanned(key,address)
   . = ..()            //check the ban lists
   if(istype(., /list))
      .["Login"] = 1   //allow banned user to login

When you ban people from paging you, this also causes them to be added to
the keyban list.  Even if they are already connected, IsBanned() will be
re-evaluated and acted upon at that time.  When you remove pager ban, they are
removed from keyban as well.

Additional data elements may be added to the ban list in the future.
The current definition includes just the following items:


Since the data in the "ban" file is in
application/x-www-form-urlencoded format, it is
probably not desirable to edit the file by hand.  No built-in facilities for
editing the file have been provided (aside from automatic addition of pager
bans), but an interface could be created, using GetConfig
and SetConfig to read and write the data.
Extra features could also be added such as automatic inference of key
associations by IP address.



IsSubscribed proc (world)



Checks a player for their subscription status to this game. This is a
simpler alternative to client.CheckPassport(), which is deprecated,
and also allows you to check even when the player has gone offline.

This proc will return null if contacting the hub was required, but there
was no way to reach the hub. Contacting the hub may take a few moments, so it
is a good idea to use spawn() to avoid
holding up the rest of the game.

Example:

mob/verb/JoinClub()
    if(!world.IsSubscribed(src))
        src << "Sorry, the club is only for subscribers."
    else
        // go to the turf with the tag "clubhouse"
        loc = locate("clubhouse")
        src << "Welcome to the clubhouse!"

Note: You can specify a different hub path and hub_password
by adding these as extra arguments, but this is not recommended for security
reasons. If you use this feature, it should only be on games that cannot be
downloaded by the public.



New proc (world)





OpenPort proc (world)




This causes the world to be hosted on the specified network port.  A value
of 0 or "any" requests that any available port be used.  The value "none"
causes the port to be closed so that no new connections are possible.

This proc may be overridden. If it is, calling ..() is necessary to open
the port. If ..() is not called, it will not open.

Example:

world/OpenPort(port)
  // only allow subscribers to host
  if(host_is_subscribed)
    return ..()

The "ports" configuration option in cfg/byond.txt can be used to control
what ports worlds may open.  The -ports command-line option may also be used.
See startup for the syntax.



PayCredits proc (world)




Removes credits from a player's account, if they have enough. The proc
will return 1 if it is successful, or 0 if the attempt failed (usually
because the player doesn't have enough credits). This feature is intended
for games that make use of the credit system, and for security all such
games must use a hub password.

This proc will return null if there was no way to reach the hub. Use
isnull() to check for a null value. Contacting the hub may take a few
moments, so it is often a good idea to use spawn() to avoid holding up the
rest of the game.

Example:

mob/proc/ItemShop()
    var/items = list("Get credits!", "Magic sword"=10, "Skeleton key"=50)
    var/choices[0]
    var/item,price
    for(item in items)
        price = items[item]
        choices["[item]: [price] credit\s"] = item

    var/credits = world.GetCredits(key)
    if(isnull(credits))
        src << "Sorry, the item shop isn't available right now."
        return

    var/choice = input(src,\
      "You have [credits] credit\s. What would you like to purchase?",\
      "Item Shop")\
      as null|anything in choices
    if(!choice) return  // cancel

    if(choice == "Get credits")
        src << link("http://www.byond.com/games/Author/MyGame/credits")
        return

    item = choices[choice]
    price = items[item]
    if(!price) return

    src << "Contacting item shop..."
    var/result = world.PayCredits(name, price, "Item shop: [item]")

    if(isnull(result))
        src << "Sorry, the item shop isn't available right now."
    else if(!result)
        src << "You need [price-credits] more credit\s to buy [item]."
    else
        src << "You bought \a [item]!"

        // Now give the user the item and save their character
        // These procs are for you to define
        src.AddEquipment(item)
        src.SaveCharacter()

Note: You can specify a different hub path and hub_password
by adding these as extra arguments, but this is not recommended for security
reasons. If you use this feature, it should only be on games that cannot be
downloaded by the public.



Profile proc (world)



Interacts with the built-in server profiler without requiring the host to do
so via Dream Daemon, or an authorized player via Dream Seeker.

The command value is built from bitflags, so it can combine any of
these three values via the | operator:


These additional values are also defined for convenience:


Profiling procs
By default, data will be returned as a list. The first six values are the
column names: "name", "self", "total",
"real", "over", and "calls", corresponding to the
columns in the profiler. These are followed by the profile data for each proc,
with the data being in the same column order. E.g. the next six items
represent the first proc in the profile.

The optional format argument however can be used to return the
data in other formats. Currently the only accepted value is "json",
which will output the same data in JSON format.

SendMaps profile
Using "sendmaps" in the type argument will profile the
routines used to send map informaiton to players. Unlike the proc profiling
this only has three data columns: "name", "value", and
"calls". The value column might be a time or number value, depending
on what's being measured. 

The JSON format will include a unit property data that is not a
raw number, such as a time value.



Reboot proc (world)



Reload the world from scratch.  Any connected players will automatically
relogin.  This would be useful if you needed to recompile the world after
changing some code.

In a UNIX environment, you can cause a running server to reboot by
sending it the signal SIGUSR1.

If you override this proc, you must call ..() if you want the reboot to
complete normally.

For reboots initiated by Dream Seeker, usr will be the mob belonging to
the player who sent the command.



Repop proc (world)




SetConfig proc (world)



This command is for storing configuration information that is shared by
applications installed on the same system.  The configuration data is
accessed by specifying the configuration "set" and the parameter within that
set.

For more information, see GetConfig.



SetMedal proc (world)




Awards a medal to a player. The proc will return 1 if it is successful, or
0 if the medal was already awarded. If the world already knows this medal was
earned before, the hub will not be contacted.

This proc will return null if there was no way to reach the hub. Use
isnull() to check for a null value. Contacting the hub may take a few
moments, so it is a good idea to use spawn() to avoid holding up the rest of
the game.


Example:

mob/monster/dragon
   Die(mob/killer)  // assume Die() is a proc all mobs have
      spawn()
         if(ismob(killer) && killer.key)
            world.SetMedal("Dragon slayer", killer)

Note: You can specify a different hub path and hub_password
by adding these as extra arguments, but this is not recommended for security
reasons. If you use this feature, it should only be on games that cannot be
downloaded by the public.



SetScores proc (world)




Updates scores that are kept on the BYOND hub.

The key is an arbitrary text value. Usually a player's key is a good
choice, but you can also use the name of their character, or anything else
you like, as long as it is unique. The key is case-insensitive.

Scores and stats use data fields, which might be things like "Score",
"Level", "Class", etc. Use list2params() to set the fields that you want to
change. Fields that you do not include in the list will not be changed. A
field with a blank value will be deleted.

Sending an empty text string for the fields will erase the scores for that
key.

This proc will return null if there was no way to reach the hub. Use
isnull() to check for a null value. Contacting the hub may take a few
moments, so it is a good idea to use spawn() to avoid holding up the rest of
the game.

Example:

var/params

// Change the Score and Pet fields
params = list("Score"=123, "Pet"="Dog")
world.SetScores("Tom", list2params(params))

// Delete the Pet field
params = list("Pet"="")
world.SetScores("Tom", list2params(params))

// Delete Tom's scores entirely
world.SetScores("Tom", "")

Note: You can specify a different hub path and hub_password
by adding these as extra arguments, but this is not recommended for security
reasons. If you use this feature, it should only be on games that cannot be
downloaded by the public.



Tick proc (world)




This proc allows you to do any updates just before map info is sent out.
One possible use for this is to run a movement loop, or sync up any user
interface input that might have arrived and deal with it all at once.

Example:

world/Tick()
    for(var/client/C)
        if(C.mob?.move_dir)
            try
                step(C.mob, move_dir)
            catch
                // empty catch, just so a failed step won't break the loop

Note: The tick will not wait if this proc sleeps. It effectively has
set waitfor=0 already built in.
It's a good idea not to sleep in this proc or any of its callees at all,
since it will keep getting called every tick.



Topic proc (world)





Example:

world/Topic(T)
  if(findtext(T,"shout:") == 1)
    world << copytext(T,7)

This example allows other servers to send this server topic text of the
form "shout:msg" and will broadcast the message to all the players in this
world.

The Keys argument is either null, or a list of user keys. Any keys in the
list are logged in to the remote server.

Always validate the input in Topic() calls
to make sure it's correct and the query you're recieving is legitimate.



vars (world)
Built-in world vars:




address var (world)

This is the network address of the machine hosting the world.  If it
cannot be determined, it will be null.

The full network address of the world may be formed by concatenating the
world address and port: "byond://[address]:[port]".

In CGI mode, this is the web address of the world.

This is the local address only. If the world is hosted via a router, the
external IP address may be different. Use internet_address to find
the external address, if available.



area var (world)

This is the default area type to be placed on the map wherever no area is
specified.  A value of 0 turns off the default area.



byond_build var (world)

This is the build number (minor version) of BYOND being run by this server.
Typically this is not useful information, but it can come in handy when
diagnosing issues reported by players when hosting with a beta build.



byond_version var (world)

This is the version of BYOND at run-time.  A game designed to work around
known bugs in older versions could use this to adapt its behavior accordingly.



cache_lifespan var (world)


Number of days items that are not in use will be saved in the resource
cache (.rsc file).  Files uploaded by players are stored in the world's .rsc
file for future use.  If the file is not used for the specified amount of
time, it will be removed to save space.

Setting this value to 0 causes items to be saved for the current session
only.  This is used by the CGI library, because web browsers cannot make use
of server-side caches when uploading files anyway.

This value must be a whole number.



contents list var (world)


This is a list of every object in the world.  Objects in this list are in
no particular order.

Example:

proc/ListAreas(mob/M)
  var/area/A
  M << "Areas:"
  for (A in world.contents)
    M << A

This example displays a list of every area in existence.  As a convenient
short-hand, one may simply write for(A) or for(A in world) instead of the
full for(A in world.contents).



cpu var (world)

This is the percentage of a server tick that the server spends processing
running procs and the work of sending map information to players.  A value of 0
would indicate very little cpu usage.  A value of 100 would indicate full cpu
usage, which could mean that the server cannot complete all the necessary
computations during a tick to finish in time for the next tick.  In this case,
timed events (such as sleep) may take
longer than requested.

When deciding on a value for tick_lag, one could use this value to
determine if the CPU is fast enough to tick at a higher rate.

The map_cpu var is a subset of this, measuring only time used for
sending map information.



executor var (world)


This option is for direct execution of .dmb files in UNIX.
The most common use is for writing CGI programs that are executed by the web
server.

The first parameter in the executor text string is the path to
DreamDaemon.  The one listed above is the standard UNIX location.

Optional parameters may follow.  The most common are -CGI and -logself.

Example:

world/executor = "/usr/local/byond/bin/DreamDaemon -CGI -logself"

This example creates a CGI program to be executed by a web server.  It
puts its error output in the file projname.log.

All of this is configured for you when you include
html/CGI.dm from the html library.



fps var (world)


The value of world.fps defines the speed of the world in frames
(server ticks) per second. By default this is 10 fps, which is a good speed if
all objects move in full tiles. Higher values yield smoother results, but at a
cost to performance. Timing of many events may be limited by the system clock,
so fps values beyond 40 or 50 may cause unwanted effects like jitter
even for projects that are not very demanding in terms of performance.

For projects making use of pixel movement, higher fps is usually
desired. 40 seems to be a good value for general use, but in worlds that have
a large number of players, you may wish to lower the value and give players a
higher step_size per tick instead.

This var exists for convenience; it is calculated by 10 /
world.tick_lag. The value of world.tick_lag is actually more
accurate, but it is easier to think of world speed in terms of frames per
second. The actual tick rate has a resolution of 1 ms.

When reading world.fps, the result is always given as a whole
number to gloss over rounding error.

If you set client.tick_lag or client.fps to a value other
than 0, you can make the client tick at a different (usually faster) rate.



game_state var (world)


At runtime, this value may be changed to let the BYOND hub know about
certain changes in the game's status. An example for using this value is if
the number of players in the game gets too high and most new logins are
rejected, you can set game_state to 1 to let the hub know this server is
full.

The following values are accepted:


Note that this value does not affect how your world actually reacts to new
players logging in. It is only used by the hub and website.



host var (world)


If the information is made available by the pager, this will provide the
key of the world's host. If the host is not known, this value will be either
null or an empty string.



hub var (world)


This is a registered BYOND hub path.
The default value of null is for unregistered games.  Registered games (don't
worry, it's free!) have their own hub page showing a brief description of the
game, the author, an optional installation package, and links to online games.
The hub path is a string of the form "YourName.GameName" and can be found in your
hub console.

Even unregistered games show up in the hub when they are live (that is
online with people connected).  It just doesn't show any of the extra info
like a description, and there is no way for people to find out about it when
nobody is logged in.

If you do not want your game to show up in the hub (like while you are in
the initial stages of development), just compile with
visibility=0.  Either that, or turn off your pager or your BYOND
locator when you are connected to it.

You (or the players) might also wish to turn off the notice of a live
game in the hub when there is no longer any room for new players or if it is
too late in the game for new people to join.  At such times, you can simply
set the visibility to 0.

Example:

world
   hub = "Dan.PipeStock"   //registered hub path

mob/verb/start_game()
   world.visibility = 0
   //...

If you configure your hub page to require a hub password, you must also
specify world.hub_password.



hub_password var (world)


If world.hub is set, any live session of the game will be
attached to the specified BYOND Hub page.  Under the default settings,
any game can set world.hub and attach itself to any BYOND
Hub page.
To beef up security, you can set a hub password in your hub's
configuration page via the BYOND website.  This will ensure that
only authorized copies of your game can attach themselves to your
hub page when live.  Then simply copy that password into your code as
world.hub_password so that your game's live broadcast will
be accepted by the hub.
Example:

world
   hub = "Dan.PipeStock"   //registered hub path
   hub_password = "UPAggnJaeXmSBoKK"   //password for live game authentication

Note that for security reasons, reading this variable at runtime will
return a hashed version of the value that was set.


icon_size var (world)


This is the tile size that will be used as a default for icons in the
world. It can be set to a single number that represents both the width and
height, or you can use a format like "[width]x[height]" (such as "16x48") to
specify width and height separately.

This value affects several calculations, including icon operations and
gliding between turfs.

Note: If you do not use a square icon size and you are using a topdown map
format, you may experience display issues if setting client.dir
to EAST or WEST. A non-square tile with a topdown map format
will also interfere with pixel movement. For this reason, square sizes are
recommended when using any topdown-view map format.



internet_address var (world)

This is the network address of the machine hosting the world, as it is
seen by the outside network (from the Internet) and the hub.  If it cannot
be determined, it will be null.

The full network address of the world may be formed by concatenating the
world address and port: "byond://[address]:[port]".

This var exists because world.address may not be accurate if the
world is hosted on a machine behind a router using NAT. The value returned
by internet_address can be given to other players who wish to log
in.



log var (world)

Sending output to world.log may be useful for debugging purposes.  The
output goes to the same place run-time proc errors are displayed.

Example:

if(1+1 != 2)
  world.log << "Uh oh."

You can assign world.log to a file name or file() object to redirect output
to that file.  (There is also a command-line option to Dream Daemon that does
this.)

Example:

world.log = file("mylog.txt")



loop_checks var (world)

Setting this to 0 disables the very long loop protection.  By default,
loops in the code which undergo a very large number of iterations or
recursions are aborted (by crashing the proc).  This prevents the proc from
locking up the server for too long.

You may need to disable this feature if your code has some very long loops
in it.  Before doing that, make sure it's not infinitely long!  Your
program will utterly crash if it runs out of system stack space, which can
happen in a very deep or infinite recursion.

Note: The compiler will now generate a warning when you disable
loop_checks. It is not advisable to disable the check unless you're
trying to debug something, since you can cause the server to hang. Generally
if you have a loop so long it can cause the regular loop checks to freak out,
you need to make a change to the loop behavior anyway.



map_format var (world)



This value says how the world will display maps. In a normal overhead
tiled map the value is TOPDOWN_MAP for the top-down format. For older
games that predate this feature, the value is TILED_ICON_MAP.

If you use a map format other than top-down, the HUD will still use a
tile format like it would in top-down display. HUD objects are not projected
into whatever map_format you use and they are not affected by changing
client.dir. The size of the HUD is rounded up to the nearest number of full
screen tiles; the size of each tile is defined by world.icon_size.

Top-down format

(See more at Topdown maps.)

This is the default map format. Icons are drawn in a tile form and viewed
from overhead. In this layout, the layer assigned to each atom is very
important. The number of tiles shown is set by client.view or world.view.

Because this format is familiar and easy to understand, it is the default
setting. Most of the vars related to maps and atoms are designed and
documented with this format in mind.

Tiled icon format

(See more at Tiled icons.)

In BYOND 4.0 a new feature was introduced for using "big" icons, bigger than
the standard tile size, by splitting them up into states like "0,0", "1,0",
and so on. This functionality is no longer needed since BYOND now has the
ability to display icons in their natural size. Some games that were designed
before this, however, may still need to make use of this splitting feature
that breaks icons into smaller tile-sized pieces.

When an icon is broken into chunks, each state in the icon is given a
thumbail version of the full image, and then new states are added to show
each chunk. For instance if world.icon_size is the default 32×32, and
the icon is 64×64, then the "door" state would become a thumbnail of
the full door image while "door 0,0" (the lower left corner), "door 1,0",
"door 0,1", and "door 1,1" were created to show each smaller section of the
image. If the default "" state is broken into chunks, those chunks are just
named "0,0" and so on without a space.

This format is deprecated. It exists to support
older games and allow them to be compiled without causing them to break,
until they can be redesigned for one of the newer formats.

Isometric format

(See more at Isometric maps.)

If map_format is set to ISOMETRIC_MAP, the map is displayed in
isometric form. Isometric tiles are displayed in a foreshortened diagonal
perspective, where the "north" direction actually displays as northeast on
the player's screen, and "east" shows up as southeast. The value of
client.view or world.view is used to calculate the
minimum number of tiles to display, and extra tiles to each side will
be shown to fill in the corners.

In an isometric map, the tile width set in world.icon_size is the most
important factor. This should be a multiple of 4 for best results. The
minimum tile height is half that value, and any extra height is used to show
vertical structures that "stick up" off the map surface. When you draw an
isometric tile icon, start with a flattened diamond shape at the bottom that
is only half as high as it is wide.

Isometric maps behave differently during drawing than top-down maps. In
isometric, tiles that are nearer to the viewer's perspective are drawn in
front of tiles farther back, regardless of layer. Layers only count within an
individual tile. This means that if you want to have a vertical structure
"stick up" to partially hide something behind it, the icon sticking up should
always be on a tile forward from the one being partly covered. E.g. if you
have a wall taking up part of your tile, it needs to be at the "back" end of
the tile to properly hide anything on the tiles behind it.

The pixel_x and pixel_y values, step_x and
step_y values, and the gliding that happens when moving between
tiles, are based on the width set by world.icon_size. If you set
world.icon_size="64x128" to show tall buildings, only the 64 matters
for pixel offsets. Use pixel_w and pixel_z to adjust the
position of atoms (or the client) horizontally or vertically without respect
to client.dir or the map format.

Note: Offsets for x and y also affect the layering order used to draw
the icons. Any object with a pixel offset onto another tile is considered
part of whichever tile is closer.

If you use an icon wider than one tile, the "footprint" of the isometric
icon (the actual map tiles it takes up) will always be a square. That is, if
your normal tile size is 64 and you want to show a 128x128 icon, the icon is
two tiles wide and so it will take up a 2×2-tile area on the map. The
height of a big icon is irrelevant--any excess height beyond width/2 is used
to show vertical features. To draw this icon properly, other tiles on that
same ground will be moved behind it in the drawing order.

One important warning about using big icons in isometric mode is that you
should only do this with dense atoms. If part of a big mob icon covers the
same tile as a tall building for instance, the tall building is moved back
and it could be partially covered by other turfs that are actually behind it.
A mob walking onto a very large non-dense turf icon would experience similar
irregularities.

Side-view format

(See more at Side-view maps.)

The SIDE_MAP format is like a cross between TOPDOWN_MAP
and ISOMETRIC_MAP. It looks very similar to a top-down view but it is
intended for more of a 3/4 perspective, where tiles lower on the screen are
considered closer to the viewer. Because this impacts the way layers work,
most of the layering behavior is the same as with isometric.

In a 3/4 perspective the tiles are often foreshortened, so pixel offsets
are adjusted to account for this. For example, you may set
world.icon_size to "32x24", but the tile is considered to be
a perfect square if you look at it from the top down. Because the width is 32
pixels, the virtual height is also 32, so if you use pixel_y=32 the atom will
appear one tile further back than it normally is. (This adjustment doesn't
affect screen objects or pixel_w/pixel_z.)

Changing client.dir preserves the same tile size regardless of
orientation.



map_cpu var (world)

This is the percentage of a server tick that the server spends processing
information about the map to send to players.  A value of 0 would indicate very
little cpu usage.  A value of 100 would indicate full cpu usage, which means
that the server cannot complete all the necessary computations during a tick to
finish in time for the next tick.  In this case, timed events (such as sleep)
may take longer than requested.



maxx var (world)


The world map is a three-dimensional block of turfs with coordinates
ranging from (1,1,1) to (maxx,maxy,maxz).  If set at compile time, it
provides a lower bound and will be increased as needed by the map files.

The default value is 0, indicating no map.  If any of the map dimensions
are set to non-zero values at compile time, the others will default to 1.

New territory created by increasing the map boundaries is filled in with
the default turf and area (world.turf, and world.area).



maxy var (world)


The world map is a three-dimensional block of turfs with coordinates
ranging from (1,1,1) to (maxx,maxy,maxz).  If set at compile time, it
provides a lower bound and will be increased as needed by the map files.

The default value is 0, indicating no map.  If any of the map dimensions
are set to non-zero values at compile time, the others will default to 1.

New territory created by increasing the map boundaries is filled in with
the default turf and area (world.turf, and world.area).



maxz var (world)


The world map is a three-dimensional block of turfs with coordinates
ranging from (1,1,1) to (maxx,maxy,maxz).  If set at compile time, it
provides a lower bound and will be increased as needed by the map files.

The default value is 0, indicating no map.  If any of the map dimensions
are set to non-zero values at compile time, the others will default to 1.

New territory created by increasing the map boundaries is filled in with
the default turf and area (world.turf, and world.area).



mob var (world)


When a player connects to the world, the world is searched for a mob with
the player's key.  If one is found, the player is connected to that mob.  If
none is found, a new mob of type world.mob is created and the player is
connected to this new mob.

The default value is /mob.  Setting world.mob to 0 prevents the creation
of default mobs.

Example:

world
  mob = /mob/newbie

mob/newbie
  Login()
    src << "Welcome, [name]."
    ..()

This example will connect new players to mobs of type /mob/newbie.  They
are welcomed when they connect.



movement_mode var (world)



Controls how movement works on the map.

TILE_MOVEMENT_MODE allows you to easily discard any and all pixel
movement, so if step_x or step_y coordinates or unexpected atom bounds were
loaded from a savefile, for instance, they would be eliminated. If you use any
other movement mode, you can give an atom the
TILE_MOVER flag and it will
behave as if it were in this mode, while other atoms are free to do their own
thing.

LEGACY_MOVEMENT_MODE exists to distinguish between old and new
movement behavior. In older versions of BYOND before pixel movement, turfs
took their contents into consideration by default in Enter() and Exit(). This
doesn't really make sense for newer games, so in any other movement mode the
turf behavior will ignore its contents. mob.Cross() is also affected, since
it would return 0 by default in legacy mode when both mobs were dense; now
by default it checks mob.group.



name var (world)

This is the name of the world.

Example:

world
  name = "The Void"



params var (world)


This is a list of parameters passed to the world from the command-line
-params option when the server was started.  The parameter text is passed
through params2list() to generate the world.params list.

Example:

world/New()
   var/p
   if(params.len) world.log << "Command-line parameters:"
   for(p in params)
      world.log << "[p] = [params[p]]"

This example displays the value of each parameter.



port var (world)

This is the network port of the world.  If the world does not have an
open network port, this is 0.



process var (world)

This read-only variable indicates the ID of the server's process on the
system running it. The result is a number, unless for some unexpected
reason the number won't fit in a num type, in which case it will
be text. (In practice it should always be a number.)



realtime var (world)

This is the time (in 1/10 seconds) since 00:00:00 GMT, January 1, 2000
(also known as the BYOND era).

Because this is a large number, BYOND's number system isn't capable of
enough precision to deliver the exact number of 1/10 second ticks. It usually
rounds off to the nearest several seconds. For more accurate readings use
world.timeofday.



reachable var (world)

Returns 1 if the world is currently hosted and the port can be reached by
players (as determined by the BYOND hub), 0 if not.

If the port is not reachable, there may be a brief period during which the
hub is still attempting to make contact; during that time the port is assumed
to be reachable. Currently, the reachability test times out and fails after
30 seconds.



sleep_offline var (world)

Setting this to 1 causes the world to be suspended when there are no
players, even if you have sleeping procs waiting to happen.  The default
value is 0, which means the server will only sleep if there are no players
and no procs waiting to happen.  The main purpose of the variable is to save
the cpu from doing work when there is nobody around to appreciate it.  On the
other hand, that doesn't give the poor NPC's a break from the nasty humans.



status var (world)

This is a short text string used in BYOND hub to describe the state of a
game in progress.  For example, you might want to indicate if new players
will be able to actively play, or whether they would have to join as
spectators.

Example:

world
   status = "accepting players"
mob/verb/start_game()
   world.status = "accepting spectators"
   //...



system_type var (world)

This variable indicates the operating system type at run-time.  It will be
one of the following constants:


MS_WINDOWS
UNIX



tick_lag var (world)


This is the smallest unit of time (one server tick) measured in 1/10
seconds.  The duration of events that take some finite amount of time (like
sleep) will be rounded to a whole number of ticks.

Players are limited to one command (including movements) per server tick,
so this value can be used to adjust the responsiveness of the game.  If the
network is too slow to keep up with players, their commands will get queued
up, which can be annoying when trying to move.  In this case, tick_lag
should be increased so that the stored up movement commands are discarded.
On the other hand, if you have a very fast network, you may wish to decrease
tick_lag to speed up the response time to player commands.

Often it is more convenient to set world.fps instead of world.tick_lag,
since fps (frames per second) is an easier way to think of server ticks.
world.tick_lag is 10 / world.fps and vice-versa, so a tick_lag of 0.25 is
equal to 40 fps.

If you set client.tick_lag or client.fps to a value other than 0, you can
make the client tick at a different (usually faster) rate.



tick_usage var (world)

This is the approximate percentage of the server tick that has been used
already.  A value under 100 means there's time to do more calculations, which
can include any pending procs that are still waiting to run on this tick.
When the value is over 100, the tick is running long and your world will
experience lag.

Keep in mind that sending maps to clients is the last thing that happens
during a tick, except for handling any events such as player commands that
might arrive before the next tick begins. Therefore in a verb,
tick_usage might have a higher value than you would expect to see in
a proc that loops and sleeps.



time var (world)

This gives the amount of time (in 1/10 seconds) that the world has been
running.  In actual fact, it is the number of server ticks that have passed
multiplied by world.tick_lag.  Therefore if the server sleeps (when no
players are connected) this time is not counted.  Also, if the server runs
overtime during a tick (because procs take longer than tick_lag to finish)
this still only counts as one tick.  This value is therefore a measure of
"game time" rather than real time.



timeofday var (world)

This is the time (in 1/10 seconds) since 00:00:00 GMT today. It is
basically identical to world.realtime but doesn't include any
information about the date. This is a much smaller number; hence it is more
accurate.



timezone var (world)

This is the time offset from UTC, in hours, for the world's time zone. It
can be used in the time2text() proc, although it is the default time
zone for that proc.



turf var (world)

This is the default turf type to be placed on the map wherever no turf is
specified.  A value of 0 turns off the default turf.



url var (world)

This is the full network address of the world.  (For example,
byond://dan.byond.com:6005.)



version var (world)


If you are distributing your game to players, you can use this variable
to automatically notify them of new releases.  To do so, you will first need
to set world.hub to the hub
path of your game.  You can then advertise the current version by
configuring that value in your
hub console.

When players boot up an outdated version of your game (as indicated by
comparing world.version with the version advertised by BYOND
hub), they will be notified of the new release.



view var (world)



This is the default map viewport range.  The default value of 5 produces an
11x11 viewport.  A value of -1 turns off the map display altogether.  The client may automatically
scale down icons in order to conveniently fit the map on the player's screen.

For non-square views, you can assign this to a text string of the form
"WIDTHxHEIGHT".  For example, "11x11" is equivalent to a view depth of 5, but
you could make it wider like this: "13x11".

This setting also affects the default range of the view(),
oview(), range(), and orange()
procedures.

If the entire map is small enough to fit on one screen 
(arbitrarily defined to be 21x21 or less),
the default view is automatically adjusted to fit the map.  In
this case, client.lazy_eye is also automatically turned on by
default, since you probably don't want the map to scroll around.



visibility var (world)


This controls whether the world advertises itself in the
BYOND Hub when it has an open network
port for accepting players.  The visibility of the world still depends on
whether any of the connected players has their location reporter turned on,
and that in turn relies on the pager being turned on.



Special notes
This section of the reference should help explain some concepts that
may be harder to understand or that can use more clarification.




BACKGROUND_LAYER

This is mostly no longer needed. A negative value for plane is the
preferred way to do show objects in the background. It can still be used
however when you want to rearrange objects in the same plane when using
PLANE_MASTER for visual
effects.

BACKGROUND_LAYER is a special high value that can be added to the
regular layer of any atom.

The purpose of this value is to make an atom appear below any regular
atoms, even if they share the same plane. In an isometric map for instance,
HUD objects will always appear above the map, but makeing a HUD object appear
behind the map was basically impossible without this feature until
plane was implemented.

When using this special layer, it should be added to the layer an atom
normally uses. For instance an obj should have a layer of BACKGROUND_LAYER
+ OBJ_LAYER.

This can be mixed with TOPDOWN_LAYER and EFFECTS_LAYER,
but it will take precedence over both. Anything with BACKGROUND_LAYER
will always appear below anything without it on the same plane.

Images or overlays with FLOAT_LAYER can be left alone. They will
automatically have the same layer as whatever atom they are attached to.



Big icons

BYOND allows you to use icons that are not the same size as the tile size
defined in world.icon_size. These icons can be manipulated with the /icon datum
using their raw, native size, and shown on the map in full size. To use the old
behavior where an atom can display only an icon of the normal tile size, use
the TILED_ICON_MAP value for map_format instead.

When you use an icon of non-standard size on an atom, the icon is "anchored"
to the southwest corner of the atom. If you are using a top-down view
(world.map_format=TOPDOWN_MAP), the icon will appear to spread out further to
the east and north. In an isometric map (world.map_format=ISOMETRIC_MAP), the
icon will cover additional tiles north and east as well. The "footprint" of an
isometric icon--the actual map tiles it covers--is always square, so if your
tile size is 64x64 and you use a 128x64 icon, the 128-pixel width means the
icon will cover a 2x2 section of map tiles.

It is important to remember that using a big icon is a visual effect
only. It will not affect how the atom bumps into other atoms or
vice-versa.

Big icons will affect layering--the order in which icons are drawn. In
general, because a big icon is covering more than one tile of the map, it will
try to draw above any other tiles in that space that are on the same layer.
This way, you can set a turf to use a big icon without having to change the
turfs to the north and east. If an atom has a big icon, any overlays and
underlays attached to it will be pulled forward as well, so they will draw in
front of anything on their same layer. In isometric mode this is about the same,
except that the layer isn't that important--anything in the way will just be
moved back behind the big icon.

Note: Big overlays will not "pull forward" on their own. If the main atom
uses a single-tile icon, a big overlay attached to it will not try to draw in
front of other icons on the same layer. This is so that name labels, health
bar overlays, etc. will not cause any odd behavior. To be safe, you should
always specify a layer when adding an overlay.

In isometric mode, layering is affected by the "distance" between the atom
and the viewer, so putting a regular-sized icon and part of a big icon on the
same tile could cause layering oddities. Tiles that are covered by a big icon
will tend to be drawn behind the big icon as mentioned above. For this reason,
any atoms whose icons cover more than one tile (the extra height of an
isometric icon doesn't count) should always be dense, and you should block
movement onto any tile covered by them.

When manipulating icons with the /icon datum, you can still use Blend() to
combine icons of different sizes. By default, the icons will be lined up at
their southwest corners. You can change the position at which the second icon
is blended.



Color gradient

A color gradient is a special list that defines a range of colors that you
can smoothly interpolate between. A simple example is a gradient from red to
white:

Example:

list("red", "white")
// OR
list(0, "red", 1, "white")

Applying a number like 0.2 to this gradient would give you a color that's
20% of the way from red to white. More complex gradients however are also
possible.

The format of a gradient is a list that contains a number (the position
along the gradient, from 0 to 1 unless you use values outside that range)
followed by a color. You can have as complex a gradient as you like. If you
reuse the same number twice in a row, the gradient will have a sudden color
change at that point.

It is also possible to skip numbers or colors, and they will be filled in
automatically with the previous number or color. The exceptions are at the
beginning and ends of the list; at the end of the gradient, the last color is
assigned a number 1 by default, and the first is assigned 0. If you skip
colors at the beginning, they will be filled in with the first color you use.

Include "loop" anywhere in the list to make this a looped gradient. If you
don't, any numbers outside the gradient's range will be clamped to that range.
E.g., in a normal gradient ranging from 0 to 1, a number of 1.2 is
interpreted as 1 without a loop and 0.2 with a loop.

Here are some more examples:

Example:

// color wheel; ranges 0 to 6 and loops
list(0, "#f00", 1, "#ff0", 2, "#0f0", 3, "#0ff", 4, "#00f", 5, "#f0f", 6, "#f00", "loop")

// 10% each red, yellow, green, blue, with a 20% transition zone between each
// notice no color follows 0.4 or 0.7, so the previous color is used
list(0.1, "#f00", 0.3, "#ff0", 0.4, 0.6, "#008000", 0.7, 0.9, "#00f")

// green and black stripes
list(0.5, "#008000", 0.5, "#000000", "loop")

You can also include "space" in the list, and give it an associated value
that describes the color space this gradient uses to interpolate between
colors. For instance, "space"=COLORSPACE_HSL will use HSL
interpolation instead of the default RGB. See
Color space for more information.

Example:

// color wheel with a different color space
list(0, "#f00", 3, "#0ff", 6, "#f00", "loop", "space"=COLORSPACE_HSLA)

Currently, color gradients are only used by particle effects and the
gradient proc. With particles, if you use
a gradient the particle's color is given as a number, and that number is used
to look up its real color from the gradient. The number can change over time,
thus changing the particle's color.



Color matrix

A color matrix is used to transform colors, in the same way that a matrix
represented by the /matrix datum is used to transform 2D coordinates.
A transformation matrix is 3x3, of which only 6 values are needed because the
last column is always the same.  A color matrix, because it transforms four
different numbers instead of two, is 5x5.


                |rr rg rb ra 0|
                |gr gg gb ga 0|
[r g b a 255] x |br bg bb ba 0| = [r' g' b' a' 255]
                |ar ag ab aa 0|
                |cr cg cb ca 1|

In that formula, values like rg mean "red to green", meaning
that's the ratio of red in of green out. (The "c" is for "constant".) In
an identity matrix, which just produces the original color, the values
rr, gg, bb, and aa are all 1 and
everything else is 0.

In easier-to-understand terms, this is how the result is calculated:


new_red   = red * rr + green * gr + blue * br + alpha * ar + 255 * cr
new_green = red * rg + green * gg + blue * bg + alpha * ag + 255 * cg
new_blue  = red * rb + green * gb + blue * bb + alpha * ab + 255 * cb
new_alpha = red * ra + green * ga + blue * ba + alpha * aa + 255 * ca

It is helpful to think of each row in the matrix as what each component of
the original color will become. The first row of the matrix is the rgba value
you'll get for each unit of red; the second is what each green becomes, and so
on.

Because the fifth column of the matrix is always the same, only 20 of the
values need to be provided.  You can use a color matrix with atom.color or
client.color in any of the following ways:


Reading a color var that has been set to a matrix will return the full
20-item list, where every 4 items represent a row in the matrix (without the
fifth column).

In the MapColors() icon proc, the values are sent as arguments,
not as a list.

Other color spaces
The color filter allows the use of
other color spaces for a matrix. In those other color spaces, the matrix
calculations work the same but instead of red, green, and blue, they'll be
whatever values that color space uses. For instance an HSL color matrix uses
hue in place of red, saturation in place of green, and luminance in place of
blue. (Alpha is always alpha.)

The way that works internally is that the shader will convert a color from
RGB to the color space used by the matrix, then apply the matrix, then convert
back to RGB.



EFFECTS_LAYER

This is mostly no longer needed. A negative value for plane is the
preferred way to do show objects in the background. It can still be used
however when you want to rearrange objects in the same plane when using
PLANE_MASTER for visual
effects.

EFFECTS_LAYER is a special high value that can be added to the
regular layer of any atom.

The purpose of this value is to make an atom appear above any regular
atoms. For instance, in an isometric map if you want to display a character's
name below them, it does not make much sense to have nearer objects cover up
that name, so you can tell the name overlay to use EFFECTS_LAYER +
MOB_LAYER and it will show up on top of all the normal icons on the map.
This has been somewhat obviated by plane but may still be useful in
some cases.

When using this special layer, it should be added to the layer an atom
normally uses. For instance an obj should have a layer of EFFECTS_LAYER +
OBJ_LAYER.

This can be mixed with TOPDOWN_LAYER, in non-topdown map formats.
Anything in TOPDOWN_LAYER will display on top of
EFFECTS_LAYER, and TOPDOWN_LAYER + EFFECTS_LAYER will be
above both.

This can also be mixed with BACKGROUND_LAYER, which takes priority
over everything else.

Images or overlays with FLOAT_LAYER can be left alone. They will
automatically have the same layer as whatever atom they are attached to.



Filter effects

Filters are a way of adding special effects to an icon, or a group of icons
(see KEEP_TOGETHER in
appearance_flags), by
post-processing the image. A filter object describes a specific form of image
processing, like for instance a blur or a drop shadow. Filters can be added or
removed at will, and can even be animated.

A filter is created by using the filter proc like
so:


// halo effect
mob.filters += filter(type="drop_shadow", x=0, y=0,\
                      size=5, offset=2, color=rgb(255,255,170))

These are the filters currently supported:


Alpha mask
Angular blur
Bloom
Color matrix
Displacement map
Drop shadow
Gaussian blur
Layering (composite)
Motion blur
Outline
Radial blur
Rays
Ripple
Wave



Alpha mask filter



Uses an icon or render target as a mask over this image. Every pixel that
is transparent in either the image or the mask, is transparent in the result.

The x and y values can move the mask from its normal
position. By default, the mask is centered over the center of the image.

The MASK_INVERSE flag will invert the alpha mask so that opaque
areas in the mask become transparent, and vice-versa. There is also a
MASK_SWAP flag which treats the source image as the mask and
vice-versa, which might be useful for some effects.

Note: Unlike many other filters, this filter is taken into account
for mouse-hit purposes.



Angular blur filter



Blurs the image by a certain amount in a circular formation, as if the
image is spinning. The size of the blur can roughly be thought of in "degrees"
worth of blur. As the distance from the center increases, the blur becomes
more noticeable since the same amount of angular motion has to travel farther
along a circle.

Typically this blur is used with an entire plane, but it could be used to
give a sense of motion blur to a spinning object.

Note: Large blurs will look worse toward the edges due to limited sampling.
Loss of accuracy will appear where size × distance is greater
than about 300. You can increase accuracy by breaking up large sizes into
multiple filter passes with differing sizes. The blur used is Gaussian, so
combining blur sizes A and B will give a total size of
sqrt(A2+B2).

The offset parameter, if used, is effectively subtracted from the
pixel distance to the center. Pixels within that radius won't blur. Anything
outside that radius will act as if it's offset pixels closer to the
center.



Bloom filter



Post-processing effect that makes bright colors look like they're a strong
light source, spreading their light additively to other nearby pixels. This is
a complex effect that involves multiple shader passes. For both performance and
visual reasons, it is usually best applied to an entire plane rather than to
individual objects.

The color threshold determines which pixels this effect applies to.
If any of the red, green, or blue components of the pixel are greater than the
same component for the threshold, that pixel will bloom. The blooming pixels
then have their colors spread outward to create a glow that gets added to the
original image.

The offset and size parameters are used to control the
glow effect. They work the same as they do in the drop shadow filter:
offset causes the light to grow outwards, and a blur of size
is then applied to soften it. Often just using a blur alone will produce a
pleasing effect. By playing with these two values you can make the bloom effect
appear differently.

The alpha value is applied to any light contributions from bloomed
pixels that get added to the original image, so values lower than 255 can make
the effect less pronounced. This can be very useful if you choose to animate
the filter.



Gaussian blur filter



Blurs the image by a certain amount. The size of the blur can roughly be
thought of in "pixels" worth of blur.

Note: Large blurs will result in reduced performance. The
highest size that can be handled easily in this filter is 6. Higher sizes
require multiple passes, although the filter will "cheat" and use low-quality
passes for much higher sizes.



Color matrix filter



Applies a color matrix to this image. Unlike with the atom.color var, you
can apply color conversions other than the regular RGBA color space, depending
on the value of space. See Color
space for more information.



Displacement map filter



Uses an icon or render target as a template for various warping effects on
the main image. Think of displacement as "pulling" a pixel from an offset
location.

In the displacement map, pixels that have a higher red component will make
the image appear to warp to the left, lower reds warp it to the right, and
gray (r=128) will cause no horizontal warping. The green component affects the
vertical: higher to warp upward, lower to warp downward. Transparent pixels in
the displacement map will have no effect.

This can be used for very complex distortion, unlike other distortion
filters such as wave and ripple that are confined to specific equations.

The optional FILTER_OVERLAY flag is supported for the
flags argument, which will overlay the displaced image onto the
original.



Drop shadow filter



Applies a drop shadow to this image. This is a combination of multiple
filters, since it will apply an outline if offset is included, a
Gaussian blur to the shadow, and will underlay the shadow beneath the image.

You can also think of this filter as an outer glow.

If you use a size less than 0, the shadow will appear inside the
image instead. This would be an inset shadow, or inner glow.



Layering (composite) filter



Composites another image over or under this image. Using the
FILTER_OVERLAY flag, which is the default, puts the second image
on top of what's already here. FILTER_UNDERLAY puts it underneath.

The x and y values can move the mask from its normal
position. By default, the second image is centered over the center of the
first.

The color, transform, and blend_mode vars are
available for convenience. Because the bottom image is drawn over a blank
background, blend_mode is always applied to the top image. All of
the other vars apply to the second image being drawn.

Note: Transforms use default bilinear scaling, since
PIXEL_SCALE is not
available here.
Note: Like most other filters, this filter is not taken into account
for mouse-hit purposes. Any layered icons will be strictly visual.



Motion blur filter



Applies Gaussian blur in one direction only. The amount and direction are
both specified by x and y. The size of the blur is equal to
sqrt(x*x + y*y).

See Gaussian blur for more information.



Outline filter



Applies an outline to this image.

At larger sizes, the outline is less accurate and will take more passes to
produce. Performance and appearance are best at sizes close to 1 or less.

flags can be a combination of the following values:



Radial blur filter



Blurs the image by a certain amount outward from the center, as if the
image is zooming in or out. As the distance from the center increases, the
amount of blurring increases, and near the center the blur is hardly visible
at all. The size value is smaller by default for this filter than it
is for other filters, since it's typically used with an entire plane where the
distance from the center can easily be several hundred pixels.

Typically this blur is used with an entire plane.

Note: Large blurs will look worse toward the edges due to limited sampling.
Loss of accuracy will begin when size × distance is greather
than 6. You can increase accuracy by breaking up large sizes into multiple
filter passes. The blur used is Gaussian, so combining blur sizes A and B will
give a total size of sqrt(A2+B2).

The offset parameter, if used, is effectively subtracted from the
pixel distance to the center. Pixels within that radius won't blur. Anything
outside that radius will act as if it's offset pixels closer to the
center.



Rays filter


Draws random rays that radiate outward from a center point. (That point may
be outside of the image.) As they move outward, their alpha value diminishes
linearly. These are meant to be animated. The offset value determines
the "time", where every jump of +1 can be a very different set of rays, and
every 1000 units this filter will repeat.

The threshold value can be thought of as a way of culling
lower-strength rays. Ray strength is anywhere from 0 to 1 at any given angle,
but values below threshold may as well be 0. Values above that are
re-scaled into a range of 0 to 1.

The factor parameter allows you to tie the ray's length to its
strength. At 0, the length of every ray is the same. At 1, the length ranges
from 0 to size. Generally speaking, the higher factor is,
the more the rays will appear to move outward as they strengthen and inward
as they weaken.

Ray color can be provided as a matrix. Only the diagonal values of the
color matrix will be used, but using a matrix will allow you to set values
outside of the normal color range.

flags can have the following values:



Ripple filter



Applies a ripple distortion effect to this image.

This filter is meant to be animated. A good animation will typically start
at a radius of 0 and animate to a larger value, with size
decreasing to 0.

The falloff parameter can be tweaked to your liking. A value of 1
should look reasonably like ripples in water, with the inner ripples losing
strength. A value of 0 will cause no reduction in strength.

The equation governing the ripple distortion is size × sin(2πr') ÷ (2.5 × falloff × r'2 + 1),
where r' = (radius - distance) ÷ repeat.

Up to 10 ripples can be stacked together in a single pass of the filter, as
long as they have the same repeat, falloff, and
flags values. (See the wave filter for the WAVE_BOUNDED flag.)



Wave filter



Applies a wave distortion effect to this image.

The x and y parameters specify both the direction and
period of the wave; the period is sqrt(x*x + y*y).

This filter is meant to be animated, from whatever offset you want
to offset+1, and then repeating. With multiple waves, you can produce
a very convincing water effect.

Example

#define WAVE_COUNT 7
atom/proc/WaterEffect()
    var/start = filters.len
    var/X,Y,rsq,i,f
    for(i=1, i<=WAVE_COUNT, ++i)
        // choose a wave with a random direction and a period between 10 and 30 pixels
        do
            X = 60*rand() - 30
            Y = 60*rand() - 30
            rsq = X*X + Y*Y
        while(rsq<100 || rsq>900)   // keep trying if we don't like the numbers
        // keep distortion (size) small, from 0.5 to 3 pixels
        // choose a random phase (offset)
        filters += filter(type="wave", x=X, y=Y, size=rand()*2.5+0.5, offset=rand())
    for(i=1, i<=WAVE_COUNT, ++i)
        // animate phase of each wave from its original phase to phase-1 and then reset;
        // this moves the wave forward in the X,Y direction
        f = filters[start+i]
        animate(f, offset=f:offset, time=0, loop=-1, flags=ANIMATION_PARALLEL)
        animate(offset=f:offset-1, time=rand()*20+10)

The equation governing the wave distortion is size × sin(2π(d - offset)),
where d is the number of wave periods' distance from the center along the x, y
direction.

The WAVE_SIDEWAYS flag will cause the distortion to be transverse
(perpendicular) to the wave instead of in the same direction as the wave. The
WAVE_BOUNDED flag limits the distortion to the confines of this image,
instead of lettings its pixels spill out a little further from the distortion
(and likewise, transparent pixels spill inward).

Up to 10 waves can be stacked together in a single pass of the filter, as long as they
have the same WAVE_BOUNDED flags.



Generators

A generator is an object that can produce a random number, vector (list of 3 numbers), color (as a text string), or color matrix (list of 20 numbers) in a specified range according to rules you set down. It is used primarily for particle effects, since it can run on the client.

There are several types of generators:


Numbers: Generate a random real number.
Vectors: Generate a random vector.
Shapes: Generate a random vector within a specific shaped region.
Colors: Generate a random color or color matrix.

Generators can also be chained together with math operators and some procs. The second value can be a regular value instead of a generator, so for instance you can multiply a vector by 2, or by a matrix to transform it.


OperatorsAction
+ - * /Arithmetic operators. You can multiply a 3D vector by a color matrix (where red,green,blue in the matrix correspond to x,y,z) to do a 3D transform, or by a 2D matrix for a 2D transform.
- (unary)Negate the value, same as multiplying by -1.
turn(), generator.Turn()Rotate a vector clockwise in the XY plane.



Gliding

Gliding is a "glitz" effect applied by BYOND to cover up the visual sins
of tile-based movement, by making objects and the map appear to move smoothly
from one tile to another instead of immediately jumping. It is also available to
smooth over small jumps in pixel movement that might occur, for instance if the
client FPS is set higher than the server's.

To control the gliding speed of an atom, set glide_size to the
value of your choice. If this is not set, the client will attempt to adjust
the speed manually.  glide_size is measured in server ticks, so
if client.fps is set to a value greater than world.fps,
it will be scaled appropriately.

Whether an object glides or jumps is based on how far it moves relative to
its step_size value, which by default is a full tile width. If the
movement goes too far past step_size in the X or Y directions, it's
no longer a glide.

The animate_movement var can be used to control the way in which
an object glides, or suppress gliding altogether.

By using the LONG_GLIDE flag in appearance_flags, a
diagonal glide will take just as long as a cardinal-direction glide by moving
a fullt glide_size pixels in the dominant X or Y direction.
Otherwise, gliding tries to move by that many pixels in strict Euclidean
distance (a straight line) and diagonal glides take longer.

In LEGACY_MOVEMENT_MODE,
gliding is turned off if you set any of the bound or step vars for an atom to
a non-default value. The only gliding that occurs in this case is when
client.fps is higher than world.fps. All other movement modes base gliding on
an atom's glide_size value.



HUD / screen objects

HUD stands for Heads-Up Display, and refers to any atoms that appear on
the screen but don't move when the player moves. These are also called screen
objects. Any movable atom can be added to the HUD by setting its
screen_loc var, and adding it to client.screen for each user
who is supposed to see it. This can be used to display a character's vital
stats, scores, etc.

If you want to have something like a health meter or name attached to a
moving atom, use overlays or /image objects instead. An
/image object is similar to a screen object in that it can be shown
to only certain players instead of being shown to everyone.

The size of the screen depends on client.view (or
world.view), world.map_format, and world.icon_size.
In a normal topdown map format, client.view is the same as the screen
size; in other map formats the screen might be a different size.

The screen_loc var can be set to a value like "1,1" (the
southwest tile of the screen), "4,NORTH" (fourth tile from the west,
along the north side of the screen), "SOUTHEAST", and so on. You can
also include pixel offsets, percentages, and specify two corners to tile an
icon repeatedly from one end to the other. See
screen_loc for more
details.

screen_loc can also be used to stretch the bounds of the HUD. A
value of "0,0" will cause the atom to appear to the southwest of the
southwest-most tile on the visible map, outside of the regular map bounds.
Using HUDs in this way, you can provide a nice decorative "frame" for your map.

More complex 

You can use HUDs in other map controls as well, by preceding screen_loc with
the name of the map you will use followed by a colon. For instance,
screen_loc="map2:1,1" will show an icon in the southwest corner of the
map2 control. The actual size of a secondary HUD is based on how far
out the icons in it extend in any direction. If you have one icon at
"map2:1,1" and another at "map2:4,3", then that HUD will be
four tiles wide and three high.



Isometric maps




Isometric projection is a form of pseudo-3D in which the 2D icons used by
BYOND can be arranged in a way to give the appearance of three dimensions. If
you look at a map top-down, each tile on the map is a square. The map is
rotated 45° clockwise and then tilted at an angle (30°) so that each
square now looks like a foreshortened diamond from the viewer's perspective.
What was once north now points to the northeast end of the viewer's screen;
what was once east now points southeast to the viewer. Tiles that are more to
the south or east are "nearer" to the viewer, and tiles that are north or west
are "farther". The actual direction the map faces can be changed by using
client.dir.

It is important to remember that this is an illusion of 3D, not real 3D.

To use isometric mapping, set world.map_format to
ISOMETRIC_MAP. You should set world.icon_size so the tile
width is a multiple of 4 pixels. The width of the tile is highly important.
The height of your tiles should be at least half that value. BYOND uses a 2:1
isometric format, meaning that the diamond base of each tile is half as high
as its width. For example if you have a 64x64 tile size, every diamond in the
map will be 64 pixels wide by 32 high, and you have an extra 32 pixels at the
top of your icon for vertical projections like buildings. If you set the tile
size to 64x80, the base is still a 64x32 diamond and you have 48 pixels left
over for vertical structures.

In this mode pixel_x and pixel_y will offset icons along the
"ground". To adjust horizontal and vertical positions, use the pixel_w
and pixel_z vars.

Layers
The layer var behaves differently in isometric mode. Because some
tiles are nearer to the viewer than others, the tiles that are farther back
need to be drawn first so they are behind any tiles that should go in front of
them. So in isometric mode, the back row of tiles (a diagonal line of them) is
drawn first, followed by the next row forward, and so on. The layer
var only matters when icons overlap each other in the "physical" space, like
an obj sitting on a turf.

When pixel or step offsets, or gliding, place an object on multiple turfs,
it is drawn on top of the nearer turf (assuming its layer is higher).

Using icons wider than the regular tile size can have an impact on layering
as well. See Big icons for more information.

Because of the order in which icons are drawn, you may want to limit the
ability of an atom to cut diagonally around corners. While moving northeast
behind a dense wall, for instance, a mob might temporarily appear in front of
the wall because its pixel offsets (from gliding) temporarily put it on the
same tile as the wall. If you do not want to limit corner-cutting, a simple
workaround for this case is to give the wall a higher layer than the mob.

Screen objects (in client.screen) are always drawn on top of all
isometric tiles, as is the case in other map modes as well.

Since it may be desirable in some games to use a topdown map for some
situations (like a special battle map), you can add TOPDOWN_LAYER to
any atom's layer—e.g., TOPDOWN_LAYER+TURF_LAYER—to make
it appear in topdown mode. Topdown and isometric tiles really aren't meant to
be mixed, but if they do mix you'll see topdown tiles always display above
isometric tiles, just like screen objects do. The best way to use this is to
apply TOPDOWN_LAYER to every tile in a certain part of the map that
the players can't walk to.

If you want to use an overlay that should not be covered by other "nearer"
icons on the map, such as a name or health meter, you can add
EFFECTS_LAYER to the overlay's layer. Icons with
EFFECTS_LAYER will draw above regular icons. Then objects with
TOPDOWN_LAYER will draw on top of everything else. However, be aware
that EFFECTS_LAYER has largely been superseded by the plane
var.

Screen size
In this mode, world.view or client.view is used to define
the minimum number of map tiles you will see, not the screen/HUD size
which is calculated from client.view. Extra map tiles are shown to fill out
the screen size. HUD objects use screen coordinates, so 1,1 is still the lower
left.

The actual HUD size is always a full number of tiles, whose size is defined
by world.icon_size. If you have a tile size of 64x64, and
world.view=6 (a 13x13 map), a full 13x13 diamond of map tiles will be
shown. The width of this diamond is 13 tiles. The height is only half that,
plus whatever vertical space is needed to show the icons in that area. Then
everything is rounded up to a full tile size, so the result is a 13x7-tile
screen. This is the formula you need if you want to calculate the screen size:


pixel_width = round(icon_width * (view_width + view_height) / 2)
pixel_height = round(icon_width * (view_width + view_height - 2) / 4) + icon_height

screen_width = round((pixel_width + icon_width - 1) / icon_width)
screen_height = round((pixel_height + icon_height - 1) / icon_height)

If you use TOPDOWN_LAYER, any topdown sections of the map will be
limited to this same view.



Numbers
In DM, all numbers are stored in floating point format. Specifically,
single-precision (32-bit) floating point. This is important to know if you
think you will be working with large numbers or decimal values a lot, because
the accuracy of the numbers is limited.

32-bit floating point numbers can represent integers from -16777216
to 16777216 (224). Non-integer values can get about as small as
2-126 and as large as 2127.

Floating point numbers do not handle most decimal values precisely. For
instance, 0.1 is not exactly 0.1, because floating point numbers are stored
in a binary format and in binary, 1/10 is a fraction that repeats
forever—the same way 1/3 repeats as 0.33333... in decimal numbers. It
ends up being rounded off, either a little higher or a littler lower than
its true value. This means that the following loop won't work like you might
expect:

Example:

for(i = 0, i < 100, i += 0.1)
    world << i

You might expect that code to loop exactly 1000 times, with i
going from 0 up to 99.9 before stopping. The truth is more complicated,
because 0.1 stored in floating point is actually greater than the exact value
of 0.1. Other values might be more or less than their exact numbers, and as
you add these numbers together repeatedly you'll introduce more and more
rounding error.

Even more insidious, if you add 0.1 a bunch of times starting from 0, and
then subtract it out again the same number of times, the result you get may
not be 0. This is counterintuitive, because you might expect rounding errors
to reverse themselves in the same order they crept in. Unfortunately it
doesn't work that way.

You can correct for rounding error somewhat by using the
round proc to adjust the loop var each time,
although for performance reasons it might be preferable to find another
alternative.


for(i = 0, i < 100, i = round(i + 0.1, 0.1))
    world << i

Only fractions whose denominators are powers of 2 are immune to this
rounding error, so 0.5 is in fact stored as an exact value.

Another place floating point may lose accuracy is when you try to add
numbers of very different sizes. For instance as stated above, the upper
limit for accurate integers is 16777216. If you try to use a number such
as 100 million it will only be approximate, so adding 1 to that number
won't actually change it because the 1 is so much smaller, it will be
gobbled up by rounding error.

Also for the same reasons stated above, division will cost you
accuracy. Again you can divide by powers of 2 easily enough, and you can
divide an integer by any of its factors (like dividing 9 by 3) without a
problem, but a fraction like 1/3 will repeat forever so it gets rounded
to as much precision as floating point can manage.

In decimal, floating point numbers have at least six decimal digits of
precision. Since they're actually stored in binary, their true precision
is exactly 24 bits.



Particle effects

A particle set is a special effect, whose computations are handled entirely
on the client, that spawns and tracks multiple pixels or icons with a
temporary lifespan. Examples of this might be confetti, sparks, rocket
exhaust, or rain or snow. Particles are rendered on a special surface and that
gets attached to an obj or a mob like an overlay.

Particles can exist in 3 dimensions instead of the usual 2, so a particle's
position, velocity, and other values may have a z coordinate. To make use of
this z coordinate, you can use a projection
matrix. (The value of the z coordinate must be between -100 and
100 after projection. Otherwise it's not guaranteed the particle will be
displayed.)

To create a particle set, use new to create a new
/particles datum, and then you can set the datum's vars. The vars can
be set to constant values, or generator functions that will allow the client
to choose from a range of values when spawning those particles. (The easiest
way to handle this is to create your own type that inherits from
/particles, and set up the parameters you'll want at compile-time.)

After the datum is created, it can be assigned to an obj or mob using their
particles var. The particles will appear on the map wherever that obj
or mob appears.

Example:

particles/snow
    width = 500     // 500 x 500 image to cover a moderately sized map
    height = 500
    count = 2500    // 2500 particles
    spawning = 12    // 12 new particles per 0.1s
    bound1 = vector(-1000, -300, -1000)   // end particles at Y=-300
    lifespan = 600  // live for 60s max
    fade = 50       // fade out over the last 5s if still on screen
    // spawn within a certain x,y,z space
    position = generator("box", vector(-300,250,0), vector(300,300,50))
    // control how the snow falls
    gravity = vector(0, -1)
    friction = 0.3  // shed 30% of velocity and drift every 0.1s
    drift = generator("sphere", 0, 2)
obj/snow
    screen_loc = "CENTER"
    particles = new/particles/snow

mob
    proc/CreateSnow()
        client?.screen += new/obj/snow

These are the vars that can be used in a particle set. "Tick" refers to a
BYOND standard tick of 0.1s.


Particle vars that affect the entire set (generators are not allowed for these)
VarTypeDescription
widthnumSize of particle image in pixels
height
countnumMaximum particle count
spawningnumNumber of particles to spawn per tick (can be fractional)
bound1vectorMinimum particle position in x,y,z space; defaults to list(-1000,-1000,-1000)
bound2vectorMaximum particle position in x,y,z space; defaults to list(1000,1000,1000)
gravityvectorConstant acceleration applied to all particles in this set (pixels per squared tick)
gradientcolor gradientColor gradient used, if any
transformmatrixTransform done to all particles, if any (can be higher than 2D)
Vars that apply when a particle spawns
lifespannumMaximum life of the particle, in ticks
fadenumFade-out time at end of lifespan, in ticks
fadeinnumFade-in time, in ticks
iconiconIcon to use, if any; no icon means this particle will be a dotCan be assigned a weighted list of icon files, to choose an icon at random
icon_statetextIcon state to use, if anyCan be assigned a weighted list of strings, to choose an icon at random
colornum or colorParticle color (not a color matrix); can be a number if a gradient is used
color_changenumColor change per tick; only applies if gradient is used
positionnumx,y,z position, from center in pixels
velocitynumx,y,z velocity, in pixels
scalevector (2D)Scale applied to icon, if used; defaults to list(1,1)
grownumChange in scale per tick; defaults to list(0,0)
rotationnumAngle of rotation (clockwise); applies only if using an icon
spinnumChange in rotation per tick
frictionnumAmount of velocity to shed (0 to 1) per tick, also applied to acceleration from drift
Vars that are evalulated every tick
driftvectorAdded acceleration every tick; e.g. a circle or sphere generator can be applied to produce snow or ember effects

The icon and icon_state values are special in that they can't be assigned a generator, but they can be assigned a constant icon or string, respectively, or a list of possible values to choose from like so:

icon = list('confetti.dmi'=5, 'coin.dmi'=1)
The list used can either be a simple list, or it can contain weights as shown above.

Changing a var on a particle datum will make changes to future particles.
For instance, you can set the datum's spawning var to 0 to make it
stop creating new particles. (Note: If you are changing a vector or color
matrix, such as gravity, you need to assign a new value. You can't
for instance set particles.gravity[2] = 0 because it won't do
anything to update the particle stream.)

The same particle datum can be assigned to more than one movable atom.
However the particles displayed by each atom will be different.

The .add-particles command
If you want to spawn particles at specific times, you can use the client
.add-particles command.
From the server, you can run this command via
winset().

Example:

// spawn 100 particles for src's particle set right now
winset(player, null, list(command=".add-particles \ref[src] 100"))



Pixel movement

Pixel movement is a concept that allows atoms to escape the constraints of
BYOND's historically tile-based movement, and move in smaller steps. In the
past this had to be done with soft code, but that was sometimes inconvenient
and it did not perform as well in projects with many objects moving.

The key to understanding pixel movement is to use the bound and step vars.
You use the bound family of vars to define a bounding box for a movable atom,
instead of just making it one full tile in size. The step vars can give it a
movement speed and offset it from the corner of the tile it's standing on.

bound_x: The left edge of the bounding box
bound_y: The bottom edge of the bounding box
bound_width: Width of the bounding box
bound_height: Height of the bounding box
step_size: default movement speed
step_x: x offset from the corner of loc
step_y: y offset from the corner of loc
Those are for movable atoms only; they do not apply to turfs.

If world.movement_mode
is set to TILED_MOVEMENT_MODE, all movable atoms must be aligned
to the tile grid: their step_x/y/size values must be multiples of the icon
size, and their bounds must also land on tile boundaries although the atom
can be bigger than one tile. In other movement modes you can specify that
only specific atoms use this behavior, by giving them the
TILE_MOVER appearance
flag.

Bounding boxes


Left: The bounding box (blue) is the only part of the mob that actually collides with anything. By default, it would cover the whole turf (brown). Any turfs covered by the bounding box are in the mob's locs var. Right: The atom's true position (shaded) is offset from the turf by step_x and step_y.

As an example, if your players' mobs have icons that only cover the center
24×24 pixels of a regular 32×32 icon, then you would set the
mobs' bound_x and bound_y to 4--because there are 4 pixels unused to the left
and bottom--and bound_width and bound_height to 24.

The mob's physical location on the map depends on four things: Its loc,
its step_x/y values, its bound_x/y values, and its bound_width/height. The
lower left corner of the bounding box, relative to the turf the mob is
actually standing on, begins at step_x+bound_x on the left and step_y+bound_y
on the bottom.

The physical position of the bounding box is not affected by the
pixel_x/y/z vars. Those are still strictly visual offsets.

The turfs the mob is covering can be read from the read-only locs var. The
mob will also appear in the contents of those turfs.

Note: This means if an atom is in a turf's contents, its loc is not
necessarily that turf. The contents list is made to include "overhangers"
from another tile for ease of use.

Movement
All of the step and walk procs have been upgraded to take an additional
argument, which is the speed at which the atom should move. If that argument
is left out, the atom's own step_size is used by default. The step_size
determines how fast the step_x and step_y values will change when moving.

Move() has two new arguments that handle the position change gracefully.
These are the step_x and step_y values for the target location.

Pixel movement changes the behavior of the Move() proc, because a lot of
things are possible that were not possible when BYOND only supported moving
one tile at a time. For starters, a Move() is either a "slide" or a "jump"
depending on the distance. A slide is when the move can be stopped partway;
a jump is strictly pass/fail. Anything greater than one tile and the
mover's regular step_size is considered a jump. Changing z levels is also a
jump, as is moving to/from a non-turf.

If step_x and step_y aren't within a good range, the new loc and the
step_x/y values may be changed so that the southwest corner of the mover's
bounding box is standing on its actual loc, or as close to it as possible.

Enter() and Exit() can be called for several turfs and/or areas, not
just one at a time. It is also possible for them not to be called at all,
if the moving atom moves within a turf but doesn't cross a new turf
boundary. Enter() and Exit() are only called when first attempting to enter
or fully exit. The behavior of these procs depends on
world.movement_mode; in
legacy mode, they look at some of the contents of the turfs as well as the
turfs themselves, to preserve behavior found in older BYOND versions.

Cross() and Uncross() are the equivalent of Enter() and Exit() but apply
to objects the mover will either overlap or stop overlapping. (For turfs,
Enter() and Exit() call these procs by default, since the mover is both
stepping into and onto a turf.) Likewise Crossed() and
Uncrossed() are the equivalents of Entered() and Exited().

If an atom is sliding, its movement can be halted if it encounters an
obstacle partway along its route. Bump() will still be called for any
obstacles the atom runs into, but Move() will return the number of pixels
moved (the most in any direction). When sliding at a speed so fast that the
distance is bigger than the atom itself, the move will be split up into
several smaller slides to avoid skipping over any obstacles.

Gliding, which is used to show smooth movement between atoms in tile
movement, is mostly not used in pixel movement. It only applies when the
client uses a higher fps than the
server.

Pixel procs
The bounds() and obounds() procs have been added to grab a list of atoms
within a given bounding box. That box can be relative to an atom, or in
absolute coordinates.

bounds_dist() tells the distance between two atoms, in pixels. If it is
positive, that is the minimum distance the atoms would have to traverse to be
touching. At 0, they are touching but not in collision. A negative value
means the two atoms are in collision.



Projection matrix

Note: Currently this feature applies only to particle effects, using the
transform var.

Normally icons in BYOND can only be transformed in 2D, using a simple 3x3
matrix. This is represented by the /matrix object, which cuts off the
last column because it isn't used. However particles can have coordinates in x,
y, and z, and the whole particle set can be given a transformation matrix that
handles all three dimensions.

Simple 2D transforms
The easiest transformation for particles is a simple 2D one, which you can
do by setting the particle datum's transform var to a /matrix
object.

          a d 0
x y 1  *  b e 0  =  x' y' 1
          c f 1
When an x,y point is multiplied by the matrix, it becomes the new point
x',y'. This is equivalent to:

x' = a*x + b*y + c
y' = d*x + e*y + f
This is called an affine transform because all the operations are
"linear" in math terms. (That is, every term in the formula above has a single
variable, not raised to a higher power than 1.)

3x4 matrix (x,y,z with translation)
3D affine transforms of this type are also affine transformations. There is
no special object for this so a list is used (see below).

            xx xy xz 0
x y z 1  *  yx yy yz 0  =  x' y' z' 1
            zx zy zz 0
            cx cy cz 1
The way to read the vars above is that the first letter says what input
component is being transformed (x,y,z, or c for "constant"), and the second
letter is the output component.

x' = xx*x + yx*y + zx*z + cx
y' = xy*x + yy*y + zy*z + cy
z' = xz*x + yz*y + zz*z + cz
To use this kind of matrix, you can cut off the 4th column and provide the
values in a list form, in row-major order:

list(xx,xy,xz, yx,yy,yz, zx,zy,zz, cx,cy,cz)
Note the 4th row is also optional.
4x4 matrix (x,y,z,w with projection)
This is the most interesting matrix, since if you use all 4 columns you're
actually altering an "axis" called w. This isn't a real axis, but is just a
number that the resulting vector will be divided by.

            xx xy xz xw
x y z 1  *  yx yy yz yw  =  x'w' y'w' z'w' w'
            zx zy zz zw
            wx wy wz ww

w' = xw*x + yw*y + zw*z + ww
x' = (xx*x + yx*y + zx*z + wx) / w'
y' = (xy*x + yy*y + zy*z + wy) / w'
z' = (xz*x + yz*y + zz*z + wz) / w'
In a regular affine transform, w always stays at 1. In projection you can
think of w as a distance from the "camera". 1 is where objects are their
"normal" size. If you make the z value affect w' by setting zw, you basically
make an object look smaller at higher z values.

This is a simple projection matrix where x,y,z are left untouched, but
there's a projection effect. The "D" value is how far away the "camera" is
from z=0, so a point at z=D looks like it's twice as far away.


1  0  0  0
0  1  0  0
0  0  1  1/D
0  0  0  1

This 4x4 matrix is handled as a list just like the 3x4 affine matrix:

list(xx,xy,xz,xw, yx,yy,yz,yw, zx,zy,zz,zw, wx,wy,wz,ww)


Regular expressions

Regular expressions are patterns that can be searched for within a text
string, instead of searching for an exact match to a known piece of text.
They are much more versatile for find and replace operations, and therefore
useful for parsing, filtering, etc.

Some example regular expressions are:


PatternCodeMeaning
B.*Dregex("B.*D")Find B, followed by any number of characters (including none), followed by a D.
[0-3]regex(@"[0-3]")Find any digit from 0 to 3
foo|barregex("foo|bar","i")Find foo or bar, case-insensitive
\d+regex(@"\d+","g")Find all sequences of digits

These are some of the patterns you can use. If you want to use any of the
operators as an actual character, it must be escaped with a backslash.

It is highly recommended that you use raw strings
like @"..." for your regular expression patterns, because with a
regular DM string you have to escape all backslash \ and open
bracket [ characters, which will make your regular expression
much harder for you to read. It's easier to write @"[\d]\n" than
"\[\\d]\\n".


PatternMatches
a|ba or b
.Any character (except a line break)
^Beginning of text; or line if m flag is used
$End of text; or line if m flag is used
\ABeginning of text
\ZEnd of text
[chars]Any character between the brackets. Ranges can be specified with a hyphen, like 0-9. Character classes like \d and \s can also be used (see below).
[^chars]Any character NOT matching the ones between the brackets.
\bWord break
\BWord non-break
(pattern)Capturing group: the pattern must match, and its contents will be captured in the group list.
(?:pattern)Non-capturing group: Match the pattern, but do not capture its contents.
\1 through \9Backreference; \N is whatever was captured in the Nth capturing group.
Modifiers
Modifiers are "greedy" by default, looking for the longest match possible.  When following a word, they only apply to the last character.
a*Match a zero or more times
a+Match a one or more times
a?Match a zero or one time
a{n}Match a, exactly n times
a{n,}Match a, n or more times
a{n,m}Match a, n to m times
modifier?Make the previous modifier non-greedy (match as little as possible)
Escape codes and character classes
\xNNEscape code for a single character, where NN is its hexadecimal ASCII value
\uNNNNEscape code for a single 16-bit Unicode character, where NNNN is its hexadecimal value
\UNNNNNNEscape code for a single 21-bit Unicode character, where NNNNNN is its hexadecimal value
\dAny digit 0 through 9
\DAny character except a digit or line break
\lAny letter A through Z, case-insensitive
\LAny character except a letter or line break
\wAny identifier character: digits, letters, or underscore
\WAny character except an identifier character or line break
\sAny space character
\SAny character except a space or line break
Assertions
(?=pattern)Look-ahead: Require this pattern to come next, but don't include it in the match
(?!pattern)Look-ahead: Require this pattern NOT to come next
(?<=pattern)Look-behind: Require this pattern to come before, but don't include it in the match (must be a fixed byte length)
(?<!pattern)Look-behind: Require this pattern NOT to come before (must be a fixed byte length)

The optional flags can be any combination of these:


FlagMeaning
iCase-insensitive matching
gGlobal: In Find() subsequent calls will start where this left off, and in Replace() all matches are replaced.
mMulti-line: ^ and $ refer to the beginning and end of a line, respectively.

After calling Find() on a /regex datum, the datum's
group var will contain a list—if applicable—of any
sub-patterns found with the () parentheses operator. For instance,
searching the string "123" for 1(\d)(\d) will match
"123", and the group var will be list("2","3").
Groups can also be used in replacement expressions; see the
Replace() proc for more details.



Understanding the renderer

To get the most out of BYOND's visual effects, it helps to understand how
the map is displayed.

Every atom has an appearance that holds
all of its visual info (and sometimes a little non-visual info). This
appearance has to be turned into sprites in order to be rendered.

Although many atoms need little more than a simple
icon and
icon_state and produce only a
single sprite, some are more complex with overlays, underlays, maptext, etc.
Also there may be image objects and
visual contents involved, although
they're not part of the atom's appearance.

For a simple icon and icon_state, just one sprite is
generated. The client looks up the icon it's given. Then it looks up an icon
state, which may be influenced by whether the atom is moving or not since you
can have moving and non-moving icon states. Then it determines which
direction to draw and which frame of the icon's
animation (if any) to use.

So with several simple icons, and not worrying about layers for now, a list
of sprites lays out like this:


Atom #1
Atom #2
&vellip;
Atom #N

Overlays and underlays
Now let's consider what happens when an appearance has overlays.


Underlay #1
&vellip;
Underlay #N
Main icon
Overlay #1
&vellip;
Overlay #N

The underlays list is processed
first, then overlays. These lists
contain appearances themselves, rather than actual atoms. This means that
overlays are recursive: an overlay can have overlays itself. To picture how
that works, just replace
one of the overlays above with another list.


Underlay #1
Underlay #2
Main icon
Underlays of overlay #1
Overlay #1 icon
Overlays of overlay #1
Overlay #2

Image objects and visual contents
Any atom can have an image object attached, which can
be shown to only specific players. Most atoms, and image objects, can have
visual contents that display other atoms
as if they're overlays.


Underlays
Main icon
Overlays
Image objects
Visual contents

As you see this is very similar to overlays. Just like overlays, image
objects and visual contents have appearances of their own (and may also have
their own images or visual contents), so this may be recursive as they add
new overlays, etc.

A couple of things to keep in mind:


If an image object uses the override
  var, it will replace the main appearance's icon and overlays, although it
  won't replace other images or visual contents.
An object in visual contents can use
  vis_flags to set
  VIS_UNDERLAY and move itself before the parent's underlays.

Maptext and particles
Any appearance may have maptext
attached. That maptext draws above the icon but is grouped with it. That
grouping will be discussed further below.

Particle effects also get grouped with the main icon in a similar way to
maptext.

For simplicity, from this point forward the diagram will just treat underlays,
overlays, image objects, and visual contents as overlays.



Main icon
Maptext
Particles

Overlays

Color, transform, and filters
An appearance's color and
alpha vars (from here forwarded
they'll just be referred to by color) and
transform are inherited by any
overlays, which also includes images and visual contents. You can avoid that
inheritance by giving those overlays special
appearance_flags:
RESET_COLOR, RESET_ALPHA, and RESET_TRANSFORM.

The appearance's filters are only applied to the main icon.



Main icon
Maptext
Main color, transform, and filters apply


Overlays
color and transform are inherited from Mainfilters are not inherited from Main


When color and transform are inherited, they "stack". The
inherited color and transform values are applied after those of the overlays.

KEEP_TOGETHER and KEEP_APART
There are times it's desirable for an appearance and all its overlays to be
treated as a single unit so any colors or filters can be applied all at once.
One simple example is if the appearance has an alpha of 128 to make it
translucent, you probably want to draw the whole atom faded instead of drawing
each sprite faded, one on top of the other.

By using the KEEP_TOGETHER value in
appearance_flags (called KT for
short), an appearance will group all of its underlays and overlays together.
If this is an atom with image objects and visual contents, those will be
grouped with it as well.



KT group
Main color, transform, and filters apply

Main icon
Maptext

Overlays


With KEEP_TOGETHER all of these sprites are rendered to a
temporary drawing surface, and then the main appearance's color,
transform, and filters are all applied to the combined
drawing. This comes with a trade-off, since you can no longer use flags
such as RESET_COLOR to opt out of inheritance.

If an overlay doesn't want to be part of a KT group, it can use the
KEEP_APART flag (KA for short). If there are multiple nested
KT groups, KA will only escape the innermost group.

If an overlay inside a KT group has a different
plane than the group's owner, it
will be separated as if it defined KEEP_APART, except it can
escape multiple nested groups.

Layers and planes
Any appearance can have a layer
or plane, and these influence how
it gets sorted. (There's also a concept called a "sub-plane" that's
influenced by whether an atom is a
HUD/screen object or special layers like
BACKGROUND_LAYER.)

If a sprite is created with FLOAT_LAYER (any negative value
counts as a floating layer) its layer has to be resolved, or "unfloated".
The main sprite for an atom can never float; it has to have a real layer.
Its overlays and underlays with floating layers will reorder themselves in
numerical order, then look for the next closest sprites in the rendering
list that has a non-negative layer.

A similar process happens with FLOAT_PLANE. Planes can have
negative values but FLOAT_PLANE and the values close to it are
special. Sprites with floating planes have to resolve those as well.

Once all atoms that will appear on the map are assembled into a rendering
list of sprites, the order in which they're rendered on the map is determined
in this order:


The plane var matters most.
Subplane is counted next. E.g., HUD objects render above non-HUD objects.
Depending on world.map_format, layer or physical position determine the drawing order from here.
After everything else has been checked, the order the sprites were generated in is the final tie-breaker.

In a typical topdown map, layer is basically all that matters
after the plane and subplane are taken into account. There is a legacy
concept called micro-layers that helps break ties between sprites with the
same layer; for instance if an atom is moving it's usually desirable to
draw it above other atoms with the same layer; this applies only to topdown
maps.

Plane masters
Sometimes it's helpful to group multiple sprites on one plane as if the
plane itself were a KT group. For this,
appearance_flags has a value
called PLANE_MASTER. An object with this flag will act as a "parent"
for everything else on the plane. All other sprites on the plane will be
grouped together and rendered on a temporary drawing surface, and then the
plane master's color, transform, and filters will
be applied.

A plane master does not, however, get an icon or maptext of its own;
they're simply ignored. It can have overlays added to the group.

Advanced topics
There are other topics not covered in this article, such as
render targets and special map formats.
Any details on how those features impact rendering are discussed in their
own articles.



Side-view maps

The side-view map format is used for 3/4 perspective, where the map is
basically similar to a top-down view but is usually foreshortened. Just like
with isometric projection, tiles that are closer to the bottom of the screen
are considered to be closer to the viewer. This is a form of pseudo-3D in
which the 2D icons used by BYOND can be arranged in a way to give the
appearance of three dimensions.

It is important to remember that this is an illusion of 3D, not real 3D.

The layer var behaves much the same way it does in
ISOMETRIC_MAP mode.See isometric maps
for more information.

When using this mode you may want to use a foreshortened
world.icon_size, like a 32x24 format instead of 32x32 for example,
and use taller icons for any vertical structures like walls or buildings. If
you set world.icon_size to use foreshortening, then pixel_y
(or pixel_x, depending on the orientation of client.dir) will be
adjusted for you; the same applies to step_x and step_y.
For example, with world.icon_size set to "64x32", the
physical tile—what you would see if you were to look at it
straight down from above— is considered to be 64x64, so you would need
pixel_y=64 or step_y=64 to offset by a whole tile. This
adjustment does not apply to screen objects, pixel_w, or
pixel_z.



Tiled icons

In BYOND 3.0, any file like a large .bmp would be treated like a regular
icon that had been broken up into several tile-sized icon states. All tiles
then were 32x32 pixels. An image that was 100x100 would therefore take at
least 4x4 tiles to display. The icon was padded to the right and the top with
blank space to become an even multiple of 32x32, and then broken up into
sections. The lower left section was given an icon_state of "0,0",
the next to the right was "1,0", and so on, up to the upper right
which was "3,3". Another icon state, a 32x32 thumbnail of the big
image, was also included.

BYOND 4.0 expanded on this concept by allowing icons to be defined that had
individual graphics bigger than 32x32, and it would break each one up into
tiles just like 3.0 did. If an icon had a state called "open" then it
might break down into "open 0,0", "open 1,0", and so on,
while the actual "open" state would be a thumbnail image. To show the
whole image, you would have to have a separate atom or overlay for each
individual tile.

In newer versions, breaking big icons into tiles is no longer done by
default. Instead, icons are shown and manipulated in their
native size. To use the old method of breaking
icons into tiles, set world.map_format to TILED_ICON_MAP.
This is the default for all projects compiled before version 455.

When using tiled icons, there are some important things to note:


You need to use extra atoms or overlays to show any icon bigger than a
    single tile, where each atom/overlay shows an individual tile-sized piece
    of the big icon.
The icon_state names of each tile are always the original name followed
    by a space, followed by x,y tile coordinates such as 0,0 or 2,1, so the
    northeast corner of "flag" might for instance be
    "flag 3,2". If the original icon_state had no name, the space is
    left out and only the x,y coordinates are used.
Every icon's size is a multiple of world.icon_size. If an icon of an
    incompatible size is used, it will be padded to the nearest full tile
    size.
Crop() and Scale() always pad their results to the
    nearest full tile size.
icon.Insert() can insert a single-tile icon into a multi-tiled
    big icon using the appropriate icon_state; e.g., inserting into
    "door 0,0" will replace the southwest corner of the
    "door" state.
Using the icon() proc, you can extract a single tile from a
    multi-tiled big icon.

This example shows a big icon being applied to an atom in tiled mode, as
overlays:

Example:

// icon is 3 tiles wide by 2 high
icon_state = "0,0"

// A temporary object used for the overlays
var/obj/O = new
O.icon = icon
O.layer = FLOAT_LAYER

for(var/tile_y=0, tile_y<2, ++tile_y)
   for(var/tile_x=0, tile_x<3, ++tile_x)
      if(tile_x && tile_y)
         O.pixel_x = tile_x * 32
         O.pixel_y = tile_y * 32
         O.icon_state = "[tile_x],[tile_y]"
         overlays += O



Topdown maps

By default, BYOND displays all maps in top-down format, so
world.map_format is set to TOPDOWN_MAP unless you say
otherwise. This view means players are looking down on the map, and
"north" corresponds to the top of their screen. (This can be changed by
setting client.dir.)

A related map_format, used by older games, is TILED_ICON_MAP. This
is also topdown but it handles icons differently.

In this form, the layer var behaves exactly as you would expect:
Icons with a lower layer are drawn beneath icons with a higher layer. The only
exception is when you use big icons, which will
be drawn above any other icons on the same layer. Also an atom's underlays will
be drawn behind it unless their layer is changed, and its overlays will draw in
front of it unless otherwise stated.

Topdown mode also guarantees that world.view or client.view
will set the exact screen size used by the HUD, except for HUD objects that
appear outside of the normal bounds.

Screen objects (also called the HUD) cannot be intermixed with topdown
icons. They will appear on top of other icons, unless using a lower plane or a
special layer like BACKGROUND_LAYER.



TOPDOWN_LAYER

TOPDOWN_LAYER is a special high value that can be added to the regular layer
of any atom. This is only available when using a non-topdown world.map_format,
such as isometric mapping.

The purpose of this value is to make an atom appear as if it belongs in a
top-down map, when using a map_format other than TOPDOWN_MAP or TILED_ICON_MAP.
This can be handy for title screens, or for special battle maps or the inside
of a building in an RPG.

When using this special layer, it should be added to the layer an atom
normally uses. For instance a turf should have a layer of TOPDOWN_LAYER +
TURF_LAYER. Usually you will want one part of the map to have TOPDOWN_LAYER,
and for players to be unable to walk to there from the regular map. Mixing
topdown icons and icons in the normal map_format in view of each other could
look very strange. For safety's sake, the easiest thing to do is to keep them
on separate z layers.

This can be mixed with EFFECTS_LAYER. Anything in TOPDOWN_LAYER will
display on top of EFFECTS_LAYER, and TOPDOWN_LAYER + EFFECTS_LAYER will be
above both.

This can also be mixed with BACKGROUND_LAYER, which takes priority over
everything else.

Images or overlays with FLOAT_LAYER can be left alone. They will
automatically have the same layer as whatever atom they are attached to.



Unicode

BYOND was originally written to handle 8-bit ("ANSI") characters only.
However as time has marched on, Unicode has become ubiquitous for supporting
multiple languages, special characters, and emojis. To adapt to this, BYOND
now supports Unicode.

When ANSI was king, every character was exactly one byte in width, because
the only valid characters were between 1 and 255. (And technically, BYOND
reserved 255 for its own use.) Now, BYOND uses an encoding called UTF-8 to
store characters that can't fit in one byte.

UTF-8 breaks up characters with codes of 128 or higher into multiple
bytes, like so:


Character codeSize in bytes
0 - 0x7F1
0x80 - 0x7FF2
0x800 - 0xFFFF3
0x10000 - 0x10FFFF4

Text handling
Importantly, BYOND's text procs are based on the byte position, not the
character position which may be lower. In other words,
length("abcdéfg") is greater than 7; it's 8, because
é takes up 2 bytes in UTF-8. That also means f is at
position 7, not position 6.

Why do the text procs work with byte position instead of character
position? Because ultimately, it's faster. Going by character position would
require counting every byte in a string (at least when it uses UTF-8) until
the right character position was found. This would be detrimental to
performance in most cases.

For the most part, this distinction should be fairly invisible to you.
Most code isn't going to encounter problems, but if you do a lot of text
processing you should be aware of it.

In particular, text2ascii()
returns the Unicode value at a specific position, which may cover several
bytes. If you loop through a string calling this proc for each character,
you'll have to make adjustments for cases when multiple bytes have been
read.

The read-only [] index operator also uses byte positions.

If you read a byte or cut text at an inappropriate point, any broken
characters resulting from the cut will be turned into the Unicode
replacement character � which is 0xFFFD.

_char procs
Most of the text handling procs have slower _char versions (e.g.,
copytext_char) that use character positions instead of byte
positions.

These should be used sparingly if at all; whenever it's possible to use
byte positions, you should. When you do use a _char version of a
proc, prefer using -offset instead of
length_char(text)-offset for positions near the end of the string.
Most text procs allow negative position values that count backwards from the
end, and counting a small number of characters backward is faster than
counting a lot of characters going forward.

Old code
Code written in ANSI will be up-converted to UTF-8 by Dream Maker, based on
your current locale when the code is loaded.



User interface skins

BYOND games used to have very limited interface options, all effectively
sharing the same layout. In BYOND 4.0, skins were introduced, allowing
developers more control over the layout.

A skin consists of macro sets for
keyboard/gamepad input, menus, and windows and/or panes. All of these are
considered controls that a game can interact with
via winset(),
winget(),
output(), and a few other procs.

About the simplest possible skin is a single window with a single
map control, and a single macro set.



Client commands
Several commands can be executed on the client that are not verbs, but
instructions for Dream Seeker. Some of these commands have detailed syntax
described in their own reference entries.


Client commands have a special syntax that allows you to query information
from the skin and include it directly in the command, as if you had called
winget(). Embedded expressions look like
[[expression]] in your command text. Some commands have
built-in data that gets filled in via [[*]]. See
embedded winget for more information.



.add-particles (client command)


Immediately spawns a batch of particles for a known particle set.

The object parameter is a reference string for the
object that holds the particles.

A negative count is allowed, which will absorb some ordinary particle
spawns.

.add-particles [0x200004f] 50
If the object isn't known to the client, nothing will happen.



.output (client command)


Sends output to a control. The text does not need quotes, but any
backslashes, newlines, and tabs should be escaped with a backslash. This works
similarly to the output() proc. If text is
omitted, the control is cleared.

Here is an example of using a map control's
on-status event to set a
label rather than using the window's own statusbar.

.output statuslabel [[* as escaped]]


.sound (client command)


Plays, stops, or modifies a sound. This command can be used for instance to
play a click sound when using mouse macros, for instance, without waiting for
the server to initiate the sound which would introduce a small delay.

.sound 'click.ogg'
The file can be none or - when updating or stopping a
sound. Any options should be separated by spaces; most are in a
name=value format, as seen below.

Supported options are:


*T represents a true/false value. True values include true, on, or 1. False would be false, off, or 0.



.winset (client command)


Sets skin parameters like the winset() proc.
You can set more than one parameter by separating them with semicolons.

This command also allows you to use conditional expressions, like so:

condition ? choice1 : choice2
The condition is the same as any other parameter you might use in
.winset, but instead of setting the parameter, it checks to see if
it's true. If so, then the parameters in choice1 will be set.
Otherwise, the parameters in choice2 are set. This example makes the
window background red if bigbutton is checked.

.winset "bigbutton.is-checked=true ? window.background-color=#ff0000 : window.background-color=none"
If you want to look for values that don't match instead of values that do,
use != instead of = in the condition.

.winset "bigbutton.is-checked!=false ? window.background-color=#f00 : window.background-color=none"
The choice2 item is optional.

.winset "bigbutton.is-checked=true ? window.background-color=#f00"
Because it's often useful to do more than one thing at a time,
choice1 and choice2 don't have to be just one parameter. You
can use multiple parameters, but they are separated with a space instead of a
semicolon. (A semicolon indicates the conditional expression is over.)

.winset "bigbutton.is-checked=true ? window.text-color=#fff window.background-color=#f00 : window.text-color=none window.background-color=none"


Embedded Winget

Commands that are initiated by the skin (like button.command, map.on-show,
etc.) have a special syntax that allows you to include information that would
normally require a winget call. By including [[something]] in
the command, the double-bracketed text will be replaced by the result of
running a winget on that parameter.

A value of [[id.parameter]] will run a winget on the control with
the given ID. Just using [[parameter]] will run a winget for the
control that initiated this command. You can also use parent in place
of the ID to do something with the parent of the control, or parent.id
for access to a sibling control. Position and size parameters can be further
broken down by appending .x or .y to get at the numbers
directly.

Several commands already support some special cases like [[*]] or
[[width]] or such, where the special-case values are relevant to the
command. An example is that in on-size the value of [[*]] is
a size value. The Any macro, gamepad macros, and mouse macros, also support this
syntax; see macros for more info.

You can choose how embedded wingets get formatted by following the value with
as and a type, such as [[window.size as string]]. There are
several types you can use, and different types of parameters get formatted differently:


The arg type is the default, unless the [[...]]
expression has double quotes on both sides, in which case escaped is the
default.



controls (skin)


Creating/Destroying at runtime
Controls can be created or deleted at runtime. (Only controls you created
during runtime may be deleted.) To create a control, call
winset() using the
id of the new control, and the
parameter list should include type,
parent, and probably also
pos,
size, and any
anchors.

To delete the control again, set its parent to a blank value.

Menu items and macros work similarly, except they have no positional info.
For those, the name parameter is
important when you create them, and you will either need
command or (for macros)
map-to to do anything with them.



bar control (skin)
A progress bar or interactive slider. This can be made to use several different orientations. Its value can be read or set as a percentage from 0 to 100.




browser control (skin)
A browser panel integrated into the skin.


Browsers are capable of displaying HTML documents, and can also interact with the skin.

Browsers and popups
A longstanding behavior of BYOND is the ability to create a new browser window by sending an extra argument to the browse() proc. Since the advent of skins in BYOND 4.0, this behavior was kept. When you create a new browser popup, the window name you specify for the popup is used for the name of a new window control, and within that window there will be a new browser control simply called browser.

If you want to interact with the new browser, its full "decorated" id is windowname.browser.

Running JavaScript from DM
Sending output() to a browser will send a document to display there, but if you follow the browser's control name with a colon and a function name, you can call a JavaScript function in the document displayed within that browser.

Example:

var/list/info = list("name"="fridge", "power"=12)
// send {"name":"fridge","power":12} to a JavaScript function
usr << output(url_encode(json_encode(info)), "mybrowser:myJSfunction")

The text that you send as output will be parsed like URL parameters, where mutliple arguments to the function are separated by & or ;, which is why url_encode() is wrapped around the json_encode() call in this example.

More browser options
These topics cover more advanced uses of the browser control.




BYOND object (JavaScript)

The BYOND object is a built-in shortcut for interacting with the client
via JavaScript in a browser control. It contains the following methods:

BYOND.winset(id, params)
Performs a winset, where
id is the ID of the control to change (or null for global settings),
and params is an object with parameter,value pairs such as
{"text-color": "red"}. Parameters can use camelCase, where a capital
letter indicates where a hyphen would normally go, e.g. "textColor"
and "text-color" are the same.

Example:

// uncheck a button from JavaScript
BYOND.winset("inventory_button", {isChecked: false});

BYOND.winget(id, props)
Sends a winget, where
id is the ID of the control to retrieve (or null for global
settings), and props is a single property or an array of properties
to retrieve. As with winset, camelCase is allowed, but the result
will not use camelCase.

Returns a Promise object, so this call can be used with the await
keyword or followed by then(). The result inside the promise is an
object with parameter,value pairs, such as
{"background-color": {value: "#ff0000", red: 255, green: 0, blue: 0, isDefault: false}}.

Example:

// get a button's status JavaScript
let buttonData = await BYOND.winget("inventory_button", "isChecked");
if(buttonData["is-checked"]) {
    alert("The button is checked!");
}

BYOND.command(command)
Initiates a client command. This is basically just a shortcut for using winset to run a command.

Example:

// play a sound
BYOND.command(".sound 'ding.ogg'");



byondStorage (browser control)

A replacement for localStorage that can be used to hold
information for reuse in later sessions of the same game. (This must be
enabled via browser-options with the
winset() proc.)

There are three actual storage objects you can use:


hubStorageStores info that can be shared for all games falling under this same hub entry. (This will not be available without a hub path.)
serverStorageStores info that can be shared for all games with the same hub path using this same server address.
domainStorageSame as serverStorage, but ignores the connection port.

Interacting with these storage objects is done in JavaScript, the same way
you would use localStorage or sessionStorage.

Note: Technically localStorage does work, but because of the way
BYOND handles browser controls it acts more like sessionStorage in
practice.



winset and winget (JavaScript)

Browser controls can interact with the skin via JavaScript, by setting window.location to a special URL.

Winset
byond://winset?id=[control ID]&[property]=[value]&...
This works like an ordinary winset() call from the server. If id is omitted, it's the same as a winset with a null ID. You can also leave the id blank if you use "fully decorated" property names such as mybutton.is-checked instead of just is-checked.

Any text you use other than letters, numbers, hyphens, commas, and periods should be encoded via the encodeURIComponent() function in JavaScript.

Winget
byond://winget?callback=[callback function]&id=[control ID/list]&property=[property/list]
In this winget, the IDs and properties you want can be separated by commas if you want to retrieve more than one. The winget operation works via a callback function you must define in JavaScript. The callback is given just one argument, a JavaScript object with all of the properties you requested. For example, this URL:

byond://winget?callback=wgcb&id=button1&property=is-checked,size,background-color
...might send this to the callback function wgcb:


{
    "is-checked": true,
    "size": {
        "x": 60,
        "y": 20
    },
    "background-color": {
        "value": "none",
        "isDefault": true,
        "red": 236,
        "green": 233,
        "blue": 216,
        "alpha": 255,
        "css": "#ece9d8"
    }
}

The property names will be in the same format you would expect from winget(), so when you're looking at multiple elements' properties, you'll get the full names in id.property format. The values are always sent back in a convenient form for JavaScript to work with; in the case of size, position, and color these will always be objects.

An optional control parameter for the winget call can be used if you want to send data to a callback in a different browser control.


button control (skin)
A button that can be pressed to run a command, or possibly toggled.




child control (skin)
A container that can hold one or two panes. If it holds two panes, a splitter may appear between them. This control can therefore be used to subdivide a window or pane into smaller units.




grid control (skin)
A grid that contains multiple cells that can show various kinds of output data.


Sending output to a grid looks like this:

Example:

// output to column 3, row 2
winset(usr, "thegrid", "current-cell=3,2")
usr << output("Text", "thegrid")

// or even easier:
usr << output("Text", "thegrid:3,2")

// when is-list is true:
usr << output("5th item", "thegrid:5")

You can output an atom to the grid, which can be clicked, dragged, etc.
However, you should make sure that atom is not temporary and will
persist until you no longer need it, or else the server may recycle it and
the object in the cell will either disappear or be impossible to interact
with anymore.

There are some limitations to output in grid controls:


Only one character style (font, color, bold, etc.) may appear within a single cell.
A cell is either a link, or not.
One image is allowed per cell.
A cell can hold an object (atom), sent to it via the output() proc, which can be clicked, dragged, etc.; it will not act as a link.
The same margin is used all around the cell, not different margins for left, right, top, bottom.
There will always be a 1-pixel space for grid lines, whether they're shown or not.



info control (skin)
The classic BYOND statpanel, which contains both stat and verb tabs. This
is technically a 3-column grid with a variable number of rows.


Output to a statpanel is done via the stat()
and statpanel() procs, during
mob/Stat().

The same limitations that apply to grid
output apply here.

Info controls can now be split so that one displays stats and another
handles verbs.



input control (skin)
A text box into which the user can type. By default this is used for sending client commands, but it can be used for other purposes as well.


Note that when in "standard" mode of accepting user commands, built-in verbs like .click, or local commands like .winset, are not accepted when typed in. This kind of command can still be entered manually through the Client menu of the Options & Messages window.



label control (skin)
A text label that appears on the skin.




macro control (skin)
A keyboard/gamepad/mouse macro, usually designed to run a command. The control is a means of interacting with the macro as an object, allowing some of its properties to be changed at runtime.




main control (skin)
A container for other controls. The Main control takes two forms: a window or a pane. 

A window exists independently and can be moved around on the screen. A pane has to be used within another container control such as a Child or Tab control.


The font parameters have no impact on a window's statusbar or titlebar; those are drawn by the operating system.



map control (skin)
A map that will display icons from the game.




menu control (skin)
A menu item, that when activate will run a command.




output control (skin)
Displays text output.




tab control (skin)
A tab control, where each tab holds a different pane.




macros (skin)
Macros are used to convert keyboard and gamepad events into actions. There
are two ways this works: A macro can run a command, or in some cases (such as
gamepad controls) it can be used to remap one control to another.

A collection of macros is called a macro set, and the window currently in
use defines which macro set will be used via its
macro parameter.

Macros can be changed at runtime. If a macro does not have an
id, you can refer to it by its key
combination (name). If you have a
macro set named macro1 and have a Ctrl+E macro for instance,
you could use winset() with
"macro1.Ctrl+E". See the Macro
control for information on which parameters you can change with
winset().

The name of the macro is actually the full key combination as it
would appear in the macro editor, like CTRL+E, Space+REP, or
Alt+Shift+F1. This is not case-specific and it doesn't matter where
you put modifiers like CTRL+, SHIFT+, etc.

The Any macro
Oftentimes it's desirable to keep track of key presses yourself rather than
have a hundred different macros defined. BYOND makes this possible via the
Any and Any+UP macros, which respond to any key or gamepad
button. UP is the only allowed modifier for this macro, since other
modifier keys are handled by this same macro.

Typically, you will want to use set
instant=1 on the verbs that will be tied to the Any macro, so that
keyboard input doesn't queue up and lag behind.

In the command that goes with
this macro, [[*]] will be replaced with the name of the key or gamepad
button that was pressed/released. (See
embedded winget for more details on the
[[...]] format.)

Mapping
The map-to parameter is used
by mappings, which are like macros but are used to convert gamepad
inputs easily and quickly to keyboard inputs. E.g., GamepadLeft can
map to West which is the left arrow key. A set of default mappings
will be added automatically at runtime if you don't include any gamepad
mapping in your project.

Gamepads
BYOND will support up to four gamepads, and breaks up their input into the
following categories:


Buttons: Buttons on the controller that are either pressed or not pressed.
Directions: Directions pressed on the D-pad, which act like buttons. Diagonals are also included.
D-pad: The D-pad itself, which can be used to read a dir number.
Analog: The analog sticks (BYOND supports left and right).

See the list of available macros below for information on how to harness
these inputs.

To let a user configure their gamepad, you need to call the client-side
.gamepad-mapping command. Or, if they
have access to the Options & Messages window and Dream Seeker's default
menus, they can reach it from there. However it's a good idea to make this
easy for them to find. Several common gamepads are already known by BYOND.

There is also the GamepadRaw macro, which is similar
to Any in some ways and will avoid doing any processing (e.g.
checking for dead zones on the analog sticks) so you can handle all input
yourself. GamepadRaw does not rely on BYOND's controller
configuration, so it will not, for instance, know that button 0 should be
GamepadFace1. See below for more information on how to use this
macro.

Mouse macros
You can add macros (not local player-defined ones) for any of the mouse
input commands, thereby bypassing the normal mouse verbs. This can be helpful
for designing custom setups where you don't want to have to parse the normal
parameter string that provides most of the info, and instead want to provide
data directly to the verb. You will want set instant=1 on any such
verb.

Mouse macro commands use the [[...]] syntax to embed values, just
like embedded wingets. These are the
values you can include in a mouse macro:


Embedded keywordMeaning
actionName of the mouse action (e.g. MouseDown, MouseMove, etc.).
srcObject the mouse is touching, or dragging/dropping.
locTurf or statpanel that src is over; in a drag-drop you should split this into src.loc and over.loc.
buttonMouse button used for this action, if any: left, middle, or right.
dragMouse button currently used for dragging.
buttonsMouse buttons currently down or involved in this action, separated by commas.
keysModifier keys currently held (shift, ctrl, alt), separated by commas.
overObject the mouse is over in a drag/drop operation.
idControl ID; in a drag-drop you should split this into src.id and over.id.
iconThe icon offset (starting from 1,1 at the lower left) where the mouse action occurred.*
tileThe tile where the mouse action occurred, if relevant.*
visPixel coordinates relative to the icon's position on screen (same as icon but without taking transform into account).*
screen_locThe regular screen_loc cordinate string.*
screenscreen_loc coordinates but entirely in pixels starting at 0,0 from lower left.*
screen_tilescreen_loc coordinates but only the tile number starting at 1,1.*
screen_offsetscreen_loc coordinates but only the pixel offset from the tile, starting at 0,0.*
deltaWheel changes in a mouse wheel command.*
left, right, middle1 if this button is down or involved in this action, 0 otherwise
shift, ctrl, alt1 if this modifier key is held, 0 otherwise
link1 if the mouse is over a maptext link, 0 otherwise
cellGrid cell involved in a mouse action. In a drag/drop action, src.cell is the dragging cell and over.cell is the drop cell.
drag-cellAlias for src.cell.
drop-cellAlias for over.cell.
paramsParameter list that would be sent with the default mouse command.
* Coordinate values are comma-separated, but you can follow them with .x or .y to get the individual X and Y numbers.

An example mouse macro command might look like this:

my-mousedown-verb [[src]] [[button]] "keys=[[keys as params]];drag=[[drag as params]]"
And the verb to go with it looks like this:


client
    // "in src" is the same as "in usr.client" here
    verb/my_mousedown_verb(object as anything in src, button as text, params as text)

In the example, the src value is a reference such as you would get
with the ref() proc. It can be used as a verb
argument directly and won't be enclosed by quotes by default. The button
value is a string and the default formatting will put quotes around it. The
keys and drag values were given the as params format
specifier so they would behave as part of a parameter
list.

In drag/drop actions, you can precede any value with src or
over if there may be different information for the dragged object and
the mouseover object/location. This also applies to things like keys,
which by default will be the currently held keys but you can use src.keys
to refer to the values from when the drag began.

Available macros
This is a list of all keys and gamepad events that can be used in macros.



Macro modifiers are part of the macro name, and control the conditions in which the macro will fire.
ModifierMeaning


SHIFT+This macro only counts if either Shift key is pressed.
CTRL+This macro only counts if either Ctrl key is pressed.
ALT+This macro only counts if either Alt key is pressed.
+REPIf a key/button is held down, this macro repeats.
+UPThis macro fires when the key/button is released.


Keyboard keys are the garden-variety macros. (This list is abridged to exclude keys probably no one has.)
KeyDescription


A - ZLetter key
0 - 9Number key
Numpad0 - Numpad9Numpad numbers
NorthUp arrow
SouthDown arrow
EastRight arrow
WestLeft arrow
NorthwestHome key
SouthwestEnd key
NortheastPage Up key
SoutheastPage Down key
CenterCenter key (numpad)
ReturnEnter / Return key
EscapeEsc key
TabTab key
SpaceSpace bar
BackBackspace key
InsertIns key
DeleteDel key
PausePause key
SnapshotSnapshot / Print Screen key
LWinLeft Windows key
RWinRight Windows key
AppsApps key
MultiplyMultiply key
AddAdd key
SubtractSubtract key
DivideDivide / Slash key
SeparatorSeparator / Backslash key
ShiftShift key (when not used as a modifier)
CtrlCtrl key (when not used as a modifier)
AltAlt key (when not used as a modifier)
VolumeMuteMute key
VolumeUpVolume up key
VolumeDownVolume down key
MediaPlayPausePlay/pause media key
MediaStopStop media key
MediaNextNext track key
MediaPrevPrevious track key


Special macros


AnyA special macro that can run a command on press/release of any key or gamepad button. UP is the only modifier allowed. In the command, [[*]] is replaced with the key/button name.*
GamepadRaw*Captures raw input from a gamepad, without regard to the adjustments done by the Gamepad Setup dialog. In the command, [[id]] is replaced by the name of the button or axis changed ("Button0" through "Button15" and "Axis0" through "Axis11"), [[value]] is replaced with the value of the button or axis, and [[*]] is equivalent to [[id]] [[value]].

* If no gamepad mappings are included in a game's interface, the default mappings are used instead, which will map the Dpad buttons to the arrow keys. This will cause the Any macro to register both a gamepad directional button and the mapped key on the same press. If you plan on using macros to capture gamepad input, you may wish instead to map any one of the directional buttons to "None", which will override the default gamepad mappings completely.



Gamepad buttons† can use another gamepad button as a modifier (but not CTRL, SHIFT, ALT), and can be mapped to one or two keyboard keys or mouse buttons.
ButtonDescription


GamepadFace1A (Xbox), X (PS), bottom of diamond
GamepadFace2B (Xbox), Circle (PS), right of diamond
GamepadFace3X (Xbox), Square (PS), left of diamond
GamepadFace4Y (Xbox), Triangle (PS), top of diamond
GamepadL1Left top shoulder
GamepadR1Right top shoulder
GamepadL2Left bottom shoulder
GamepadR2Right bottom shoulder
GamepadSelectSelect / Back
GamepadStartStart / Forward
GamepadL3Left analog click
GamepadR3Right analog click
Directional buttons: only one can pressed at a time, and the diagonal buttons are virtual.
GamepadUpUp button
GamepadDownDown button
GamepadLeftLeft button
GamepadRightRight button
GamepadUpLeftUp+left virtual button
GamepadUpRightUp+right virtual button
GamepadDownLeftDown+left virtual button
GamepadDownRightDown+right virtual button


Gamepad analog sticks† can have commands and/or map to GamepadDir, GamepadDir4, or Mouse. They can use a gamepad button as a modifier. In a command, [[x]] and [[y]] are replaced by coordinates, and [[*]] is replaced by both with a comma for separation.


GamepadLeftAnalogLeft analog stick
GamepadRightAnalogLeft analog stick


Gamepad Dpads†‡ can have commands or are used as mapping targets for analog sticks. A gamepad button can be used as a modifier. In a command, [[*]] is replaced by a direction number, which can be 0.


GamepadDirDpad, converted to one of the eight standard directions.
GamepadDir4Dpad, converted to a cardinal direction.

† All of the gamepad macros defined above apply to the first gamepad. BYOND can now support up to four gamepads, and you can replace Gamepad in the names above with Gamepad2, Gamepad3, or Gamepad4 to access them. Each gamepad also has its own raw macro (i.e., Gamepad2Raw).
‡ If you use a Dpad macro like GamepadDir as a map-to target, you don't have to specify gamepad 2-4 in map-to; the mapping will automatically know that when Gamepad2LeftAnalog is mapped to GamepadDir, it means Gamepad2Dir.



Mouse macros can have commands but not be used as mapping targets.


MouseDownMouse button pressed (replaces MouseDown verb)
MouseUpMouse button released (replaces MouseUp verb)
MouseClickA click action has occurred (replaces Click verb)
MouseDblClickA double-click action has occurred (replaces DblClick verb)
MouseOverMouse has moved over a new icon or entered/exited a control (replaces MouseEntered and MouseExited verbs)
MouseMoveMouse has moved to a new pixel of the same icon (replaces MouseMove verb)
MouseDragMouse has begin dragging or is over a new drop target (replaces MouseDrag verb)
MouseDragMoveMouse is dragging and is over a new pixel of the same drop target (replaces MouseDrag verb in situations where MouseMove would apply)
MouseDropMouse drag has been released over a target (replaces MouseDrop verb)
MouseWheelA wheel movement has occurred (replaces MouseWheel verb)


Mouse targets can only be used as mapping targets for another macro.


MouseThe mouse cursor, mappable by a gamepad analog stick.
MouseLeftButtonLeft button, mappable by a gamepad button.
MouseRightButtonRight button, mappable by a gamepad button.
MouseMiddleButtonMiddle button, mappable by a gamepad button.




parameters (skin)
Controls can be interacted with via winset()
and winget() to change or read various
parameters.

Parameters come in a few different formats:


Boolean: true or false
Numeric: any number, sometimes allowing decimal or negative numbers
String: text
Position: x,y
Size: widthxheight
Enumerated: one of several text choices, sometimes accepting numbers or true/false values as shortcuts

The list of all controls which shows which
parameters are universal, and each individual control type lists additional
parameters that apply to that type specifically.

Note: In any parameter's "Applies to" section, "all" refers to positionable
controls only, not Macro or Menu controls. Macro and Menu will be listed
separately if supported.



align parameter (skin)




Default alignment of text/image, both horizontal and vertical.

A BYOND direction flag like WEST may be assigned to this parameter, or 0 for center alignment.



allow-html parameter (skin)



Info control: Allow HTML tags to be used in stat() info. The same limitations apply as to the Grid control.

Label control: Currently, the label control will not actually use the HTML; it will simply strip it out. Full support may appear in a later version.



alpha parameter (skin)




Opacity of the window, from 0 (invisible) to 255 (opaque).



anchor1, anchor2 parameters (skin)




Anchors the control within the window or pane. If the anchor is not none, it is expressed as pecentages of the container's width and height. For example, an anchor of 100,100 means that the X and Y position are tied to the lower right of the container, and 50,0 is tied to the top center.

Setting only anchor1 will control the position of the control but won't affect its size.

Setting anchor2 as well will allow you to stretch the control as the container's size changes. You can think of this anchor1 controlling the top left corner, and anchor2 the bottom right corner.



angle1, angle2 parameters (skin)




The angle of the bar control's arc when its dir is clockwise or counterclockwise. Angles are measured clockwise from due north, so 0 is north, 90 is east, and so on.

angle1 is the beginning of the arc, and angle2 is the end.



auto-format parameter (skin)



This parameter only existed to inject compatibility scripts into very old versions of the embedded browser. It is no longer used.



background-color parameter (skin)



The control's background color. The exact way this applies depends on the control.



bar-color parameter (skin)



The color of the bar or slider.



border parameter (skin)



Border type around the control or window. May not work the same in all controls.



button-type parameter (skin)




Changes the type of button.



can-check parameter (skin)




If true, this menu item is toggled like a checkbox or radio button when clicked.



can-close parameter (skin)




Allow the window to be closed, and also shows a system menu for the window.



can-minimize parameter (skin)




Allow the window to be minimized.



can-resize parameter (skin)




Allow the window to be resized or maximized.

If is-fullscreen is true, can-resize is ignored, so this value represents the state of the window when is-fullscreen is turned off again.



can-scroll parameter (skin)




Allow this pane to retain its horizontal and/or vertical size and show scrollbars if necessary, instead of shrinking to fit the container.



command parameter (skin)



Command executed when this control is activated.

For the Input control, whatever the user types in follows this command. If your command starts with an exclamation point !, everything after the ! is shown as a default prompt that may be cleared by the user.



cell-span parameter (skin)




The span of the current grid cell; it can be merged with cells to the right and down. If is-list is true, this setting is ignored. This setting is only available at runtime.



cells parameter (skin)




The number of columns and rows in the grid. Using -1 for either columns or rows will leave that value unchanged.

If is-list is true, this value can be set to a single number.



current-cell parameter (skin)




The active cell. Any output sent to the grid, that is not sent to a specific cell, will go into this cell.

If is-list is true, this value can be set to a single number.



current-tab parameter (skin)



The name of the pane in the active/default tab. If set to a pane that is not currently in this tab control, the pane by that name will be added as another tab.



dir parameter (skin)




The direction/orientation of the bar. As the value increases the bar will move further in this direction.

Shorthand values like cw and ccw can be used, or also numerical BYOND directions.



dpi parameter (skin)




Read-only and unlisted parameter that returns the DPI scaling factor. A value of 1 indicates 100%. This is currently system-wide for the whole application and won't vary by window, but is implemented for windows in case future scaling changes allow them to differ.

This is also a special global parameter. Calling winget() with no id and dpi as the parameter will return the system DPI scaling.

Note: The DPI scale is currently set at the time Dream Seeker starts, and does not change after that.



drop-zone parameter (skin)




True if dragged objects may be dropped here. Default is true for Map, Info, and Grid controls, false for others. When in use, this will be the value of the over_control argument in MouseDrop() if you drop an atom here.

Grids can also add drag-cell and drop-cell to mouse proc parameters. The mouse procs' src_location and over_location arguments are in the form "[column],[row]" (or "[item"] if is-list is true) when dragging to/from a grid cell.

In Info controls, src_location and over_location in mouse procs will be the name of the statpanel tab.



enable-http-images parameter (skin)




Allows images to be pulled from the Web when using the <img> tag; otherwise only locally stored images can be shown.



flash parameter (skin)



Set to a positive number to make the window flash that many times, -1 to flash forever, and 0 to stop flashing.



focus parameter (skin)




This parameter is true if this control currently has focus.

This is also a special read-only global parameter. Calling winget() with no id and focus as the parameter will return the id of the currently focused control, if any.



font-family parameter (skin)



Leave blank to use the default font. This can be used for CSS-style fallback fonts, e.g. "Arial,Helvetica".

You can include fonts in your resource file, making them available to the client, like so:


var/list/extra_resources = list(\
    'myfont.ttf',
    'myfont_bold.ttf')



font-size parameter (skin)




Point size of the font, or leave at 0 for the default size.

The Output control behaves differently for legacy reasons, unless legacy-size is false.



font-style parameter (skin)




Sets the font style. Any combination of the above values may be used, or none of them. Multiple values may be separated by spaces or commas.



group parameter (skin)



Used for "radio" buttons and menu items, where only one of them in the same group may be checked at a time. This value is a text string, or may be left empty.

Buttons in different windows/panes, or menu items in another menu/submenu, are always treated as a different group.



has-stats parameter (skin)




True if this info control contains the statpanels created via stat() and statpanel().

Only one info control can have statpanels.



has-verbs parameter (skin)




True if this info control contains the verbs used in the game.

Currently only one info control can have verbs.



highlight-color parameter (skin)




The color used to highlight moused-over statpanel items or verbs. In grids, this color is used when hovering over objects or links.



icon parameter (skin)




Custom icon used for the window. If no icon is specified, the Dream Seeker icon is used by windows by default.

If this control is a pane, its icon will appear on the tab if the pane is inside a tab control. Lack of an icon will mean no icon appears in the tab.

Note: The Windows .ico format is not used. Only image formats BYOND can already use are supported.



icon-size parameter (skin)




Size, in pixels, of icons on the map. A size of 0 stretches to fit available space.

This parameter has been deprecated. Use zoom instead.



id parameter (skin)



The name of this control. Read-only.

If this is a Main control, the name should always be unique. For others, it is usually still a good idea to use a unique name, but they can be referenced by window.id at runtime.

You can use a colon in front of the type to refer to the default control of a certain type, if one exists, e.g. :map is the default map.



image parameter (skin)



A background image to show in this control.

In the Output control this image is always tiled.

Note: Icons displayed in the output control will not show the background image underneath their transparent parts, but will instead show the background color.
For Label and Main, use image-mode to control how the image is displayed.



image-mode parameter (skin)




Determines how the background image is displayed.



index parameter (skin)



Moves the menu item to the Nth position among its siblings. 0 or less is no change. Write-only.



inner-mouse-pos / mouse-pos parameter (skin)



Read-only.

Reads the position of the mouse cursor relative to the upper left corner of this control, not including the control's borders.

mouse-pos is an alias for inner-mouse-pos.

This parameter is "unlisted" and must be explicitly queried. It won't appear when sending * as the parameter in winget().



inner-pos parameter (skin)



Read-only.

Reads the position where the window's interior contents begin (i.e., not counting titlebar, statusbar, borders, etc.), relative to its outer-pos.



inner-size parameter (skin)



Read-only.

If the control is a window, this refers to its current interior size: i.e., not counting titlebar, statusbar, borders, etc. If it's maximized, this will be the true size of the window interior, as opposed to size which is the interior size once this window is no longer maximized.

If this control is a pane and can-scroll is true, this is the size of the display area not including the scrollbars.



is-checked parameter (skin)




True if the button or menu item is checked. Menu items can set this even if can-check is false.



is-default parameter (skin)




Specifies that this is a default control. This should be true for your main window, and for your primary map, info, output, input, and browser controls.

The default control of a given type can be referenced in winset() and other skin-related procs by the name ":type", e.g. ":map".

Changing this value at runtime should be avoided, especially for windows. Results may be unpredictable.



is-disabled parameter (skin)




Disables the control, menu item, or macro.



is-flat parameter (skin)




Gives this button a flat appearance instead of pseudo-3D highlights.



is-fullscreen parameter (skin)




True if the window should be in fullscreen mode. This suppresses
can-resize, titlebar, is-maximized, and
is-minimized. They will continue to return the values that would apply
if fullscreen mode were turned off.



is-list parameter (skin)




True if the grid is used for a flexible list of items; the number of columns and rows may change to fit them.



is-maximized parameter (skin)




True if the window is maximized.

If is-fullscreen is true, this value represents the state of the window when is-fullscreen is turned off again.



is-minimized parameter (skin)




True if the window is minimized.

If is-fullscreen is true, this value represents the state of the window when is-fullscreen is turned off again.



is-pane parameter (skin)




True if this is a pane that will be used in other container controls, instead of an independent window. Read-only.



is-password parameter (skin)




Hide text with asterisks. Copy to clipboard is not available in this mode, but the text parameter can still read the control's contents.

Note: For obvious reasons, you should never use the same password in a game that you would use anywhere else.



is-slider parameter (skin)




Make this an adjustable slider capable of being changed by the user, instead of a progress bar.



is-transparent parameter (skin)



Make this control transparent.

Transparency support is extremely limited. Only some controls can actually use it, and only when on top of certain other controls.

Bars and labels handle transparency reasonably well, when not on top of other controls (or only on top of other conrols of these types).



is-vert parameter (skin)




The splitter between the two panes in this control is vertical.



is-visible parameter (skin)




True if this control can be seen. The main window should usually be made visible.



keep-aspect parameter (skin)




If stretching a background image, preserve its aspect ratio.



left, top parameters (skin)




The id of the left/top pane in this control. The parameter names left and top can be used interchangeably.



legacy-size parameter (skin)




When true, font sizes are scaled slightly larger for readability, which is legacy (and default) BYOND behavior. Set to false for exact font sizing.



letterbox parameter (skin)




If map auto-scales its icons (zoom is 0), make sure the entire map fits, and fill excess space with the background color.

If letterbox is not enabled, auto-zoom will fill all available space, and any excess will be cut off.



line-color parameter (skin)




The color of grid lines.



link-color parameter (skin)




The color used for links. In some controls visited links may have a different color.



lock parameter (skin)




Allows one pane to "lock" the splitter so if this Child control is resized, the splitter will stay put on that side.



macro parameter (skin)



The id of the macro set this window will use, if any, when it's active.



map-to parameter (skin)



The macro name (e.g., "SOUTH") of a key combo, Dpad, mouse button, etc. that this macro maps to.



max-lines parameter (skin)



Maximum number of lines before the control drops old text to make room for more. 0 is no limit.

An overflow of 5% is allowed, to reduce flicker.



menu parameter (skin)



The id of the menu this window will use, if any, when it's active.



multi-line parameter (skin)



Input control: Create a multi-line input control. Read-only for this control.

Info and Tab controls: Show tabs in multiple rows if there are too many to fit in a single row.



name parameter (skin)



Macro control: The key/gamepad combination such as R+REP, CTRL+Northwest, GamepadLeft.

Menu control: This is the menu item label. A tab character can be used between the name and a keyboard shortcut, like "Help\tF1". (Keyboard shortcuts must be implemented as macros in order to work. This is just a label.) A blank name shows just a separator.



no-command parameter (skin)




True if this input control is for typing only; hitting Enter will not run a command.



on-blur parameter (skin)



Command executed when the control loses focus.



on-close parameter (skin)



Command executed when the window is closed.



on-change parameter (skin)



Command executed when the value of the bar/slider is changed. If you drag the slider around, the command will not run until you let go.

If you include [[*]] in the command, it will be replaced by the control's new value.  (See embedded winget for more details on the [[...]] format.)



on-focus parameter (skin)



Command executed when the control gains focus.



on-hide parameter (skin)



Commandexecuted when this control is hidden by the game. Must be the default control for the game to show/hide it.

Currently not editable in Dream Maker.



on-show parameter (skin)



Command executed when this control is shown by the game. Must be the default control for the game to show/hide it.

Currently not editable in Dream Maker.



on-size parameter (skin)



Command executed when this control is resized. If you are dragging a window edge or splitter, the command won't run until you finish.

No command will be sent in response to size or splitter changes made by winset().

If you include [[*]] in the command, it will be replaced by the control's new size. Likewise, [[width]] will be replaced with the width and [[height]] with the height. (See embedded winget for more details on the [[...]] format.)



on-status parameter (skin)



Command executed when the text that would go in the statusbar is changed. This applies even if this control is a pane and not a window, or is a window without a statusbar. It applies to all panes and windows that directly or indirectly contain whatever control generated the statusbar text (e.g., a map).

If you include [[*]] in the command, it will be replaced by the new text. (See embedded winget for more details on the [[...]] format.)

[[from]] can be used to reference the control (if any) that generated the next text. You can also use expressions like [[from.type]], [[from.parent.pos.x]], etc.



on-tab parameter (skin)



Command executed when the current tab is changed.

If you include [[*]] in the command, it will be replaced by the new tab's id. (See embedded winget for more details on the [[...]] format.)



outer-mouse-pos parameter (skin)



Read-only.

Reads the position of the mouse cursor relative to the upper left corner of this control, including the control's borders.

This parameter is "unlisted" and must be explicitly queried. It won't appear when sending * as the parameter in winget().



outer-pos parameter (skin)



Read-only.

Reads the control's current exterior position including titlebar, statusbar, borders, etc. If the window is not minimized or maximized, this is identical to pos.



outer-size parameter (skin)



Read-only.

If the control is a window, this refers to its current exterior size including titlebar, statusbar, borders, etc. If the window is maximized, this is the maximized size.

If this control is a pane and can-scroll is true, this is the size of the display area including the scrollbars.



parent parameter (skin)



The id of this control's parent. Write-only, used when creating a new control at runtime or deleting a control that was created this way.



pass-through parameter (skin)




Sends default action for this input after the user macro. Currently this applies only to mouse macros.

An example of this is if you want to override MouseDown with new functionality in your own verb, but still handle default mouse processing.



pos parameter (skin)




Position of this control's upper left corner, relative to its container. (Not applicable to panes.)



prefix-color parameter (skin)




The color used for the prefix/header column of statpanel displays. No color means the default text-color will be used.

In BYOND 3.0, this color was red.



right, bottom parameters (skin)




The id of the right/bottom pane in this control. The parameter names top and bottom can be used interchangeably.



right-click parameter (skin)




True if this control should allow right-clicks to behave like any other click instead of opening up popup menus or similar special behavior.



saved-params parameter (skin)



A semicolon-separated list of parameters that get saved with this control. This is often used for things a user might set, like zoom level for a map.

Currently not editable in Dream Maker.



screen-pos parameter (skin)



Read-only.

For windows, this is the upper left corner of the nearest monitor's area.

This is also a special read-only global parameter, which returns the position for the main monitor.



screen-size parameter (skin)



Read-only.

For windows, this is the size of the nearest monitor's area (minus taskbar).

This is also a special read-only global parameter, which returns the size (minus taskbar) for the main monitor.



size parameter (skin)



The size of this control.

Setting 0 for width or height uses up any available space right/downward.

If the control is a window, this refers to its interior size when not maximized or minimized. That is, it does not count borders, titlebar, menu, or statusbar, and if the window is minimized/maximized, this refers to the window's normal size when it is restored. See the inner-size and outer-size params for comparison.

If this control is a pane and can-scroll is true, size refers to the total scrollable size of the pane, NOT the smaller size displayed. In this case, outer-size and inner-size refer to the display area with and without scrollbars, respectively.



show-history parameter (skin)




Show forward/back navigation buttons.



show-lines parameter (skin)




Determines which grid lines to display.



show-names parameter (skin)




When atoms are output to the grid, show the atom's name next to its icon.

If the atom has no icon and show-names is false, the grid cell will be blank.



show-splitter parameter (skin)




Show a splitter if both the left and right (or top and bottom) panes are in use. The splitter can be dragged to resize the panes.



show-url parameter (skin)




Shows an address bar for this browser control.



small-icons parameter (skin)




When output(object,grid) is sent, show smaller icons in this control instead of larger ones.



splitter parameter (skin)




Position of the splitter when two panes are in use, whether show-splitter is true or not. This value is a percentage. Specifically, it is the percentage of the available width/height that is given to the left/top pane. 



suffix-color parameter (skin)




The color used for the suffix column of statpanel displays. No color means the default text-color will be used.

In BYOND 3.0, this color was blue.



statusbar parameter (skin)




Shows a status bar at the bottom of the window. This will show the name of an atom when you hover over it with the mouse.



stretch parameter (skin)




Stretch the background image.

Deprecated; use image-mode instead.



style parameter (skin)


Custom stylesheet used for the control. Changes made at runtime will usually not impact any existing text.

For Map controls, this affects any maptext drawn, and changes to the style should appear on the next refresh.



tab-background-color parameter (skin)




Affects the background color for tabs. The regular background-color is used for the content area.



tab-font-family, tab-font-size, tab-font-style parameters (skin)


Affects the font for tabs. The regular versions of these without the tab- prefix are used for the content area.



tab-text-color parameter (skin)




Affects the text color for tabs. The regular text-color is used for the content area.



tabs parameter (skin)



A comma-separated list of id values for the panes included as tabs in this control.

When setting this value, you can put + in front of the list to add tabs to the existing control, without affecting current tabs. You can likewise use - in front of the list to remove tabs.

Note: When using this with winset(), remember you will need to escape + as %2B via url_encode() or list2params().



text parameter (skin)



Text shown in this control. For Input controls this setting is only available at runtime.



text-color parameter (skin)



The control's foreground text color.



text-mode parameter (skin)




Show text mode even if icons are available. Text mode will be used if no icons are present, regardless of this setting.



text-wrap parameter (skin)




Wrap text that is too long for the width of the label.



title parameter (skin)



The title of this window or pane. For a window, the title will appear in the titlebar if present. For a pane, this will be displayed on the tab if this pane is in a Tab control.

If this is the default window, world.name takes precedence over the window title.



titlebar parameter (skin)




Show a titlebar for this window. This is also required for the close, minimize, and maximize buttons to appear.

If is-fullscreen is true, titlebar is ignored, so this value represents the state of the window when is-fullscreen is turned off again.



transparent-color parameter (skin)




A color that will be turned into transparency wherever it appears in this window. Overall, this method of transparency comes with many limitations, so it is considered deprecated.



type parameter (skin)



The type of this control. Read-only.



use-title parameter (skin)




Use the browser's document title to override the title of the window or pane it appears in.



value parameter (skin)




The "fullness" of this bar/slider, as a percentage.



view-size parameter (skin)



The size, in pixels, of the map after zoom has been applied.

For instance, if the client view has 10×10 tiles (this includes any extended tiles caused by HUD objects) and world.icon_size is 32x32, the map has a native size of 320×320 pixels. If the map has a zoom level of 2, then view-size will be 640x640.

With a zoom value of 0, which is the default for most projects, the actual zoom level is automatically determined by the size of the map control, the map's native pixel size as explained above, and the value of the letterbox parameter.



visited-color parameter (skin)




The color used for visited links.



width parameter (skin)




Width, in pixels, of the bar or slider. A value of 0 uses all available width.



zoom parameter (skin)




Zoom factor for icons on the map. 1 means to show the icons at their original size, 2 is 200%, 0.5 is 50%, and so on. A value of 0 stretches to fit available space.



zoom-mode parameter (skin)




Controls the way the map is upscaled.

Preserves a pixelated look, but does some blending between adjacent pixels when the zoom factor is not an integer. This is equivalent to upscaling by the next highest integer, then downscaling.
distortUses nearest-neighbor sampling to upscale. This may look odd if the zoom factor is not an integer, since for instance some pixels might scale up to be 2 pixels wide, others 3 pixels wide. Some users prefer it anyway.
blurUses bilinear sampling to upscale. This will cause a blurry appearance if the zoom factor is high, but it may be desired in some cases.


Appendix
This section contains miscellaneous information that may apply to multiple
vars or procs.




Byondapi

Byondapi is a set of exported functions from BYOND's core library that can
be used by external libraries that you call via the
call_ext() proc. The purpose is to make
interfacing with native code easier, and to allow external access to BYOND's
functionality. Before this existed, all external calls had to use text strings
to pass data back and forth, which was inefficient for many uses and very
limited.

To build your external library with Byondapi, you have to include the
byondapi.h header file that's included in BYOND's distribution. When
compiling in Windows, you'll also need to link with byondapi.lib; in
Linux, your makefile should link with byondcore.so from BYOND's own
bin directory.

Simple BYOND types
For simplicity, BYOND defines some basic types and macros in
byondapi.h. The one most relevant to you is u4c, which is an
unsigned 4-byte integer. There's also s4c which is a signed integer,
as well as simple 1-byte and 2-byte ints that use 1c and 2c
(respectively) insteaed of the 4c suffix.

CByondValue struct
The main structure used to pass data back and forth is
CByondValue. This mimics an internal structure in BYOND that holds
values of all sorts: numbers, null, references to strings, references to
objects and lists, and so on.

The exact functions used for interfacing with this structure are documented
in byondapi.h.

The main tricky aspect of working with BYOND data is strings. If you need
to get the contents of a string, you'll need to allocate memory for the
character data and call Byond_ToString() to get a copy of the string.
For converting character data to an internal string stored in CByondValue,
you'll need to call ByondValue_SetStr().

Other function calls
There are many function calls available in Byondapi for interacting with
the server. These include the ability to read and write vars, call procs,
create lists, read and write from lists, and so on.

Most of these procs return boolean values: true if they succeed, false if
not. In the event of a failure, you can call Byond_LastError() to
get the error message.

In any functions that read data from lists or read string data—including
Byond_LastError()—you need to allocate the required memory for
a copy of the string or list items. These functions take a pointer to the
buffer that will be filled, and a u4c pointer for the buffer size (in
items for lists, in bytes for strings). If the return value is false and the
length is set to zero, an error occurred. If the return value is false and the
length is non-zero, the new length value is the required length of the array;
the memory should be allocated and the function called again.

Example:

char *errmsg = NULL;
u4c buflen = 0;
while(!Byond_LastError(errmsg, &buflen)) {
    free(errmsg);
    errmsg = (char*)malloc(buflen);
    if(!errmsg) break;
}
... // do someting with the error message
free(errmsg);

The C++ wrappers have a better way of calling Byond_LastError()
and other functions like it, where you don't need to worry about allocations.

Reference counting
Objects in BYOND are reference-counted; when an object's count reaches 0
it gets garbage-collected. In Byondapi you can call ByondValue_IncRef()
and ByondValue_DecRef() to increment or decrement the reference
count, respectively.

Byondapi maintains its own internal reference count for any object, so
you can't decref past the number of references Byondapi holds.

The results you get from calls to Byondapi functions, such as reading a
var or getting a return value from a proc call, have already had their
reference count increased. That means when you're done using the value, you
need to clean it up with ByondValue_DecRef() or else you'll have a
memory leak.

The value you return from a function called by call_ext() should
have a reference.

The C++ wrappers take care of most of the reference counting issues for you
(see below).

Threads
BYOND servers handle proc execution and the management of data in a single
thread. If your library tries to call any BYOND server functions in a
different thread of its own, the call will block until the server thread can
handle it.

The special function Byond_ThreadSync() will run a callback
function on the main thread, avoiding the need to keep syncing over multiple
Byondapi calls.

C++ wrappers
If you want to use the handy C++ wrappers and classes, you can include
byondapi_cpp_wrappers.cpp and byondapi_cpp_wrappers.h in
your library.

The ByondValue class is a wrapper around CByondValue
that handles a number of operations for you. You can redefine the argv
argument of any call_ext() functions as an array of
ByondValue instead of CByondValue, but the return value
should stay a CByondValue.

Example:

#include <string>
#include <byondapi.h>
#include <byondapi_cpp_wrappers.h>
#include <string>

extern "C" BYOND_EXPORT CByondValue merge(int n, ByondValue v[])
{
    ByondValue result;
    std::string merged, str;
    for(int i=0; i<n; i++) {
        v[i].ToString(str);
        if(str) merged += str;
    }
    result = merged.c_str();   // ByondValue's assignment operator takes care of everything
    return result;
}

The external function calls like ByondValue_CallProc() have C++
wrappers that use the C calls internally, but if an error happens they'll call
an error handler. The default error handler does nothing, but you can change it
to a a different handler that accepts an error string.

If you define a CatchingByondExceptions variable inside of a
try block, it will automatically change the error handler to one that
throws a ByondExtException. This replaces the more cumbersome approach
of checking if the return value is false and then calling
Byond_LastError().



CSS attributes
DM-CSS is a subset of CSS, and only supports some kinds of selectors and
attributes.

The following table lists all supported attributes, and whether they are
supported in text output, maptext, and in other controls (labels/etc.) Other
controls will often allow only one style for an entire unit of text. A
checkbox in "Other" only indicates that some support exists in other
controls, but it may vary by the type of control.



AttributeOutputMaptextOtherNotes
color✔️✔️✔️Alpha colors may not be supported in some controls.
background✔️✔️✔️In most cases, only applies to the entire text body.
background-color✔️✔️
background-image✔️
font✔️✔️✔️
font-family✔️✔️✔️
font-style✔️✔️✔️
font-weight✔️✔️✔️
font-size✔️✔️✔️
text-decoration✔️✔️✔️Limited to underline, overline, line-through, blink, and none. Support for each of these may vary depending on where they are used.
text-align✔️✔️✔️justify is supported in output and maptext.
vertical-align✔️✔️Limited to top, middle, and bottom.
text-indent✔️✔️
margin-left✔️✔️✔️
margin-right✔️✔️✔️
margin-top✔️
margin-bottom✔️
margin✔️✔️✔️
width✔️✔️Applies only to some elements such as images.
height✔️✔️Applies only to some elements such as images.
line-height✔️✔️Support in output control is limited; line heights less than 1 are not respected.Only unitless numbers, percentages, or em units are allowed.
white-space✔️✔️normal, nowrap, pre, pre-wrap, pre-line
text-overflow✔️clip, ellipsis, or quoted string; maptext defaults to empty string
text-shadow✔️
-dm-text-outline✔️Custom attribute: Adds an outline to text. Values are in the form: width color style.The style is either blank, or any combination of the sharp and square keywords (see Outline filter).

These pseudo-classes are allowed in some contexts, but they can only change
the text color.



Psuedo-classOutputMaptextOtherNotes
:link✔️✔️✔️
:visited✔️
:activeCurrently not used, but future support is planned.
:hover✔️



HTML colors

Text colors may be specified by name or RGB value. The RGB color format
uses hexadecimal numbers, with 2 hex digits each for red, green, and blue.
These range from 0 (00 in hex) to 255 (FF in hex). In certain situations
BYOND will also honor a fourth pair of digits for alpha.


#rrggbb
#rrggbbaa

It is also possible to use 4 bit values by using only one hex digit per
color.  The full 8 bit color is produced by repeating each digit. For example,
#F00 (red) is the same as #FF0000.

The named colors supported by BYOND, and their corresponding RGB values,
are listed in the following table:



black #000000 
silver #C0C0C0 
gray or
        grey #808080 
white #FFFFFF 
maroon #800000 
red #FF0000 
purple #800080 
fuchsia or
        magenta #FF00FF 
green #00C000 
lime #00FF00 
olive or
        gold #808000 
yellow #FFFF00 
navy #000080 
blue #0000FF 
teal #008080 
aqua or
        cyan #00FFFF 



Color space

There are different ways of interpreting color besides RGB. Several parts of
BYOND are capable of using other color spaces.

COLORSPACE_RGB
The default color space is RGB, where each color is split into red, green,
and blue components, as well as an optional alpha. All of these components range
from 0 to 255.

The color yellow for instance is rgb(255,255,0) which is red and
green mixed together at their maximum brightness, but no blue component.

COLORSPACE_HSV


  Hue values on the color wheel

HSV stands for hue, saturation, and value.


Hue ranges from 0 to 360 on a color wheel, where 0 is red, 60 is yellow,
120 is green, and so on as seen in the image.
Saturation is how colorful this color is; it ranges from 0 which means a
shade of gray, to 100 which is fully colored.
Value is the brightness of the biggest red, green, or blue component, and
ranges from 0 to 100. A value of 0 is always black.

All pure hues such as red (hue=0) have a saturation of 100 and a value of
100. As saturation decreases, the colors turns whiter. Lower values mean
darker colors and darker shades of gray.

In HSV, saturation is less meaningful as value gets closer to 0. Black
of course always has a value of 0. With 10 as the value, saturation=100 gives
you a very dark color whereas saturation=0 is a 10% shade of gray.

COLORSPACE_HSL
HSL is a little more intuitive than HSV. Here, value is replaced by
luminance, which again ranges from 0 to 100. Luminance is the average of the
minimum and maximum values of the red, green, and blue components.

Black has a luminance of 0; white has a luminance of 100. Pure hues all
have a saturation of 100 and luminance of 50. As saturation decreases, the
color will approach a grayscale shade of L%.

Saturation is less meaningful the closer luminance is to 0 or 100. At a
luminance of 100, the saturation is totally irrelevant. At 90, high saturation
will get you a very light shade of the hue but that isn't very far off from a
90% shade of gray.

COLORSPACE_HCY
HCY stands for hue, chroma, and the Y is for grayscale
luminance. (Again chroma and Y range from 0 to 100.) This color space is
based around the apparent brightness of each color according to a rough
approximation of human vision.

Chroma is similar to saturation in that it determines how far from
grayscale the color is. As chroma decreases toward 0, the color approaches
a grayscale shade of Y%. What's different about HCY color from HSV or HSL
is that at chroma=0 and chroma=100 the colors should appear equally
bright. Pure red, therefore, has a hue of 0, a chroma of 100, and a Y
luminance of only 29.9—roughly what red would look like in black &
white with all of the color leached out.



stddef.dm file
This is a special file that's included in all projects when you compile.
It contains various constants, definitions of some built-in datums, and so on.

You can see the contents of this file by creating a new file in Dream
Maker called stddef.dm. It will automatically be filled with the
standard definitions.

The contents of stddef.dm may change with new BYOND versions.
However an eye is always kept on backwards-compatibility.



```



> [!CAUTION]
> Note: You can specify a different hub path and hub_password by adding these as extra arguments, but this is not recommended for security reasons. If you use this feature, it should only be on games that cannot be downloaded by the public.


```dm

//sending the file
mob/proc/Export(Addr)
  var/savefile/F = new()
  F.Write(src)
  world.Export(Addr,F)

//receiving the file
world/Topic()
  var/savefile/F = new(world.Import())
  F.Read() //read the mob

```


This example defines a mob proc called Export() which writes the mob to a savefile and sends it to another server (specified by Addr). The remote server opens it as a savefile and creates the mob (if the same mob type is defined on both servers and mob.Read() is compatible with the sending server's mob.Write()).

Note that another method of transferring player mobs is to use the key savefile (accessed by client.Export() and client.Import()). Direct server to server communication on the other hand could transfer data (like non-players) without the need for player involvement at all.

Savefiles are the most common type of file to transfer, but world.Import() simply returns a reference to an item in the world's .rsc file, which could be any type of file. This particular example demonstrates how to open such a file as a temporary savefile. (It gets dumped from the cache into a separate temporary file, which is then opened as a savefile.) Other types of files would be handled differently. For example, you could use fcopy() to dump the cached item to its own separate file.

By default, this procedure checks the "ban" configuration file. If an entry is found for the current world (based on the value of world.hub), the parameter text is converted into a list (using params2list()), and the result is returned. Otherwise, null is returned.

A ban that applies to all worlds on the host's computer will not call IsBanned(). The connection will simply be denied.

This procedure is called internally whenever a new user connects (before client/New() is called). If the result is true, access is denied. If you want to ban a user but still allow them to log in (perhaps with reduced functionality), you can put "Login=1" in the parameter text. If you want to display an explanation to the user about why they are banned, you can also put "message=X" in the parameter text, where X is the message to display to the user. A reason for the ban can be added with a "reason=X" field. Of course, you can also override IsBanned() and insert these values directly into the list that is returned.


```dm

world/IsBanned(key,address)
   . = ..()            //check the ban lists
   if(istype(., /list))
      .["Login"] = 1   //allow banned user to login

```


When you ban people from paging you, this also causes them to be added to the keyban list. Even if they are already connected, IsBanned() will be re-evaluated and acted upon at that time. When you remove pager ban, they are removed from keyban as well.

Additional data elements may be added to the ban list in the future. The current definition includes just the following items:

Since the data in the "ban" file is in <a href="#/proc/list2params">application/x-www-form-urlencoded</a> format, it is probably not desirable to edit the file by hand. No built-in facilities for editing the file have been provided (aside from automatic addition of pager bans), but an interface could be created, using <a href="#/world/proc/GetConfig">GetConfig</a> and <a href="#/world/proc/SetConfig">SetConfig</a> to read and write the data. Extra features could also be added such as automatic inference of key associations by IP address.

Checks a player for their subscription status to this game. This is a simpler alternative to `client.CheckPassport()`, which is deprecated, and also allows you to check even when the player has gone offline.

This proc will return null if contacting the hub was required, but there was no way to reach the hub. Contacting the hub may take a few moments, so it is a good idea to use <a class="code" href="#/proc/spawn">spawn()</a> to avoid holding up the rest of the game.


```dm

mob/verb/JoinClub()
    if(!world.IsSubscribed(src))
        src << "Sorry, the club is only for subscribers."
    else
        // go to the turf with the tag "clubhouse"
        loc = locate("clubhouse")
        src << "Welcome to the clubhouse!"

```



> [!CAUTION]
> Note: You can specify a different hub path and hub_password by adding these as extra arguments, but this is not recommended for security reasons. If you use this feature, it should only be on games that cannot be downloaded by the public.

This causes the world to be hosted on the specified network port. A value of 0 or "any" requests that any available port be used. The value "none" causes the port to be closed so that no new connections are possible.

This proc may be overridden. If it is, calling ..() is necessary to open the port. If ..() is not called, it will not open.


```dm

world/OpenPort(port)
  // only allow subscribers to host
  if(host_is_subscribed)
    return ..()

```


The "ports" configuration option in cfg/byond.txt can be used to control what ports worlds may open. The -ports command-line option may also be used. See <a href="#/proc/startup">startup</a> for the syntax.

Removes credits from a player's account, if they have enough. The proc will return 1 if it is successful, or 0 if the attempt failed (usually because the player doesn't have enough credits). This feature is intended for games that make use of the credit system, and for security all such games must use a hub password.

This proc will return null if there was no way to reach the hub. Use isnull() to check for a null value. Contacting the hub may take a few moments, so it is often a good idea to use spawn() to avoid holding up the rest of the game.


```dm

mob/proc/ItemShop()
    var/items = list("Get credits!", "Magic sword"=10, "Skeleton key"=50)
    var/choices[0]
    var/item,price
    for(item in items)
        price = items[item]
        choices["[item]: [price] credit\s"] = item

    var/credits = world.GetCredits(key)
    if(isnull(credits))
        src << "Sorry, the item shop isn't available right now."
        return

    var/choice = input(src,\
      "You have [credits] credit\s. What would you like to purchase?",\
      "Item Shop")\
      as null|anything in choices
    if(!choice) return  // cancel

    if(choice == "Get credits")
        src << link("http://www.byond.com/games/Author/MyGame/credits")
        return

    item = choices[choice]
    price = items[item]
    if(!price) return

    src << "Contacting item shop..."
    var/result = world.PayCredits(name, price, "Item shop: [item]")

    if(isnull(result))
        src << "Sorry, the item shop isn't available right now."
    else if(!result)
        src << "You need [price-credits] more credit\s to buy [item]."
    else
        src << "You bought \a [item]!"

        // Now give the user the item and save their character
        // These procs are for you to define
        src.AddEquipment(item)
        src.SaveCharacter()

```



> [!CAUTION]
> Note: You can specify a different hub path and hub_password by adding these as extra arguments, but this is not recommended for security reasons. If you use this feature, it should only be on games that cannot be downloaded by the public.

Interacts with the built-in server profiler without requiring the host to do so via Dream Daemon, or an authorized player via Dream Seeker.

The `command` value is built from bitflags, so it can combine any of these three values via the `|` operator:

These additional values are also defined for convenience:

By default, data will be returned as a list. The first six values are the column names: `"name"`, `"self"`, `"total"`, `"real"`, `"over"`, and `"calls"`, corresponding to the columns in the profiler. These are followed by the profile data for each proc, with the data being in the same column order. E.g. the next six items represent the first proc in the profile.

The optional `format` argument however can be used to return the data in other formats. Currently the only accepted value is `"json"`, which will output the same data in JSON format.

Using `"sendmaps"` in the `type` argument will profile the routines used to send map informaiton to players. Unlike the proc profiling this only has three data columns: `"name"`, `"value"`, and `"calls"`. The value column might be a time or number value, depending on what's being measured.

The JSON format will include a `unit` property data that is not a raw number, such as a time value.

Reload the world from scratch. Any connected players will automatically relogin. This would be useful if you needed to recompile the world after changing some code.

In a UNIX environment, you can cause a running server to reboot by sending it the signal SIGUSR1.

If you override this proc, you must call ..() if you want the reboot to complete normally.

For reboots initiated by Dream Seeker, usr will be the mob belonging to the player who sent the command.

This command is for storing configuration information that is shared by applications installed on the same system. The configuration data is accessed by specifying the configuration "set" and the parameter within that set.

For more information, see <a href="#/world/proc/GetConfig">GetConfig</a>.

Awards a medal to a player. The proc will return 1 if it is successful, or 0 if the medal was already awarded. If the world already knows this medal was earned before, the hub will not be contacted.

This proc will return null if there was no way to reach the hub. Use isnull() to check for a null value. Contacting the hub may take a few moments, so it is a good idea to use spawn() to avoid holding up the rest of the game.


```dm

mob/monster/dragon
   Die(mob/killer)  // assume Die() is a proc all mobs have
      spawn()
         if(ismob(killer) && killer.key)
            world.SetMedal("Dragon slayer", killer)

```



> [!CAUTION]
> Note: You can specify a different hub path and hub_password by adding these as extra arguments, but this is not recommended for security reasons. If you use this feature, it should only be on games that cannot be downloaded by the public.

Updates scores that are kept on the BYOND hub.

The key is an arbitrary text value. Usually a player's key is a good choice, but you can also use the name of their character, or anything else you like, as long as it is unique. The key is case-insensitive.

Scores and stats use data fields, which might be things like "Score", "Level", "Class", etc. Use list2params() to set the fields that you want to change. Fields that you do not include in the list will not be changed. A field with a blank value will be deleted.

Sending an empty text string for the fields will erase the scores for that key.

This proc will return null if there was no way to reach the hub. Use isnull() to check for a null value. Contacting the hub may take a few moments, so it is a good idea to use spawn() to avoid holding up the rest of the game.


```dm

var/params

// Change the Score and Pet fields
params = list("Score"=123, "Pet"="Dog")
world.SetScores("Tom", list2params(params))

// Delete the Pet field
params = list("Pet"="")
world.SetScores("Tom", list2params(params))

// Delete Tom's scores entirely
world.SetScores("Tom", "")

```



> [!CAUTION]
> Note: You can specify a different hub path and hub_password by adding these as extra arguments, but this is not recommended for security reasons. If you use this feature, it should only be on games that cannot be downloaded by the public.

This proc allows you to do any updates just before map info is sent out. One possible use for this is to run a movement loop, or sync up any user interface input that might have arrived and deal with it all at once.


```dm

world/Tick()
    for(var/client/C)
        if(C.mob?.move_dir)
            try
                step(C.mob, move_dir)
            catch
                // empty catch, just so a failed step won't break the loop

```


Note: The tick will not wait if this proc sleeps. It effectively has <a class="code" href="#/proc/set/waitfor">set waitfor=0</a> already built in. It's a good idea not to sleep in this proc or any of its callees at all, since it will keep getting called every tick.


```dm

world/Topic(T)
  if(findtext(T,"shout:") == 1)
    world << copytext(T,7)

```


This example allows other servers to send this server topic text of the form "shout:msg" and will broadcast the message to all the players in this world.

The Keys argument is either null, or a list of user keys. Any keys in the list are logged in to the remote server.


> [!CAUTION]
> 
> > [!NOTE]
> > Always validate the input in `Topic()` calls to make sure it's correct and the query you're recieving is legitimate.

Built-in world vars:

This is the network address of the machine hosting the world. If it cannot be determined, it will be null.

The full network address of the world may be formed by concatenating the world address and port: "byond://[address]:[port]".

In CGI mode, this is the web address of the world.

This is the local address only. If the world is hosted via a router, the external IP address may be different. Use `internet_address` to find the external address, if available.

This is the default area type to be placed on the map wherever no area is specified. A value of 0 turns off the default area.

This is the build number (minor version) of BYOND being run by this server. Typically this is not useful information, but it can come in handy when diagnosing issues reported by players when hosting with a beta build.

This is the version of BYOND at run-time. A game designed to work around known bugs in older versions could use this to adapt its behavior accordingly.

Number of days items that are not in use will be saved in the resource cache (.rsc file). Files uploaded by players are stored in the world's .rsc file for future use. If the file is not used for the specified amount of time, it will be removed to save space.

Setting this value to 0 causes items to be saved for the current session only. This is used by the CGI library, because web browsers cannot make use of server-side caches when uploading files anyway.

This value must be a whole number.

This is a list of every object in the world. Objects in this list are in no particular order.


```dm

proc/ListAreas(mob/M)
  var/area/A
  M << "Areas:"
  for (A in world.contents)
    M << A

```


This example displays a list of every area in existence. As a convenient short-hand, one may simply write for(A) or for(A in world) instead of the full for(A in world.contents).

This is the percentage of a server tick that the server spends processing running procs and the work of sending map information to players. A value of 0 would indicate very little cpu usage. A value of 100 would indicate full cpu usage, which could mean that the server cannot complete all the necessary computations during a tick to finish in time for the next tick. In this case, timed events (such as sleep) may take longer than requested.

When deciding on a value for tick_lag, one could use this value to determine if the CPU is fast enough to tick at a higher rate.

The `map_cpu` var is a subset of this, measuring only time used for sending map information.

This option is for direct execution of <code>.dmb</code> files in UNIX. The most common use is for writing CGI programs that are executed by the web server.

The first parameter in the `executor` text string is the path to DreamDaemon. The one listed above is the standard UNIX location.

Optional parameters may follow. The most common are -CGI and -logself.


```dm

world/executor = "/usr/local/byond/bin/DreamDaemon -CGI -logself"

```


This example creates a CGI program to be executed by a web server. It puts its error output in the file <code>`projname`.log</code>.

All of this is configured for you when you include <code>html/CGI.dm</code> from the html library.

The value of `world.fps` defines the speed of the world in frames (server ticks) per second. By default this is 10 fps, which is a good speed if all objects move in full tiles. Higher values yield smoother results, but at a cost to performance. Timing of many events may be limited by the system clock, so `fps` values beyond 40 or 50 may cause unwanted effects like jitter even for projects that are not very demanding in terms of performance.

For projects making use of pixel movement, higher `fps` is usually desired. 40 seems to be a good value for general use, but in worlds that have a large number of players, you may wish to lower the value and give players a higher `step_size` per tick instead.

This var exists for convenience; it is calculated by `10 / world.tick_lag`. The value of `world.tick_lag` is actually more accurate, but it is easier to think of world speed in terms of frames per second. The actual tick rate has a resolution of 1 ms.

When reading `world.fps`, the result is always given as a whole number to gloss over rounding error.

If you set `client.tick_lag` or `client.fps` to a value other than 0, you can make the client tick at a different (usually faster) rate.

At runtime, this value may be changed to let the BYOND hub know about certain changes in the game's status. An example for using this value is if the number of players in the game gets too high and most new logins are rejected, you can set game_state to 1 to let the hub know this server is full.

The following values are accepted:

Note that this value does not affect how your world actually reacts to new players logging in. It is only used by the hub and website.

If the information is made available by the pager, this will provide the key of the world's host. If the host is not known, this value will be either null or an empty string.

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

If <code>world.hub</code> is set, any live session of the game will be attached to the specified BYOND Hub page. Under the default settings, any game can set <code>world.hub</code> and attach itself to any BYOND Hub page.

To beef up security, you can set a hub password in your hub's configuration page via the BYOND website. This will ensure that only authorized copies of your game can attach themselves to your hub page when live. Then simply copy that password into your code as <code>world.hub_password</code> so that your game's live broadcast will be accepted by the hub.


```dm

world
   hub = "Dan.PipeStock"   //registered hub path
   hub_password = "UPAggnJaeXmSBoKK"   //password for live game authentication

```


Note that for security reasons, reading this variable at runtime will return a hashed version of the value that was set.

This is the tile size that will be used as a default for icons in the world. It can be set to a single number that represents both the width and height, or you can use a format like "[width]x[height]" (such as "16x48") to specify width and height separately.

This value affects several calculations, including icon operations and gliding between turfs.

Note: If you do not use a square icon size and you are using a topdown map format, you may experience display issues if setting `client.dir` to `EAST` or `WEST`. A non-square tile with a topdown map format will also interfere with pixel movement. For this reason, square sizes are recommended when using any topdown-view map format.

This is the network address of the machine hosting the world, as it is seen by the outside network (from the Internet) and the hub. If it cannot be determined, it will be null.

The full network address of the world may be formed by concatenating the world address and port: "byond://[address]:[port]".

This var exists because `world.address` may not be accurate if the world is hosted on a machine behind a router using NAT. The value returned by `internet_address` can be given to other players who wish to log in.

Sending output to world.log may be useful for debugging purposes. The output goes to the same place run-time proc errors are displayed.


```dm

if(1+1 != 2)
  world.log << "Uh oh."

```


You can assign world.log to a file name or file() object to redirect output to that file. (There is also a command-line option to Dream Daemon that does this.)


```dm

world.log = file("mylog.txt")

```


Setting this to 0 disables the very long loop protection. By default, loops in the code which undergo a very large number of iterations or recursions are aborted (by crashing the proc). This prevents the proc from locking up the server for too long.

You may need to disable this feature if your code has some very long loops in it. Before doing that, make sure it's not <em>infinitely</em> long! Your program will utterly crash if it runs out of system stack space, which can happen in a very deep or infinite recursion.

Note: The compiler will now generate a warning when you disable `loop_checks`. It is not advisable to disable the check unless you're trying to debug something, since you can cause the server to hang. Generally if you have a loop so long it can cause the regular loop checks to freak out, you need to make a change to the loop behavior anyway.

This value says how the world will display maps. In a normal overhead tiled map the value is `TOPDOWN_MAP` for the top-down format. For older games that predate this feature, the value is `TILED_ICON_MAP`.

If you use a map format other than top-down, the HUD will still use a tile format like it would in top-down display. HUD objects are not projected into whatever map_format you use and they are not affected by changing client.dir. The size of the HUD is rounded up to the nearest number of full screen tiles; the size of each tile is defined by world.icon_size.

This is the default map format. Icons are drawn in a tile form and viewed from overhead. In this layout, the layer assigned to each atom is very important. The number of tiles shown is set by client.view or world.view.

Because this format is familiar and easy to understand, it is the default setting. Most of the vars related to maps and atoms are designed and documented with this format in mind.


> [!WARNING]
> 
> > [!NOTE]
> > This format is deprecated. It exists to support older games and allow them to be compiled without causing them to break, until they can be redesigned for one of the newer formats.

If map_format is set to `ISOMETRIC_MAP`, the map is displayed in isometric form. Isometric tiles are displayed in a foreshortened diagonal perspective, where the "north" direction actually displays as northeast on the player's screen, and "east" shows up as southeast. The value of `client.view` or `world.view` is used to calculate the *minimum* number of tiles to display, and extra tiles to each side will be shown to fill in the corners.

In an isometric map, the tile width set in world.icon_size is the most important factor. This should be a multiple of 4 for best results. The minimum tile height is half that value, and any extra height is used to show vertical structures that "stick up" off the map surface. When you draw an isometric tile icon, start with a flattened diamond shape at the bottom that is only half as high as it is wide.

Isometric maps behave differently during drawing than top-down maps. In isometric, tiles that are nearer to the viewer's perspective are drawn in front of tiles farther back, regardless of layer. Layers only count within an individual tile. This means that if you want to have a vertical structure "stick up" to partially hide something behind it, the icon sticking up should always be on a tile forward from the one being partly covered. E.g. if you have a wall taking up part of your tile, it needs to be at the "back" end of the tile to properly hide anything on the tiles behind it.

The `pixel_x` and `pixel_y` values, `step_x` and `step_y` values, and the gliding that happens when moving between tiles, are based on the width set by `world.icon_size`. If you set `world.icon_size="64x128"` to show tall buildings, only the 64 matters for pixel offsets. Use `pixel_w` and `pixel_z` to adjust the position of atoms (or the client) horizontally or vertically without respect to `client.dir` or the map format.

Note: Offsets for x and y also affect the layering order used to draw the icons. Any object with a pixel offset onto another tile is considered part of whichever tile is closer.

If you use an icon wider than one tile, the "footprint" of the isometric icon (the actual map tiles it takes up) will always be a square. That is, if your normal tile size is 64 and you want to show a 128x128 icon, the icon is two tiles wide and so it will take up a 2×2-tile area on the map. The height of a big icon is irrelevant--any excess height beyond width/2 is used to show vertical features. To draw this icon properly, other tiles on that same ground will be moved behind it in the drawing order.

One important warning about using big icons in isometric mode is that you should only do this with dense atoms. If part of a big mob icon covers the same tile as a tall building for instance, the tall building is moved back and it could be partially covered by other turfs that are actually behind it. A mob walking onto a very large non-dense turf icon would experience similar irregularities.

The `SIDE_MAP` format is like a cross between `TOPDOWN_MAP` and `ISOMETRIC_MAP`. It looks very similar to a top-down view but it is intended for more of a 3/4 perspective, where tiles lower on the screen are considered closer to the viewer. Because this impacts the way layers work, most of the layering behavior is the same as with isometric.

In a 3/4 perspective the tiles are often foreshortened, so pixel offsets are adjusted to account for this. For example, you may set `world.icon_size` to `"32x24"`, but the tile is considered to be a perfect square if you look at it from the top down. Because the width is 32 pixels, the virtual height is also 32, so if you use pixel_y=32 the atom will appear one tile further back than it normally is. (This adjustment doesn't affect screen objects or `pixel_w`/`pixel_z`.)

Changing `client.dir` preserves the same tile size regardless of orientation.

This is the percentage of a server tick that the server spends processing information about the map to send to players. A value of 0 would indicate very little cpu usage. A value of 100 would indicate full cpu usage, which means that the server cannot complete all the necessary computations during a tick to finish in time for the next tick. In this case, timed events (such as sleep) may take longer than requested.

The world map is a three-dimensional block of turfs with coordinates ranging from (1,1,1) to (maxx,maxy,maxz). If set at compile time, it provides a lower bound and will be increased as needed by the map files.

The default value is 0, indicating no map. If any of the map dimensions are set to non-zero values at compile time, the others will default to 1.

New territory created by increasing the map boundaries is filled in with the default turf and area (world.turf, and world.area).

The world map is a three-dimensional block of turfs with coordinates ranging from (1,1,1) to (maxx,maxy,maxz). If set at compile time, it provides a lower bound and will be increased as needed by the map files.

The default value is 0, indicating no map. If any of the map dimensions are set to non-zero values at compile time, the others will default to 1.

New territory created by increasing the map boundaries is filled in with the default turf and area (world.turf, and world.area).

The world map is a three-dimensional block of turfs with coordinates ranging from (1,1,1) to (maxx,maxy,maxz). If set at compile time, it provides a lower bound and will be increased as needed by the map files.

The default value is 0, indicating no map. If any of the map dimensions are set to non-zero values at compile time, the others will default to 1.

New territory created by increasing the map boundaries is filled in with the default turf and area (world.turf, and world.area).

When a player connects to the world, the world is searched for a mob with the player's key. If one is found, the player is connected to that mob. If none is found, a new mob of type world.mob is created and the player is connected to this new mob.

The default value is /mob. Setting world.mob to 0 prevents the creation of default mobs.


```dm

world
  mob = /mob/newbie

mob/newbie
  Login()
    src << "Welcome, [name]."
    ..()

```


This example will connect new players to mobs of type /mob/newbie. They are welcomed when they connect.

Controls how movement works on the map.

`TILE_MOVEMENT_MODE` allows you to easily discard any and all pixel movement, so if step_x or step_y coordinates or unexpected atom bounds were loaded from a savefile, for instance, they would be eliminated. If you use any other movement mode, you can give an atom the <a class="code" href="#/atom/var/appearance_flags">TILE_MOVER</a> flag and it will behave as if it were in this mode, while other atoms are free to do their own thing.

`LEGACY_MOVEMENT_MODE` exists to distinguish between old and new movement behavior. In older versions of BYOND before pixel movement, turfs took their contents into consideration by default in Enter() and Exit(). This doesn't really make sense for newer games, so in any other movement mode the turf behavior will ignore its contents. mob.Cross() is also affected, since it would return 0 by default in legacy mode when both mobs were dense; now by default it checks `mob.group`.

This is the name of the world.


```dm

world
  name = "The Void"

```


This is a list of parameters passed to the world from the command-line -params option when the server was started. The parameter text is passed through params2list() to generate the world.params list.


```dm

world/New()
   var/p
   if(params.len) world.log << "Command-line parameters:"
   for(p in params)
      world.log << "[p] = [params[p]]"

```


This example displays the value of each parameter.

This is the network port of the world. If the world does not have an open network port, this is 0.

This read-only variable indicates the ID of the server's process on the system running it. The result is a number, unless for some unexpected reason the number won't fit in a `num` type, in which case it will be text. (In practice it should always be a number.)

This is the time (in 1/10 seconds) since 00:00:00 GMT, January 1, 2000 (also known as the BYOND era).

Because this is a large number, BYOND's number system isn't capable of enough precision to deliver the exact number of 1/10 second ticks. It usually rounds off to the nearest several seconds. For more accurate readings use <code>world.timeofday</code>.

Returns 1 if the world is currently hosted and the port can be reached by players (as determined by the BYOND hub), 0 if not.

If the port is not reachable, there may be a brief period during which the hub is still attempting to make contact; during that time the port is assumed to be reachable. Currently, the reachability test times out and fails after 30 seconds.

Setting this to 1 causes the world to be suspended when there are no players, even if you have sleeping procs waiting to happen. The default value is 0, which means the server will only sleep if there are no players and no procs waiting to happen. The main purpose of the variable is to save the cpu from doing work when there is nobody around to appreciate it. On the other hand, that doesn't give the poor NPC's a break from the nasty humans.

This is a short text string used in BYOND hub to describe the state of a game in progress. For example, you might want to indicate if new players will be able to actively play, or whether they would have to join as spectators.


```dm

world
   status = "accepting players"
mob/verb/start_game()
   world.status = "accepting spectators"
   //...

```


This variable indicates the operating system type at run-time. It will be one of the following constants:

This is the smallest unit of time (one server tick) measured in 1/10 seconds. The duration of events that take some finite amount of time (like sleep) will be rounded to a whole number of ticks.

Players are limited to one command (including movements) per server tick, so this value can be used to adjust the responsiveness of the game. If the network is too slow to keep up with players, their commands will get queued up, which can be annoying when trying to move. In this case, tick_lag should be increased so that the stored up movement commands are discarded. On the other hand, if you have a very fast network, you may wish to decrease tick_lag to speed up the response time to player commands.

Often it is more convenient to set world.fps instead of world.tick_lag, since fps (frames per second) is an easier way to think of server ticks. world.tick_lag is 10 / world.fps and vice-versa, so a tick_lag of 0.25 is equal to 40 fps.

If you set client.tick_lag or client.fps to a value other than 0, you can make the client tick at a different (usually faster) rate.

This is the approximate percentage of the server tick that has been used already. A value under 100 means there's time to do more calculations, which can include any pending procs that are still waiting to run on this tick. When the value is over 100, the tick is running long and your world will experience lag.

Keep in mind that sending maps to clients is the last thing that happens during a tick, except for handling any events such as player commands that might arrive before the next tick begins. Therefore in a verb, `tick_usage` might have a higher value than you would expect to see in a proc that loops and sleeps.

This gives the amount of time (in 1/10 seconds) that the world has been running. In actual fact, it is the number of server ticks that have passed multiplied by world.tick_lag. Therefore if the server sleeps (when no players are connected) this time is not counted. Also, if the server runs overtime during a tick (because procs take longer than tick_lag to finish) this still only counts as one tick. This value is therefore a measure of "game time" rather than real time.

This is the time (in 1/10 seconds) since 00:00:00 GMT today. It is basically identical to <code>world.realtime</code> but doesn't include any information about the date. This is a much smaller number; hence it is more accurate.

This is the time offset from UTC, in hours, for the world's time zone. It can be used in the `time2text()` proc, although it is the default time zone for that proc.

This is the default turf type to be placed on the map wherever no turf is specified. A value of 0 turns off the default turf.

This is the full network address of the world. (For example, byond://dan.byond.com:6005.)

If you are distributing your game to players, you can use this variable to automatically notify them of new releases. To do so, you will first need to set <a href="#/world/var/hub"><code>world.hub</code></a> to the hub path of your game. You can then advertise the current version by configuring that value in your <a href="https://secure.byond.com/members/?command=edit_hub">hub console</a>.

When players boot up an outdated version of your game (as indicated by comparing <code>world.version</code> with the version advertised by BYOND hub), they will be notified of the new release.

This is the default map viewport range. The default value of 5 produces an 11x11 viewport. A value of -1 turns off the map display altogether. The client may automatically scale down icons in order to conveniently fit the map on the player's screen.

For non-square views, you can assign this to a text string of the form "WIDTHxHEIGHT". For example, "11x11" is equivalent to a view depth of 5, but you could make it wider like this: "13x11".

This setting also affects the default range of the <code>view()</code>, <code>oview()</code>, <code>range()</code>, and <code>orange()</code> procedures.

If the entire map is small enough to fit on one screen (arbitrarily defined to be 21x21 or less), the default <code>view</code> is automatically adjusted to fit the map. In this case, <code>client.lazy_eye</code> is also automatically turned on by default, since you probably don't want the map to scroll around.

This controls whether the world advertises itself in the <a href="http://www.byond.com/games/">BYOND Hub</a> when it has an open network port for accepting players. The visibility of the world still depends on whether any of the connected players has their location reporter turned on, and that in turn relies on the pager being turned on.

This section of the reference should help explain some concepts that may be harder to understand or that can use more clarification.

This is mostly no longer needed. A negative value for plane is the preferred way to do show objects in the background. It can still be used however when you want to rearrange objects in the same plane when using <a class="code" href="#/atom/var/appearance_flags">PLANE_MASTER</a> for visual effects.

`BACKGROUND_LAYER` is a special high value that can be added to the regular layer of any atom.

The purpose of this value is to make an atom appear below any regular atoms, even if they share the same plane. In an isometric map for instance, HUD objects will always appear above the map, but makeing a HUD object appear behind the map was basically impossible without this feature until `plane` was implemented.

When using this special layer, it should be added to the layer an atom normally uses. For instance an obj should have a layer of `BACKGROUND_LAYER + OBJ_LAYER`.

This can be mixed with `TOPDOWN_LAYER` and `EFFECTS_LAYER`, but it will take precedence over both. Anything with `BACKGROUND_LAYER` will always appear below anything without it on the same plane.

Images or overlays with `FLOAT_LAYER` can be left alone. They will automatically have the same layer as whatever atom they are attached to.

BYOND allows you to use icons that are not the same size as the tile size defined in world.icon_size. These icons can be manipulated with the /icon datum using their raw, native size, and shown on the map in full size. To use the old behavior where an atom can display only an icon of the normal tile size, use the TILED_ICON_MAP value for map_format instead.

When you use an icon of non-standard size on an atom, the icon is "anchored" to the southwest corner of the atom. If you are using a top-down view (world.map_format=TOPDOWN_MAP), the icon will appear to spread out further to the east and north. In an isometric map (world.map_format=ISOMETRIC_MAP), the icon will cover additional tiles north and east as well. The "footprint" of an isometric icon--the actual map tiles it covers--is always square, so if your tile size is 64x64 and you use a 128x64 icon, the 128-pixel width means the icon will cover a 2x2 section of map tiles.

It is important to remember that using a big icon is a visual effect *only*. It will not affect how the atom bumps into other atoms or vice-versa.

Big icons will affect layering--the order in which icons are drawn. In general, because a big icon is covering more than one tile of the map, it will try to draw above any other tiles in that space that are on the same layer. This way, you can set a turf to use a big icon without having to change the turfs to the north and east. If an atom has a big icon, any overlays and underlays attached to it will be pulled forward as well, so they will draw in front of anything on their same layer. In isometric mode this is about the same, except that the layer isn't that important--anything in the way will just be moved back behind the big icon.

Note: Big overlays will not "pull forward" on their own. If the main atom uses a single-tile icon, a big overlay attached to it will not try to draw in front of other icons on the same layer. This is so that name labels, health bar overlays, etc. will not cause any odd behavior. To be safe, you should always specify a layer when adding an overlay.

In isometric mode, layering is affected by the "distance" between the atom and the viewer, so putting a regular-sized icon and part of a big icon on the same tile could cause layering oddities. Tiles that are covered by a big icon will tend to be drawn behind the big icon as mentioned above. For this reason, any atoms whose icons cover more than one tile (the extra height of an isometric icon doesn't count) should always be dense, and you should block movement onto any tile covered by them.

When manipulating icons with the /icon datum, you can still use Blend() to combine icons of different sizes. By default, the icons will be lined up at their southwest corners. You can change the position at which the second icon is blended.

A color gradient is a special list that defines a range of colors that you can smoothly interpolate between. A simple example is a gradient from red to white:


```dm

list("red", "white")
// OR
list(0, "red", 1, "white")

```


Applying a number like 0.2 to this gradient would give you a color that's 20% of the way from red to white. More complex gradients however are also possible.

The format of a gradient is a list that contains a number (the position along the gradient, from 0 to 1 unless you use values outside that range) followed by a color. You can have as complex a gradient as you like. If you reuse the same number twice in a row, the gradient will have a sudden color change at that point.

It is also possible to skip numbers or colors, and they will be filled in automatically with the previous number or color. The exceptions are at the beginning and ends of the list; at the end of the gradient, the last color is assigned a number 1 by default, and the first is assigned 0. If you skip colors at the beginning, they will be filled in with the first color you use.

Include "loop" anywhere in the list to make this a looped gradient. If you don't, any numbers outside the gradient's range will be clamped to that range. E.g., in a normal gradient ranging from 0 to 1, a number of 1.2 is interpreted as 1 without a loop and 0.2 with a loop.

Here are some more examples:


```dm

// color wheel; ranges 0 to 6 and loops
list(0, "#f00", 1, "#ff0", 2, "#0f0", 3, "#0ff", 4, "#00f", 5, "#f0f", 6, "#f00", "loop")

// 10% each red, yellow, green, blue, with a 20% transition zone between each
// notice no color follows 0.4 or 0.7, so the previous color is used
list(0.1, "#f00", 0.3, "#ff0", 0.4, 0.6, "#008000", 0.7, 0.9, "#00f")

// green and black stripes
list(0.5, "#008000", 0.5, "#000000", "loop")

```


You can also include "space" in the list, and give it an associated value that describes the color space this gradient uses to interpolate between colors. For instance, `"space"=COLORSPACE_HSL` will use HSL interpolation instead of the default RGB. See <a href="#/{{appendix}}/color-space">Color space</a> for more information.


```dm

// color wheel with a different color space
list(0, "#f00", 3, "#0ff", 6, "#f00", "loop", "space"=COLORSPACE_HSLA)

```


Currently, color gradients are only used by particle effects and the <a href="#/proc/gradient">`gradient` proc</a>. With particles, if you use a gradient the particle's color is given as a number, and that number is used to look up its real color from the gradient. The number can change over time, thus changing the particle's color.

A color matrix is used to transform colors, in the same way that a matrix represented by the `/matrix` datum is used to transform 2D coordinates. A transformation matrix is 3x3, of which only 6 values are needed because the last column is always the same. A color matrix, because it transforms four different numbers instead of two, is 5x5.

In that formula, values like `rg` mean "red to green", meaning that's the ratio of red in of green out. (The "c" is for "constant".) In an identity matrix, which just produces the original color, the values `rr`, `gg`, `bb`, and `aa` are all 1 and everything else is 0.

In easier-to-understand terms, this is how the result is calculated:


```dm

new_red   = red * rr + green * gr + blue * br + alpha * ar + 255 * cr
new_green = red * rg + green * gg + blue * bg + alpha * ag + 255 * cg
new_blue  = red * rb + green * gb + blue * bb + alpha * ab + 255 * cb
new_alpha = red * ra + green * ga + blue * ba + alpha * aa + 255 * ca

```


It is helpful to think of each row in the matrix as what each component of the original color will become. The first row of the matrix is the rgba value you'll get for each unit of red; the second is what each green becomes, and so on.

Because the fifth column of the matrix is always the same, only 20 of the values need to be provided. You can use a color matrix with atom.color or client.color in any of the following ways:

Reading a color var that has been set to a matrix will return the full 20-item list, where every 4 items represent a row in the matrix (without the fifth column).

In the `MapColors()` icon proc, the values are sent as arguments, not as a list.

The <a href="#/{notes}/filters/color">color filter</a> allows the use of other color spaces for a matrix. In those other color spaces, the matrix calculations work the same but instead of red, green, and blue, they'll be whatever values that color space uses. For instance an HSL color matrix uses hue in place of red, saturation in place of green, and luminance in place of blue. (Alpha is always alpha.)

The way that works internally is that the shader will convert a color from RGB to the color space used by the matrix, then apply the matrix, then convert back to RGB.

This is mostly no longer needed. A negative value for plane is the preferred way to do show objects in the background. It can still be used however when you want to rearrange objects in the same plane when using <a class="code" href="#/atom/var/appearance_flags">PLANE_MASTER</a> for visual effects.

`EFFECTS_LAYER` is a special high value that can be added to the regular layer of any atom.

The purpose of this value is to make an atom appear above any regular atoms. For instance, in an isometric map if you want to display a character's name below them, it does not make much sense to have nearer objects cover up that name, so you can tell the name overlay to use `EFFECTS_LAYER + MOB_LAYER` and it will show up on top of all the normal icons on the map. This has been somewhat obviated by `plane` but may still be useful in some cases.

When using this special layer, it should be added to the layer an atom normally uses. For instance an obj should have a layer of `EFFECTS_LAYER + OBJ_LAYER`.

This can be mixed with `TOPDOWN_LAYER`, in non-topdown map formats. Anything in `TOPDOWN_LAYER` will display on top of `EFFECTS_LAYER`, and `TOPDOWN_LAYER + EFFECTS_LAYER` will be above both.

This can also be mixed with `BACKGROUND_LAYER`, which takes priority over everything else.

Images or overlays with `FLOAT_LAYER` can be left alone. They will automatically have the same layer as whatever atom they are attached to.

Filters are a way of adding special effects to an icon, or a group of icons (see `KEEP_TOGETHER` in <a class="code" href="#/atom/var/appearance_flags">appearance_flags</a>), by post-processing the image. A filter object describes a specific form of image processing, like for instance a blur or a drop shadow. Filters can be added or removed at will, and can even be animated.

A filter is created by using the <a href="#/proc/filter">filter proc</a> like so:


```dm

// halo effect
mob.filters += filter(type="drop_shadow", x=0, y=0,\
                      size=5, offset=2, color=rgb(255,255,170))

```


These are the filters currently supported:

Uses an icon or render target as a mask over this image. Every pixel that is transparent in either the image or the mask, is transparent in the result.

The `x` and `y` values can move the mask from its normal position. By default, the mask is centered over the center of the image.

The `MASK_INVERSE` flag will invert the alpha mask so that opaque areas in the mask become transparent, and vice-versa. There is also a `MASK_SWAP` flag which treats the source image as the mask and vice-versa, which might be useful for some effects.

Note: Unlike many other filters, this filter **is** taken into account for mouse-hit purposes.

Blurs the image by a certain amount in a circular formation, as if the image is spinning. The size of the blur can roughly be thought of in "degrees" worth of blur. As the distance from the center increases, the blur becomes more noticeable since the same amount of angular motion has to travel farther along a circle.

Typically this blur is used with an entire plane, but it could be used to give a sense of motion blur to a spinning object.

Note: Large blurs will look worse toward the edges due to limited sampling. Loss of accuracy will appear where `size` × distance is greater than about 300. You can increase accuracy by breaking up large sizes into multiple filter passes with differing sizes. The blur used is Gaussian, so combining blur sizes A and B will give a total size of sqrt(A<sup>2</sup>+B<sup>2</sup>).

The `offset` parameter, if used, is effectively subtracted from the pixel distance to the center. Pixels within that radius won't blur. Anything outside that radius will act as if it's `offset` pixels closer to the center.

Post-processing effect that makes bright colors look like they're a strong light source, spreading their light additively to other nearby pixels. This is a complex effect that involves multiple shader passes. For both performance and visual reasons, it is usually best applied to an entire plane rather than to individual objects.

The color `threshold` determines which pixels this effect applies to. If any of the red, green, or blue components of the pixel are greater than the same component for the threshold, that pixel will bloom. The blooming pixels then have their colors spread outward to create a glow that gets added to the original image.

The `offset` and `size` parameters are used to control the glow effect. They work the same as they do in the drop shadow filter: `offset` causes the light to grow outwards, and a blur of `size` is then applied to soften it. Often just using a blur alone will produce a pleasing effect. By playing with these two values you can make the bloom effect appear differently.

The `alpha` value is applied to any light contributions from bloomed pixels that get added to the original image, so values lower than 255 can make the effect less pronounced. This can be very useful if you choose to animate the filter.

Blurs the image by a certain amount. The size of the blur can roughly be thought of in "pixels" worth of blur.


> [!TIP]
> Note: Large blurs will result in reduced performance. The highest size that can be handled easily in this filter is 6. Higher sizes require multiple passes, although the filter will "cheat" and use low-quality passes for much higher sizes.

Applies a color matrix to this image. Unlike with the atom.color var, you can apply color conversions other than the regular RGBA color space, depending on the value of `space`. See <a href="#/{{appendix}}/color-space">Color space</a> for more information.

Uses an icon or render target as a template for various warping effects on the main image. Think of displacement as "pulling" a pixel from an offset location.

In the displacement map, pixels that have a higher red component will make the image appear to warp to the left, lower reds warp it to the right, and gray (r=128) will cause no horizontal warping. The green component affects the vertical: higher to warp upward, lower to warp downward. Transparent pixels in the displacement map will have no effect.

This can be used for very complex distortion, unlike other distortion filters such as wave and ripple that are confined to specific equations.

The optional `FILTER_OVERLAY` flag is supported for the `flags` argument, which will overlay the displaced image onto the original.

Applies a drop shadow to this image. This is a combination of multiple filters, since it will apply an outline if `offset` is included, a Gaussian blur to the shadow, and will underlay the shadow beneath the image.

You can also think of this filter as an outer glow.

If you use a `size` less than 0, the shadow will appear inside the image instead. This would be an inset shadow, or inner glow.

Composites another image over or under this image. Using the `FILTER_OVERLAY` flag, which is the default, puts the second image on top of what's already here. `FILTER_UNDERLAY` puts it underneath.

The `x` and `y` values can move the mask from its normal position. By default, the second image is centered over the center of the first.

The `color`, `transform`, and `blend_mode` vars are available for convenience. Because the bottom image is drawn over a blank background, `blend_mode` is always applied to the top image. All of the other vars apply to the second image being drawn.

Note: Transforms use default bilinear scaling, since <a class="code" href="#/atom/var/appearance_flags">PIXEL_SCALE</a> is not available here.

Note: Like most other filters, this filter is **not** taken into account for mouse-hit purposes. Any layered icons will be strictly visual.

Applies Gaussian blur in one direction only. The amount and direction are both specified by `x` and `y`. The size of the blur is equal to `sqrt(x*x + y*y)`.

See <a href="#/{notes}/filters/blur">Gaussian blur</a> for more information.

Applies an outline to this image.

At larger sizes, the outline is less accurate and will take more passes to produce. Performance and appearance are best at sizes close to 1 or less.

`flags` can be a combination of the following values:

Blurs the image by a certain amount outward from the center, as if the image is zooming in or out. As the distance from the center increases, the amount of blurring increases, and near the center the blur is hardly visible at all. The `size` value is smaller by default for this filter than it is for other filters, since it's typically used with an entire plane where the distance from the center can easily be several hundred pixels.

Typically this blur is used with an entire plane.

Note: Large blurs will look worse toward the edges due to limited sampling. Loss of accuracy will begin when `size` × distance is greather than 6. You can increase accuracy by breaking up large sizes into multiple filter passes. The blur used is Gaussian, so combining blur sizes A and B will give a total size of sqrt(A<sup>2</sup>+B<sup>2</sup>).

The `offset` parameter, if used, is effectively subtracted from the pixel distance to the center. Pixels within that radius won't blur. Anything outside that radius will act as if it's `offset` pixels closer to the center.

Draws random rays that radiate outward from a center point. (That point may be outside of the image.) As they move outward, their alpha value diminishes linearly. These are meant to be animated. The `offset` value determines the "time", where every jump of +1 can be a very different set of rays, and every 1000 units this filter will repeat.

The `threshold` value can be thought of as a way of culling lower-strength rays. Ray strength is anywhere from 0 to 1 at any given angle, but values below `threshold` may as well be 0. Values above that are re-scaled into a range of 0 to 1.

The `factor` parameter allows you to tie the ray's length to its strength. At 0, the length of every ray is the same. At 1, the length ranges from 0 to `size`. Generally speaking, the higher `factor` is, the more the rays will appear to move outward as they strengthen and inward as they weaken.

Ray `color` can be provided as a matrix. Only the diagonal values of the color matrix will be used, but using a matrix will allow you to set values outside of the normal color range.

`flags` can have the following values:

Applies a ripple distortion effect to this image.

This filter is meant to be animated. A good animation will typically start at a `radius` of 0 and animate to a larger value, with `size` decreasing to 0.

The `falloff` parameter can be tweaked to your liking. A value of 1 should look reasonably like ripples in water, with the inner ripples losing strength. A value of 0 will cause no reduction in strength.

The equation governing the ripple distortion is size × sin(2πr') ÷ (2.5 × falloff × r'<sup>2</sup> + 1), where r' = (radius - distance) ÷ repeat.

Up to 10 ripples can be stacked together in a single pass of the filter, as long as they have the same `repeat`, `falloff`, and `flags` values. (See the wave filter for the `WAVE_BOUNDED` flag.)

Applies a wave distortion effect to this image.

The `x` and `y` parameters specify both the direction and period of the wave; the period is `sqrt(x*x + y*y)`.

This filter is meant to be animated, from whatever `offset` you want to `offset+1`, and then repeating. With multiple waves, you can produce a very convincing water effect.


```dm

#define WAVE_COUNT 7
atom/proc/WaterEffect()
    var/start = filters.len
    var/X,Y,rsq,i,f
    for(i=1, i<=WAVE_COUNT, ++i)
        // choose a wave with a random direction and a period between 10 and 30 pixels
        do
            X = 60*rand() - 30
            Y = 60*rand() - 30
            rsq = X*X + Y*Y
        while(rsq<100 || rsq>900)   // keep trying if we don't like the numbers
        // keep distortion (size) small, from 0.5 to 3 pixels
        // choose a random phase (offset)
        filters += filter(type="wave", x=X, y=Y, size=rand()*2.5+0.5, offset=rand())
    for(i=1, i<=WAVE_COUNT, ++i)
        // animate phase of each wave from its original phase to phase-1 and then reset;
        // this moves the wave forward in the X,Y direction
        f = filters[start+i]
        animate(f, offset=f:offset, time=0, loop=-1, flags=ANIMATION_PARALLEL)
        animate(offset=f:offset-1, time=rand()*20+10)

```


The equation governing the wave distortion is size × sin(2π(d - offset)), where d is the number of wave periods' distance from the center along the x, y direction.

The `WAVE_SIDEWAYS` flag will cause the distortion to be transverse (perpendicular) to the wave instead of in the same direction as the wave. The `WAVE_BOUNDED` flag limits the distortion to the confines of this image, instead of lettings its pixels spill out a little further from the distortion (and likewise, transparent pixels spill inward).

Up to 10 waves can be stacked together in a single pass of the filter, as long as they have the same `WAVE_BOUNDED` flags.

A generator is an object that can produce a random number, vector (list of 3 numbers), color (as a text string), or color matrix (list of 20 numbers) in a specified range according to rules you set down. It is used primarily for particle effects, since it can run on the client.

There are several types of generators:

Generators can also be chained together with math operators and some procs. The second value can be a regular value instead of a generator, so for instance you can multiply a vector by 2, or by a matrix to transform it.

Gliding is a "glitz" effect applied by BYOND to cover up the visual sins of tile-based movement, by making objects and the map appear to move smoothly from one tile to another instead of immediately jumping. It is also available to smooth over small jumps in pixel movement that might occur, for instance if the client FPS is set higher than the server's.

To control the gliding speed of an atom, set <code>glide_size</code> to the value of your choice. If this is not set, the client will attempt to adjust the speed manually. <code>glide_size</code> is measured in server ticks, so if <code>client.fps</code> is set to a value greater than <code>world.fps</code>, it will be scaled appropriately.

Whether an object glides or jumps is based on how far it moves relative to its `step_size` value, which by default is a full tile width. If the movement goes too far past `step_size` in the X or Y directions, it's no longer a glide.

The `animate_movement` var can be used to control the way in which an object glides, or suppress gliding altogether.

By using the `LONG_GLIDE` flag in `appearance_flags`, a diagonal glide will take just as long as a cardinal-direction glide by moving a fullt `glide_size` pixels in the dominant X or Y direction. Otherwise, gliding tries to move by that many pixels in strict Euclidean distance (a straight line) and diagonal glides take longer.


> [!NOTE]
> In <a class="code" href="#/world/var/movement_mode">LEGACY_MOVEMENT_MODE</a>, gliding is turned off if you set any of the bound or step vars for an atom to a non-default value. The only gliding that occurs in this case is when client.fps is higher than world.fps. All other movement modes base gliding on an atom's `glide_size` value.

HUD stands for Heads-Up Display, and refers to any atoms that appear on the screen but don't move when the player moves. These are also called screen objects. Any movable atom can be added to the HUD by setting its `screen_loc` var, and adding it to `client.screen` for each user who is supposed to see it. This can be used to display a character's vital stats, scores, etc.

If you want to have something like a health meter or name attached to a moving atom, use overlays or `/image` objects instead. An `/image` object is similar to a screen object in that it can be shown to only certain players instead of being shown to everyone.

The size of the screen depends on `client.view` (or `world.view`), `world.map_format`, and `world.icon_size`. In a normal topdown map format, `client.view` is the same as the screen size; in other map formats the screen might be a different size.

The `screen_loc` var can be set to a value like `"1,1"` (the southwest tile of the screen), `"4,NORTH"` (fourth tile from the west, along the north side of the screen), `"SOUTHEAST"`, and so on. You can also include pixel offsets, percentages, and specify two corners to tile an icon repeatedly from one end to the other. See <a class="code" href="#/atom/movable/var/screen_loc">screen_loc</a> for more details.

`screen_loc` can also be used to stretch the bounds of the HUD. A value of `"0,0"` will cause the atom to appear to the southwest of the southwest-most tile on the visible map, outside of the regular map bounds. Using HUDs in this way, you can provide a nice decorative "frame" for your map.

More complex

You can use HUDs in other map controls as well, by preceding screen_loc with the name of the map you will use followed by a colon. For instance, `screen_loc="map2:1,1"` will show an icon in the southwest corner of the `map2` control. The actual size of a secondary HUD is based on how far out the icons in it extend in any direction. If you have one icon at `"map2:1,1"` and another at `"map2:4,3"`, then that HUD will be four tiles wide and three high.

Isometric projection is a form of pseudo-3D in which the 2D icons used by BYOND can be arranged in a way to give the appearance of three dimensions. If you look at a map top-down, each tile on the map is a square. The map is rotated 45° clockwise and then tilted at an angle (30°) so that each square now looks like a foreshortened diamond from the viewer's perspective. What was once north now points to the northeast end of the viewer's screen; what was once east now points southeast to the viewer. Tiles that are more to the south or east are "nearer" to the viewer, and tiles that are north or west are "farther". The actual direction the map faces can be changed by using `client.dir`.

It is important to remember that this is an illusion of 3D, not real 3D.

To use isometric mapping, set `world.map_format` to `ISOMETRIC_MAP`. You should set `world.icon_size` so the tile width is a multiple of 4 pixels. The width of the tile is highly important. The height of your tiles should be at least half that value. BYOND uses a 2:1 isometric format, meaning that the diamond base of each tile is half as high as its width. For example if you have a 64x64 tile size, every diamond in the map will be 64 pixels wide by 32 high, and you have an extra 32 pixels at the top of your icon for vertical projections like buildings. If you set the tile size to 64x80, the base is still a 64x32 diamond and you have 48 pixels left over for vertical structures.

In this mode `pixel_x` and `pixel_y` will offset icons along the "ground". To adjust horizontal and vertical positions, use the `pixel_w` and `pixel_z` vars.

The `layer` var behaves differently in isometric mode. Because some tiles are nearer to the viewer than others, the tiles that are farther back need to be drawn first so they are behind any tiles that should go in front of them. So in isometric mode, the back row of tiles (a diagonal line of them) is drawn first, followed by the next row forward, and so on. The `layer` var only matters when icons overlap each other in the "physical" space, like an obj sitting on a turf.

When pixel or step offsets, or gliding, place an object on multiple turfs, it is drawn on top of the nearer turf (assuming its layer is higher).

Using icons wider than the regular tile size can have an impact on layering as well. See <a href="#/{notes}/big-icons">Big icons</a> for more information.

Because of the order in which icons are drawn, you may want to limit the ability of an atom to cut diagonally around corners. While moving northeast behind a dense wall, for instance, a mob might temporarily appear in front of the wall because its pixel offsets (from gliding) temporarily put it on the same tile as the wall. If you do not want to limit corner-cutting, a simple workaround for this case is to give the wall a higher layer than the mob.

Screen objects (in `client.screen`) are always drawn on top of all isometric tiles, as is the case in other map modes as well.

Since it may be desirable in some games to use a topdown map for some situations (like a special battle map), you can add `TOPDOWN_LAYER` to any atom's layer—e.g., `TOPDOWN_LAYER+TURF_LAYER`—to make it appear in topdown mode. Topdown and isometric tiles really aren't meant to be mixed, but if they do mix you'll see topdown tiles always display above isometric tiles, just like screen objects do. The best way to use this is to apply `TOPDOWN_LAYER` to every tile in a certain part of the map that the players can't walk to.

If you want to use an overlay that should not be covered by other "nearer" icons on the map, such as a name or health meter, you can add `EFFECTS_LAYER` to the overlay's layer. Icons with `EFFECTS_LAYER` will draw above regular icons. Then objects with `TOPDOWN_LAYER` will draw on top of everything else. However, be aware that `EFFECTS_LAYER` has largely been superseded by the `plane` var.

In this mode, `world.view` or `client.view` is used to define the minimum number of map tiles you will see, *not* the screen/HUD size which is calculated from client.view. Extra map tiles are shown to fill out the screen size. HUD objects use screen coordinates, so 1,1 is still the lower left.

The actual HUD size is always a full number of tiles, whose size is defined by `world.icon_size`. If you have a tile size of `64x64`, and `world.view=6` (a 13x13 map), a full 13x13 diamond of map tiles will be shown. The width of this diamond is 13 tiles. The height is only half that, plus whatever vertical space is needed to show the icons in that area. Then everything is rounded up to a full tile size, so the result is a 13x7-tile screen. This is the formula you need if you want to calculate the screen size:


```dm

pixel_width = round(icon_width * (view_width + view_height) / 2)
pixel_height = round(icon_width * (view_width + view_height - 2) / 4) + icon_height

screen_width = round((pixel_width + icon_width - 1) / icon_width)
screen_height = round((pixel_height + icon_height - 1) / icon_height)

```


If you use `TOPDOWN_LAYER`, any topdown sections of the map will be limited to this same view.

In DM, all numbers are stored in floating point format. Specifically, single-precision (32-bit) floating point. This is important to know if you think you will be working with large numbers or decimal values a lot, because the accuracy of the numbers is limited.

32-bit floating point numbers can represent integers from -16777216 to 16777216 (2<sup>24</sup>). Non-integer values can get about as small as 2<sup>-126</sup> and as large as 2<sup>127</sup>.

Floating point numbers do not handle most decimal values precisely. For instance, 0.1 is not exactly 0.1, because floating point numbers are stored in a binary format and in binary, 1/10 is a fraction that repeats forever—the same way 1/3 repeats as 0.33333... in decimal numbers. It ends up being rounded off, either a little higher or a littler lower than its true value. This means that the following loop won't work like you might expect:


```dm

for(i = 0, i < 100, i += 0.1)
    world << i

```


You might expect that code to loop exactly 1000 times, with `i` going from 0 up to 99.9 before stopping. The truth is more complicated, because 0.1 stored in floating point is actually greater than the exact value of 0.1. Other values might be more or less than their exact numbers, and as you add these numbers together repeatedly you'll introduce more and more rounding error.

Even more insidious, if you add 0.1 a bunch of times starting from 0, and then subtract it out again the same number of times, the result you get may not be 0. This is counterintuitive, because you might expect rounding errors to reverse themselves in the same order they crept in. Unfortunately it doesn't work that way.

You can correct for rounding error somewhat by using the <a href="#/proc/round">`round` proc</a> to adjust the loop var each time, although for performance reasons it might be preferable to find another alternative.


```dm

for(i = 0, i < 100, i = round(i + 0.1, 0.1))
    world << i

```


Only fractions whose denominators are powers of 2 are immune to this rounding error, so 0.5 is in fact stored as an exact value.

Another place floating point may lose accuracy is when you try to add numbers of very different sizes. For instance as stated above, the upper limit for accurate integers is 16777216. If you try to use a number such as 100 million it will only be approximate, so adding 1 to that number won't actually change it because the 1 is so much smaller, it will be gobbled up by rounding error.

Also for the same reasons stated above, division will cost you accuracy. Again you can divide by powers of 2 easily enough, and you can divide an integer by any of its factors (like dividing 9 by 3) without a problem, but a fraction like 1/3 will repeat forever so it gets rounded to as much precision as floating point can manage.

In decimal, floating point numbers have at least six decimal digits of precision. Since they're actually stored in binary, their true precision is exactly 24 bits.

A particle set is a special effect, whose computations are handled entirely on the client, that spawns and tracks multiple pixels or icons with a temporary lifespan. Examples of this might be confetti, sparks, rocket exhaust, or rain or snow. Particles are rendered on a special surface and that gets attached to an obj or a mob like an overlay.

Particles can exist in 3 dimensions instead of the usual 2, so a particle's position, velocity, and other values may have a z coordinate. To make use of this z coordinate, you can use a <a href="#/{notes}/projection-matrix">projection matrix</a>. (The value of the z coordinate must be between -100 and 100 after projection. Otherwise it's not guaranteed the particle will be displayed.)

To create a particle set, use `new` to create a new `/particles` datum, and then you can set the datum's vars. The vars can be set to constant values, or generator functions that will allow the client to choose from a range of values when spawning those particles. (The easiest way to handle this is to create your own type that inherits from `/particles`, and set up the parameters you'll want at compile-time.)

After the datum is created, it can be assigned to an obj or mob using their `particles` var. The particles will appear on the map wherever that obj or mob appears.


```dm

particles/snow
    width = 500     // 500 x 500 image to cover a moderately sized map
    height = 500
    count = 2500    // 2500 particles
    spawning = 12    // 12 new particles per 0.1s
    bound1 = vector(-1000, -300, -1000)   // end particles at Y=-300
    lifespan = 600  // live for 60s max
    fade = 50       // fade out over the last 5s if still on screen
    // spawn within a certain x,y,z space
    position = generator("box", vector(-300,250,0), vector(300,300,50))
    // control how the snow falls
    gravity = vector(0, -1)
    friction = 0.3  // shed 30% of velocity and drift every 0.1s
    drift = generator("sphere", 0, 2)
obj/snow
    screen_loc = "CENTER"
    particles = new/particles/snow

mob
    proc/CreateSnow()
        client?.screen += new/obj/snow

```


These are the vars that can be used in a particle set. "Tick" refers to a BYOND standard tick of 0.1s.

The `icon` and `icon_state` values are special in that they can't be assigned a generator, but they can be assigned a constant icon or string, respectively, or a list of possible values to choose from like so:


```dm
icon = list('confetti.dmi'=5, 'coin.dmi'=1)
```


The list used can either be a simple list, or it can contain weights as shown above.

Changing a var on a particle datum will make changes to future particles. For instance, you can set the datum's `spawning` var to 0 to make it stop creating new particles. (Note: If you are changing a vector or color matrix, such as `gravity`, you need to assign a new value. You can't for instance set `particles.gravity[2] = 0` because it won't do anything to update the particle stream.)

The same particle datum can be assigned to more than one movable atom. However the particles displayed by each atom will be different.

If you want to spawn particles at specific times, you can use the client <a href="#/{skin}/commands/%2eadd-particles">`.add-particles` command</a>. From the server, you can run this command via <a class="code" href="#/proc/winset">winset()</a>.


```dm

// spawn 100 particles for src's particle set right now
winset(player, null, list(command=".add-particles \ref[src] 100"))

```


Pixel movement is a concept that allows atoms to escape the constraints of BYOND's historically tile-based movement, and move in smaller steps. In the past this had to be done with soft code, but that was sometimes inconvenient and it did not perform as well in projects with many objects moving.

The key to understanding pixel movement is to use the bound and step vars. You use the bound family of vars to define a bounding box for a movable atom, instead of just making it one full tile in size. The step vars can give it a movement speed and offset it from the corner of the tile it's standing on.

Those are for movable atoms only; they do not apply to turfs.

If <a class="code" href="#/world/var/movement_mode">world.movement_mode</a> is set to `TILED_MOVEMENT_MODE`, all movable atoms must be aligned to the tile grid: their step_x/y/size values must be multiples of the icon size, and their bounds must also land on tile boundaries although the atom can be bigger than one tile. In other movement modes you can specify that only specific atoms use this behavior, by giving them the <a class="code" href="#/atom/var/appearance_flags">TILE_MOVER</a> appearance flag.

**Left:** The bounding box (blue) is the only part of the mob that actually collides with anything. By default, it would cover the whole turf (brown). Any turfs covered by the bounding box are in the mob's locs var. **Right:** The atom's true position (shaded) is offset from the turf by step_x and step_y.

As an example, if your players' mobs have icons that only cover the center 24×24 pixels of a regular 32×32 icon, then you would set the mobs' bound_x and bound_y to 4--because there are 4 pixels unused to the left and bottom--and bound_width and bound_height to 24.

The mob's physical location on the map depends on four things: Its loc, its step_x/y values, its bound_x/y values, and its bound_width/height. The lower left corner of the bounding box, relative to the turf the mob is actually standing on, begins at step_x+bound_x on the left and step_y+bound_y on the bottom.

The physical position of the bounding box is **not affected** by the pixel_x/y/z vars. Those are still strictly visual offsets.

The turfs the mob is covering can be read from the read-only locs var. The mob will also appear in the contents of those turfs.

Note: This means if an atom is in a turf's contents, its loc is *not necessarily* that turf. The contents list is made to include "overhangers" from another tile for ease of use.

All of the step and walk procs have been upgraded to take an additional argument, which is the speed at which the atom should move. If that argument is left out, the atom's own step_size is used by default. The step_size determines how fast the step_x and step_y values will change when moving.

Move() has two new arguments that handle the position change gracefully. These are the step_x and step_y values for the target location.

Pixel movement changes the behavior of the Move() proc, because a lot of things are possible that were not possible when BYOND only supported moving one tile at a time. For starters, a Move() is either a "slide" or a "jump" depending on the distance. A slide is when the move can be stopped partway; a jump is strictly pass/fail. Anything greater than one tile *and* the mover's regular step_size is considered a jump. Changing z levels is also a jump, as is moving to/from a non-turf.

If step_x and step_y aren't within a good range, the new loc and the step_x/y values may be changed so that the southwest corner of the mover's bounding box is standing on its actual loc, or as close to it as possible.

Enter() and Exit() can be called for several turfs and/or areas, not just one at a time. It is also possible for them not to be called at all, if the moving atom moves within a turf but doesn't cross a new turf boundary. Enter() and Exit() are only called when first attempting to enter or fully exit. The behavior of these procs depends on <a class="code" href="#/world/var/movement_mode">world.movement_mode</a>; in legacy mode, they look at some of the contents of the turfs as well as the turfs themselves, to preserve behavior found in older BYOND versions.

Cross() and Uncross() are the equivalent of Enter() and Exit() but apply to objects the mover will either overlap or stop overlapping. (For turfs, Enter() and Exit() call these procs by default, since the mover is both stepping *into* and *onto* a turf.) Likewise Crossed() and Uncrossed() are the equivalents of Entered() and Exited().

If an atom is sliding, its movement can be halted if it encounters an obstacle partway along its route. Bump() will still be called for any obstacles the atom runs into, but Move() will return the number of pixels moved (the most in any direction). When sliding at a speed so fast that the distance is bigger than the atom itself, the move will be split up into several smaller slides to avoid skipping over any obstacles.

Gliding, which is used to show smooth movement between atoms in tile movement, is mostly not used in pixel movement. It only applies when the client uses a higher <a class="code" href="#/client/var/fps">fps</a> than the server.

The bounds() and obounds() procs have been added to grab a list of atoms within a given bounding box. That box can be relative to an atom, or in absolute coordinates.

bounds_dist() tells the distance between two atoms, in pixels. If it is positive, that is the minimum distance the atoms would have to traverse to be touching. At 0, they are touching but not in collision. A negative value means the two atoms are in collision.

Note: Currently this feature applies only to particle effects, using the `transform` var.

Normally icons in BYOND can only be transformed in 2D, using a simple 3x3 matrix. This is represented by the `/matrix` object, which cuts off the last column because it isn't used. However particles can have coordinates in x, y, and z, and the whole particle set can be given a transformation matrix that handles all three dimensions.

The easiest transformation for particles is a simple 2D one, which you can do by setting the particle datum's `transform` var to a `/matrix` object.

When an x,y point is multiplied by the matrix, it becomes the new point x',y'. This is equivalent to:

This is called an **affine transform** because all the operations are "linear" in math terms. (That is, every term in the formula above has a single variable, not raised to a higher power than 1.)

3D affine transforms of this type are also affine transformations. There is no special object for this so a list is used (see below).

The way to read the vars above is that the first letter says what input component is being transformed (x,y,z, or c for "constant"), and the second letter is the output component.

To use this kind of matrix, you can cut off the 4th column and provide the values in a list form, in row-major order:


```dm
list(xx,xy,xz, yx,yy,yz, zx,zy,zz, cx,cy,cz)
```


Note the 4th row is also optional.

This is the most interesting matrix, since if you use all 4 columns you're actually altering an "axis" called w. This isn't a real axis, but is just a number that the resulting vector will be divided by.

In a regular affine transform, w always stays at 1. In projection you can think of w as a distance from the "camera". 1 is where objects are their "normal" size. If you make the z value affect w' by setting zw, you basically make an object look smaller at higher z values.

This is a simple projection matrix where x,y,z are left untouched, but there's a projection effect. The "D" value is how far away the "camera" is from z=0, so a point at z=D looks like it's twice as far away.

This 4x4 matrix is handled as a list just like the 3x4 affine matrix:


```dm
list(xx,xy,xz,xw, yx,yy,yz,yw, zx,zy,zz,zw, wx,wy,wz,ww)
```


Regular expressions are patterns that can be searched for within a text string, instead of searching for an exact match to a known piece of text. They are much more versatile for find and replace operations, and therefore useful for parsing, filtering, etc.

Some example regular expressions are:

These are some of the patterns you can use. If you want to use any of the operators as an actual character, it must be escaped with a backslash.

It is highly recommended that you use <a href="#/DM/text">raw strings</a> like <code>@"..."</code> for your regular expression patterns, because with a regular DM string you have to escape all backslash <code>\</code> and open bracket <code>[</code> characters, which will make your regular expression much harder for you to read. It's easier to write <code>@"[\d]\n"</code> than <code>"\[\\d]\\n"</code>.

The optional flags can be any combination of these:

After calling `Find()` on a `/regex` datum, the datum's `group` var will contain a list—if applicable—of any sub-patterns found with the `()` parentheses operator. For instance, searching the string `"123"` for `1(\d)(\d)` will match `"123"`, and the `group` var will be `list("2","3")`. Groups can also be used in replacement expressions; see the <a class="code" href="#/regex/proc/Replace">Replace() proc</a> for more details.

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

The side-view map format is used for 3/4 perspective, where the map is basically similar to a top-down view but is usually foreshortened. Just like with isometric projection, tiles that are closer to the bottom of the screen are considered to be closer to the viewer. This is a form of pseudo-3D in which the 2D icons used by BYOND can be arranged in a way to give the appearance of three dimensions.

It is important to remember that this is an illusion of 3D, not real 3D.

The `layer` var behaves much the same way it does in `ISOMETRIC_MAP` mode.See <a href="#/{notes}/isometric">isometric maps</a> for more information.

When using this mode you may want to use a foreshortened `world.icon_size`, like a 32x24 format instead of 32x32 for example, and use taller icons for any vertical structures like walls or buildings. If you set `world.icon_size` to use foreshortening, then `pixel_y` (or `pixel_x`, depending on the orientation of client.dir) will be adjusted for you; the same applies to `step_x` and `step_y`. For example, with `world.icon_size` set to `"64x32"`, the *physical* tile—what you would see if you were to look at it straight down from above— is considered to be 64x64, so you would need `pixel_y=64` or `step_y=64` to offset by a whole tile. This adjustment does not apply to screen objects, `pixel_w`, or `pixel_z`.

In BYOND 3.0, any file like a large .bmp would be treated like a regular icon that had been broken up into several tile-sized icon states. All tiles then were 32x32 pixels. An image that was 100x100 would therefore take at least 4x4 tiles to display. The icon was padded to the right and the top with blank space to become an even multiple of 32x32, and then broken up into sections. The lower left section was given an icon_state of `"0,0"`, the next to the right was `"1,0"`, and so on, up to the upper right which was `"3,3"`. Another icon state, a 32x32 thumbnail of the big image, was also included.

BYOND 4.0 expanded on this concept by allowing icons to be defined that had individual graphics bigger than 32x32, and it would break each one up into tiles just like 3.0 did. If an icon had a state called `"open"` then it might break down into `"open 0,0"`, `"open 1,0"`, and so on, while the actual `"open"` state would be a thumbnail image. To show the whole image, you would have to have a separate atom or overlay for each individual tile.

In newer versions, breaking big icons into tiles is no longer done by default. Instead, icons are shown and manipulated in their <a href="#/{notes}/big-icons">native size</a>. To use the old method of breaking icons into tiles, set `world.map_format` to `TILED_ICON_MAP`. This is the default for all projects compiled before version 455.

When using tiled icons, there are some important things to note:

This example shows a big icon being applied to an atom in tiled mode, as overlays:


```dm

// icon is 3 tiles wide by 2 high
icon_state = "0,0"

// A temporary object used for the overlays
var/obj/O = new
O.icon = icon
O.layer = FLOAT_LAYER

for(var/tile_y=0, tile_y<2, ++tile_y)
   for(var/tile_x=0, tile_x<3, ++tile_x)
      if(tile_x && tile_y)
         O.pixel_x = tile_x * 32
         O.pixel_y = tile_y * 32
         O.icon_state = "[tile_x],[tile_y]"
         overlays += O

```


By default, BYOND displays all maps in top-down format, so `world.map_format` is set to `TOPDOWN_MAP` unless you say otherwise. This view means players are looking down on the map, and "north" corresponds to the top of their screen. (This can be changed by setting `client.dir`.)

A related map_format, used by older games, is `TILED_ICON_MAP`. This is also topdown but it handles icons differently.

In this form, the `layer` var behaves exactly as you would expect: Icons with a lower layer are drawn beneath icons with a higher layer. The only exception is when you use <a href="#/{notes}/big-icons">big icons</a>, which will be drawn above any other icons on the same layer. Also an atom's underlays will be drawn behind it unless their layer is changed, and its overlays will draw in front of it unless otherwise stated.

Topdown mode also guarantees that `world.view` or `client.view` will set the exact screen size used by the HUD, except for HUD objects that appear outside of the normal bounds.

Screen objects (also called the HUD) cannot be intermixed with topdown icons. They will appear on top of other icons, unless using a lower plane or a special layer like `BACKGROUND_LAYER`.

TOPDOWN_LAYER is a special high value that can be added to the regular layer of any atom. This is only available when using a non-topdown world.map_format, such as isometric mapping.

The purpose of this value is to make an atom appear as if it belongs in a top-down map, when using a map_format other than TOPDOWN_MAP or TILED_ICON_MAP. This can be handy for title screens, or for special battle maps or the inside of a building in an RPG.

When using this special layer, it should be added to the layer an atom normally uses. For instance a turf should have a layer of TOPDOWN_LAYER + TURF_LAYER. Usually you will want one part of the map to have TOPDOWN_LAYER, and for players to be unable to walk to there from the regular map. Mixing topdown icons and icons in the normal map_format in view of each other could look very strange. For safety's sake, the easiest thing to do is to keep them on separate z layers.

This can be mixed with EFFECTS_LAYER. Anything in TOPDOWN_LAYER will display on top of EFFECTS_LAYER, and TOPDOWN_LAYER + EFFECTS_LAYER will be above both.

This can also be mixed with BACKGROUND_LAYER, which takes priority over everything else.

Images or overlays with FLOAT_LAYER can be left alone. They will automatically have the same layer as whatever atom they are attached to.

BYOND was originally written to handle 8-bit ("ANSI") characters only. However as time has marched on, Unicode has become ubiquitous for supporting multiple languages, special characters, and emojis. To adapt to this, BYOND now supports Unicode.

When ANSI was king, every character was exactly one byte in width, because the only valid characters were between 1 and 255. (And technically, BYOND reserved 255 for its own use.) Now, BYOND uses an encoding called UTF-8 to store characters that can't fit in one byte.

UTF-8 breaks up characters with codes of 128 or higher into multiple bytes, like so:

Importantly, BYOND's text procs are based on the byte position, not the character position which may be lower. In other words, `length("abcdéfg")` is greater than 7; it's 8, because `é` takes up 2 bytes in UTF-8. That also means `f` is at position 7, not position 6.

Why do the text procs work with byte position instead of character position? Because ultimately, it's faster. Going by character position would require counting every byte in a string (at least when it uses UTF-8) until the right character position was found. This would be detrimental to performance in most cases.

For the most part, this distinction should be fairly invisible to you. Most code isn't going to encounter problems, but if you do a lot of text processing you should be aware of it.

In particular, <a class="code" href="#/proc/text2ascii">text2ascii()</a> returns the Unicode value at a specific position, which may cover several bytes. If you loop through a string calling this proc for each character, you'll have to make adjustments for cases when multiple bytes have been read.

The read-only `[]` index operator also uses byte positions.

If you read a byte or cut text at an inappropriate point, any broken characters resulting from the cut will be turned into the Unicode replacement character � which is 0xFFFD.

Most of the text handling procs have slower `_char` versions (e.g., `copytext_char`) that use character positions instead of byte positions.

These should be used sparingly if at all; whenever it's possible to use byte positions, you should. When you do use a `_char` version of a proc, prefer using `-offset` instead of `length_char(text)-offset` for positions near the end of the string. Most text procs allow negative position values that count backwards from the end, and counting a small number of characters backward is faster than counting a lot of characters going forward.

Code written in ANSI will be up-converted to UTF-8 by Dream Maker, based on your current locale when the code is loaded.

BYOND games used to have very limited interface options, all effectively sharing the same layout. In BYOND 4.0, skins were introduced, allowing developers more control over the layout.

A skin consists of <a href="#/{skin}/macros">macro sets</a> for keyboard/gamepad input, menus, and windows and/or panes. All of these are considered <a href="#/{skin}/control">controls</a> that a game can interact with via <a class="code" href="#/proc/winset">winset()</a>, <a class="code" href="#/proc/winget">winget()</a>, <a class="code" href="#/proc/output">output()</a>, and a few other procs.

About the simplest possible skin is a single window with a single <a href="#/{skin}/control/map">map control</a>, and a single macro set.

Several commands can be executed on the client that are not verbs, but instructions for Dream Seeker. Some of these commands have detailed syntax described in their own reference entries.

Client commands have a special syntax that allows you to query information from the skin and include it directly in the command, as if you had called <a class="code" href="#/proc/winget">winget()</a>. Embedded expressions look like `[[*expression*]]` in your command text. Some commands have built-in data that gets filled in via `[[*]]`. See <a href="#/{skin}/commands/embed">embedded winget</a> for more information.

Immediately spawns a batch of particles for a known particle set.

The object parameter is a <a href="#/proc/ref">reference string</a> for the object that holds the particles.

A negative count is allowed, which will absorb some ordinary particle spawns.

If the object isn't known to the client, nothing will happen.

Sends output to a control. The text does not need quotes, but any backslashes, newlines, and tabs should be escaped with a backslash. This works similarly to the <a href="#/proc/output">`output()` proc</a>. If text is omitted, the control is cleared.

Here is an example of using a map control's <a class="code" href="#/{skin}/param/on-status">on-status</a> event to set a label rather than using the window's own statusbar.

Plays, stops, or modifies a sound. This command can be used for instance to play a click sound when using mouse macros, for instance, without waiting for the server to initiate the sound which would introduce a small delay.

The file can be `none` or `-` when updating or stopping a sound. Any options should be separated by spaces; most are in a `name=value` format, as seen below.

Supported options are:

**T* represents a true/false value. True values include `true`, `on`, or 1. False would be `false`, `off`, or 0.

Sets skin parameters like the <a href="#/proc/winset">`winset()` proc</a>. You can set more than one parameter by separating them with semicolons.

This command also allows you to use conditional expressions, like so:

The condition is the same as any other parameter you might use in `.winset`, but instead of setting the parameter, it checks to see if it's true. If so, then the parameters in `choice1` will be set. Otherwise, the parameters in `choice2` are set. This example makes the window background red if bigbutton is checked.

If you want to look for values that don't match instead of values that do, use `!=` instead of `=` in the condition.

The `choice2` item is optional.

Because it's often useful to do more than one thing at a time, `choice1` and `choice2` don't have to be just one parameter. You can use multiple parameters, but they are separated with a space instead of a semicolon. (A semicolon indicates the conditional expression is over.)

Commands that are initiated by the skin (like button.command, map.on-show, etc.) have a special syntax that allows you to include information that would normally require a winget call. By including `[[*something*]]` in the command, the double-bracketed text will be replaced by the result of running a winget on that parameter.

A value of `[[id.parameter]]` will run a winget on the control with the given ID. Just using `[[parameter]]` will run a winget for the control that initiated this command. You can also use `parent` in place of the ID to do something with the parent of the control, or `parent.id` for access to a sibling control. Position and size parameters can be further broken down by appending `.x` or `.y` to get at the numbers directly.

Several commands already support some special cases like `[[*]]` or `[[width]]` or such, where the special-case values are relevant to the command. An example is that in `on-size` the value of `[[*]]` is a size value. The Any macro, gamepad macros, and mouse macros, also support this syntax; see <a href="#/{skin}/macros">macros</a> for more info.

You can choose how embedded wingets get formatted by following the value with `as` and a type, such as `[[window.size as string]]`. There are several types you can use, and different types of parameters get formatted differently:

The `arg` type is the default, unless the `[[`*...*`]]` expression has double quotes on both sides, in which case `escaped` is the default.

Controls can be created or deleted at runtime. (Only controls you created during runtime may be deleted.) To create a control, call <a class="code" href="#/proc/winset">winset()</a> using the <a class="code" href="#/{skin}/param/id">id</a> of the new control, and the parameter list should include <a class="code" href="#/{skin}/param/type">type</a>, <a class="code" href="#/{skin}/param/parent">parent</a>, and probably also <a class="code" href="#/{skin}/param/pos">pos</a>, <a class="code" href="#/{skin}/param/size">size</a>, and any <a href="#/{skin}/param/anchor">anchors</a>.

To delete the control again, set its `parent` to a blank value.

Menu items and macros work similarly, except they have no positional info. For those, the <a class="code" href="#/{skin}/param/name">name</a> parameter is important when you create them, and you will either need <a class="code" href="#/{skin}/param/command">command</a> or (for macros) <a class="code" href="#/{skin}/param/map-to">map-to</a> to do anything with them.

A progress bar or interactive slider. This can be made to use several different orientations. Its `value` can be read or set as a percentage from 0 to 100.

A browser panel integrated into the skin.

Browsers are capable of displaying HTML documents, and can also interact with the skin.

A longstanding behavior of BYOND is the ability to create a new browser window by sending an extra argument to the <a class="code" href="#/proc/browse">browse()</a> proc. Since the advent of skins in BYOND 4.0, this behavior was kept. When you create a new browser popup, the window name you specify for the popup is used for the name of a new <a href="#/{skin}/control/main">window control</a>, and within that window there will be a new browser control simply called `browser`.

If you want to interact with the new browser, its full "decorated" <a class="code" href="#/{skin}/param/id">id</a> is `*windowname*.browser`.

Sending <a class="code" href="#/proc/output">output()</a> to a browser will send a document to display there, but if you follow the browser's control name with a colon and a function name, you can call a JavaScript function in the document displayed within that browser.


```dm

var/list/info = list("name"="fridge", "power"=12)
// send {"name":"fridge","power":12} to a JavaScript function
usr << output(url_encode(json_encode(info)), "mybrowser:myJSfunction")

```


The text that you send as output will be parsed like URL parameters, where mutliple arguments to the function are separated by `&amp;` or `;`, which is why <a class="code" href="#/proc/url_encode">url_encode()</a> is wrapped around the <a class="code" href="#/proc/json_encode">json_encode()</a> call in this example.

These topics cover more advanced uses of the browser control.

The BYOND object is a built-in shortcut for interacting with the client via JavaScript in a browser control. It contains the following methods:

Performs a <a href="#/{skin}/control/browser/winset">winset</a>, where `id` is the ID of the control to change (or null for global settings), and `params` is an object with parameter,value pairs such as `{"text-color": "red"}`. Parameters can use camelCase, where a capital letter indicates where a hyphen would normally go, e.g. `"textColor"` and `"text-color"` are the same.


```dm

// uncheck a button from JavaScript
BYOND.winset("inventory_button", {isChecked: false});

```


Sends a <a href="#/{skin}/control/browser/winset">winget</a>, where `id` is the ID of the control to retrieve (or null for global settings), and `props` is a single property or an array of properties to retrieve. As with `winset`, camelCase is allowed, but the result will not use camelCase.

Returns a Promise object, so this call can be used with the `await` keyword or followed by `then()`. The result inside the promise is an object with parameter,value pairs, such as `{"background-color": {value: "#ff0000", red: 255, green: 0, blue: 0, isDefault: false}}`.


```dm

// get a button's status JavaScript
let buttonData = await BYOND.winget("inventory_button", "isChecked");
if(buttonData["is-checked"]) {
    alert("The button is checked!");
}

```


Initiates a <a href="#/{skin}/commands">client command</a>. This is basically just a shortcut for using `winset` to run a command.


```dm

// play a sound
BYOND.command(".sound 'ding.ogg'");

```


A replacement for `localStorage` that can be used to hold information for reuse in later sessions of the same game. (This must be enabled via `browser-options` with the <a href="#/proc/winset">`winset()` proc</a>.)

There are three actual storage objects you can use:

Interacting with these storage objects is done in JavaScript, the same way you would use `localStorage` or `sessionStorage`.

Note: Technically `localStorage` does work, but because of the way BYOND handles browser controls it acts more like `sessionStorage` in practice.

Browser controls can interact with the skin via JavaScript, by setting `window.location` to a special URL.

This works like an ordinary <a class="code" href="#/proc/winset">winset()</a> call from the server. If `id` is omitted, it's the same as a winset with a null ID. You can also leave the `id` blank if you use "fully decorated" property names such as `mybutton.is-checked` instead of just `is-checked`.

Any text you use other than letters, numbers, hyphens, commas, and periods should be encoded via the `encodeURIComponent()` function in JavaScript.

In this winget, the IDs and properties you want can be separated by commas if you want to retrieve more than one. The winget operation works via a callback function you must define in JavaScript. The callback is given just one argument, a JavaScript object with all of the properties you requested. For example, this URL:

...might send this to the callback function `wgcb`:

The property names will be in the same format you would expect from <a class="code" href="#/proc/winget">winget()</a>, so when you're looking at multiple elements' properties, you'll get the full names in `id.property` format. The values are always sent back in a convenient form for JavaScript to work with; in the case of size, position, and color these will always be objects.

An optional `control` parameter for the winget call can be used if you want to send data to a callback in a different browser control.

A button that can be pressed to run a <a href="#/{skin}/commands">command</a>, or possibly toggled.

A container that can hold one or two <a href="#/{skin}/control/main">panes</a>. If it holds two panes, a splitter may appear between them. This control can therefore be used to subdivide a window or pane into smaller units.

A grid that contains multiple cells that can show various kinds of output data.

Sending output to a grid looks like this:


```dm

// output to column 3, row 2
winset(usr, "thegrid", "current-cell=3,2")
usr << output("Text", "thegrid")

// or even easier:
usr << output("Text", "thegrid:3,2")

// when is-list is true:
usr << output("5th item", "thegrid:5")

```


You can output an atom to the grid, which can be clicked, dragged, etc. However, you should make sure that atom is *not* temporary and will persist until you no longer need it, or else the server may recycle it and the object in the cell will either disappear or be impossible to interact with anymore.

There are some limitations to output in grid controls:

The classic BYOND statpanel, which contains both stat and verb tabs. This is technically a 3-column grid with a variable number of rows.

Output to a statpanel is done via the <a class="code" href="#/proc/stat">stat()</a> and <a class="code" href="#/proc/statpanel">statpanel()</a> procs, during <a class="code" href="#/atom/proc/stat">mob/Stat()</a>.

The same limitations that apply to <a href="#/{skin}/control/grid">grid</a> output apply here.

Info controls can now be split so that one displays stats and another handles verbs.

A text box into which the user can type. By default this is used for sending <a href="#/{skin}/commands">client commands</a>, but it can be used for other purposes as well.

Note that when in "standard" mode of accepting user commands, built-in verbs like `.click`, or local commands like `.winset`, are not accepted when typed in. This kind of command can still be entered manually through the Client menu of the Options &amp; Messages window.

A text label that appears on the skin.

A <a href="#/{skin}/macros">keyboard/gamepad/mouse macro</a>, usually designed to run a <a href="#/{skin}/commands">command</a>. The control is a means of interacting with the macro as an object, allowing some of its properties to be changed at runtime.

A container for other controls. The Main control takes two forms: a window or a pane.

A window exists independently and can be moved around on the screen. A pane has to be used within another container control such as a <a href="#/{skin}/control/child">Child</a> or <a href="#/{skin}/control/tab">Tab control</a>.

The font parameters have no impact on a window's statusbar or titlebar; those are drawn by the operating system.

A map that will display icons from the game.

A menu item, that when activate will run a <a href="#/{skin}/commands">command</a>.

Displays text output.

A tab control, where each tab holds a different <a href="#/{skin}/control/main">pane</a>.

Macros are used to convert keyboard and gamepad events into actions. There are two ways this works: A macro can run a command, or in some cases (such as gamepad controls) it can be used to remap one control to another.

A collection of macros is called a macro set, and the window currently in use defines which macro set will be used via its <a class="code" href="#/{skin}/param/macro">macro</a> parameter.

Macros can be changed at runtime. If a macro does not have an <a class="code" href="#/{skin}/param/id">id</a>, you can refer to it by its key combination (<a class="code" href="#/{skin}/param/name">name</a>). If you have a macro set named `macro1` and have a `Ctrl+E` macro for instance, you could use <a class="code" href="#/proc/winset">winset()</a> with `"macro1.Ctrl+E"`. See the <a href="#/{skin}/control/macro">Macro control</a> for information on which parameters you can change with `winset()`.

The `name` of the macro is actually the full key combination as it would appear in the macro editor, like `CTRL+E`, `Space+REP`, or `Alt+Shift+F1`. This is not case-specific and it doesn't matter where you put modifiers like `CTRL+`, `SHIFT+`, etc.

Oftentimes it's desirable to keep track of key presses yourself rather than have a hundred different macros defined. BYOND makes this possible via the `Any` and `Any+UP` macros, which respond to any key or gamepad button. `UP` is the only allowed modifier for this macro, since other modifier keys are handled by this same macro.

Typically, you will want to use <a class="code" href="#/verb/set/instant">set instant=1</a> on the verbs that will be tied to the Any macro, so that keyboard input doesn't queue up and lag behind.

In the <a class="code" href="#/{skin}/param/command">command</a> that goes with this macro, `[[*]]` will be replaced with the name of the key or gamepad button that was pressed/released. (See <a href="#/{skin}/commands/embed">embedded winget</a> for more details on the `[[...]]` format.)

The <a class="code" href="#/{skin}/param/map-to">map-to</a> parameter is used by **mappings**, which are like macros but are used to convert gamepad inputs easily and quickly to keyboard inputs. E.g., `GamepadLeft` can map to `West` which is the left arrow key. A set of default mappings will be added automatically at runtime if you don't include any gamepad mapping in your project.

BYOND will support up to four gamepads, and breaks up their input into the following categories:

See the list of available macros below for information on how to harness these inputs.

To let a user configure their gamepad, you need to call the client-side `.gamepad-mapping` <a href="#/{skin}/commands">command</a>. Or, if they have access to the Options &amp; Messages window and Dream Seeker's default menus, they can reach it from there. However it's a good idea to make this easy for them to find. Several common gamepads are already known by BYOND.

There is also the `GamepadRaw` macro, which is similar to `Any` in some ways and will avoid doing any processing (e.g. checking for dead zones on the analog sticks) so you can handle all input yourself. `GamepadRaw` does not rely on BYOND's controller configuration, so it will not, for instance, know that button 0 should be `GamepadFace1`. See below for more information on how to use this macro.

You can add macros (not local player-defined ones) for any of the mouse input commands, thereby bypassing the normal mouse verbs. This can be helpful for designing custom setups where you don't want to have to parse the normal parameter string that provides most of the info, and instead want to provide data directly to the verb. You will want `set instant=1` on any such verb.

Mouse macro commands use the `[[...]]` syntax to embed values, just like <a href="#/{skin}/commands/embed">embedded wingets</a>. These are the values you can include in a mouse macro:

An example mouse macro command might look like this:

And the verb to go with it looks like this:


```dm

client
    // "in src" is the same as "in usr.client" here
    verb/my_mousedown_verb(object as anything in src, button as text, params as text)

```


In the example, the `src` value is a reference such as you would get with the <a href="#/proc/ref">`ref()` proc</a>. It can be used as a verb argument directly and won't be enclosed by quotes by default. The `button` value is a string and the default formatting will put quotes around it. The `keys` and `drag` values were given the `as params` format specifier so they would behave as part of a <a href="#/proc/list2params">parameter list</a>.

In drag/drop actions, you can precede any value with `src` or `over` if there may be different information for the dragged object and the mouseover object/location. This also applies to things like `keys`, which by default will be the currently held keys but you can use `src.keys` to refer to the values from when the drag began.

This is a list of all keys and gamepad events that can be used in macros.

<sup>*</sup> If no gamepad mappings are included in a game's interface, the default mappings are used instead, which will map the Dpad buttons to the arrow keys. This will cause the Any macro to register both a gamepad directional button and the mapped key on the same press. If you plan on using macros to capture gamepad input, you may wish instead to map any one of the directional buttons to "None", which will override the default gamepad mappings completely.

<sup>†</sup> All of the gamepad macros defined above apply to the first gamepad. BYOND can now support up to four gamepads, and you can replace Gamepad in the names above with Gamepad2, Gamepad3, or Gamepad4 to access them. Each gamepad also has its own raw macro (i.e., Gamepad2Raw).

<sup>‡</sup> If you use a Dpad macro like GamepadDir as a `map-to` target, you don't have to specify gamepad 2-4 in map-to; the mapping will automatically know that when Gamepad2LeftAnalog is mapped to GamepadDir, it means Gamepad2Dir.

Controls can be interacted with via <a class="code" href="#/proc/winset">winset()</a> and <a class="code" href="#/proc/winset">winget()</a> to change or read various parameters.

Parameters come in a few different formats:

The list of <a href="#/{skin}/control">all controls</a> which shows which parameters are universal, and each individual control type lists additional parameters that apply to that type specifically.

Note: In any parameter's "Applies to" section, "all" refers to positionable controls only, not Macro or Menu controls. Macro and Menu will be listed separately if supported.

Default alignment of text/image, both horizontal and vertical.

A BYOND direction flag like `WEST` may be assigned to this parameter, or 0 for center alignment.

Info control: Allow HTML tags to be used in <a class="code" href="#/proc/stat">stat()</a> info. The same limitations apply as to the <a href="#/{skin}/control/grid">Grid control</a>.

Label control: Currently, the label control will not actually use the HTML; it will simply strip it out. Full support may appear in a later version.

Opacity of the window, from 0 (invisible) to 255 (opaque).

Anchors the control within the window or pane. If the anchor is not `none`, it is expressed as pecentages of the container's width and height. For example, an anchor of 100,100 means that the X and Y position are tied to the lower right of the container, and 50,0 is tied to the top center.

Setting only `anchor1` will control the position of the control but won't affect its size.

Setting `anchor2` as well will allow you to stretch the control as the container's size changes. You can think of this `anchor1` controlling the top left corner, and `anchor2` the bottom right corner.

The angle of the bar control's arc when its <a class="code" href="#/{skin}/param/dir">dir</a> is `clockwise` or `counterclockwise`. Angles are measured clockwise from due north, so 0 is north, 90 is east, and so on. `angle1` is the beginning of the arc, and `angle2` is the end.


> [!WARNING]
> 
> > [!NOTE]
> > This parameter only existed to inject compatibility scripts into very old versions of the embedded browser. It is no longer used.

The control's background color. The exact way this applies depends on the control.

The color of the bar or slider.

Border type around the control or window. May not work the same in all controls.

Changes the type of button.

If true, this menu item is toggled like a checkbox or radio button when clicked.

Allow the window to be closed, and also shows a system menu for the window.

Allow the window to be minimized.

Allow the window to be resized or maximized.

If `is-fullscreen` is true, `can-resize` is ignored, so this value represents the state of the window when `is-fullscreen` is turned off again.

Allow this pane to retain its horizontal and/or vertical size and show scrollbars if necessary, instead of shrinking to fit the container.

<a href="#/{skin}/commands">Command</a> executed when this control is activated.

For the Input control, whatever the user types in follows this command. If your command starts with an exclamation point `!`, everything after the `!` is shown as a default prompt that may be cleared by the user.

The span of the current grid cell; it can be merged with cells to the right and down. If `is-list` is true, this setting is ignored. This setting is only available at runtime.

The number of columns and rows in the grid. Using -1 for either columns or rows will leave that value unchanged.

If <a class="code" href="#/{skin}/param/is-list">is-list</a> is true, this value can be set to a single number.

The active cell. Any output sent to the grid, that is not sent to a specific cell, will go into this cell.

If <a class="code" href="#/{skin}/param/is-list">is-list</a> is true, this value can be set to a single number.

The name of the <a href="#/{skin}/control/main">pane</a> in the active/default tab. If set to a pane that is not currently in this tab control, the pane by that name will be added as another tab.

The direction/orientation of the bar. As the <a class="code" href="#/{skin}/param/value">value</a> increases the bar will move further in this direction.

Shorthand values like `cw` and `ccw` can be used, or also numerical BYOND directions.

Read-only and unlisted parameter that returns the DPI scaling factor. A value of 1 indicates 100%. This is currently system-wide for the whole application and won't vary by window, but is implemented for windows in case future scaling changes allow them to differ.

This is also a special global parameter. Calling <a class="code" href="#/proc/winget">winget()</a> with no `id` and `dpi` as the parameter will return the system DPI scaling.

Note: The DPI scale is currently set at the time Dream Seeker starts, and does not change after that.

True if dragged objects may be dropped here. Default is true for Map, Info, and Grid controls, false for others. When in use, this will be the value of the `over_control` argument in <a class="code" href="#/client/proc/MouseDrop">MouseDrop()</a> if you drop an atom here.

Grids can also add `drag-cell` and `drop-cell` to mouse proc parameters. The mouse procs' `src_location` and `over_location` arguments are in the form `"[column],[row]"` (or `"[item"]` if <a class="code" href="#/{skin}/param/is-list">is-list</a> is true) when dragging to/from a grid cell.

In Info controls, `src_location` and `over_location` in mouse procs will be the name of the statpanel tab.

Allows images to be pulled from the Web when using the `&lt;img&gt;` tag; otherwise only locally stored images can be shown.

Set to a positive number to make the window flash that many times, -1 to flash forever, and 0 to stop flashing.

This parameter is true if this control currently has focus.

This is also a special read-only global parameter. Calling <a class="code" href="#/proc/winget">winget()</a> with no `id` and `focus` as the parameter will return the <a class="code" href="#/{skin}/param/id">id</a> of the currently focused control, if any.

Leave blank to use the default font. This can be used for CSS-style fallback fonts, e.g. "Arial,Helvetica".

You can include fonts in your resource file, making them available to the client, like so:


```dm

var/list/extra_resources = list(\
    'myfont.ttf',
    'myfont_bold.ttf')

```


Point size of the font, or leave at 0 for the default size.

The <a href="#/{skin}/control/output">Output control</a> behaves differently for legacy reasons, unless <a href="#/{skin}/param/legacy-size">legacy-size</a> is false.

Sets the font style. Any combination of the above values may be used, or none of them. Multiple values may be separated by spaces or commas.

Used for "radio" buttons and menu items, where only one of them in the same group may be checked at a time. This value is a text string, or may be left empty.

Buttons in different windows/panes, or menu items in another menu/submenu, are always treated as a different group.

True if this info control contains the statpanels created via <a class="code" href="#/proc/stat">stat()</a> and <a class="code" href="#/proc/statpanel">statpanel()</a>.

Only one info control can have statpanels.

True if this info control contains the verbs used in the game.

Currently only one info control can have verbs.

The color used to highlight moused-over statpanel items or verbs. In grids, this color is used when hovering over objects or links.

Custom icon used for the window. If no icon is specified, the Dream Seeker icon is used by windows by default.

If this control is a pane, its icon will appear on the tab if the pane is inside a tab control. Lack of an icon will mean no icon appears in the tab.

Note: The Windows `.ico` format is not used. Only image formats BYOND can already use are supported.

Size, in pixels, of icons on the map. A size of 0 stretches to fit available space.


> [!WARNING]
> 
> > [!NOTE]
> > This parameter has been deprecated. Use <a class="code" href="#/{skin}/param/zoom">zoom</a> instead.

The name of this control. Read-only.

If this is a <a href="#/{skin}/control/main">Main control</a>, the name should always be unique. For others, it is usually still a good idea to use a unique name, but they can be referenced by *window*.*id* at runtime.

You can use a colon in front of the <a class="code" href="#/{skin}/param/type">type</a> to refer to the default control of a certain type, if one exists, e.g. `:map` is the default map.

A background image to show in this control.

In the Output control this image is always tiled.

Note: Icons displayed in the output control will not show the background image underneath their transparent parts, but will instead show the background color.

For Label and Main, use <a class="code" href="#/{skin}/param/image-mode">image-mode</a> to control how the image is displayed.

Determines how the background image is displayed.

Moves the menu item to the *N*th position among its siblings. 0 or less is no change. Write-only.

Read-only.

Reads the position of the mouse cursor relative to the upper left corner of this control, not including the control's borders.

`mouse-pos` is an alias for `inner-mouse-pos`.

This parameter is "unlisted" and must be explicitly queried. It won't appear when sending `*` as the parameter in <a class="code" href="#/proc/winget">winget()</a>.

Read-only.

Reads the position where the window's interior contents begin (i.e., not counting titlebar, statusbar, borders, etc.), relative to its `outer-pos`.

Read-only.

If the control is a window, this refers to its current interior size: i.e., not counting titlebar, statusbar, borders, etc. If it's maximized, this will be the true size of the window interior, as opposed to `size` which is the interior size once this window is no longer maximized.

If this control is a pane and <a class="code" href="#/{skin}/param/can-scroll">can-scroll</a> is true, this is the size of the display area not including the scrollbars.

True if the button or menu item is checked. Menu items can set this even if <a class="code" href="#/{skin}/param/can-check">can-check</a> is false.

Specifies that this is a default control. This should be true for your main window, and for your primary map, info, output, input, and browser controls.

The default control of a given type can be referenced in <a class="code" href="#/proc/winset">winset()</a> and other skin-related procs by the name `":*type*"`, e.g. `":map"`.

Changing this value at runtime should be avoided, especially for windows. Results may be unpredictable.

Disables the control, menu item, or macro.

Gives this button a flat appearance instead of pseudo-3D highlights.

True if the window should be in fullscreen mode. This suppresses `can-resize`, `titlebar`, `is-maximized`, and `is-minimized`. They will continue to return the values that would apply if fullscreen mode were turned off.

True if the grid is used for a flexible list of items; the number of columns and rows may change to fit them.

True if the window is maximized.

If `is-fullscreen` is true, this value represents the state of the window when `is-fullscreen` is turned off again.

True if the window is minimized.

If `is-fullscreen` is true, this value represents the state of the window when `is-fullscreen` is turned off again.

True if this is a pane that will be used in other container controls, instead of an independent window. Read-only.

Hide text with asterisks. Copy to clipboard is not available in this mode, but the <a class="code" href="#/{skin}/param/text">text</a> parameter can still read the control's contents.


> [!CAUTION]
> Note: For obvious reasons, you should never use the same password in a game that you would use anywhere else.

Make this an adjustable slider capable of being changed by the user, instead of a progress bar.

Make this control transparent.

Transparency support is extremely limited. Only some controls can actually use it, and only when on top of certain other controls.

Bars and labels handle transparency reasonably well, when not on top of other controls (or only on top of other conrols of these types).

The splitter between the two panes in this control is vertical.

True if this control can be seen. The main window should usually be made visible.

If stretching a background image, preserve its aspect ratio.

The <a class="code" href="#/{skin}/param/id">id</a> of the left/top pane in this control. The parameter names `left` and `top` can be used interchangeably.

When true, font sizes are scaled slightly larger for readability, which is legacy (and default) BYOND behavior. Set to false for exact font sizing.

If map auto-scales its icons (<a class="code" href="#/{skin}/param/zoom">zoom</a> is 0), make sure the entire map fits, and fill excess space with the background color.

If `letterbox` is not enabled, auto-zoom will fill all available space, and any excess will be cut off.

The color of grid lines.

The color used for links. In some controls <a href="#/{skin}/param/visited-color">visited links</a> may have a different color.

Allows one pane to "lock" the splitter so if this Child control is resized, the splitter will stay put on that side.

The <a class="code" href="#/{skin}/param/id">id</a> of the macro set this window will use, if any, when it's active.

The <a href="#/{skin}/macros">macro name</a> (e.g., "SOUTH") of a key combo, Dpad, mouse button, etc. that this macro maps to.

Maximum number of lines before the control drops old text to make room for more. 0 is no limit.

An overflow of 5% is allowed, to reduce flicker.

The <a class="code" href="#/{skin}/param/id">id</a> of the menu this window will use, if any, when it's active.

Input control: Create a multi-line input control. Read-only for this control.

Info and Tab controls: Show tabs in multiple rows if there are too many to fit in a single row.

Macro control: The key/gamepad combination such as `R+REP`, `CTRL+Northwest`, `GamepadLeft`.

Menu control: This is the menu item label. A tab character can be used between the name and a keyboard shortcut, like "Help\tF1". (Keyboard shortcuts must be implemented as macros in order to work. This is just a label.) A blank name shows just a separator.

True if this input control is for typing only; hitting Enter will not run a command.

<a href="#/{skin}/commands">Command</a> executed when the control loses focus.

<a href="#/{skin}/commands">Command</a> executed when the window is closed.

<a href="#/{skin}/commands">Command</a> executed when the <a class="code" href="#/{skin}/param/value">value</a> of the bar/slider is changed. If you drag the slider around, the command will not run until you let go.

If you include `[[*]]` in the command, it will be replaced by the control's new `value`. (See <a href="#/{skin}/commands/embed">embedded winget</a> for more details on the `[[...]]` format.)

<a href="#/{skin}/commands">Command</a> executed when the control gains focus.

<a href="#/{skin}/commands">Command</a>executed when this control is hidden by the game. Must be the default control for the game to show/hide it.

Currently not editable in Dream Maker.

<a href="#/{skin}/commands">Command</a> executed when this control is shown by the game. Must be the default control for the game to show/hide it.

Currently not editable in Dream Maker.

<a href="#/{skin}/commands">Command</a> executed when this control is resized. If you are dragging a window edge or splitter, the command won't run until you finish.

No command will be sent in response to size or splitter changes made by <a class="code" href="#/proc/winset">winset()</a>.

If you include `[[*]]` in the command, it will be replaced by the control's new size. Likewise, `[[width]]` will be replaced with the width and `[[height]]` with the height. (See <a href="#/{skin}/commands/embed">embedded winget</a> for more details on the `[[...]]` format.)

<a href="#/{skin}/commands">Command</a> executed when the text that would go in the statusbar is changed. This applies even if this control is a pane and not a window, or is a window without a statusbar. It applies to all panes and windows that directly or indirectly contain whatever control generated the statusbar text (e.g., a map).

If you include `[[*]]` in the command, it will be replaced by the new text. (See <a href="#/{skin}/commands/embed">embedded winget</a> for more details on the `[[...]]` format.)

`[[from]]` can be used to reference the control (if any) that generated the next text. You can also use expressions like `[[from.type]]`, `[[from.parent.pos.x]]`, etc.

<a href="#/{skin}/commands">Command</a> executed when the current tab is changed.

If you include `[[*]]` in the command, it will be replaced by the new tab's <a class="code" href="#/{skin}/param/id">id</a>. (See <a href="#/{skin}/commands/embed">embedded winget</a> for more details on the `[[...]]` format.)

Read-only.

Reads the position of the mouse cursor relative to the upper left corner of this control, including the control's borders.

This parameter is "unlisted" and must be explicitly queried. It won't appear when sending `*` as the parameter in <a class="code" href="#/proc/winget">winget()</a>.

Read-only.

Reads the control's current exterior position *including* titlebar, statusbar, borders, etc. If the window is not minimized or maximized, this is identical to `pos`.

Read-only.

If the control is a window, this refers to its current exterior size *including* titlebar, statusbar, borders, etc. If the window is maximized, this is the maximized size.

If this control is a pane and <a class="code" href="#/{skin}/param/can-scroll">can-scroll</a> is true, this is the size of the display area including the scrollbars.

The <a class="code" href="#/{skin}/param/id">id</a> of this control's parent. Write-only, used when creating a new control at runtime or deleting a control that was created this way.

Sends default action for this input after the user macro. Currently this applies only to mouse macros.

An example of this is if you want to override MouseDown with new functionality in your own verb, but still handle default mouse processing.

Position of this control's upper left corner, relative to its container. (Not applicable to panes.)

The color used for the prefix/header column of statpanel displays. No color means the default <a class="code" href="#/{skin}/param/text-color">text-color</a> will be used.

In BYOND 3.0, this color was red.

The <a class="code" href="#/{skin}/param/id">id</a> of the right/bottom pane in this control. The parameter names `top` and `bottom` can be used interchangeably.

True if this control should allow right-clicks to behave like any other click instead of opening up popup menus or similar special behavior.

A semicolon-separated list of parameters that get saved with this control. This is often used for things a user might set, like zoom level for a map.

Currently not editable in Dream Maker.

Read-only.

For windows, this is the upper left corner of the nearest monitor's area.

This is also a special read-only global parameter, which returns the position for the main monitor.

Read-only.

For windows, this is the size of the nearest monitor's area (minus taskbar).

This is also a special read-only global parameter, which returns the size (minus taskbar) for the main monitor.

The size of this control.

Setting 0 for width or height uses up any available space right/downward.

If the control is a window, this refers to its *interior size when not maximized or minimized*. That is, it does not count borders, titlebar, menu, or statusbar, and if the window is minimized/maximized, this refers to the window's normal size when it is restored. See the <a class="code" href="#/{skin}/param/inner-size">inner-size</a> and <a class="code" href="#/{skin}/param/outer-size">outer-size</a> params for comparison.

If this control is a pane and <a class="code" href="#/{skin}/param/can-scroll">can-scroll</a> is true, `size` refers to the total scrollable size of the pane, NOT the smaller size displayed. In this case, `outer-size` and `inner-size` refer to the display area with and without scrollbars, respectively.

Show forward/back navigation buttons.

Determines which grid lines to display.

When atoms are output to the grid, show the atom's name next to its icon.

If the atom has no icon and `show-names` is false, the grid cell will be blank.

Show a splitter if both the left and right (or top and bottom) panes are in use. The splitter can be dragged to resize the panes.

Shows an address bar for this browser control.

When output(object,grid) is sent, show smaller icons in this control instead of larger ones.

Position of the splitter when two panes are in use, whether <a class="code" href="#/{skin}/param/show-splitter">show-splitter</a> is true or not. This value is a percentage. Specifically, it is the percentage of the available width/height that is given to the left/top pane.

The color used for the suffix column of statpanel displays. No color means the default <a class="code" href="#/{skin}/param/text-color">text-color</a> will be used.

In BYOND 3.0, this color was blue.

Shows a status bar at the bottom of the window. This will show the name of an atom when you hover over it with the mouse.

Stretch the background image.


> [!WARNING]
> 
> > [!NOTE]
> > Deprecated; use <a class="code" href="#/{skin}/param/image-mode">image-mode</a> instead.

Custom stylesheet used for the control. Changes made at runtime will usually not impact any existing text.

For Map controls, this affects any <a href="#/atom/var/maptext">maptext</a> drawn, and changes to the style should appear on the next refresh.

Affects the background color for tabs. The regular <a class="code" href="#/{skin}/param/background-color">background-color</a> is used for the content area.

Affects the font for tabs. The regular versions of these without the `tab-` prefix are used for the content area.

Affects the text color for tabs. The regular <a class="code" href="#/{skin}/param/text-color">text-color</a> is used for the content area.

A comma-separated list of <a class="code" href="#/{skin}/param/id">id</a> values for the panes included as tabs in this control.

When setting this value, you can put `+` in front of the list to add tabs to the existing control, without affecting current tabs. You can likewise use `-` in front of the list to remove tabs.

Note: When using this with <a class="code" href="#/proc/winset">winset()</a>, remember you will need to escape `+` as `%2B` via <a class="code" href="#/proc/url_encode">url_encode()</a> or <a class="code" href="#/proc/list2params">list2params()</a>.

Text shown in this control. For Input controls this setting is only available at runtime.

The control's foreground text color.

Show text mode even if icons are available. Text mode will be used if no icons are present, regardless of this setting.

Wrap text that is too long for the width of the label.

The title of this window or pane. For a window, the title will appear in the titlebar if present. For a pane, this will be displayed on the tab if this pane is in a <a href="#/{skin}/control/tab">Tab control</a>.

If this is the default window, <a class="code" href="#/world/var/name">world.name</a> takes precedence over the window title.

Show a titlebar for this window. This is also required for the close, minimize, and maximize buttons to appear.

If `is-fullscreen` is true, `titlebar` is ignored, so this value represents the state of the window when `is-fullscreen` is turned off again.

A color that will be turned into transparency wherever it appears in this window. Overall, this method of transparency comes with many limitations, so it is considered deprecated.

The type of this control. Read-only.

Use the browser's document title to override the title of the window or pane it appears in.

The "fullness" of this bar/slider, as a percentage.

The size, in pixels, of the map after `zoom` has been applied.

For instance, if the client view has 10×10 tiles (this includes any extended tiles caused by HUD objects) and `world.icon_size` is 32x32, the map has a native size of 320×320 pixels. If the map has a zoom level of 2, then `view-size` will be 640x640.

With a `zoom` value of 0, which is the default for most projects, the actual zoom level is automatically determined by the size of the map control, the map's native pixel size as explained above, and the value of the <a class="code" href="#/{skin}/param/letterbox">letterbox</a> parameter.

The color used for visited links.

Width, in pixels, of the bar or slider. A value of 0 uses all available width.

Zoom factor for icons on the map. 1 means to show the icons at their original size, 2 is 200%, 0.5 is 50%, and so on. A value of 0 stretches to fit available space.

Controls the way the map is upscaled.

This section contains miscellaneous information that may apply to multiple vars or procs.

Byondapi is a set of exported functions from BYOND's core library that can be used by external libraries that you call via the <a href="#/proc/call_ext">`call_ext()` proc</a>. The purpose is to make interfacing with native code easier, and to allow external access to BYOND's functionality. Before this existed, all external calls had to use text strings to pass data back and forth, which was inefficient for many uses and very limited.

To build your external library with Byondapi, you have to include the `byondapi.h` header file that's included in BYOND's distribution. When compiling in Windows, you'll also need to link with `byondapi.lib`; in Linux, your makefile should link with `byondcore.so` from BYOND's own `bin` directory.

For simplicity, BYOND defines some basic types and macros in `byondapi.h`. The one most relevant to you is `u4c`, which is an unsigned 4-byte integer. There's also `s4c` which is a signed integer, as well as simple 1-byte and 2-byte ints that use `1c` and `2c` (respectively) insteaed of the `4c` suffix.

The main structure used to pass data back and forth is `CByondValue`. This mimics an internal structure in BYOND that holds values of all sorts: numbers, null, references to strings, references to objects and lists, and so on.

The exact functions used for interfacing with this structure are documented in `byondapi.h`.

The main tricky aspect of working with BYOND data is strings. If you need to get the contents of a string, you'll need to allocate memory for the character data and call `Byond_ToString()` to get a copy of the string. For converting character data to an internal string stored in CByondValue, you'll need to call `ByondValue_SetStr()`.

There are many function calls available in Byondapi for interacting with the server. These include the ability to read and write vars, call procs, create lists, read and write from lists, and so on.

Most of these procs return boolean values: true if they succeed, false if not. In the event of a failure, you can call `Byond_LastError()` to get the error message.

In any functions that read data from lists or read string data—including `Byond_LastError()`—you need to allocate the required memory for a copy of the string or list items. These functions take a pointer to the buffer that will be filled, and a `u4c` pointer for the buffer size (in items for lists, in bytes for strings). If the return value is false and the length is set to zero, an error occurred. If the return value is false and the length is non-zero, the new length value is the required length of the array; the memory should be allocated and the function called again.

The C++ wrappers have a better way of calling `Byond_LastError()` and other functions like it, where you don't need to worry about allocations.

Objects in BYOND are reference-counted; when an object's count reaches 0 it gets garbage-collected. In Byondapi you can call `ByondValue_IncRef()` and `ByondValue_DecRef()` to increment or decrement the reference count, respectively.

Byondapi maintains its own internal reference count for any object, so you can't decref past the number of references Byondapi holds.

The results you get from calls to Byondapi functions, such as reading a var or getting a return value from a proc call, have already had their reference count increased. That means when you're done using the value, you need to clean it up with `ByondValue_DecRef()` or else you'll have a memory leak.

The value you return from a function called by `call_ext()` should have a reference.

The C++ wrappers take care of most of the reference counting issues for you (see below).

BYOND servers handle proc execution and the management of data in a single thread. If your library tries to call any BYOND server functions in a different thread of its own, the call will block until the server thread can handle it.

The special function `Byond_ThreadSync()` will run a callback function on the main thread, avoiding the need to keep syncing over multiple Byondapi calls.

If you want to use the handy C++ wrappers and classes, you can include `byondapi_cpp_wrappers.cpp` and `byondapi_cpp_wrappers.h` in your library.

The `ByondValue` class is a wrapper around `CByondValue` that handles a number of operations for you. You can redefine the `argv` argument of any `call_ext()` functions as an array of `ByondValue` instead of `CByondValue`, but the return value should stay a `CByondValue`.

The external function calls like `ByondValue_CallProc()` have C++ wrappers that use the C calls internally, but if an error happens they'll call an error handler. The default error handler does nothing, but you can change it to a a different handler that accepts an error string.

If you define a `CatchingByondExceptions` variable inside of a `try` block, it will automatically change the error handler to one that throws a `ByondExtException`. This replaces the more cumbersome approach of checking if the return value is false and then calling `Byond_LastError()`.

DM-CSS is a subset of CSS, and only supports some kinds of selectors and attributes.

The following table lists all supported attributes, and whether they are supported in text output, maptext, and in other controls (labels/etc.) Other controls will often allow only one style for an entire unit of text. A checkbox in "Other" only indicates that *some* support exists in other controls, but it may vary by the type of control.

These pseudo-classes are allowed in some contexts, but they can only change the text color.

Text colors may be specified by name or RGB value. The RGB color format uses hexadecimal numbers, with 2 hex digits each for red, green, and blue. These range from 0 (00 in hex) to 255 (FF in hex). In certain situations BYOND will also honor a fourth pair of digits for alpha.

It is also possible to use 4 bit values by using only one hex digit per color. The full 8 bit color is produced by repeating each digit. For example, <code>#F00</code> (red) is the same as <code>#FF0000</code>.

The named colors supported by BYOND, and their corresponding RGB values, are listed in the following table:

There are different ways of interpreting color besides RGB. Several parts of BYOND are capable of using other color spaces.

The default color space is RGB, where each color is split into red, green, and blue components, as well as an optional alpha. All of these components range from 0 to 255.

The color yellow for instance is `rgb(255,255,0)` which is red and green mixed together at their maximum brightness, but no blue component.

HSV stands for hue, saturation, and value.

All pure hues such as red (hue=0) have a saturation of 100 and a value of 100. As saturation decreases, the colors turns whiter. Lower values mean darker colors and darker shades of gray.

In HSV, saturation is less meaningful as value gets closer to 0. Black of course always has a value of 0. With 10 as the value, saturation=100 gives you a very dark color whereas saturation=0 is a 10% shade of gray.

HSL is a little more intuitive than HSV. Here, value is replaced by luminance, which again ranges from 0 to 100. Luminance is the average of the minimum and maximum values of the red, green, and blue components.

Black has a luminance of 0; white has a luminance of 100. Pure hues all have a saturation of 100 and luminance of 50. As saturation decreases, the color will approach a grayscale shade of L%.

Saturation is less meaningful the closer luminance is to 0 or 100. At a luminance of 100, the saturation is totally irrelevant. At 90, high saturation will get you a very light shade of the hue but that isn't very far off from a 90% shade of gray.

HCY stands for **hue**, **chroma**, and the Y is for grayscale luminance. (Again chroma and Y range from 0 to 100.) This color space is based around the apparent brightness of each color according to a rough approximation of human vision.

Chroma is similar to saturation in that it determines how far from grayscale the color is. As chroma decreases toward 0, the color approaches a grayscale shade of Y%. What's different about HCY color from HSV or HSL is that at chroma=0 and chroma=100 the colors should appear equally bright. Pure red, therefore, has a hue of 0, a chroma of 100, and a Y luminance of only 29.9—roughly what red would look like in black &amp; white with all of the color leached out.

This is a special file that's included in all projects when you compile. It contains various constants, definitions of some built-in datums, and so on.

You can see the contents of this file by creating a new file in Dream Maker called `stddef.dm`. It will automatically be filled with the standard definitions.

The contents of `stddef.dm` may change with new BYOND versions. However an eye is always kept on backwards-compatibility.
***
**Related Pages:**
+    [rgb proc](/ref/proc/rgb)
+    [rgb2num proc](/ref/proc/rgb2num)
+    [gradient proc](/ref/proc/gradient)
+    [animate proc](/ref/proc/animate)
+    [Color gradient](/ref/{notes}/color-gradient)
+    [Color matrix filter](/ref/{notes}/filters/color)
