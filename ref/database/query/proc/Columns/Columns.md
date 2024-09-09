[]{#/database/query/proc/Columns}
  ## Columns proc (database query) {#columns-proc-database-query byondver="506"}
  **See also:**
  :   [database query datum](ref/database/query)
  :   [Execute proc (database query)](ref/database/query/proc/Execute)
  :   [GetColumn proc (database query)](ref/database/query/proc/GetColumn)
  :   [GetRowData proc (database query)](ref/database/query/proc/GetRowData)
  :   [NextRow proc (database query)](ref/database/query/proc/NextRow)
  <!-- -->
  **Format:**
  :   Columns()\
      *or*\
      Columns(column)
  <!-- -->
  **Args:**
  :   column: The Nth column whose name should be read
  Returns a list of column names for the current query, or the name of the
  Nth column.
  You must call Execute() before calling Columns().