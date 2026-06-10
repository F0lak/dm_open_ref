
## control_freak (var)

**Default Value:**
+   0
***
This var lets you set flags to turn off options that are normally present for the end user. You can combine these flags with the `|` operator. The value 1 is equivalent to `CONTROL_FREAK_ALL` and will disable everything.

Using `CONTROL_FREAK_ALL` will default to disabling everything, and the other flags will reenable only the features you want. For example, `CONTROL_FREAK_MACROS` alone will disable the ability to use your own macros but nothing else. `CONTROL_FREAK_ALL | CONTROL_FREAK_MACROS` will disable everything *except* macros.

This value can be changed at runtime.

Note: If you define your own skin for the world, and disable the ability to use a custom skin or user-defined macros, you must be sure to define any macros your world may need. For instance, arrow keys may be needed for movement.
***
**Related Pages:**
+    [User interface skins](/ref/{skin})
+    [macros (skin)](/ref/{skin}/macros)
+    [macros (client script)](/ref/client/var/script/macro)
