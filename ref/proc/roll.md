## roll proc

**Format:**
+   roll(ndice=1,sides)
+   roll(dice)
<!-- -->
**Returns:**
+   The sum of the rolled dice.
<!-- -->
**Args:**
+   ndice: number of dice to role.
+   sides: number of sides to the dice.
+   dice: a text string encoding both ndice and sides (see below).


The sides of the dice are numbered 1 through the total number
of sides and each is equally likely. 

An alternate form takes
the dice parameters in a single text value such as "3d4". This may be
useful when you want to store the dice information in a single variable.
You can even specify an offset, such as "3d4+5". That adds 5 to the
sum of 3 dice having 4 sides each.
### Example:

``` dm
 obj/potion/healing var/dice = "3d6" verb/drink() var/h =
roll(dice) if(h>15) usr << "Very refreshing!" else usr << "You
feel better." 
```


> [!TIP] 
> **See also:**
> +   [rand proc](/ref/proc/rand.md) <!-- -->