## SetConfig proc (world)

<!-- -->
**Format:**
+   SetConfig(config_set,param,value)
<!-- -->
**Args:**
+   config_set: name of the configuration set (see below)
+   param: name of the configuration parameter
+   value: data to store (or null to delete this entry)


This command is for storing configuration information that is
shared by applications installed on the same system. The configuration
data is accessed by specifying the configuration \"set\" and the
parameter within that set. 

For more information, see
[GetConfig](/ref/world/proc/GetConfig.md) 

**See also:**
+   [GetConfig proc (world)](/ref/world/proc/GetConfig.md) 