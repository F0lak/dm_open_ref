## operator overloading 
###### BYOND Version 512" short="overloading


DM allows you to overload most of the operators it uses when
working with datums and other objects. This means that A + B can call a
proc defined under A instead, with B as an argument, and the return
value of that proc would be the result. 

The proc name for an
overloaded operator is "operator" followed immediately by the operator
itself, such as `operator*` to override the multiplication operator.
`A * B` will call `A.operator*(B)` if the proc is available.
### Example:

```dm
 complex // complex number a+bi var/a as num var/b as num
New(\_a,\_b) a = \_a b = \_b proc/operator+(complex/C) if(istype(C))
return new/complex(a+C.a, b+C.b) if(isnum(C)) return new/complex(a+C, b)
return src proc/operator+=(complex/C) if(istype(C)) a += C.a b += C.b
else if(isnum(C)) a += C 
```
 

The following operators may
be overloaded:
Operators
Proc
Notes
Arithmetic and binary (return new value)
A + B
A.operator+(B)
A - B
A.operator-(B)
-A
A.operator-()
Same proc as subtraction, but has no arguments
A * B
A.operator*(B)
A / B
A.operator/(B)
A % B
A.operator%(B)
A %% B
A.operator%%(B)
A ** B
A.operator**(B)
A \| B
A.operator\|(B)
A & B
A.operator&(B)
A \^ B
A.operator\^(B)
\~A
A.operator\~()
A << B (shift)
A.operator<<(B)
A >> B (shift)
A.operator>>(B)
A << B (output)
A.operator<<(B,A,window)\
world.operator<<(B,target,window)
Ignores return value\
..() falls back on world proc, then default behavior
A >> B (input)
A.operator>>(null,A)\
world.operator>>(null,source)
Return value is assigned to B\
..() falls back on world proc, then default behavior
Comparisons (return true or false)
A \~= B
A.operator\~=(B)
A \~! B
A.operator\~!(B)
A < B
A.operator<(B)
A >= B
A.operator>=(B)
A > B
A.operator>(B)
A <= B
A.operator<=(B)
A <=> B
A.operator<=>(B)
Assignments with side effects (return value defaults to src)
A += B
A.operator+=(B)
A -= B
A.operator\--(B)
A *= B
A.operator*=(B)
A /= B
A.operator/=(B)
A %= B
A.operator%=(B)
A %%= B
A.operator%%=(B)
A \|= B
A.operator\|=(B)
A &= B
A.operator&=(B)
A \^= B
A.operator\^=(B)
A <<= B
A.operator<<=(B)
A >>= B
A.operator>>=(B)
A := B
A.operator:=(B)
++A
A.operator++()
\--A
A.operator\--()
A++
A.operator++(1)
A\--
A.operator\--(1)
List access
A[idx]
A.operator[](idx)
Used for reading a list value
A[idx] = B
A.operator[]=(idx, B)
Used for writing a list value; ignores return value
Other
turn(A, B)
A.operator_turn(B)
"[A]"
A.operator""()
Specifies a custom way for converting A to text (see notes below)


Some operators cannot be overloaded. The `=` operator for
direct assignment is one. The `!` operator is another. The `==` and `!=`
operators measure equality and can\'t be overloaded, but `~=` and `~!`
for equivalence can be. It would also be meaningless to override the
ternary `? :` operator pair, and the `.` and `:` family of operators for
accessing vars and procs. 

Comparison operators come in opposing
pairs: `~=` vs. `~!`, `<` vs. `>=`, `>` vs. `<=`. You only need to
override one operator from each pair; DM is smart enough to know that
`!(A ~= B)` is the same as `A ~! B`. 

By the same logic, you
don\'t have to define the assign-with-side-effect operators like `+=` if
you don\'t want to. For instance if you override `+` but not `+=`, then
`A += B` will be handled internally as `A = A + B`, which means the
value of `A` after the statement may be a different datum than `A` was
before. The value of `A` can also change if you *do* overload `+=` but
the proc returns a value other than null; its return value will be the
new `A`. 

If an overloaded proc is not available for an operator
you try to use on a datum, a runtime error may result. 

The
output and input operators are given special treatment. If no overload
is defined for the current left-hand-side value, the overload proc is
looked up under `world` instead. The world overload proc is also a
fallback if `..()` is called, and after that `..()` does the default
behavior. These procs are always called with multiple arguments, to
distinguish them from bitwise shift operators. The output version gets a
third argument when the result `output()` is sent, since that can
include a window reference.
### Example:

```dm
 // Send an effect to a player or list of players
proc/DoEffect(target, effect/E) if(istype(target, /list)) for(var/i in
target) DoEffect(i, E) return if(target == world \|\| target ==
world.contents) for(var/client/C) DoEffect(C, E) if(istype(target,
/client)) DoEffect(target:mob) if(istype(target, /mob))
if(target:client) ... // do something here to show the effect
world/proc/operator<<(out, target) if(istype(target,/savefile)) return
..() // always save normally if(istype(out, /effect)) DoEffect(target,
out) else ..() 
```
 

The list access operators are a
special case as well, because reading to a list and writing to it are
different things, so there are two procs for the purpose. The `[]`
overload is for reading, and `[]=` is for writing. 

There is
also now an overload for converting a datum to text. By having
`operator""` return a text string, that text will automatically appear
anywhere you embed the datum in a string, use `json_encode()` on the
datum, or many other situations. It won\'t work for atoms being sent
directly to output (e.g., `world << obj`) or other skin controls because
the client has special handling for these situations and the client
isn\'t given any info about the overloaded text. Likewise, the
overloaded text won\'t appear for objects in an `input()` prompt list,
which is also handled mainly on the client. Despite these limitations,
the text overload offers greater flexibility.

> [!TIP] 
> **See also:**
> +   [datum](/ref/datum.md) 
> +   [operators](/ref/operator.md) 