[]{#/process var (world).md}    
## process var (world)    
**See also:**    
:   [byond_version var (world)]/world/var/byond_version    
:   [system_type var (world)]/world/var/system_type    
:   [shell proc]/proc/shell    
This read-only variable indicates the ID of the server\'s process on the    
system running it. The result is a number, unless for some unexpected    
reason the number won\'t fit in a `num` type, in which case it will be    
text. (In practice it should always be a number.)  