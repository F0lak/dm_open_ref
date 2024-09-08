[]{#/sound/var/echo}
## echo var (sound)
**See also:**
:   [vars (sound)](#/sound/var)
:   [x, y, z vars (sound)](#/sound/var/xyz)
:   [environment var (sound)](#/sound/var/environment)
<!-- -->
**Default value:**
:   null
If set to an 18-element list, this value customizes reverbration
settings for this sound only. A null or non-numeric value for any
setting will select its default. Please see the EAX2 documentation at
http://developer.creative.com/ for indepth information about these
settings.
Here\'s a rundown of some of the terms: **Direct** refers to the amount
of effect when the sound is on a direct path to the listener.
**Obstruction** is when an object is blocking the direct path but there
are other ways for the sound to reach the listener. **Occlusion** means
the sound is on the other side of a wall, and mostly blocked.
**Exclusion** means the sound is on the other side of a wall, but a
doorway or window is allowing it to pass through to the listener. You
can use a little of each of these effects to increase realism.
1 Direct (-10,000 to 1,000) default = 0
:   direct path level (at low and mid frequencies)
2 DirectHF (-10,000 to 0) default = 0
:   relative direct path level at high frequencies
3 Room (-10,000 to 1,000) default = 0
:   room effect level (at low and mid frequencies)
4 Room HF (-10,000 to 0) default = 0
:   relative room effect level at high frequencies
5 Obstruction (-10,000 to 0) default = 0
:   main obstruction control (attenuation at high frequencies)
6 ObstructionLFRatio (0.0 to 1.0) default = 0.0
:   obstruction low-frequency level re. main control
7 Occlusion (-10,000 to 0) default = 0
:   main occlusion control (attenuation at high frequencies)
8 OcclusionLFRatio (0.0 to 1.0) default = 0.25
:   occlusion low-frequency level re. main control
9 OcclusionRoomRatio (0.0 to 10.0) default = 1.5
:   relative occlusion control for room effect
10 OcclusionDirectRatio (0.0 to 10.0) default = 1.0
:   relative occlusion control for direct path
11 Exclusion (-10,000 to 0) default = 0
:   main exlusion control (attenuation at high frequencies)
12 ExclusionLFRatio (0.0 to 1.0) default = 1.0
:   exclusion low-frequency level re. main control
13 OutsideVolumeHF (-10,000 to 0) default = 0
:   outside sound cone level at high frequencies
14 DopplerFactor (0.0 to 10.0) default = 0.0
:   like DS3D flDopplerFactor but per source
15 RolloffFactor (0.0 to 10.0) default = 0.0
:   like DS3D flRolloffFactor but per source
16 RoomRolloffFactor (0.0 to 10.0) default = 0.0
:   like DS3D flRolloffFactor but for room effect
17 AirAbsorptionFactor (0.0 to 10.0) default = 1.0
:   multiplies AirAbsorptionHF member of environment reverb properties.
18 Flags default = 7
:   Bit flags that modify the behavior of properties
    -   1 - Automatic setting of \'Direct\' due to distance from
        listener
    -   2 - Automatic setting of \'Room\' due to distance from listener
    -   4 - Automatic setting of \'RoomHF\' due to distance from
        listener