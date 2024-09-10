[]{#/null.md}    
## null    
Variables that are not initialized have the value null. This value is    
distinct from 0 and \"\". If you compare it to these, using the `==`    
operator, it is not equal. However, in a numeric context (like a    
mathematical operation), null evaluates to 0 and in a text context (like    
insertion into a text expression), null evaluates to \"\". In a logical    
expression, null, 0, and \"\" evaluate to false and all other values are    
true.    
In an embedded text expression, null behaves like \"\". That means, if    
you are expecting a variable to display a 0, you should explicitly    
initialize it to 0 rather than leaving it as null.  