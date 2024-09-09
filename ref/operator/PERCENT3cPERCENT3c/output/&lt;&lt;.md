[]{#/operator/%3c%3c/output}
  ## \<\< output operator
  **See also:**
  :   [\<\< operator (savefile)](ref/savefile/operator/%3c%3c)
  :   [output proc](ref/proc/output)
  :   [browse proc](ref/proc/browse)
  :   [browse_rsc proc](ref/proc/browse_rsc)
  :   [file proc](ref/proc/file)
  :   [ftp proc](ref/proc/ftp)
  :   [image proc](ref/proc/image)
  :   [link proc](ref/proc/link)
  :   [load_resource proc](ref/proc/load_resource)
  :   [run proc](ref/proc/run)
  :   [sound proc](ref/proc/sound)
  <!-- -->
  **Format:**
  :   A \<\< B
  Cause the value B to be output to any players connected to mobs
  specified in A.
  B may be an image, sound, or text. A may be a mob, the whole world, or
  any list containing mobs.
  ### Example:
  usr \<\< \"Hi, \[usr.name\]\" view() \<\< \"To all in view\" world \<\<
  \"Hi everybody!\" usr \<\< \'giggle.wav\' view() \<\<
  image(/obj/Fireball,usr)