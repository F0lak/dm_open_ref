[]{#/input proc.md}    
## input proc    
**See also:**    
:   [alert proc]/proc/alert    
:   [arguments (verb)]/verb/arguments    
<!-- -->    
**Format:**    
:   input(Recipient=usr,Message,Title,Default) as Type in List    
<!-- -->    
**Returns:**    
:   User\'s response.    
<!-- -->    
**Args:**    
:   Recipient: The user who will see this input prompt.    
:   Message: A message in the prompt, to tell the user what it\'s asking    
    for.    
:   Title: The title of the prompt window.    
:   Default: Default value if the user cancels the input.    
:   Type: A verb input type, such as `text`, `message`, `num`,    
    `anything`. If you omit \"as Type\", the type defaults to `text`.    
:   List: An optional list of items to choose from.    
Creates a prompt dialog that asks the user for a response. The current    
proc sleeps until they respond.    
The only required argument is the message. The type may be any    
combination of input types allowed for verb arguments, which can be    
combined with the `|` operator. The `null` type will allow the user to    
cancel, e.g. `as null | anything in contents`.    
### Example:    
mob/verb/create_character() usr.name = input(\"Choose a name for your    
character.\", \"Your Name\", usr.name) usr.gender = input(\"Select a    
gender for your character.\", \"Your Gender\", usr.gender) in    
list(\"male\",\"female\",\"neuter\")    
If the target of the input prompt is not a player, the result will be    
the default value. If no default value is specified and null is allowed    
by the input type, null will be returned. Otherwise, an error will    
result, crashing the proc that called `input()`.    
A more common use for `input()` is to give a player a list of things to    
choose from. For example, this is a simple shopkeeper NPC, where the    
shopkeeper\'s inventory is its contents.    
### Example:    
mob/shopkeeper/verb/Buy() var/list/options = list() var/obj/item    
for(item in src) // show a pretty list of options with prices included    
options\[\"\[item\]: \$\[item.price\]\"\] = item var/choice =    
input(\"Buy something!\", \"Shop\") as null\|anything in options item =    
options\[choice\] if(!item) return // user canceled if(item.price \>    
usr.gold) usr \<\< \"You can\'t afford that.\" else // give the buyer a    
copy of the item var/t = item.type new t(usr) usr.gold -= item.price usr    
\<\< \"You bought \\a \[item\] for \$\[item.price\].\"    
Using `as num` is another popular input choice, which you might use for    
haggling, deciding how many of an item to pick up or drop, etc.    
This next part is important! Always validate input from a user to make    
sure it\'s correct.    
You should be sure to sanitize any user input to make sure the value is    
valid. For instance, if you have a verb that gives gold to another    
player, you should check that the amount isn\'t negative and doesn\'t    
contain any fractions, and isn\'t more than they have.    
### Example:    
mob/player/verb/Give_Gold() set src in oview(1) var/amount = input(\"How    
much?\", \"Give gold\") as null\|num if(isnull(amount)) return amount =    
floor(amount) // round down to a whole number amount = min(amount,    
usr.gold) // don\'t give more than you have if(amount \<= 0) return //    
ignore negatives and 0 gold += amount usr.gold -= amount usr \<\< \"You    
gave \[src\] \$\[amount\].\" src \<\< \"\[src\] gave you \$\[amount\].\"    
Likewise if you\'re allowing a user to input text, it too should be    
sanitized. If they shouldn\'t enter multi-line text, you should strip    
out `"\n"` characters. If they\'re putting in something like a character    
name, strip out any HTML via `html_encode()`, or you can simply reject    
anything that contains invalid characters and make them do it again.  