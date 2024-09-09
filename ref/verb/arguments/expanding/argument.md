[]{#/verb/arguments/expanding}
  ## argument expanding
  **See also:**
  :   [arguments (verb)](ref/verb/arguments)
  The expression used to to provide a list of possible values for a verb
  argument may reference the value of arguments prior to the one being
  expanded. It may even reference the value of the argument being
  expanded, but this will always be a text string equal to what the user
  has typed so far.
  In addition, there is a special variable called \"expanding\" which is
  only accessible in this context. It is 1 if the user\'s input is being
  expanded and 0 if the user\'s final input is being validated. In certain
  rare cases, you may wish to tell the difference between these two cases.
  For example, you could use this to have possible values which do not
  show up in the expansion lists, but which are accepted when typed in
  full.
  ### Example:
  mob/verb/test(A in MyProc(A,expanding)) usr \<\< \"You typed: \[A\]\"
  proc/MyProc(A,expanding) var/values\[\] =
  list(\"one\",\"two\",\"three\") if(!expanding) values += \"secret\"
  return values