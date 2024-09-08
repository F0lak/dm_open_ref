[]{#/verb/set/src}
## src setting (verb)
**Format:**
:   set src in List
:   set src = List
<!-- -->
**Args:**
:   List: One of view(), oview(), world, world.contents, usr,
    usr.contents, usr.loc, or usr.group
With the first format, if src is in List for a particular player, then
that player will have access to the proc. The player must explicitly
specify the name of the source on the command line.
The second format behaves the same, except the source is not read from
the command line. If more than one possible source exists, one will be
chosen at random.
When usr or world is specified for the first format, it will be expanded
to usr.contents and world.contents respectively.
The default setting depends on the type of src: mob: src = usr obj: src
in usr // short for usr.contents turf: src = view(0) area: src = view(0)
### Example:
obj/verb/examine() set src in view() usr \<\< \"You examine \[src\].\"
### Example:
obj/MagicCloak/verb/disappear() set src = usr.contents usr.invisibility
= 1 view() \<\< \"\[usr\] disappears!\"