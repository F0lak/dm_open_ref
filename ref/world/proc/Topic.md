
## Topic (proc)
***

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
***