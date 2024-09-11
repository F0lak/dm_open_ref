## ref text macro 
###### BYOND Version 513
**See also:**
*   [Topic proc (client)](/ref/client/proc/Topic.md) -m
*   [icon text macro](/ref/DM/text/macros/icon.md) -m
*   [locate proc](/ref/proc/locate.md) -m
*   [macros (text)](/ref/DM/text/macros.md) -m
*   [tag var (datum)](/ref/datum/var/tag.md) -m


The `\ref` text macro inserts a unique identification number or
text string for the following embedded object (inside \[\]\'s).


In older versions of BYOND, if an object had a tag, that was
used instead. However this has often proved to be problematic, so
anything compiled from version 512 onward should expect to output a
reference number. If you want to use the tag, which stands a better
chance of still being valid if the object is deleted and recreated (like
in a world reboot), you can output the object\'s tag explicitly.


The primary use for object references embedded in text is in
topic links. This allows you to encode a reference to an object in the
href value of a hyperlink. (Just make sure the object does not get
deleted before the user executes the link. See [garbage
collection](/ref/DM/garbage.md) -m.) 

Topic links that contain a
parameter \"src\" assigned to an object reference are treated somewhat
specially. Unless you override client.Topic() to do otherwise, the
default behavior is to call the referenced object\'s own Topic()
procedure.
### Example:

```
 mob/verb/test() usr \<\< \"Click
[here](?src=\ref%5Bsrc%5D;action=start)!\" mob/Topic(href,href_list\[\])
switch(href_list\[\"action\"\]) if(\"start\") usr \<\< \"Starting the
game\...\" else return ..() 
```
 

The above example uses
an embedded reference to the player\'s own mob to create a link to a
topic handled by that mob\'s Topic() proc. The `href_list` parameter is
simply the result of `params2list(href)`. 

In that example, the
embedded reference was automatically converted back into an object
(dereferenced) for you. If you embed references to additional objects in
the href data, you would have to dereference those yourself using the
locate() instruction.
### Browser images


In output for browser controls, you can use `\ref[object]` as
the src parameter for an \<img\> tag. The object can be an
[appearance](/ref/atom/var/appearance.md) -m, an icon, or an atom or image.


If the ref string is for an icon, you can add an HTML query
string after the icon reference.
### Example:

```
 player \<\< browse({\"
![](\ref%5Bicon%5D?state=hungry&dir=%5BEAST%5D)
\"}) 
```
 

The query string can include any of the
following (separated by & characters):
sheet
*   Display all matching frames as a sprite sheet; otherwise the first
    matching frame is used
state=*ICON_STATE*
*   Use a specific icon state; be sure to
    [url_encode](/ref/proc/url_encode.md) -m.code} it)
moving=*M*
*   Specify whether to choose only moving (M=1) or non-moving (M=0)
    states
dir=*DIR*
*   Choose only frames with a specific direction (this should be a
    number, not text, so for instance `dir=[NORTH]`)
frame=*N*
*   Choose the Nth animation frame in an animated icon