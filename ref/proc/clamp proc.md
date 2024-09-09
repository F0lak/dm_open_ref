[]{#/proc/clamp}    
## clamp proc {#clamp-proc byondver="513"}    
**See also:**    
:   [min proc](/ref/proc/min.md)    
:   [max proc](/ref/proc/max.md)    
<!-- -->    
**Format:**    
:   clamp(Value, Low, High)    
:   clamp(List, Low, High)    
<!-- -->    
**Args:**    
:   Value: A number, text, pixloc, or vector (or null, treated as 0).    
:   List: A list of values.    
:   Low: The lowest value that can be returned.    
:   High: The highest value that can be returned.    
<!-- -->    
**Returns:**    
:   A copy of the original Value, constrained between Low and High.    
:   The original List, whose contents have all been clamped.    
\"Clamps\" a value, usually a number, to a given allowable range from    
`Low` to `High`. If the value is already in that range, it is unchanged.    
Otherwise, the closer of `Low` or `High` is returned.    
If the `Low` and `High` values are out of order, it doesn\'t matter.    
This is effectively equivalent to    
`min(max(Value, min(Low,High)), max(Low,High))`, but slightly faster.    
### Example:    
usr \<\< clamp(5, 0, 10) // 5; it falls between 0 and 10 usr \<\<    
clamp(-1, 0, 10) // 0; it is less than 0 usr \<\< clamp(20, 0, 10) //    
10; it is more than 10    
If the compared items are objects such as pixlocs or vectors, the result    
of clamping them is a new object, not one of the objects that was    
compared.    
The list format will accept a list in place of a value as the first    
argument, and it behaves as if you looped through the entire list and    
ran `clamp()` on each value. Please note the original list will be    
modified. If you want to leave the original list alone, use the    
[`Copy()` proc](/ref/list/proc/Copy.md) to pass a copy to `clamp()` instead.  