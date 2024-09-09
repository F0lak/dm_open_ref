[]{#/proc/num2text}
  ## num2text proc
  **See also:**
  :   [isnum proc](ref/proc/isnum)
  :   [text2num proc](ref/proc/text2num)
  <!-- -->
  **Format:**
  :   num2text(N, SigFig=6)
  :   num2text(N, Digits, Radix)
  <!-- -->
  **Returns:**
  :   A text string.
  <!-- -->
  **Args:**
  :   N: A number.
  :   SigFig: Number of significant digits.
  :   Digits: Minimum number of digits
  :   Radix: The base of the number, e.g. 16 is hexadecimal.
  Get the text string for a number. The number of significant digits
  determines when scientific notation is used. The default is 6, so
  scientific notation will only be used when there are more than 6 digits.
  ### Example:
  T = num2text(12) // = \"12\" T = num2text(12,1) // = \"1.2e1\"
  The Radix format is intended for converting numbers to bases other than
  10, although you can still use 10. In this format, Digits represents the
  minimum number of digits to use, and the result will be left-padded with
  zeroes if necessary. Also, in this form only the integer part of the
  number is used, and it can\'t be any larger than what a 32-bit integer
  could store (about 4 billion). These limitations may be lessened or
  removed in the future, but this format was mainly intended for simple
  conversions.
  ### Example:
  world \<\< num2text(11, 2, 16) // \"0b\" world \<\< num2text(343, 0, 7)
  // \"1000\"