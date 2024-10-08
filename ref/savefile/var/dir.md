## dir list var (savefile)


The name of each child directory of the current data directory
is stored in the list savefile.dir. New directories may be created with
savefile.dir.Add() and removed with savefile.dir.Remove(). To test for
the existence of a directory, use savefile.dir.Find(). (Note that these
are *database* directories inside the savefile---not real directories on
the filesystem.) 

The order of directories is not necessarily
preserved, so do not assume, for example, that newer directories will be
at the end of the list.

> [!TIP] 
> **See also:**
> +   [list](/ref/list.md) 
> +   [savefile](/ref/savefile.md) 