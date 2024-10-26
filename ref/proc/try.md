## try and catch statements 
###### BYOND Version 508

The try and catch keywords are used for error handling. Any
code that runs inside of a try block will, if an error happens or the
throw keyword is used, stop executing and jump to the matching catch
block. (This is also true of indirect proc calls. If you call a proc
from inside a try block, any errors in that proc will be sent to the
catch.) 

For every try there must be a catch, even if it does
nothing. The catch block takes an optional value that can receive the
error.
### Example:

```dm
var/a = 2
try
  a += "Hello"  // will throw a type mismatch error
catch(var/exception/e)
  // file and line info is available if you enable debugging
  world.log << "[e] on [e.file]:[e.line]"
world << "a is [a]"
```

Because the value in the catch
keyword is optional, you can simply use the catch keyword alone. It is
also not necessary to include any code under the catch keyword, if the
error is meant to be ignored. (However, it is not usually a good idea to
ignore errors.) 

The throw keyword is used if you want to throw
an error deliberately. When you use throw, the error thrown does not
have to be an /exception datum, but can be anything you like.

> [!TIP] 
> **See also:**
> +   [Error proc (world)](/ref/world/proc/Error.md) 
> +   [throw statement](/ref/proc/throw.md) 
> +   [EXCEPTION proc](/ref/proc/EXCEPTION.md) 
> +   [exception](/ref/exception.md) 