[]{#/DM/preprocessor/__PROC__}
  ## \_\_PROC\_\_ macro {#proc__-macro byondver="515"}
  **See also:**
  :   [\_\_FILE\_\_ macro](ref/DM/preprocessor/__FILE__)
  :   [\_\_LINE\_\_ macro](ref/DM/preprocessor/__LINE__)
  :   [\_\_TYPE\_\_ macro](ref/DM/preprocessor/__TYPE__)
  :   [\_\_IMPLIED_TYPE\_\_ macro](ref/DM/preprocessor/__IMPLIED_TYPE__)
  The `__PROC__` macro is replaced by a reference to the current proc
  being compiled. This may be useful when generating debugging error
  messages, especially when wrapped in `nameof`, e.g. `nameof(__PROC__)`.
  This is actually a pseudo-macro; the preprocessor doesn\'t handle it
  directly.