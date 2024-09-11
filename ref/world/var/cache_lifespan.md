## cache_lifespan var (world)
**See also:**
*   [cache](/DM/cache)
<!-- -->
**Default value:**
*   30 (days)


Number of days items that are not in use will be saved in the
resource cache (.rsc file). Files uploaded by players are stored in the
world\'s .rsc file for future use. If the file is not used for the
specified amount of time, it will be removed to save space.


Setting this value to 0 causes items to be saved for the
current session only. This is used by the CGI library, because web
browsers cannot make use of server-side caches when uploading files
anyway. 

This value must be a whole number.