## time2text proc

**Format:**
+   time2text(timestamp,format,timezone)
<!-- -->
**Args:**
+   timestamp: a time value as obtained from world.realtime or
    world.timeofday
+   format: a text string describing the output format.
+   timezone: optional offset, in hours, from UTC
<!-- -->
**Returns:**
+   a text string containing the date and time in the specified format.


A time value (UTC) is converted to text representing the time.
The world\'s local time is used, unless you specify a `timezone`
argument which will add an offset to UTC. 

The default format is
"DDD MMM DD hh:mm:ss YYYY", which produces results such as "Wed, May
23 15:41:13 2001". As you can see, the fields in the format text are
replaced by components of the date and time. The following list contains
all of the recognized fields. Anything else in the format string is
inserted directly into the output.
YYYY
+   year (2001, 2002, ...)
YY
+   year (01, 02, ...)
Month
+   January, February, ...
MMM
+   Jan, Feb, ...
MM
+   number of the month (01, 02, ...)
Day
+   Monday, Tuesday, ...
DDD
+   Mon, Tue, ...
DD
+   day of the month
hh
+   hour (00, 01, ... 23)
mm
+   minute
ss
+   second


Because world.timeofday is in a range of 0 to 864000, values in
this range are treated as a time for the current date. This way
time2text() can return accurate results for world.timeofday. Any other
values are interpreted as coming from world.realtime and will have the
right time and date.

> [!TIP] 
> **See also:**
> +   [realtime var (world)](/ref/world/var/realtime.md) 
> +   [timeofday var (world)](/ref/world/var/timeofday.md) 
> +   [timezone var (world)](/ref/world/var/timezone.md) 
> +   [timezone var (client)](/ref/client/var/timezone.md) <!-- -->