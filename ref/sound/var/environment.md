
## environment (var)

**Default Value:**
+   -1
***
Changes the environmental reverb for all 3D sounds until another environment is specified. Only 3D sounds react to the environment. Please see the EAX2 documentation at http://developer.creative.com/ for detailed information about these settings.

This value may be a number which selects a preset, or a list to choose settings manually. The default value (-1) specifies no change in environment. A numeric value from 0 to 25 specifies a set of reverb presets for the environment. The environment presets are:

As of BYOND 515, setting environment to a negative number below -1 will turn the environment off. The generic environment is not the same as off.

A 23-element list represents a custom environment with the following reverbration settings. A null or non-numeric value for any setting will select its default.
***
**Related Pages:**
+    [vars (sound)](/ref/sound/var)
+    [x, y, or z](/ref/sound/var/xyz)
+    [atom-linked](/ref/sound/var/atom)
+    [echo var (sound)](/ref/sound/var/echo)
