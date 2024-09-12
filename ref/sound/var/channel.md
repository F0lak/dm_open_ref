## channel var (sound)

**Default value:**
+   0 (any channel)


For sound effects, set to 1 through 1024 to choose a specific
sound channel. For values of 0 or less, any available channel will be
chosen. If you play a null sound (no file) on channel 0, the settings
for the datum will affect all channels. 

If you want to make any
changes to your sound later on via the `SOUND_UPDATE` status flag, you
*must* specify a channel for it. 

This var may be filled in by
the `SoundQuery` proc, but only for sounds that had a specified channel
to begin with.
Note: If you don\'t specify a channel to play a sound, the client will
choose a channel automatically but it will *not* conflict with any
specific channels you choose for other sounds later. This means if you
play some sounds with channel 0 but then later want to play something on
channel 1, you don\'t have to worry about channel 1 being taken.

**See also:**
+   [sound proc](/ref/proc/sound.md) 
+   [status var (sound)](/ref/sound/var/status.md) 
+   [vars (sound)](/ref/sound/var.md) 
+   [SoundQuery proc (client)](/ref/client/proc/SoundQuery.md) <!-- -->