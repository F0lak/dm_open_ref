
## dpi (info)
***
Read-only and unlisted parameter that returns the DPI scaling factor. A value of 1 indicates 100%. This is currently system-wide for the whole application and won't vary by window, but is implemented for windows in case future scaling changes allow them to differ.

This is also a special global parameter. Calling <a class="code" href="#/proc/winget">winget()</a> with no `id` and `dpi` as the parameter will return the system DPI scaling.

Note: The DPI scale is currently set at the time Dream Seeker starts, and does not change after that.
***