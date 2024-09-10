[]{#/GetConfig proc (world).md}    
## GetConfig proc (world)    
**See also:**    
:   [IsBanned proc (world)](/world/proc/IsBanned)    
:   [SetConfig proc (world)](/world/proc/SetConfig)    
<!-- -->    
**Format:**    
:   GetConfig(config_set,param)    
<!-- -->    
**Returns:**    
:   Value of requested parameter.    
<!-- -->    
**Args:**    
:   config_set: name of the configuration set (see below)    
:   param: name of the configuration parameter    
This command is for retrieving configuration information that is shared    
by applications installed on the same system. The configuration data is    
accessed by specifying the configuration \"set\" and the parameter    
within that set. The \"sets\" defined so far are: env system environment    
variables (changes are not persistent) admin list of site administrators    
ban list of banned users or IP addresses keyban list of banned users    
(deprecated) ipban list of banned addresses (deprecated)    
If no parameter is specified, a list of the names of all available    
parameters is returned.    
The format of the configuration data itself is currently being defined.    
It will generally be a sequence of parameters (such as produced by    
list2params()). For example, each ban entry would have the user\'s ckey    
or ckeyEx as the parameter, and might have data such as    
\"reason=jerkish;message=You+jerk!\".    
### Example:    
mob/verb ban(key as text)    
world.SetConfig(\"ban\",ckey(key),\"reason=fiendish;admin=\[ckey\]\")    
lookban(key as null\|text) if(key) usr \<\< \"\[key\]:    
\[world.GetConfig(\"ban\",key)\]\" else var/lst\[\] =    
world.GetConfig(\"ban\") for(key in lst) usr \<\< \"\[key\]:    
\[world.GetConfig(\"ban\",key)\]\"    
Ban files store information on a game-specific basis. You will only be    
able to read and write values that are set for the game you are running    
(defined by the value of world.hub). It is possible for a host to    
specify universal bans as well, but these will not be accessible via    
GetConfig or SetConfig. If you are using \"ban\" as the config_set, IP    
addresses are recognized automatically. (See the ban format info below.)    
It is possible, but rarely useful, to specify a configuration \"space\"    
of SYSTEM, USER, HOME, or APP. Settings made in the SYSTEM space are    
shared by all BYOND software on the computer. The USER space is shared    
by all software owned by the same user. The HOME space is shared by all    
worlds running with the same safe home directory. The APP space is    
shared by all software running from the same filesystem directory. By    
default, the USER space is used, and if that cannot be modified (in safe    
mode), then HOME is used instead. These distinctions are sometimes    
important on a UNIX machine, where there are many BYOND sites belonging    
to different users, but even then, the default behavior is almost always    
what you want.    
The configuration space is specified inside the configuration set    
parameter like this: world.SetConfig(\"APP/keyban\",\...)    
When reading configuration settings, the spaces are always lumped    
together. In cases of settings with the same name but different values,    
APP overrides HOME, which overrides USER, which overrides SYSTEM.    
### Ban Format    
If you want to create or read bans at runtime by using the \"ban\"    
config set, these are the main parameters currently used:    
type    
:   The ban\'s type, if any. It can be \"sticky\", \"session\", or    
    \"time\", or a combination separated by commas. Session bans expire    
    when the current session is over (world.Reboot() does not affect    
    this).    
reason    
:   The reason the ban was implemented; this is for the host\'s or    
    admin\'s purposes only and is not displayed to the user.    
message    
:   A message to display to the user.    
keys    
:   Other keys caught in a sticky ban.    
IP    
:   Other IP addresses caught in a sticky ban.    
computer_id    
:   Other computer_id values caught in a sticky ban.    
time    
:   The number of seconds remaining in the ban. The type parameter must    
    include \"time\" for this to mean anything. If this parameter is not    
    present when a timed ban is read, it means the ban has expired.    
The old \"keyban\" and \"ipban\" config files are now just aliases for    
\"ban\".  