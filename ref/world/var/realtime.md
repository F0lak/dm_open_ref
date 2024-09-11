## realtime var (world)
**See also:**
*   [time var (world)](/ref/world/var/time.md) -m
*   [timeofday var (world)](/ref/world/var/timeofday.md) -m
*   [time2text proc](/ref/proc/time2text.md) -m

This is the time (in 1/10 seconds) since 00:00:00 GMT, January
1, 2000 (also known as the BYOND era). 

Because this is a large
number, BYOND\'s number system isn\'t capable of enough precision to
deliver the exact number of 1/10 second ticks. It usually rounds off to
the nearest several seconds. For more accurate readings use
`world.timeofday`.