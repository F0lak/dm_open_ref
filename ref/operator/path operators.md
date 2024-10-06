## path operators


A "path" in DM is a constant value that identifies a
particular definition in the code tree (i.e. an object, procedure, or
variable definition). An example of this is the default mob type for new
players `/mob`. 

Paths are used in two contexts. One is to "get
to" a particular point in the code tree in order to modify the
definition. The other is to reference a particular definition made
elsewhere in the code tree. The syntax of a path is similar in both
cases. 

When you are making a definition, you simply put the
path at the beginning of a line like this: 
```dm

obj/clothes/gloves 
```
 

That automatically creates that
path in the code tree if it does not already exist. When starting at the
beginning of the line (no indentation) there is no need to begin the
path with \'/\', but that is perfectly acceptable. 

When making
definitions, DM equates the path separator \'/\' with indentation, so
the above example is really just a more compact way of writing:

```dm
 obj clothing gloves 
```
 

One generally uses
indentation when you have several things to define with a common parent
path: 
```dm
 obj clothing gloves sandals 
```
 

An
important element of DM is that you can get to the same path in the code
tree from multiple places in the source code. For example, given the
above definition of `gloves` and `sandals`, you could modify a property
of one of them from somewhere else using any path syntax you like:

```dm
 obj/clothing/sandals name = "Winged Sandals" 
```



While that was not a useful thing to do in this case, it can be
a very powerful tool when organizing source code in large projects. Also
note that the use of "/" can save your source code from getting too
deeply indented, which may sound mundane, but which is quite important!


The above examples used paths to make definitions. The other
time when you use paths is when you need to refer to a particular
definition. Creation of an object is one example: 
```dm

mob/Login() if(length(contents) == 0) //poor fellow has nothing //create
sandals in his contents list new /obj/clothing/sandals (src) return ..()

```
 

Another common use of paths is to declare the data
type of a variable. In DM, variable types do not affect what type of
data the variable may contain---variables that you define may contain
any type of value. Instead, the variable type affects what properties of
the data you can attempt to access. 

The following example
defines variables for clothing that is occupying various positions on
the body. 
```dm
 mob var/clothing feet hands torso 
```



Since there were several variables of the same type, they were
grouped under `var/clothing`. It can be done any number of ways,
depending on the situation. The same path syntax applies to variable
definitions as it does to anything else. This example produces the same
effect: 
```dm
 mob/var/clothing/feet mob/var clothing hands torso

```

### Provisos


Just do not make a mistake like the following: 
```dm

mob/var /clothing/feet 
```
 

Beginning a path with \'/\'
effectively ignores whatever indentation may precede it. That is why it
is called an *absolute* path. The above example would therefore be the
same as the following, which is not what you want: 
```dm
 mob/var
//empty variable definition clothing/feet //definition of object type
/clothing/feet 
```
 

On a related note, parameter
definitions in procedures should not begin with a "/". 
```dm

mob/Move(atom/Dest) //correct src << "Moving to
[Dest.x],[Dest.y]." return ..() mob/Move(var/atom/Dest) //ok
mob/Move(/atom/Dest) //WRONG 
```
 

Essentially, "var/"
is prepended to each entry in the parameter list.

> [!TIP] 
> **See also:**
> +   [. path operator](/ref/operator/path/%2e.md) 
> +   [/ path operator](/ref/operator/path//.md) 
> +   [: path operator](/ref/operator/path/:.md) 
> +   [procs](/ref/proc.md) 
> +   [vars](/ref/var.md) 