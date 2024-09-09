[]{#/proc/winclone}
  ## winclone proc
  **See also:**
  :   [winexists proc](ref/proc/winexists)
  :   [winget proc](ref/proc/winget)
  :   [winset proc](ref/proc/winset)
  :   [winshow proc](ref/proc/winshow)
  :   [User interface skins](ref/%7Bskin%7D)
  <!-- -->
  **Format:**
  :   winclone(player, window_name, clone_name)
  <!-- -->
  **Args:**
  :   player: A mob or client.
  :   window_name: The name of a window, pane, menu, or macro set in the
      world\'s skin file.
  :   clone_name: The name of the new window, pane, menu, or macro set to
      create.
  Creates a clone of a window, pane, menu, or macro set that exists in the
  world\'s skin file. The original object as it exists in the skin file
  (not its current state) is used as a template to build the clone. The
  clone will exist only for the player you choose.
  ### Example:
  winset(usr, \"templatewindow\", \"clonedwindow\")
  If a window is not visible by default, it will have to be shown with
  `winset()` or `winshow()`. A pane may be shown by using it in a Child or
  Tab control. Menus or macros must be assigned to a window with
  `winset()` before they will work.
  If window_name is \"window\", \"pane\", \"menu\", or \"macro\", and the
  skin file does not have a control of that name already, the proc will
  create a new control of that type from scratch.
  ### Example:
  winclone(usr, \"menu\", \"newmenu\") winset(usr, \"newmenu_file\",
  \"parent=newmenu;name=File\") winset(usr, \"newmenu_quit\",
  \"parent=newmenu_file;name=Quit;command=.quit\")
  A new window is invisible by default. For windows and panes, you should
  give them a size with `winset()` before adding any controls so you can
  set their anchors properly.
  ### Example:
  // Create the pane winclone(usr, \"pane\", \"newpane\") // Give it a
  size so we can figure out where to put controls winset(usr, \"newpane\",
  \"size=100x100\") // Add controls winset(usr, \"newpane_label\", \\
  \"parent=newpane;pos=0,0;size=100x100;anchor1=0,0;anchor2=100,100\") //
  Put the pane in a child control where it can be seen winset(usr,
  \"a_child\", \"left=newpane\") usr \<\< output(\"New label\",
  \"newpane_label\")
  Once a clone is created, it can be deleted via a `winset()` call:
  ### Example:
  winset(usr, \"clonedwindow\", \"parent=none\")