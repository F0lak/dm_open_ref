# HTML colors

Text colors may be specified by name or RGB value. The RGB
color format uses hexadecimal numbers, with 2 hex digits each for red,
green, and blue. These range from 0 (00 in hex) to 255 (FF in hex). In
certain situations BYOND will also honor a fourth pair of digits for
alpha.
  -  #rrggbb
  -  #rrggbbaa

It is also possible to use 4 bit values by using only one hex
digit per color. The full 8 bit color is produced by repeating each
digit. For example, `#F00` (red) is the same as `#FF0000`. 

The named colors supported by BYOND, and their corresponding RGB values,
are listed in the following table:
| Colour | Code | Example |
| :------ | ------| ----- |
| black                  | #000000   | <span style="color:black">Example</span> <span style="background-color:white; color:black">Example</span> <span style="background-color:black; color:black">Example</span>|
| silver                 | #C0C0C0   |  <span style="color:silver">Example</span> <span style="background-color:white; color:silver">Example</span> <span style="background-color:black; color:silver">Example</span>|
| gray *or* grey         | #808080   |  <span style="color:gray">Example</span> <span style="background-color:white; color:gray">Example</span> <span style="background-color:black; color:gray">Example</span>|
| white                  | #FFFFFF   |  <span style="color:white">Example</span> <span style="background-color:white; color:white">Example</span> <span style="background-color:black; color:white">Example</span>|
| maroon                 | #800000   |  <span style="color:maroon">Example</span> <span style="background-color:white; color:maroon">Example</span> <span style="background-color:black; color:maroon">Example</span>|
| red                    | #FF0000   |  <span style="color:red">Example</span> <span style="background-color:white; color:red">Example</span> <span style="background-color:black; color:red">Example</span>|
| purple                 | #800080   |  <span style="color:purple">Example</span> <span style="background-color:white; color:blpurpleack">Example</span> <span style="background-color:black; color:purple">Example</span>|
| fuchsia *or* magenta   | #FF00FF   |  <span style="color:fuchsia">Example</span> <span style="background-color:white; color:fuchsia">Example</span> <span style="background-color:black; color:fuchsia">Example</span>|
| green                  | #00C000   |  <span style="color:green">Example</span> <span style="background-color:white; color:green">Example</span> <span style="background-color:black; color:green">Example</span>|
| lime                   | #00FF00   |  <span style="color:lime">Example</span> <span style="background-color:white; color:lime">Example</span> <span style="background-color:black; color:lime">Example</span>|
| olive *or* gold        | #808000   |  <span style="color:olive">Example</span> <span style="background-color:white; color:olive">Example</span> <span style="background-color:black; color:olive">Example</span>|
| yellow                 | #FFFF00   |  <span style="color:yellow">Example</span> <span style="background-color:white; color:yellow">Example</span> <span style="background-color:black; color:yellow">Example</span>|
| navy                   | #000080   |  <span style="color:navy">Example</span> <span style="background-color:white; color:navy">Example</span> <span style="background-color:black; color:navy">Example</span>|
| blue                   | #0000FF   |  <span style="color:blue">Example</span> <span style="background-color:white; color:blue">Example</span> <span style="background-color:black; color:blue">Example</span>|
| teal                   | #008080   |  <span style="color:teal">Example</span> <span style="background-color:white; color:teal">Example</span> <span style="background-color:black; color:teal">Example</span>|
| aqua *or* cyan         | #00FFFF   |  <span style="color:aqua">Example</span> <span style="background-color:white; color:aqua">Example</span> <span style="background-color:black; color:aqua">Example</span>|
---------------------- --------- --

> [!TIP] 
> **See also:**
> +   [rgb proc](/ref/proc/rgb.md) 