## :: operator 
###### BYOND Version 515

**Format:**
+   ::A
+   ::A()
+   A::B
+   A::B() (proc reference, not a call; see below)


This is the scope operator. It has multiple uses.
### Global var and proc disambiguation


`::A` is a shorthand for `global.A`, so if you have a local or
object var with the same name this disambiguates to the global var. The
same is true of `:A()` which will call `global.A()` with the arguments
you give it.
### Static var disambiguation


If `A` is a constant type and `B` is a static var, `A::B`
refers to the static var. If you have a local var with the same name,
this disambiguates to the static var. This is also the only case where
`A::B` can be used as an Lvalue (modifiable expression).
### Initial value


The most common use of the scope operator is to get the initial
value for a var. If `A::B` isn\'t a static var, then it\'s equivalent to
`initial(A:B)`. If `A` is a constant type path, the compiler will go
even further by compiling this expression as the actual initial value
instead of doing a runtime lookup. 

This can also be used when
defining a var that overrides its parent, by using the `parent_type`
keyword for `A`. Multiple `parent_type` levels can be chained together.
Similarly, in a static var definition, `type` can be used for `A` the
same way.
### Example:

```
 thing var/price = 60 better price = parent_type::price + 40

```

### Proc reference


If `B` is a proc, then `A::B()` is a reference to the proc for
type `A`, which can be used in `call()`. In this case the parentheses
are just a cue for the compiler to know this is a proc reference; it
doesn\'t actually call the proc. Currently, `A` must be a constant type
for this usage.
### Example:

```
 thing proc/DoSomething() world \<\< \"Did a thing\" better
DoSomething() world \<\< \"Did a better thing\" proc/Downgrade()
var/thing/better/T = new // will print \"Did a better thing\" because T
is /thing/better T.DoSomething() // deliberately calls /thing\'s
original version; will print \"Did a thing\" call(T,
/thing::DoSomething())() 
```


**See also:**
+   [. path operator](/ref/operator/path/%2e.md) 
+   [/ path operator](/ref/operator/path//.md) 
+   [: path operator](/ref/operator/path/:.md) 
+   [operators](/ref/operator.md) 
+   [call proc](/ref/proc/call.md) 
+   [initial proc](/ref/proc/initial.md) 
+   [nameof proc](/ref/proc/nameof.md) 
+   [istype proc](/ref/proc/istype.md) <!-- -->