## environment var (sound)

**Default value:**
+   -1


Changes the environmental reverb for all 3D sounds until
another environment is specified. Only 3D sounds react to the
environment. Please see the EAX2 documentation at
http://developer.creative.com/ for detailed information about these
settings. 

This value may be a number which selects a preset, or
a list to choose settings manually. The default value (-1) specifies no
change in environment. A numeric value from 0 to 25 specifies a set of
reverb presets for the environment. The environment presets are:
0.  generic
1.  padded cell
2.  room
3.  bathroom
4.  livingroom
5.  stoneroom
6.  auditorium
7.  concert hall
8.  cave
9.  arena
10. hangar
11. carpeted hallway
12. hallway
13. stone corridor
14. alley
15. forest
16. city
17. mountains
18. quarry
19. plain
20. parking lot
21. sewer pipe
22. underwater
23. drugged
24. dizzy
25. psychotic


As of BYOND 515, setting environment to a negative number below
-1 will turn the environment off. The generic environment is not the
same as off. 

A 23-element list represents a custom environment
with the following reverbration settings. A null or non-numeric value
for any setting will select its default.
1 EnvSize (1.0 to 100.0) default = 7.5
+   environment size in meters
2 EnvDiffusion (0.0 to 1.0) default = 1.0
+   environment diffusion
3 Room (-10000 to 0) default = -1000
+   room effect level (at mid frequencies)
4 RoomHF (-10000 to 0) default = -100
+   relative room effect level at high frequencies
5 RoomLF (-10000 to 0) default = 0
+   relative room effect level at low frequencies
6 DecayTime (0.1 to 20.0) default = 1.49
+   reverberation decay time at mid frequencies
7 DecayHFRatio (0.1 to 2.0) default = 0.83
+   high-frequency to mid-frequency decay time ratio
8 DecayLFRatio (0.1 to 2.0) default = 1.0
+   low-frequency to mid-frequency decay time ratio
9 Reflections (-10000 to 1000) default = -2602
+   early reflections level relative to room effect
10 ReflectionsDelay (0.0 to 0.3) default = 0.007
+   initial reflection delay time
11 Reverb (-10000 to 2000) default = 200
+   late reverberation level relative to room effect
12 ReverbDelay (0.0 to 0.1) default = 0.011
+   late reverberation delay time relative to initial reflection
13 EchoTime (0.075 to 0.250) default = 0.25
+   echo time
14 EchoDepth (0.0 to 1.0) default = 0.0
+   echo depth
15 ModulationTime (0.04 to 4.0) default = 0.25
+   modulation time
16 ModulationDepth (0.0 to 1.0) default = 0.0
+   modulation depth
17 AirAbsorptionHF (-100 to 0.0) default = -5.0
+   change in level per meter at high frequencies
18 HFReference (1000.0 to 20000) default = 5000.0
+   reference high frequency (hz)
19 LFReference (20.0 to 1000.0) default = 250.0
+   reference low frequency (hz)
20 RoomRolloffFactor (0.0 to 10.0) default = 0.0
+   like rolloffscale in System::set3DSettings but for reverb room size
    effect
21 Diffusion (0.0 to 100.0) default = 100.0
+   Value that controls the echo density in the late reverberation
    decay.
22 Density (0.0 to 100.0) default = 100.0
+   Value that controls the modal density in the late reverberation
    decay
23 Flags default = 63
+   Bit flags that modify the behavior of above properties
    -   1 - \'EnvSize\' affects reverberation decay time
    -   2 - \'EnvSize\' affects reflection level
    -   4 - \'EnvSize\' affects initial reflection delay time
    -   8 - \'EnvSize\' affects reflections level
    -   16 - \'EnvSize\' affects late reverberation delay time
    -   32 - AirAbsorptionHF affects DecayHFRatio
    -   64 - \'EnvSize\' affects echo time
    -   128 - \'EnvSize\' affects modulation time

> [!TIP] 
> **See also:**
> +   [vars (sound)](/ref/sound/var.md) 
> +   [x, y, z vars (sound)](/ref/sound/var/xyz.md) 
> +   [echo var (sound)](/ref/sound/var/echo.md) <!-- -->