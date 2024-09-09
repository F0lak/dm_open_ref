[]{#/proc/block}    
## block proc    
**See also:**    
:   [list](ref/list)    
<!-- -->    
**Format:**    
:   block(Start,End)    
:   block(StartX,StartY,StartZ, EndX=StartX,EndY=StartY,EndZ=StartZ)    
<!-- -->    
**Returns:**    
:   The list of turfs in the 3D block defined by Start and End    
    (inclusive).    
<!-- -->    
**Args:**    
:   Start: A turf to be the lower-left corner of the block.    
:   End: A turf to be the upper-right corner of the block.    
:   StartX, StartY, StartZ: XYZ coordinates of the lower-left corner of    
    the block.    
:   EndX, EndY, EndZ: XYZ coordinates of the upper-right corner of the    
    block.    
The following example shows how to loop over a block of turfs.    
### Example:    
world maxx = 20 maxy = 20 mob/verb/block_test() var/turf/T for(T in    
block(locate(1,1,1), locate(10,10,1))) T.text = \" \"    
In the version that uses coordinates directly instead of two turfs, you    
can leave any of the EndX, EndY, or EndZ values as null, and omit the    
last arguments entirely; they will default to using the corresponding    
StartX, StartY, or StartZ. Therefore this example is equivalent to the    
one above:    
### Example:    
world maxx = 20 maxy = 20 mob/verb/block_test() var/turf/T for(T in    
block(1,1,1, 10,10)) T.text = \" \"  