[]{#/group var (regex).md}    
## group var (regex) {#group-var-regex byondver="510"}    
**See also:**    
:   [regex datum]/regex    
:   [Find proc (regex)]/regex/proc/Find    
:   [index var (regex)]/regex/var/index    
:   [match var (regex)]/regex/var/match    
After a call to Find(), if this regular expression had any parentheses    
groups, whatever text was matched in those groups is stored here in a    
list.    
### Example    
var/regex/R = new(\"B(.)(.)(.)D\") R.Find(\"BYOND\") // find this    
pattern in \"BYOND\" The result of the example is that R.group is    
list(\"Y\",\"O\",\"N\").  