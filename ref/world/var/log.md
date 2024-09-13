## log var (world)


Sending output to world.log may be useful for debugging
purposes. The output goes to the same place run-time proc errors are
displayed.
### Example:

``` dm
 if(1+1 != 2) world.log \<\< \"Uh oh.\" 
```



You can assign world.log to a file name or file() object to
redirect output to that file. (There is also a command-line option to
Dream Daemon that does this.)
### Example:

``` dm
 world.log = file(\"mylog.txt\") 
```


> [!TIP] 
> **See also:**
> +   [file proc](/ref/proc/file.md) 
> +   [startup proc](/ref/proc/startup.md) 