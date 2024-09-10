[]{#/fcopy proc.md}    
## fcopy proc    
**See also:**    
:   [fcopy_rsc proc]/fcopy proc.md_rsc    
:   [shell proc]/proc/shell    
<!-- -->    
**Format:**    
:   fcopy(Src,Dst)    
<!-- -->    
**Args:**    
:   Src: file to copy    
:   Dst: new copy to make    
<!-- -->    
**Returns:**    
:   1 on success; 0 otherwise.    
Src may be either a cache file, a savefile, or the name of an external    
file. Cache files are specified in single quotes and external files are    
in double quotes. If the path to the destination file does not already    
exist, it will be created.    
If the source and target are paths ending in \"/\", the contents of the    
source directory (including sub-directories) will be copied to the    
target path.    
This instruction could be useful when players upload files (like code)    
that you might want to dump to an external file.    
### Example:    
mob/verb/change_world(F as file) fcopy(F,\"world.dm\")    
shell(\"DreamMaker world\") world.Reboot()    
This (somewhat dangerous) example allows players to upload code,    
recompile, and reboot the world. It assumes that DreamMaker is in the    
path where the shell looks for executable files and also that the name    
of the running world is world.dmb.  