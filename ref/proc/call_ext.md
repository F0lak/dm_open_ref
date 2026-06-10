
## call_ext (proc)

**Format:**
+   call_ext(LibName,FuncName)(Arguments)
+   call_ext(LoadedFunc)(Arguments)

**Arguments:**
+   LibName: name of external library ("test.DLL") (note: the .dll or .so suffix is not required)
+   FuncName: name of function in external library ("func"), which may have prefixes to describe the type of function
+   LoadedFunc: reference to a function that was loaded via

**Returns:**
+   The return value of the external library function.
***
This instruction exists in order to access third-party libraries (.DLL files on Windows, .SO files on Unix), as long as the one or more of the following conditions is met:

If the library access or lookup fails for any reason, a runtime error will be thrown.

Normally you use LibName and FuncName, and `call_ext()` will look up the function for you. However you can save a little time by using `load_ext()`, which will do the lookup once and let you reuse the reference to that function as often as you need to, which should be helpful for performance-hungry code.

The standard way of making external calls (and until version 515, the only way) uses strings for everything. Any arguments that are not strings are passed as empty strings instead. The call is prototyped in the DLL this way:

The `argc` argument is a number of arguments, and `argv` is an array of the arguments themselves. The integer must be 32-bit.

As the library prototype is `char**`, the `call_ext()` arguments must be strings. Other types (like numbers) will be passed as the empty string (`""`) into the library function.


```dm

// DM code to use test.dll
mob/verb/test()
    usr << call_ext("test.dll","merge")("fee","fi","fo") // returns "feefifo"

// As with the other call() versions, arglist() may be used to do runtime arguments:
mob/verb/argtest()
    var/L = list("fee","fi","fo")
    usr << call_ext("test.dll","func")(arglist(L)) // returns "feefifo"

```


The `char *` pointer returned by the library is expected to be cleaned up by the library when it's unloaded, or it can be cleaned up on a subsequent function call. BYOND makes a copy of the string when the function returns and does not need it after that.

A newer and more flexible way of calling external libraries is now available, and it allows you to pass strings, numbers, and references, and also get other types of valus in return. This uses <a href="#/{{appendix}}/Byondapi">Byondapi</a> and requires your external library to be compiled with the `byondapi.h` header file (if using C or C++). Byondapi also includes helpful C++ wrapper classes in separate files.

With Byondapi calls, the function name you use in `call_ext()` should be prefixed by `byond:` so that the engine knows what type of function it is. In your library, the call is prototyped like so:

The `u4c` type is an unsigned 32-bit integer, defined in `byondapi.h`. `CByondValue` is also defined there. Interacting with a CByondValue structure requires the functions exported as part of Byondapi.


```dm

// DM code to use test_byondapi.dll
mob/verb/test()
    usr << call_ext("test_byondapi","byond:merge")("fee","fi","fo") // returns "feefifo"

mob/verb/average()
    usr << call_ext("test_byondapi","byond:average")(1,6,8)  // returns 5

```


You are of course allowed to mix different argument types, so they don't all have to be numbers or all strings. Your library code can use the Byondapi functions to interact with these values.

Reference counting in Byondapi is done by calling `ByondValue_IncRef()` to increment the reference count, and `ByondValue_DecRef()` to decrement the count (and possibly initiate garbage collection). If you use the C++ wrappers, a lot of this is taken care of for you via the `ByondValue` class (see below).

Byondapi calls that fill pointers or arrays with results will automatically increment the reference count, so for instance the value that goes into the result for `Byond_ReadVar()`, or every value received in `Byond_ReadList()`, has been incremented. You will need to clean these references up when you're done with them.

The value you return from your library function back to DM should be incremented. If you got it from a function like `Byond_ReadVar()` then that's already been done for you.

You don't have to call `ByondValue_DecRef()` on any of the arguments sent to your function. Their reference counts will be decremented when the call returns to DM.

The C++ wrapper file included for Byondapi defines a new `ByondValue` class that handles all your reference counting for you. All of the functions are wrapped so you send them a `ByondValue` reference instead of a `CByondValue` pointer. Anything that can fail with an error can throw an exception for you to catch.

The `ByondValue` class contains a referenced `CByondValue`. The destructor calls `ByondValue_DecRef()` for you. You can manage references in a few ways:

This is what your function would look like with the C++ wrappers:

Here's a different example reading from a list:

Because every value is defined as a `ByondValue` rather than a `CByondValue`, they clean up after themselves. The return value gets cast to `ByondValueResult` so it automatically detaches, meaning the reference count doesn't go down. The caller will use this reference and decrement it later.

For Byondapi, there is also an asynchronous version you can call. In `call_ext()` or `load_ext()` the function name should be prefixed with `byond,await:` instead of `byond:`, and the function in your library has a different format.

The function has no return value, and accepts a third argument which is the <a class="code" href="#/callee">/callee</a> object of the calling proc. Your BYOND proc will sleep when it calls `call_ext()` for this function. In your library function you would typically either spawn a new thread or pass `waiting_proc` to an existing thread. When it's ready to return, you call `Byond_Return(waiting_proc, return_value)`.


```dm

// this call will sleep until the library calls Byond_Return()
usr << "Sleeping now..."
usr << call_ext("mylib", "byond_await:Sleep2sec")()

```


When `Byond_Return()` is called, the sleeping proc is added to the scheduler as if it had been spawned. This is the same behavior you would see in a call such as `winget()` that has to wait for a response.

For advanced users: on Windows, `call_ext()` uses the `__cdecl` convention by default. If you are designing or linking to a DLL that uses the `__stdcall` convention instead, you can inform `call_ext()` by prefacing the function name with the `"@"` symbol. E.g., `call_ext("test.dll","@merge")` would call a version of `merge` declared with the `__stdcall` convention. Likewise if you use the Byondapi version, you can use `call_ext("test.dll","@byond:merge")` or `call_ext("test.dll","byond:@merge")` (it doesn't matter which order the prefixes go in).
***
**Related Pages:**
+    [load_ext proc](/ref/proc/load_ext)
+    [arglist proc](/ref/proc/arglist)
+    [call proc](/ref/proc/call)
+    [path operators](/ref/operator/path)
+    [Byondapi](/ref/{{appendix}}/Byondapi)
