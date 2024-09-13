## PayCredits proc (world) 
###### BYOND Version 503

**Format:**
+   PayCredits(player, credits, note)
<!-- -->
**Returns:**
+   1 if the credits were spent successfully, 0 or null otherwise.
<!-- -->
**Args:**
+   player: a mob, client, key, or ckey
+   credits: A number of credits to deduct from the player\'s account
+   note: An optional note (for author purposes) for the credit change


Removes credits from a player\'s account, if they have enough.
The proc will return 1 if it is successful, or 0 if the attempt failed
(usually because the player doesn\'t have enough credits). This feature
is intended for games that make use of the credit system, and for
security all such games must use a hub password. 

This proc will
return null if there was no way to reach the hub. Use isnull() to check
for a null value. Contacting the hub may take a few moments, so it is
often a good idea to use spawn() to avoid holding up the rest of the
game.
### Example:

``` dm
 mob/proc/ItemShop() var/items = list(\"Get credits!\",
\"Magic sword\"=10, \"Skeleton key\"=50) var/choices\[0\] var/item,price
for(item in items) price = items\[item\] choices\[\"\[item\]: \[price\]
credit\\s\"\] = item var/credits = world.GetCredits(key)
if(isnull(credits)) src \<\< \"Sorry, the item shop isn\'t available
right now.\" return var/choice = input(src,\\ \"You have \[credits\]
credit\\s. What would you like to purchase?\",\\ \"Item Shop\")\\ as
null\|anything in choices if(!choice) return // cancel if(choice ==
\"Get credits\") src \<\<
link(\"http://www.byond.com/games/Author/MyGame/credits\") return item =
choices\[choice\] price = items\[item\] if(!price) return src \<\<
\"Contacting item shop\...\" var/result = world.PayCredits(name, price,
\"Item shop: \[item\]\") if(isnull(result)) src \<\< \"Sorry, the item
shop isn\'t available right now.\" else if(!result) src \<\< \"You need
\[price-credits\] more credit\\s to buy \[item\].\" else src \<\< \"You
bought \\a \[item\]!\" // Now give the user the item and save their
character // These procs are for you to define src.AddEquipment(item)
src.SaveCharacter() 
```

Note: You can specify a different hub path and hub_password by adding
these as extra arguments, but this is not recommended for security
reasons. If you use this feature, it should only be on games that cannot
be downloaded by the public.

> [!TIP] 
> **See also:**
> +   [AddCredits proc (world)](/ref/world/proc/AddCredits.md) 
> +   [GetCredits proc (world)](/ref/world/proc/GetCredits.md) <!-- -->