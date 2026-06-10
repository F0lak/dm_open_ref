
## grid (info)
***
A grid that contains multiple cells that can show various kinds of output data.

Sending output to a grid looks like this:


```dm

// output to column 3, row 2
winset(usr, "thegrid", "current-cell=3,2")
usr << output("Text", "thegrid")

// or even easier:
usr << output("Text", "thegrid:3,2")

// when is-list is true:
usr << output("5th item", "thegrid:5")

```


You can output an atom to the grid, which can be clicked, dragged, etc. However, you should make sure that atom is *not* temporary and will persist until you no longer need it, or else the server may recycle it and the object in the cell will either disappear or be impossible to interact with anymore.

There are some limitations to output in grid controls:
***