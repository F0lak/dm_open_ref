[]{#/savefile/proc/Unlock}
## Unlock proc (savefile)
**See also:**
:   [Lock proc (savefile)](#/savefile/proc/Lock)
:   [New proc (savefile)](#/savefile/proc/New)
<!-- -->
**Format:**
:   Unlock()
Exclusive locks are automatically released when the savefile is closed,
but if you want to keep reading the file and allow other processes to do
the same, then you can explicitly unlock it.
Note that this does not allow other processes to lock the file. It only
allows them to read from it. As long as the file is open by more than
one process, no lock may be obtained.