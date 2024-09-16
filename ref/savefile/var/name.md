## name var (savefile)


The external "real" filename is stored in file.name. It is
initialized when creating a new file. If none is specified, a temporary
file with a random name will be created.
### Example:

``` dm
 var/savefile/F1 var/savefile/F2 F1 = new() // create a
temp file F2 = new("myfile") // open "myfile" world << "F1.name =
[F1]" world << "F2.name = [F2]" 
```


> [!TIP] 
> **See also:**
> +   [savefile](/ref/savefile.md) 