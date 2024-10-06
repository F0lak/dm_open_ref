## byond_build var (savefile) 
###### BYOND Version 515

**Default value:**
+   0


Sometimes when transitioning between BYOND versions you\'ll
want to keep a savefile in a condition where it can be read by older
versions. The `byond_version` var tells it to avoid using newer savefile
features (unless forced to) above a certain build number. (The build
number changes more often than the BYOND version number.) A value of 0
means not to worry about it. 

This can be changed on a
per-savefile basis so that you can use newer features in some files and
avoid changing others. For instance, character saves might want to go on
using older features for a while, but for saving parts of the map you
might prefer to allow newer features to be used. 

The default
savefile compatibility version can be set at compile-time:
### Example:

```dm
 savefile/byond_build = 1600 // do not use savefile
features from BYOND build 1601 onward 
```


> [!TIP] 
> **See also:**
> +   [savefile](/ref/savefile.md) 
> +   [byond_version var (savefile)](/ref/savefile/var/byond_version.md) 
> +   [byond_version var (world)](/ref/world/var/byond_version.md) 
> +   [byond_build var (world)](/ref/world/var/byond_build.md) <!-- -->