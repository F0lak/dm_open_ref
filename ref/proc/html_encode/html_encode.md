[]{#/proc/html_encode}
  ## html_encode proc
  **See also:**
  :   [html_decode proc](ref/proc/html_decode)
  <!-- -->
  **Format:**
  :   html_encode(PlainText)
  <!-- -->
  **Args:**
  :   PlainText: text to be html \"escaped\"
  <!-- -->
  **Returns:**
  :   escaped text
  Special characters such as \< and \> are not displayed literally in html
  and may produce garbled output. If you want to ensure that an entire
  text string is displayed literally, you can \"escape\" those characters.
  For example, \< is produced by the code `&lt;` and \> is produced by the
  code `&gt;`.
  The `html_encode()` instruction does this for you automatically. If you
  wanted to disallow html input from players, you could use this to force
  their text to be displayed literally:
  ### Example:
  mob/verb/say(T as text) view() \<\< \"\[usr\] says,
  \'\[html_encode(T)\]\'\"
  If a URL is included in the text, special characters like & that are
  part of the URL will be skipped. This keeps automatically created links
  in the output from being broken.
  Note for BYOND oldies: the old-style formatting codes such as \"\\red\"
  which are still parsed but not encouraged are completely stripped out by
  html_encode().