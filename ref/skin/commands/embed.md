
## embed (info)
***
Commands that are initiated by the skin (like button.command, map.on-show, etc.) have a special syntax that allows you to include information that would normally require a winget call. By including `[[*something*]]` in the command, the double-bracketed text will be replaced by the result of running a winget on that parameter.

A value of `[[id.parameter]]` will run a winget on the control with the given ID. Just using `[[parameter]]` will run a winget for the control that initiated this command. You can also use `parent` in place of the ID to do something with the parent of the control, or `parent.id` for access to a sibling control. Position and size parameters can be further broken down by appending `.x` or `.y` to get at the numbers directly.

Several commands already support some special cases like `[[*]]` or `[[width]]` or such, where the special-case values are relevant to the command. An example is that in `on-size` the value of `[[*]]` is a size value. The Any macro, gamepad macros, and mouse macros, also support this syntax; see <a href="#/{skin}/macros">macros</a> for more info.

You can choose how embedded wingets get formatted by following the value with `as` and a type, such as `[[window.size as string]]`. There are several types you can use, and different types of parameters get formatted differently:

The `arg` type is the default, unless the `[[`*...*`]]` expression has double quotes on both sides, in which case `escaped` is the default.
***