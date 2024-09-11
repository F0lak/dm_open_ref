## call_ext proc 
###### BYOND Version 515
**See also:**
*   [load_ext proc](/proc/load_ext)
*   [arglist proc](/proc/arglist)
*   [call proc](/proc/call)
*   [path operators](/operator/path)
*   [Byondapi](/%7B%7Bappendix%7D%7D/Byondapi)
<!-- -->
**Format:**
*   call_ext(LibName,FuncName)(Arguments)
*   call_ext(LoadedFunc)(Arguments)
<!-- -->
**Args:**
*   LibName* name of external library (\"test.DLL\") (note* the .dll or
    .so suffix is not required)
*   FuncName* name of function in external library (\"func\"), which may
    have prefixes to describe the type of function
*   LoadedFunc* reference to a function that was loaded via `load_ext()`
<!-- -->
**Returns:**
*   The return value of the external library function.


This instruction exists in order to access third-party
libraries (.DLL files on Windows, .SO files on Unix), as long as the one
or more of the following conditions is met:
-   The library is located in the BYOND user `bin/` folder
    (`~/.byond/bin` on Unix, typically `%APPDATA%/Documents/BYOND/bin/`
    on Windows). This is intended to allow the user to install
    permanently \"trusted\" libraries. ***OR***
-   The server is run in `-trusted` mode. ***OR***
-   The server grants permission to access the library at runtime,
    through a prompt query.


If the library access or lookup fails for any reason, a runtime
error will be thrown. 

Normally you use LibName and FuncName,
and `call_ext()` will look up the function for you. However you can save
a little time by using `load_ext()`, which will do the lookup once and
let you reuse the reference to that function as often as you need to,
which should be helpful for performance-hungry code.
### String version


The standard way of making external calls (and until version
515, the only way) uses strings for everything. Any arguments that are
not strings are passed as empty strings instead. The call is prototyped
in the DLL this way:
``` cpp
extern "C" char *func(unsigned int argc, char *argv[]);
```


The `argc` argument is a number of arguments, and `argv` is an
array of the arguments themselves. The integer must be 32-bit.


As the library prototype is `char**`, the `call_ext()`
arguments must be strings. Other types (like numbers) will be passed as
the empty string (`""`) into the library function.
### Example* {#example .cpp}
``` cpp
// test.dll, a win32 C++ library compiled in VC++:
#include <string.h>
// This is an example of an exported function.
// Windows requires __declspec(dllexport) to be used to declare public symbols
// The name of the function from within the dll may be compiler-dependent
// (in this case it will usually be "merge" or "_merge").
// Google "name decoration" for more information on this exciting topic.
extern "C" __declspec(dllexport) char *merge(int n, char *v[]) 
{
    static char buf[500]; 
    *buf=0;
    for(int i=0; i<n; i++) {
        strcat(buf,v[i]); // we should bounds-check but it's a stupid example!
    }
    return buf;
}
```

```
 // DM code to use test.dll mob/verb/test() usr \<\<
call_ext(\"test.dll\",\"merge\")(\"fee\",\"fi\",\"fo\") // returns
\"feefifo\" // As with the other call() versions, arglist() may be used
to do runtime arguments* mob/verb/argtest() var/L =
list(\"fee\",\"fi\",\"fo\") usr \<\<
call_ext(\"test.dll\",\"func\")(arglist(L)) // returns \"feefifo\"

```
 

The `char *` pointer returned by the library is
expected to be cleaned up by the library when it\'s unloaded, or it can
be cleaned up on a subsequent function call. BYOND makes a copy of the
string when the function returns and does not need it after that.
### Byondapi version {#byondapi-version byondver="515"}


A newer and more flexible way of calling external libraries is
now available, and it allows you to pass strings, numbers, and
references, and also get other types of valus in return. This uses
[Byondapi](/%7B%7Bappendix%7D%7D/Byondapi) and requires your external
library to be compiled with the `byondapi.h` header file (if using C or
C++). Byondapi also includes helpful C++ wrapper classes in separate
files. 

With Byondapi calls, the function name you use in
`call_ext()` should be prefixed by `byond:` so that the engine knows
what type of function it is. In your library, the call is prototyped
like so:
``` cpp
extern "C" CByondValue func(u4c argc, CByondValue argv[]);
```


The `u4c` type is an unsigned 32-bit integer, defined in
`byondapi.h`. `CByondValue` is also defined there. Interacting with a
CByondValue structure requires the functions exported as part of
Byondapi.
### Example* {#example-1 .cpp}
``` cpp
// test_byondapi.dll, a win32 C++ library compiled in VC++:
#include <byondapi.h>
#include <stdlib.h>
#include <string.h>
// a different take on the merge example above
extern "C" BYOND_EXPORT CByondValue merge(int n, CByondValue v[])
{
    CByondValue result;
    u4c buflen = 1024;  // initial size of buffer
    u4c totallen = 0;   // length of total string so far (not including trailing null)
    char *buf = (char*)malloc(buflen);
    if(!buf) {  // we couldn't allocate memory
        ByondValue_Clear(&result);
        return result;
    }
    for(int i=0; i<n; i++) {
        u4c len = buflen - totallen;    // # of bytes left in buffer
        bool success = Byond_ToString(v[i], buf+totallen, &len);
        // on success, len is filled with # of bytes written (including trailing null)
        if(success) {
            totallen += (len-1);
        }
        // if we failed but len > 0, it's the new size of the buffer we need
        else if(len) {
            len = (len + 1023) & ~1023; // round up to 1K increments
            char *newbuf = (char *)mallloc(len);
            if(!newbuf) {   // out of memory; stop here
                ByondValue_Clear(&result);
                return result;
            }
            memcpy(newbuf, buf, totallen+1);    // include trailing null in copy
            free(buf);
            buf = newbuf; buflen = len;
            --i;  // retry Byond_ToString() for this argument
        }
        // if we failed but len == 0, there was an error
        else {
            free(buf);
            ByondValue_Clear(&result);
            return result;
        }
    }
    ByondValue_SetStr(&result, buf);    // create a new internal string
    free(buf);  // free the buffer
    return result;
}
extern "C" BYOND_EXPORT CByondValue average(int n, CByondValue v[])
{
    CByondValue result;
    float total = 0.0f;
    int count = 0;
    for(int i=0; i<n; i++) {
        if(!ByondValue_IsNum(v[i])) continue;
        total += ByondValue_GetNum(v[i]);
        ++count;
    }
    if(count) ByondValue_SetNum(&result, total / count);
    else ByondValue_Clear(&result); // return null on failure
    return result;
}
```

```
 // DM code to use test_byondapi.dll mob/verb/test() usr \<\<
call_ext(\"test_byondapi\",\"byond:merge\")(\"fee\",\"fi\",\"fo\") //
returns \"feefifo\" mob/verb/average() usr \<\<
call_ext(\"test_byondapi\",\"byond:average\")(1,6,8) // returns 5

```
 

You are of course allowed to mix different argument
types, so they don\'t all have to be numbers or all strings. Your
library code can use the Byondapi functions to interact with these
values.
### Other prefixes


For advanced users* on Windows, `call_ext()` uses the `__cdecl`
convention by default. If you are designing or linking to a DLL that
uses the `__stdcall` convention instead, you can inform `call_ext()` by
prefacing the function name with the `"@"` symbol. E.g.,
`call_ext("test.dll","@merge")` would call a version of `merge` declared
with the `__stdcall` convention. Likewise if you use the Byondapi
version, you can use `call_ext("test.dll","@byond:merge")` or
`call_ext("test.dll","byond:@merge")` (it doesn\'t matter which order
the prefixes go in).