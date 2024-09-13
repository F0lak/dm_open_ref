# settings (proc)


proc settings:
    verb/set
      name
      desc
      category
      hidden
      popup_menu
      instant
      invisibility
      src
      background
      waitfor


Procs and verbs are the same \"type\" so these attributes may
be set for both procs and verbs; most of them only apply to verbs, so
they only take effect if the proc is invoked as a verb (by adding it to
a verb list).