
## overload (info)
***
DM allows you to overload most of the operators it uses when working with datums and other objects. This means that A + B can call a proc defined under A instead, with B as an argument, and the return value of that proc would be the result.

The proc name for an overloaded operator is "operator" followed immediately by the operator itself, such as <code>operator*</code> to override the multiplication operator. `A * B` will call `A.operator*(B)` if the proc is available.


```dm

complex     // complex number a+bi
    var/a as num
    var/b as num

    New(_a,_b)
        a = _a
        b = _b

    proc/operator+(complex/C)
        if(istype(C)) return new/complex(a+C.a, b+C.b)
        if(isnum(C)) return new/complex(a+C, b)
        return src

    proc/operator+=(complex/C)
        if(istype(C))
            a += C.a
            b += C.b
        else if(isnum(C)) a += C

```


The following operators may be overloaded:
***
**Related Pages:**
+    [datum](/ref/datum)
+    [operators](/ref/operator)
