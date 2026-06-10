
## map_cpu (var)
***
This is the percentage of a server tick that the server spends processing information about the map to send to players. A value of 0 would indicate very little cpu usage. A value of 100 would indicate full cpu usage, which means that the server cannot complete all the necessary computations during a tick to finish in time for the next tick. In this case, timed events (such as sleep) may take longer than requested.
***