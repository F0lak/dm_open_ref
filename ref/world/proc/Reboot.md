## Reboot proc (world)    
**Format:**    
:   Reboot(reason)    
<!-- -->    
**Args:**    
:   reason: the reason `Reboot()` was called:    
    -   0 or null: Called by game code    
    -   1: By host (Ctrl+R in Dream Seeker)    
    -   2: By [world.Topic()](/world/proc/Topic)    
    -   3: By SIGUSR1 in UNIX    
<!-- -->    
**Default action:**    
:       
Reload the world from scratch. Any connected players will automatically    
relogin. This would be useful if you needed to recompile the world after    
changing some code.    
In a UNIX environment, you can cause a running server to reboot by    
sending it the signal SIGUSR1.    
If you override this proc, you must call ..() if you want the reboot to    
complete normally.    
For reboots initiated by Dream Seeker, usr will be the mob belonging to    
the player who sent the command.  