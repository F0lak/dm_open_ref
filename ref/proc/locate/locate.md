[]{#/proc/locate}
  ## locate proc
  **See also:**
  :   [istype proc](ref/proc/istype)
  :   [tag var (datum)](ref/datum/var/tag)
  :   [\_\_IMPLIED_TYPE\_\_ macro](ref/DM/preprocessor/__IMPLIED_TYPE__)
  <!-- -->
  **Format:**
  :   locate(Type) in Container
  :   locate(X,Y,Z)
  :   locate(Tag)
  :   locate(TextRef)
  <!-- -->
  **Returns:**
  :   An object of the specified type or the turf at the given
      coordinates. If a text string is given in place of an object type,
      the object with the same tag is found. If a container is given, only
      objects directly within that object are searched.
  <!-- -->
  **Args:**
  :   Type: An object prototype or tag. If locate() is being used in an
      assignment to a variable with a declared type, this argument is
      optional and will default to the type of the variable being
      assigned.
  :   Container: An optional container object. (The default is `world`.)
  :   X,Y,Z: A set of numerical coordinates.
  :   Tag: The value of an object\'s tag variable (must be unique).
  :   TextRef: An embedded object reference created by the \\ref text
      macro.
  Types are matched in the same manner as istype(). In other words,
  locate(/obj) could return an instance of something derived from /obj,
  such as /obj/armor.
  If there is more than one instance of the specified type, the first one
  found will be chosen.
  ### Example:
  var/mob/shopkeeper/M = locate() if(M) usr \<\< \"Found the shopkeeper.\"
  else usr \<\< \"Could not find the shopkeeper.\"
  This looks for a mob of a type /mob/shopkeeper in the world
  (world.contents).
  ### Example:
  usr.Move(locate(/turf/Home))
  This \"teleports\" the usr to a turf of the type /turf/Home.
  ### Example:
  usr.Move(locate(1,2,3))
  This moves the usr to the turf at coordinates (x,y,z) = (1,2,3).