## byondStorage (browser control)
**See also:**
+   [browser control (skin)](/ref/%7Bskin%7D/control/browser.md) 
+   [winset proc](/ref/proc/winset.md) 


A replacement for `localStorage` that can be used to hold
information that can be used in later sessions of the same game. (This
must be enabled via `browser-options` with the [`winset()`
proc](/ref/proc/winset.md) .) 

There are three actual storage objects
you can use:
  --------------- ----------------------------------------------------------------------------------------------------
  hubStorage      Stores info that can be shared for all games falling under this same [hub entry](/ref/world/var/hub.md) 
  serverStorage   Stores info that can be shared for all games using this same server address.
  domainStorage   Same as serverStorage, but ignores the connection port.
  --------------- ----------------------------------------------------------------------------------------------------


Interacting with these storage objects is done in JavaScript,
the same way you would use `localStorage` or `sessionStorage`.


Note+ Technically `localStorage` does work, but because of the
way BYOND handles browser controls it acts more like `sessionStorage` in
practice.