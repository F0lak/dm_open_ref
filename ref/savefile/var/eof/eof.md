[]{#/savefile/var/eof}
## eof var (savefile)
If there is more data to read in the current buffer, eof is 0; otherwise
it is 1. Setting eof to 1 moves to the end of the buffer and 0 moves to
the beginning. Setting it to -1 deletes the current buffer.