[]{#/__MAIN__ macro.md}    
## \_\_MAIN\_\_ macro    
**See also:**    
:   [preprocessor](/DM/preprocessor)    
The \_\_MAIN\_\_ macro is defined in the main `.dme` file being    
compiled. In all other files included by this file, \_\_MAIN\_\_ is not    
defined.    
The purpose of this is for library writers to package a small demo of    
their library directly in the library source code. When users compile    
the library directly, the library\'s own `.dme` is the main file and can    
include extra files that are not normally part of the library.    
### Example:    
#ifdef \_\_MAIN\_\_ #include \"demo.dm\" #include \"demo.dmm\" #endif    
If the demo requires a lot of extra resources, it is probably better to    
package the demo as a separate project. Small demos, however, are nice    
and convenient using this \"auto-demo\" technique---especially since    
Dream Seeker automatically launches Dream Maker after installing a    
library containing a `.dme` file.  