## GetScores proc (world)

**Formats:**
+   GetScores(key, fields)
+   GetScores(count, field)
+   GetScores(count, skip, field)
<!-- -->
**Returns:**
+   A parameter list of scores for a given entry. Use params2list() to
    interpret the results.
<!-- -->
**Args:**
+   key: the name of the player, character, etc. for which scores have
    been set
+   fields: The data fields to retrieve
+   count: The number of top score records to look at
+   skip: The number of top score records to skip over


Retrieves information about scores that is kept on the BYOND
hub. 

This proc will return null if there was no way to reach
the hub. Use isnull() to check for a null value. Contacting the hub may
take a few moments, so it is a good idea to use spawn() to avoid holding
up the rest of the game.
### GetScores(key, fields)


In this form, you can get information about individual scores.
This is the most common way to use GetScores(). 

The key is an
arbitrary text value. Usually a player\'s key is a good choice, but you
can also use the name of their character, or anything else you like, as
long as it is unique. The key is case-insensitive. 

Scores and
stats use data fields, which might be things like \"Score\", \"Level\",
\"Class\", etc. To retrieve all the fields associated with a key, leave
the fields argument blank. To retrieve only certain fields, you can send
a separated list like \"Score;Level\" which is in the same format
returned by list2params(). 

If you leave the key argument blank,
you will get a complete list of keys that have scores and stats
associated with them.
### Example 1:

```
 mob/var/scores_found mob/var/score = 0 mob/Login() ..()
spawn() var/scores = world.GetScores(key) scores_found = !isnull(scores)
if(scores) var/list/params = params2list(scores) if(params\[\"Score\"\])
score = text2num(params\[\"Score\"\]) src \<\< \"You have \[score\]
point\\s!\" 
```

### GetScores(count, field) *and* GetScores(count, skip, field)


In this form, the proc gets a list of the top scores for a
certain field, and gives you the keys and scores in order. To get the
top 10 players by level, for instance, you would use
GetScores(10,\"level\"). This returns a parameter list with the top keys
and scores, so it might be in a form like
\"Bob=100;Anita=80;David=20;Charlie=5\". 

The count and skip
arguments are always numbers, not text. The count is the number of
scores to retrieve, and skip is the number to skip over to get to them.
So count=10 and skip=0 is the top 10, while count=10 and skip=5 is #6
through #15. If you leave out skip, it\'s a 0. 

The way you set
up your hub entry is how the top scores are determined. If you told the
hub that the \"score\" field is always sorted from highest number to
lowest, then that\'s what you\'ll get. If \"birthplace\" is set up to
use an alphabetical order, that\'s the order that GetScores() will use.
If a field cannot be sorted, this form of GetScores() will return an
empty text string. 

If you don\'t specify a field, your hub
entry may have a default field to use. For instance if your hub page
displays \"Score\", then \"Level\", then the \"Score\" field is the
default.
### Example 2:

```
 mob/var/scores_found mob/Login() ..() spawn() var/top_scores
= world.GetScores(10, \"Booty\") scores_found = !isnull(scores)
if(scores) var/list/params = params2list(scores) src \<\< \"**Top
Buccaneers:**\" for(var/i=1, iNote: You can specify a different hub path
and hub_password by adding these as extra arguments, but this is not
recommended for security reasons. If you use this feature, it should
only be on games that cannot be downloaded by the public.

> [!TIP] 
> **See also:**
> +   [SetScores proc (world)](/ref/world/proc/SetScores.md) 
> +   [GetMedal proc (world)](/ref/world/proc/GetMedal.md) 
> +   [SetMedal proc (world)](/ref/world/proc/SetMedal.md) 
> +   [ClearMedal proc (world)](/ref/world/proc/ClearMedal.md) <!-- -->