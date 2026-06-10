
## Export (proc)

**Format:**
+   Export(Addr,File,Persist,Clients,Method)

**Arguments:**
+   Addr: The address of the recipient server. It should be in the form , unless it's a web request. The topic portion is optional.
+   File: The (optional) file to send.  This could be a cache file (in single quotes) an external file (in double quotes) or a savefile, or an associative list if sending a  web request.
+   Persist: Set to 1 to indicate that the server should keep this connection
open, to expedite subsequent calls to the same address.  An open connection can be closed at a later time by passing 0 in the Persist field.
+   Clients: An optional client, or list of clients, to tell the receiver about.
+   Method: The request method for HTTP requests; defaults to .
about.

**Called When:**
+   Call this to send a message to another server.  The message may be
     composed of an optional topic text string (in the address) and an
     optional file.  This will call world.Topic() on the remote server,
     which may in turn call world.Import() to access the file.

**Default Action:**
+   Send the topic text string and file to the remote server and return the result of calling world.Topic() there. Note that this will cause the caller to sleep while waiting for the necessary data to be transfered.
+   Send a web request via HTTP. This will also cause the caller to sleep while waiting for the request to finish.
***
Sends a request to a remote BYOND server that will be handled by its <a class="code" href="#/world/proc/Topic">world.Topic()</a> proc, or a web request via HTTP.


```dm

mob/verb/shout(Msg as text)
  world << Msg
  world.Export("[ShadowWorld]?shout:[Msg]")

```


This example defines a verb that will broadcast a message to everyone in this world as well as sending it in the form of topic text to another world whose address is stored in the variable ShadowWorld. This address could be manually set or could be the result of calling startup().

If the Clients argument is used, it accepts a client that is currently loggedin, a mob belonging to such a client, or a list of any of these. The remote server will receive a list of their keys in world.Topic().

It is also possible to access an HTTP server via `world.Export()`. Simply use an http address such as: `http://www.byond.com`. This returns a list of HTTP header parameters as well as the extra values `"STATUS"` and `"CONTENT"`. The value associated with the `"STATUS"` entry is the HTTP status code returned by the web server (as text). The value associated with the `"CONTENT"` entry is the requested resource, as a file.


```dm

mob/verb/test()
    var/http[] = world.Export("http://www.byond.com")

    if(!http)
        usr << "Failed to connect."
        return

    usr << "HTTP Header:"
    for(var/V in http)
        usr << "[V] = [http[V]]"
    usr << "\n"

    var/F = http["CONTENT"]
    if(F)
        usr << html_encode(file2text(F))

```


Note that the HTTP request is submitted using the GET method by default.

As of BYOND 516.1664, HTTPS is supported as well, along with other methods such as POST and PUT.

If sending a POST request, the File argument should be an associative list, representing form data.


```dm

mob/verb/SendForm(name as text, favoritecolor as color)
    var/list/formdata = list("name"=name, "color"=favoritecolor)

    var/http[] = world.Export("http://mysite.com/myform", formdata, 0, null, "POST")

    if(!http || findtextEx(http["STATUS"],"200") != 1)
        usr << "Failed to send the form."
        return

```

***
**Related Pages:**
+    [Export proc (client)](/ref/client/proc/Export)
+    [Import proc (world)](/ref/world/proc/Import)
+    [Topic proc (world)](/ref/world/proc/Topic)
+    [link proc](/ref/proc/link)
+    [shutdown proc](/ref/proc/shutdown)
