
## DEBUG (info)

**Format:**
+   #define DEBUG
***
If <code>DEBUG</code> is defined, source file and line number information will be stored in the compiled <code>.dmb</code> file. If a proc crashes during execution and <code>DEBUG</code> information is present, the current source file name and line number will be indicated in the error output.

This option increases the size of the <code>.dmb</code>, typically by about 10%. Execution of the code may also be a tiny bit slower.

If you are distributing the <code>.dmb</code> to players and you do not want them to have debug access at runtime, you should <em>not</em> compile in debug mode.

If you want to use the run-time profiler (see the debugging options in Dream Seeker), you must compile in debug mode. Then you can get a report of CPU usage by your various procs.
***
**Related Pages:**
+    [#define directive](/ref/DM/preprocessor/define)
