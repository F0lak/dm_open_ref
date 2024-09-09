[]{#/verb/arguments}    
## arguments (verb)    
**See also:**    
:   [argument expanding](/ref/verb/arguments/expanding.md)    
:   [command_text (client)](/ref/client/var/command_text.md)    
:   [arglist proc](/ref/proc/arglist.md)    
:   [args var (verb)](/ref/verb/var/args.md)    
The parameters to a verb are referred to as arguments. For verbs, the    
input type and possible value list may also be specified.    
The possible input types are:    
    text          // a quoted text string    
    password      // un-echoed text (for use with input() only)    
    message       // multi-line text    
    command_text  // raw command text from the rest of the input line    
    num           // a number    
    icon          // an icon file from the user's computer    
    sound         // a sound file from the user's computer    
    file          // any type of file from the user's computer    
    key           // a key from the user's BYOND key file    
    color         // a color (see rgb proc)    
    null          // indicates that the argument is optional    
    mob    
    obj    
    turf    
    area    
    anything    
These can be combined with the \'\|\' operator. The first group are    
called *constant* input types because they turn on various types of    
literal values that the user can type in (like a number or a text    
string). The second group work in conjunction with a list of objects or    
values. They are called input type *filters* because they may be used to    
filter out certain types of values from the list. For example a mob or    
an obj within sight would be specified as follows: myverb(M as mob\|obj    
in view()) {\...}    
A default value may be specified which takes effect in the case of null    
arguments. For example: myverb(M=usr as null\|mob\|obj in view()) {\...}    
In this example, the input type `null` did not have to be used    
explicitly, because assigning a default value (in this case `usr`) turns    
it on by default.    
The `anything` input type can be used to combine values in a list with    
other constant input types. Here, this is done with the `null` input    
type: set_aggression(a=\"on\" as null\|anything in list(\"on\",\"off\"))    
For input types containing mob, obj, turf, or area, the possible value    
list defaults to view().    
If no input type is specified, the variable type will be used to    
determine whether it is a mob, obj, turf, or area.    
### Example:    
mob/verb/tell(mob/M,msg as text) M \<\< \"\[usr\] tells you,    
/\"\[msg\]/\"\"    
This example defines a verb with two arguments: a target mob, and some    
text.  