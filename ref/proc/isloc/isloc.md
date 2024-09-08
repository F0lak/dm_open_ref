[]{#/proc/isloc}
## isloc proc
**Format:**
:   isloc(Loc1, Loc2 \...)
<!-- -->
**Args:**
:   Any number of locations to test.
<!-- -->
**Returns:**
:   1 if all args are valid locs; 0 otherwise.
Tests validity of a location. If all arguments are mobs, objs, turfs, or
areas, this returns 1.
For a single argument this is equivalent to:
`(ismob(Loc) || isobj(Loc) || isturf(Loc) || isarea(Loc))`.