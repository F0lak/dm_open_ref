[]{#/DM/preprocessor/define/DEBUG}    
## DEBUG definition    
**See also:**    
:   [#define directive](/ref/DM/preprocessor/define.md)    
<!-- -->    
**Format:**    
:   #define DEBUG    
If `DEBUG` is defined, source file and line number information will be    
stored in the compiled `.dmb` file. If a proc crashes during execution    
and `DEBUG` information is present, the current source file name and    
line number will be indicated in the error output.    
This option increases the size of the `.dmb`, typically by about 10%.    
Execution of the code may also be a tiny bit slower.    
If you are distributing the `.dmb` to players and you do not want them    
to have debug access at runtime, you should *not* compile in debug mode.    
If you want to use the run-time profiler (see the debugging options in    
Dream Seeker), you must compile in debug mode. Then you can get a report    
of CPU usage by your various procs.  