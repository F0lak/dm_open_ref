[]{#/world/proc/Export}
## Export proc (world)
**See also:**
:   [Export proc (client)](#/client/proc/Export)
:   [Import proc (world)](#/world/proc/Import)
:   [Topic proc (world)](#/world/proc/Topic)
:   [link proc](#/proc/link)
:   [shutdown proc](#/proc/shutdown)
<!-- -->
**Format:**
:   Export(Addr,File,Persist,Clients)
<!-- -->
**When:**
:   Call this to send a message to another server. The message may be
    composed of an optional topic text string (in the address) and an
    optional file. This will call world.Topic() on the remote server,
    which may in turn call world.Import() to access the file.
<!-- -->
**Args:**
:   Addr: The address of the recipient server. It should be in the form
    byond://server?topic. The topic portion is optional.
:   File: The (optional) file to send. This could be a cache file (in
    single quotes) an external file (in double quotes) or a savefile.
:   Persist: Set to 1 to indicate that the server should keep this
    connection open, to expedite subsequent calls to the same address.
    An open connection can be closed at a later time by passing 0 in the
    Persist field.
:   Clients: An optional client, or list of clients, to tell the
    receiver about.
<!-- -->
**Default action:**
:   Send the topic text string and file to the remote server and return
    the result of calling world.Topic() there. Note that this will cause
    the caller to sleep while waiting for the necessary data to be
    transfered.
### Example:
mob/verb/shout(Msg as text) world \<\< Msg
world.Export(\"\[ShadowWorld\]?shout:\[Msg\]\")
This example defines a verb that will broadcast a message to everyone in
this world as well as sending it in the form of topic text to another
world whose address is stored in the variable ShadowWorld. This address
could be manually set or could be the result of calling startup().
It is also possible to access an HTTP server via world.Export(). Simply
use an http address such as: `http://www.byond.com`. This returns a list
of HTTP header parameters as well as the extra values \"STATUS\" and
\"CONTENT\". The value associated with the \"STATUS\" entry is the HTTP
status code returned by the web server (as text). The value associated
with the \"CONTENT\" entry is the requested resource.
### Example:
mob/verb/test() var/http\[\] = world.Export(\"http://www.byond.com\")
if(!http) usr \<\< \"Failed to connect.\" return usr \<\< \"HTTP
Header:\" for(var/V in http) usr \<\< \"\[V\] = \[http\[V\]\]\" usr \<\<
\"\\n\" var/F = http\[\"CONTENT\"\] if(F) usr \<\<
html_encode(file2text(F))
Note that the HTTP request is submitted using the GET method as opposed
to the POST method. Support for POST may be added in the future.
If the Clients argument is used, it accepts a client that is currently
loggedin, a mob belonging to such a client, or a list of any of these.
The remote server will receive a list of their keys in world.Topic().