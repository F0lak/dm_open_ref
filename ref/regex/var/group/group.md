[]{#/regex/var/group}    
## group var (regex) {#group-var-regex byondver="510"}    
**See also:**    
:   [regex datum](/ref/regex/regex.md)    
:   [Find proc (regex)](/ref/regex/proc/Find/Find.md)    
:   [index var (regex)](/ref/regex/var/index/index.md)    
:   [match var (regex)](/ref/regex/var/match/match.md)    
After a call to Find(), if this regular expression had any parentheses    
groups, whatever text was matched in those groups is stored here in a    
list.    
### Example    
var/regex/R = new(\"B(.)(.)(.)D\") R.Find(\"BYOND\") // find this    
pattern in \"BYOND\" The result of the example is that R.group is    
list(\"Y\",\"O\",\"N\").  