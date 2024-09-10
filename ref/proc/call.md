## call proc    
**See also:**    
:   [arglist proc](/proc/arglist)    
:   [call_ext proc](/call proc.md_ext)    
:   [hascall proc](/proc/hascall)    
:   [path operators](/operator/path)    
<!-- -->    
**Format:**    
:   call(ProcRef)(Arguments)    
:   call(Object,ProcName)(Arguments)    
:   call(LibName,FuncName)(Arguments) (use `call_ext()` instead)    
<!-- -->    
**Args:**    
:   ProcRef: path of proc (/proc/MyProc)    
:   Object: source of proc or verb    
:   ProcName: name of proc or verb (\"MyProc\")    
:   LibName: name of external library (\"test.DLL\")    
:   FuncName: name of function in external library (\"func\")    
<!-- -->    
**Returns:**    
:   The return value of the proc being called.    
This instruction exists in order to call procs dynamically, since the    
proc reference or name may be an expression rather than a hard-coded    
value. This may serve the same purpose as a \"function pointer\" in C    
programs.    
The following examples do not demonstrate why you would want to do this,    
but the syntax is illustrated. The first one calls a specific procedure    
by using a path reference to that procedure.    
### Example:    
/proc/MyProc(Arg) usr \<\< \"MyProc(\[Arg\])\" mob var MyProc =    
/proc/MyProc verb call_myproc() call(MyProc)(\"Hello, world!\")    
The next example calls an object procedure (or verb) by name, rather    
than by path.    
### Example:    
mob proc Proc1(Arg) usr \<\< \"Proc1(\[Arg\])\" Proc2(Arg) usr \<\<    
\"Proc2(\[Arg\])\" verb call_proc(Proc in list(\"Proc1\",\"Proc2\"))    
call(src,Proc)(\"Hello, world!\")    
Note: In prior versions, `call()` was also used to access third-party    
libraries (.DLL files on Windows, .SO files on Unix), but this has been    
moved to [call_ext()](/call proc.md_ext){.code} for clarity.  