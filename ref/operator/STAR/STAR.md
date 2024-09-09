[]{#/operator/*}    
## \* operator    
**See also:**    
:   [\*= operator](/ref/operator/*=/*=.md)    
:   [+ operator](/ref/operator/+/+.md)    
:   [- operator](/ref/operator/-/-.md)    
:   [/ operator](/ref/operator///.md)    
:   [operators](/ref/operator/operator.md)    
<!-- -->    
**Format:**    
:   A \* B    
<!-- -->    
**Returns:**    
:   The product of A and B.    
Multiplies A and B. The result of the operation depends on the types of    
values being multiplied, mostly on A.    
  A type            B type                 Result    
  ----------------- ---------------------- ------------------------------------------------    
  num or null (0)   num or null (0)        Numeric product    
  icon or /icon     icon or num or color   New blended icon via ICON_MULTIPLY    
  matrix            matrix                 New matrix, product of A and B    
                    num                    New matrix scaling A by B    
                    vector                 New matrix scaling A by B.x and B.y    
  vector            vector                 New vector with components multiplied together    
                    matrix                 New vector with 2D transformation applied    
                    num                    New vector scaling A by B  