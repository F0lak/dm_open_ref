
## Byondapi (info)
***
Byondapi is a set of exported functions from BYOND's core library that can be used by external libraries that you call via the <a href="#/proc/call_ext">`call_ext()` proc</a>. The purpose is to make interfacing with native code easier, and to allow external access to BYOND's functionality. Before this existed, all external calls had to use text strings to pass data back and forth, which was inefficient for many uses and very limited.

To build your external library with Byondapi, you have to include the `byondapi.h` header file that's included in BYOND's distribution. When compiling in Windows, you'll also need to link with `byondapi.lib`; in Linux, your makefile should link with `byondcore.so` from BYOND's own `bin` directory.

For simplicity, BYOND defines some basic types and macros in `byondapi.h`. The one most relevant to you is `u4c`, which is an unsigned 4-byte integer. There's also `s4c` which is a signed integer, as well as simple 1-byte and 2-byte ints that use `1c` and `2c` (respectively) insteaed of the `4c` suffix.

The main structure used to pass data back and forth is `CByondValue`. This mimics an internal structure in BYOND that holds values of all sorts: numbers, null, references to strings, references to objects and lists, and so on.

The exact functions used for interfacing with this structure are documented in `byondapi.h`.

The main tricky aspect of working with BYOND data is strings. If you need to get the contents of a string, you'll need to allocate memory for the character data and call `Byond_ToString()` to get a copy of the string. For converting character data to an internal string stored in CByondValue, you'll need to call `ByondValue_SetStr()`.

There are many function calls available in Byondapi for interacting with the server. These include the ability to read and write vars, call procs, create lists, read and write from lists, and so on.

Most of these procs return boolean values: true if they succeed, false if not. In the event of a failure, you can call `Byond_LastError()` to get the error message.

In any functions that read data from lists or read string data—including `Byond_LastError()`—you need to allocate the required memory for a copy of the string or list items. These functions take a pointer to the buffer that will be filled, and a `u4c` pointer for the buffer size (in items for lists, in bytes for strings). If the return value is false and the length is set to zero, an error occurred. If the return value is false and the length is non-zero, the new length value is the required length of the array; the memory should be allocated and the function called again.

The C++ wrappers have a better way of calling `Byond_LastError()` and other functions like it, where you don't need to worry about allocations.

Objects in BYOND are reference-counted; when an object's count reaches 0 it gets garbage-collected. In Byondapi you can call `ByondValue_IncRef()` and `ByondValue_DecRef()` to increment or decrement the reference count, respectively.

Byondapi maintains its own internal reference count for any object, so you can't decref past the number of references Byondapi holds.

The results you get from calls to Byondapi functions, such as reading a var or getting a return value from a proc call, have already had their reference count increased. That means when you're done using the value, you need to clean it up with `ByondValue_DecRef()` or else you'll have a memory leak.

The value you return from a function called by `call_ext()` should have a reference.

The C++ wrappers take care of most of the reference counting issues for you (see below).

BYOND servers handle proc execution and the management of data in a single thread. If your library tries to call any BYOND server functions in a different thread of its own, the call will block until the server thread can handle it.

The special function `Byond_ThreadSync()` will run a callback function on the main thread, avoiding the need to keep syncing over multiple Byondapi calls.

If you want to use the handy C++ wrappers and classes, you can include `byondapi_cpp_wrappers.cpp` and `byondapi_cpp_wrappers.h` in your library.

The `ByondValue` class is a wrapper around `CByondValue` that handles a number of operations for you. You can redefine the `argv` argument of any `call_ext()` functions as an array of `ByondValue` instead of `CByondValue`, but the return value should stay a `CByondValue`.

The external function calls like `ByondValue_CallProc()` have C++ wrappers that use the C calls internally, but if an error happens they'll call an error handler. The default error handler does nothing, but you can change it to a a different handler that accepts an error string.

If you define a `CatchingByondExceptions` variable inside of a `try` block, it will automatically change the error handler to one that throws a `ByondExtException`. This replaces the more cumbersome approach of checking if the return value is false and then calling `Byond_LastError()`.
***