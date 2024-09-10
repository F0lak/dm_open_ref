[]{#/issaved proc.md}    
## issaved proc    
**See also:**    
:   [initial proc]/proc/initial    
:   [savefile]/savefile    
:   [tmp vars]/var/tmp    
:   [vars list var (datum)]/datum/var/vars    
<!-- -->    
**Format:**    
:   issaved(Var)    
<!-- -->    
**Args:**    
:   Var: The variable to test.    
This returns 1 if the given variable should be automatically saved when    
writing an object to a savefile and 0 otherwise. Variables which are not    
global, const, or tmp will return 1.  