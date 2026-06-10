
## log (var)
***
Sending output to world.log may be useful for debugging purposes. The output goes to the same place run-time proc errors are displayed.


```dm

if(1+1 != 2)
  world.log << "Uh oh."

```


You can assign world.log to a file name or file() object to redirect output to that file. (There is also a command-line option to Dream Daemon that does this.)


```dm

world.log = file("mylog.txt")

```

***