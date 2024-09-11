## control_freak (client)
**See also:**
*   [User interface skins](/ref/%7Bskin%7D.md) -m
*   [macros (skin)](/ref/%7Bskin%7D/macros.md) -m
*   [macros (client script)](/ref/client/var/script/macro.md) -m<!-- -->
**Default value:**
*   0


This var lets you set flags to turn off options that are
normally present for the end user. You can combine these flags with the
`|` operator. The value 1 is equivalent to `CONTROL_FREAK_ALL` and will
disable everything.
CONTROL_FREAK_ALL
*   If this value is used, it affects all the options below.
    -   User-defined macros may not be used.
    -   Only the world\'s skin or the default BYOND skin will be loaded,
        not a user-customized version.
    -   The Options & Messages window in Dream Seeker is inaccessible.
        It will only come up while first connecting to a remotely hosted
        world, or if a world takes a long time to load. The .options
        command will not make it appear.
    -   The menu items from Options & Messages are unavailable in Dream
        Seeker\'s system menu.
    -   The default F2 macro for the .screenshot command is turned off.
        The command is then only accessible through the skin you create.
CONTROL_FREAK_SKIN
*   Toggles the ability to create a custom version of the skin.
CONTROL_FREAK_MACROS
*   Toggles the ability to use and define custom macros.


Using `CONTROL_FREAK_ALL` will default to disabling everything,
and the other flags will reenable only the features you want. For
example, `CONTROL_FREAK_MACROS` alone will disable the ability to use
your own macros but nothing else.
`CONTROL_FREAK_ALL | CONTROL_FREAK_MACROS` will disable everything
*except* macros. 

This value can be changed at runtime.


Note* If you define your own skin for the world, and disable
the ability to use a custom skin or user-defined macros, you must be
sure to define any macros your world may need. For instance, arrow keys
may be needed for movement.