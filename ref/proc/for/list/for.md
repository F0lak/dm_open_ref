[]{#/proc/for/list}    
## for list proc    
**See also:**    
:   [for loop proc](/ref/proc/for/loop/loop.md)    
:   [list](/ref/list/list.md)    
:   [list associations](/ref/list/assoc/assoc.md)    
:   [istype](/ref/proc/istype/istype.md)    
<!-- -->    
**Format:**    
:   for (Var \[as Type\] \[in List\]) Statement    
:   for (Var in Start to End \[step Step\]) Statement    
:   for (Key \[as Type\], Value in List) Statement    
<!-- -->    
**Args:**    
:   Var: A variable to sequentially contain each member of the list.    
:   List: The list to loop through. This defaults to the whole world.    
:   Type: One or more of area, turf, mob, or obj, ORed together. If no    
    type is specified, the declared type of Var will be used to skip    
    over inappropriate elements in the list.    
:   Start: A starting numeric value.    
:   End: An ending numeric value (inclusive).    
:   Step: An increment for the numeric value; default is 1.    
:   Key: A variable to sequentially contain each \"key\" in a key,value    
    pair from an [associative list](/list/assoc)    
:   Value: A variable to sequentially contain each associated value in a    
    key,value pair list    
### Example:    
usr \<\< \"Mobs:\" var/mob/M for(M in view()) usr \<\< M.name    
This loops M through the mobs in view(), outputting the name at each    
iteration.    
When you loop through a list, with the exception of looping through    
world, you\'re actually looping through a copy of that list. If the list    
changes, those changes won\'t have any bearing on this loop. If you want    
to be able to handle a list that might change, you\'ll need to use the    
[for loop proc](/ref/proc/for/loop/loop.md) instead.    
You can declare the variable right inside the for statement. Its scope    
is entirely contained within the for statement, so it will not conflict    
with a similar variable declared elsewhere in the same procedure.    
### Example:    
client/verb/who() for(var/client/Player) usr \<\< Player    
If the loop var has a type, a hidden `istype()` call is included in the    
code. Only items of that type, or its descendants, are handled within    
the loop. That means null values and objects of unrelated types will be    
skipped.    
### Numeric loop    
The numeric loop form is a quick internal version of the [for loop    
proc](/ref/proc/for/loop/loop.md). It\'s equivalent to    
`for(Var = Start, Var <= End, Var += Step)` unless Step is negative, in    
which case a \>= comparison is used instead. The main difference is that    
unlike in a for loop proc, the values of Step and End are calculated at    
the beginning and never change after that, so an expression like    
`list.len` that might be subject to change will not be read again---in    
much the same way that looping through a list only loops through a copy    
of that list.    
### Example:    
for(var/count in 1 to 100) src \<\< count    
Note: Although you can use fractional values for `step` in this numeric    
format, there may be accuracy considerations to keep in mind. See    
[Numbers](/ref/%7Bnotes%7D/numbers/numbers.md) for more information.    
### Key,value pair loop {#keyvalue-pair-loop byondver="516"}    
The key,value pair loop is meant for quickly traversing the items in an    
[associative list](/list/assoc), without having to do an additional    
lookup of `List[Key]` in the list. Additionally this also copies the    
associated values when the list is copied, so the loop won\'t react to    
changes in the original list.    
### Example:    
var/alist/prices = alist(/obj/item/weapon/sword = 100,    
/obj/item/armor/helmet = 50) player \<\< \"**Welcome to my shop!**\"    
for(var/item,price in prices) player \<\< \"\[item::name\] -    
\$\[price\]\"    
If the key var has a type, a hidden `istype()` call is included in the    
loop, just like in a regular `for(Var in List)` loop. You can also use    
the `as` clause to specify basic types like `obj`, `num`, `text`, etc.    
If this format is used with non-associative lists, then the associated    
value will always be assigned null.  