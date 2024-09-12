## byond_build var (client) 
###### BYOND Version 512
**See also:**
*   [DM_VERSION macro](/ref/DM/preprocessor/DM_VERSION.md) 
*   [byond_version var (client)](/ref/client/var/byond_version.md) 
*   [byond_version var (world)](/ref/world/var/byond_version.md) 

This is the build number (minor version) of BYOND being run by
this client. Typically this is not useful information, but it can come
in handy when diagnosing issues reported by players using a beta build.


Clients running versions of BYOND prior to 512 (major version)
will not have this information. It is also not guaranteed to exist for
non-Dream Seeker connections. When not available, byond_build is 0.