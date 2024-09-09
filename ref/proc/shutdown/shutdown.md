[]{#/proc/shutdown}
  ## shutdown proc
  **See also:**
  :   [Export proc (world)](ref/world/proc/Export)
  :   [startup proc](ref/proc/startup)
  <!-- -->
  **Format:**
  :   shutdown(Addr,Natural=0)
  <!-- -->
  **Args:**
  :   Addr: This is the address of the child world returned by startup().
  :   Natural: Specifies whether to wait for the child world to die
      naturally, or whether it should be killed with the \"Del\" world
      topic. The default value of 0 kills the child, and a value of 1
      waits for the child to exit of its own accord.
  If no address is specified, the current world is shut down.