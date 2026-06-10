
## params (var)
***
This is a list of parameters passed to the world from the command-line -params option when the server was started. The parameter text is passed through params2list() to generate the world.params list.


```dm

world/New()
   var/p
   if(params.len) world.log << "Command-line parameters:"
   for(p in params)
      world.log << "[p] = [params[p]]"

```


This example displays the value of each parameter.
***