## macros (text)    
**See also:**    
:   [icon text macro](/macros (text).md/icon)    
:   [text](/DM/text)    
:   [text proc](/proc/text)    
Text macros start with \'\\\' (a backslash) and end with a space or    
other punctuation. \\the, \\The // insert \'the\' (if needed) \\a, \\an,    
// insert \'a(n)\' or \'some\' (if needed) \\A, \\An \\he, \\He //    
insert \'he/she/they/it\' \\she, \\She // same \\his, \\His // insert    
\'his/her/their/its\' \\him // insert \'him/her/them/it\' \\himself //    
insert \'himself/herself/themself/itself\' \\herself // same \\hers //    
insert \'his/hers/theirs/its\' \\proper // used in an object name to    
force proper-noun behavior \\improper // used in an object name to force    
improper-noun behavior \\th // insert 1st, 2nd, 5th etc. \\s // insert    
\'s\' if \[\] was plural \\icon // insert icon of following \[\] \\ref    
// insert a unique id for following \[\] \\roman // insert following    
\[\] as a lower-case roman numeral \\Roman // insert following \[\] as    
an upper-case roman numeral \\\... // suppress final new line \\t //    
insert tab \\n // insert new line \\\" // insert double quote \\\\ //    
insert backslash \\\< // insert &lt; (less than) \\\> // insert &gt;    
(greater than) \\(space) // skip a space \\(newline) // skip a newline    
(and following space) \\xNN // insert a character by its ASCII/Unicode    
value \\uNNNN // \" \\UNNNNNN // \"    
### Example:    
mob/verb/steal(M as mob,obj/O as obj in M) O.loc = usr view() \<\<    
\"\[usr\] finds \\himself \\an \[O\].\"    
### Example:    
var/DayCount proc/NewDay() DayCount++ world \<\< \"The \[DayCount\]\\th    
day dawns.\"    
### Example:    
obj/CPU name = \"\\improper CPU\" //prevent capitalization from causing    
proper-noun behavior  