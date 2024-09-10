## isnan proc {#isnan-proc byondver="515"}    
**See also:**    
:   [isnum proc](/proc/isnum)    
:   [isinf proc](/proc/isinf)    
:   [Numbers](/%7Bnotes%7D/numbers)    
<!-- -->    
**Format:**    
:   isnan(n)    
<!-- -->    
**Args:**    
:   n: A number    
<!-- -->    
**Returns:**    
:   1 if this is a numeric value but is an invalid \"not a number\"    
    (NaN); 0 otherwise    
Some math operations return the special number `NaN` if they\'re    
undefined, such as dividing 0 by 0. This tells you if a number is that    
type.    
NaN is never greater than, less than, or equal to another number, even    
itself.  