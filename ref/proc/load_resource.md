## load_resource proc
**See also:**
*   [\<\< output operator](/ref/operator/%3c%3c/output.md) -m<!-- -->
**Format:**
*   Player \<\< load_resource(File)
*   Player \<\< load_resource(File, KeepTime)
*   Player \<\< load_resource(File1, File2\..., KeepTime1, File3,
    File4\..., KeepTime2\...)
<!-- -->
**Args:**
*   Player* A mob or client, a list of them, or world
*   File* A resource file (image or sound)
*   KeepTime* Minimum time (in seconds) to keep the file loaded;
    0=default, -1=forever


Tells the player\'s client (or multiple players) to load the
specified resources now, and how long to keep them. If you do not
specify a keep time, 0 is used which will use the default time.


This may be useful for loading sounds into memory before they
play, or to load an icon as soon as possible even if it hasn\'t been
displayed yet. This can avoid delays later on when the resources are
needed. 

Dream Seeker keeps most assets loaded for at least 5
minutes (300 seconds) after their last use. However if you think a more
appropriate time is closer to half an hour, you can set a keep time of
1800 seconds. Or if you want them to stay loaded indefinitely, set a
keep time of -1.
### Example:

```
 mob/Login() ..() // load up these songs now and keep them
loaded indefinitely src \<\< load_resource(\'music1.ogg\',
\'music2.ogg\', \'music3.ogg\', -1) 
```
 

In cases of
extreme memory duress, Dream Seeker\'s garbage collector will get more
aggressive and can still override your choices if need be.