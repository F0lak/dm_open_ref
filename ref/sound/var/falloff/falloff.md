[]{#/sound/var/falloff}
  ## falloff var (sound)
  **See also:**
  :   [vars (sound)](ref/sound/var)
  :   [x, y, z vars (sound)](ref/sound/var/xyz)
  <!-- -->
  **Default value:**
  :   1
  Within the falloff distance a 3D sound stays at the constant loudest
  volume possible. Outside of this distance it attenuates at a rate
  determined by the falloff.
  Higher values will make sounds fade out more slowly as they get farther
  away. The distance of a sound is set by `x`, `y`, and `z`.