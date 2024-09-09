[]{#/proc/ckey}    
## ckey proc    
**See also:**    
:   [ckeyEx proc](/ref/proc/ckeyEx)    
:   [ckey var (mob)](/ref/mob/var/ckey)    
:   [savefile](/ref/savefile)    
<!-- -->    
**Format:**    
:   ckey(Key)    
<!-- -->    
**Args:**    
:   Key: The player key to convert to canonical form.    
<!-- -->    
**Returns:**    
:   The key in canonical form. To do this, it strips all punctuation and    
    space from the key and converts to lowercase. The result is still    
    unique for each different key.    
The result could be used as a unique directory name in a server-side    
save file. Each player could be stored in a separate directory. By    
converting to canonical form, possible problems resulting from    
punctuation (like the path delimiter \'/\') in the key would be avoided.    
If players are saved in stand-alone files, it could be equally useful    
for generating a unique file name.    
Note that this may be used on any text string. It is not just limited to    
keys.    
### Example:    
var/savefile/SaveFile = new(\"world.sav\") proc/SavePlayer(mob/M)    
var/keydir = ckey(M.key) SaveFile.cd = \"/players\" SaveFile.cd = keydir    
M.Write(SaveFile) proc/LoadPlayer(mob/M) var/keydir = ckey(M.key)    
SaveFile.cd = \"/players\" if(!SaveFile.Find(keydir)) return 0    
SaveFile.cd = keydir M.Read(SaveFile) return 1    
This example defines two procs for saving and loading players to a    
server-side file. These could be called in mob.Login() and mob.Logout().    
Notice that instead of calling SaveFile.Write(M), this example instead    
calls M.Write(SaveFile) directly. The difference is that in this example    
we did not want a new mob to be created when loading the player but    
instead wanted to load information into an existing mob.    
In this example, the ckey() proc was used, but it would be more    
efficient to use mob.ckey, which is the same value precomputed.  