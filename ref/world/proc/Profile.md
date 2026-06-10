
## Profile (proc)
***
Interacts with the built-in server profiler without requiring the host to do so via Dream Daemon, or an authorized player via Dream Seeker.

The `command` value is built from bitflags, so it can combine any of these three values via the `|` operator:

These additional values are also defined for convenience:

By default, data will be returned as a list. The first six values are the column names: `"name"`, `"self"`, `"total"`, `"real"`, `"over"`, and `"calls"`, corresponding to the columns in the profiler. These are followed by the profile data for each proc, with the data being in the same column order. E.g. the next six items represent the first proc in the profile.

The optional `format` argument however can be used to return the data in other formats. Currently the only accepted value is `"json"`, which will output the same data in JSON format.

Using `"sendmaps"` in the `type` argument will profile the routines used to send map informaiton to players. Unlike the proc profiling this only has three data columns: `"name"`, `"value"`, and `"calls"`. The value column might be a time or number value, depending on what's being measured.

The JSON format will include a `unit` property data that is not a raw number, such as a time value.
***