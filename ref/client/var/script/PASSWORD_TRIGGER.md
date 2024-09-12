# PASSWORD_TRIGGER (client script)
**Format:**
+   #define PASSWORD_TRIGGER \"assword:\"


This defines a special text *trigger* used to detect when the
user is being prompted for a password in telnet mode. Most MUDs
automatically suppress password echo, but if they do not, it is
necessary to use this setting to hide it. Multiple triggers may be
defined as necessary. 

The example above is more robust than the
more polite version because it works whether they capitalize the \'P\'
or not\...