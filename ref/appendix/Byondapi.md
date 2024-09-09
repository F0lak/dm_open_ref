[]{#/{{appendix}}/Byondapi}    
## Byondapi {#byondapi byondver="515"}    
**See also:**    
:   [call_ext() proc](/ref/proc/call_ext)    
Byondapi is a set of exported functions from BYOND\'s core library that    
can be used by external libraries that you call via the [`call_ext()`    
proc](/ref/proc/call_ext). The purpose is to make interfacing with native    
code easier, and to allow external access to BYOND\'s functionality.    
Before this existed, all external calls had to use text strings to pass    
data back and forth, which was inefficient for many uses and very    
limited.    
To build your external library with Byondapi, you have to include the    
`byondapi.h` header file that\'s included in BYOND\'s distribution. When    
compiling in Windows, you\'ll also need to link with `byondapi.lib`; in    
Linux, your makefile should link with `byondcore.so` from BYOND\'s own    
`bin` directory.    
### Simple BYOND types    
For simplicity, BYOND defines some basic types and macros in    
`byondapi.h`. The one most relevant to you is `u4c`, which is an    
unsigned 4-byte integer. There\'s also `s4c` which is a signed integer,    
as well as simple 1-byte and 2-byte ints that use `1c` and `2c`    
(respectively) insteaed of the `4c` suffix.    
### CByondValue struct    
The main structure used to pass data back and forth is `CByondValue`.    
This mimics an internal structure in BYOND that holds values of all    
sorts: numbers, null, references to strings, references to objects and    
lists, and so on.    
The exact functions used for interfacing with this structure are    
documented in `byondapi.h`.    
The main tricky aspect of working with BYOND data is strings. If you    
need to get the contents of a string, you\'ll need to allocate memory    
for the character data and call `Byond_ToString()` to get a copy of the    
string. For converting character data to an internal string stored in    
CByondValue, you\'ll need to call `ByondValue_SetStr()`.    
### Other function calls    
There are many function calls available in Byondapi for interacting with    
the server. These include the ability to read and write vars, call    
procs, create lists, read and write from lists, and so on.    
Most of these procs return boolean values: true if they succeed, false    
if not. In the event of a failure, you can call `Byond_LastError()` to    
get the error message.    
In any functions that read data from lists, or read string data, they    
require the caller to allocate the needed memory for a copy of the    
string or list items. In these cases, the functions also take a `u4c`    
pointer for the length. If the return value is false and the length is    
set to zero, an error occurred. If the return value is false and the    
length is non-zero, the new length value is the required length of the    
array; the memory should be allocated and the function called again.    
BYOND servers handle proc executin and the management of data in a    
single thread. If your library tries to call any BYOND server functions    
in a different thread of its own, the call will block until the server    
thread can handle it.    
### C++ wrappers    
If you want to use the handy C++ wrappers and classes, you can include    
`byondapi_cpp_wrappers.cpp` and `byondapi_cpp_wrappers.h` in your    
library.    
The `ByondValue` class is a wrapper around `CByondValue` that handles a    
number of operations for you. You can redefine the `argv` argument of    
any `call_ext()` functions as an array of `ByondValue` instead of    
`CByondValue`, but the return value should stay a `CByondValue`.    
### Example: {#example .cpp}    
``` cpp    
#include <string>    
#include <byondapi.h>    
#include <byondapi_cpp_wrappers.h>    
#include <string>    
extern "C" BYOND_EXPORT CByondValue merge(int n, ByondValue v[])    
{    
    ByondValue result;    
    std::string merged, str;    
    for(int i=0; i<n; i++) {    
        v[i].ToString(str);    
        if(str) merged += str;    
    }    
    result = merged.c_str();   // ByondValue's assignment operator takes care of everything    
    return result;    
}    
```    
There is also a `ByondValueList` wrapper class for the list structure.    
The external function calls like `ByondValue_CallProc()` have C++    
wrappers that use the C calls internally, but if an error happens    
they\'ll throw a `ByondExtException` for you to catch. This replaces the    
more cumbersome approach of checking if the return value is false and    
then calling `Byond_LastError()`.  