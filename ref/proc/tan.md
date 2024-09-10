[]{#/tan proc.md}    
## tan proc {#tan-proc byondver="513"}    
**See also:**    
:   [arctan proc](/proc/arctan)    
:   [cos proc](/proc/cos)    
:   [sin proc](/proc/sin)    
:   [turn proc](/proc/turn)    
<!-- -->    
**Format:**    
:   tan(X)    
<!-- -->    
**Returns:**    
:   The tangent of X, where X is in degrees.    
### Example:    
mob/verb/test() usr \<\< tan(0) // 0 usr \<\< tan(45) // 1 usr \<\<    
tan(90) // infinity (or close enough)  