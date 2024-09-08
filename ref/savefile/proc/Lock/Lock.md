[]{#/savefile/proc/Lock}
## Lock proc (savefile)
**See also:**
:   [New proc (savefile)](#/savefile/proc/New)
:   [Unlock proc (savefile)](#/savefile/proc/Unlock)
<!-- -->
**Format:**
:   Lock(timeout)
<!-- -->
**Args:**
:   timeout: seconds to wait; -1 for no timeout
<!-- -->
**Returns:**
:   1 on success; 0 on failure
In order to modify a savefile, exclusive access to the file must be
guaranteed, so that other processes reading or writing to the file do
not experience data corruption. This is known as \"locking\" the file.
While the file is locked, only the world that obtained the lock may
access it.
Normally, you do not need to worry about this, because a lock is
automatically obtained upon the first attempt to write to the file. In a
CGI application, where many instances of the program might be running
simultaneously, the normal locking, which just tries once and crashes
the proc on failure, would not be ideal.
Explicitly calling Lock() allows you to specify a timeout and it also
allows you to handle the case in which no lock could be obtained. If you
want it to wait indefinitely, use -1. Just be careful if there are
several files read by multiple processes that it is not possible for
deadlock to occur.
Obtaining a lock will fail if the file is locked by another world or if
it is even open by any other world.
If you are using Lock(), then you probably also want to specify a
timeout when you open the savefile, since that too can fail due to the
file being locked by another process.