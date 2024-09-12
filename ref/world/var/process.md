## process var (world)
**See also:**
+   [byond_version var (world)](/ref/world/var/byond_version.md) 
+   [system_type var (world)](/ref/world/var/system_type.md) 
+   [shell proc](/ref/proc/shell.md) 

This read-only variable indicates the ID of the server\'s
process on the system running it. The result is a number, unless for
some unexpected reason the number won\'t fit in a `num` type, in which
case it will be text. (In practice it should always be a number.)