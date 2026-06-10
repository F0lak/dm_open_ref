
## Unicode (info)
***
BYOND was originally written to handle 8-bit ("ANSI") characters only. However as time has marched on, Unicode has become ubiquitous for supporting multiple languages, special characters, and emojis. To adapt to this, BYOND now supports Unicode.

When ANSI was king, every character was exactly one byte in width, because the only valid characters were between 1 and 255. (And technically, BYOND reserved 255 for its own use.) Now, BYOND uses an encoding called UTF-8 to store characters that can't fit in one byte.

UTF-8 breaks up characters with codes of 128 or higher into multiple bytes, like so:
***