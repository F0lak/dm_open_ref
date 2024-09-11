# Profile proc (world) 
###### BYOND Version 513
**Format:**
*   Profile(command, format)
*   Profile(command, type, format)
<!-- -->
**Returns:**
*   Profilng data or null
<!-- -->
**Args:**
*   command* A numerical value that says whether to start, stop,
    refresh, etc.
*   type* A type of profile to use, other than proc profiling.
*   format* Optional format for output data


Interacts with the built-in server profiler without requiring
the host to do so via Dream Daemon, or an authorized player via Dream
Seeker. 

The `command` value is built from bitflags, so it can
combine any of these three values via the `|` operator:
PROFILE_STOP
*   Stop profiling. Not using this flag will start/continue profiling.
PROFILE_CLEAR
*   Clear all profile data. This will also cause the proc to return
    null.
PROFILE_AVERAGE
*   Any output data should use average times instead of total times.


These additional values are also defined for convenience:
PROFILE_START
*   Start/continue profiling but don\'t clear any existing data.
PROFILE_REFRESH
*   Currently this is the same as `PROFILE_START`.
PROFILE_RESTART
*   Start profiling and clear existing data.
### Profiling procs


By default, data will be returned as a list. The first six
values are the column names* `"name"`, `"self"`, `"total"`, `"real"`,
`"over"`, and `"calls"`, corresponding to the columns in the profiler.
These are followed by the profile data for each proc, with the data
being in the same column order. E.g. the next six items represent the
first proc in the profile. 

The optional `format` argument
however can be used to return the data in other formats. Currently the
only accepted value is `"json"`, which will output the same data in JSON
format.
### SendMaps profile


Using `"sendmaps"` in the `type` argument will profile the
routines used to send map informaiton to players. Unlike the proc
profiling this only has three data columns* `"name"`, `"value"`, and
`"calls"`. The value column might be a time or number value, depending
on what\'s being measured. 

The JSON format will include a
`unit` property data that is not a raw number, such as a time value.