## \#define directive

**Format:**
+   #define Name Value
+   #define Name(Parameters) Value
<!-- -->
**Args:**
+   Name: A macro definition.
+   Value: The value to substitute for Name.
+   Parameters: Arguments to pass into the macro.


The #define statement creates a macro that is substituted for
Name. Substitution only applies to whole words. Text inside of double or
single quotes is not processed for substitution, so `"This is BIG."`
would not be modified even if a macro named BIG were defined. That is
different from `"This is [BIG]."`, where BIG is an embedded expression,
which does get processed for macro substitution.
### Example:

```dm
#define DAY   0
#define NIGHT 1
var/daytime = NIGHT  //daytime = 1
```

### Example:

```dm
#define SQR(X) ((X)*(X))
var/x = SQR(2)       //x = ((2)*(2)) = 4
```
 
> [!NOTE] 
> it\'s usually important to use
parentheses around any arguments you use in a macro. Otherwise strange
results may occur if you use an expression such as 2+3. In the SQR(X)
example, if there were no parentheses around each X then the expansion
of the macro would be (2+3*2+3). Since the * operator has a higher
precedence than + the result is 11, not 25 as expected. It\'s equally
important to put parentheses around the entire macro for the same
reason.
### Variadic macros

The last parameter of a macro can end in `...` which means that
it and all other arguments following it count as a single argument. This
is called a variadic macro because it lets you use a variable number of
arguments. The last parameter will also become optional.
### Example:

```dm
 #define DEFAULT_LIST(n, items...) if(!n) n = list(items)
```

### `#var` to string

In a macro\'s body, if you precede a parameter by `#`, the
replacement value will be turned into a string. For instance, 2 would
become "2".
### Example:

```dm
#define DEBUG_VAR(v) world.log << "[#v] = [v]"
DEBUG_VAR(usr.x)    // world.log << "usr.x = [usr.x]"
```
### `##var` concatenation

A parameter preceded by `##` in the macro body is substituted
directly, without any spaces. If you use this with the last argument in
a variadic macro, any preceding spaces and a comma (if found) will be
removed if the replacement is empty.
### Example:

```dm
#define MACROVAR(k) var/macro_state_##k
// MACROVAR(right) becomes var/macro_state_right

#define PREFIX_LIST(x, y...) list(x, src, ##y)
// PREFIX_LIST(1, 2, 3) becomes list(1, src, 2, 3)
// PREFIX_LIST(4) becomes list(4, src)
```
### `n###var` repeat


Using `###` in the macro body, preceded by a number, will
repeat the replacement a certain number of times.
### Example:

```dm
#define SAYTWICE(t) 2###t
#define TOTEXT(t) #t
world << "[TOTEXT(SAYTWICE(hi))]"   // world << "hihi"
```

> [!TIP] 
> **See also:**
> +   [preprocessor](/ref/DM/preprocessor.md) <!-- -->