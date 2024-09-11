## cmptext proc
**See also:**
*   [cmptextEx proc](/ref/proc/cmptextEx.md) -m<!-- -->
**Format:**
*   cmptext(T1,T2,\...)
<!-- -->
**Returns:**
*   1 if all arguments are equal; 0 otherwise.
<!-- -->
**Args:**
*   Any number of text strings to compare.


This instruction is NOT sensitive to case. It also ignores the
`\proper` and `\improper` text macros. The case-sensitive version is
cmptextEx().
### Example:

```
 if(cmptext(\"Hi\",\"HI\")) world \<\< \"Equal!\" else world
\<\< \"Not equal!\" 
```
 

This outputs \"Equal!\" since
\"Hi\" and \"HI\" are the same, ignoring case.