## style sheets



HTML tags, such as `<font>` may be used to directly format
output text. Another approach, however, is to use HTML tags to specify
purely structural information and use a style sheet to define how
various elements within that structure should be treated. DM uses a
[subset of the Cascading Style Sheet (CSS)
language](/ref/%7B%7Bappendix%7D%7D/css.md) , which was introduced for this
purpose in HTML documents. 

This section discusses the syntax of
style sheets as an independent element. For information on how to
include the style sheets in your DM code, see the section on
[client.script](/ref/client/var/script.md) . 

As an example of a
style sheet, one might want combat and conversational messages to appear
differently---perhaps using different colors. Instead of using the
`<font>` tag to color the text, you could use `<span>` to mark the
beginning and ending of the text and to specify what kind of message it
is. The result might be text such as the following: 
``` dm

\"\[usr\] [spanks]{.combat} \[targ\]!\" \"\[usr\] says,
\'[\[msg\]]{.chat}\'\" 
```
 

The `class` attribute may be
used with any tag, but `span` and `div` are often convenient because
they have no other side-effect but defining the style class. `span` is
for text within a single paragraph and `div` is for whole paragraphs.
The way text belonging to a particular class is formatted may be
controlled in a style sheet such as the following: 
``` dm
 .combat
{color: red} .chat {color: green} 
```
 

This says that
text in the `combat` class should be colored red and text in the `chat`
class should be colored green. These classes are not pre-defined; you
can create whatever new style classes you need. (The color names are
predefined however. You can find a list of them in [HTML
colors](/ref/%7B%7Bappendix%7D%7D/html-colors.md) . 

The advantage of
using style sheets instead of direct formatting tags is that you can
cleanly separate structural information (such as combat and
conversational messages) from formatting information (such as red and
green text). By separating the two, you or the player can easily plug in
different formatting schemes without changing any of the actual content.


A style sheet is composed of a list of rules, such as the two
rules in the preceding example. Each rule contains one or more
*selectors* followed by a body of attribute assignments (in braces). The
selector specifies the context of the rule and the body specifies the
format. 

A selector may specify a container tag (such as `span`,
`body`, or `p`) and a class. The above example could have been written
with a selector of `span.chat`. However, by leaving out the tag, it
applies to any tag with `class=chat`. It is also possible to only
specify the tag and not the class. In that case, the selector applies to
any matching tag, regardless of class. 

To specify a *nested*
context, several simple selectors may be listed one after the other. For
example, emphasized text within a combat message could be enlarged with
the following rule: 
``` dm
 .combat em {font-size: larger}

```
 

It is also possible to list several selectors
separated by commas in order to make them all apply to the same body.
For example, this next rule is equivalent to the two following ones:

``` dm
 .combat em, .chat em {font-size: larger} .combat em
{font-size: larger} .chat em {font-size: larger} 
```
 

The
style rule body contains a list of attribute assignments, delimited by
semicolons. Each assignment takes the form of an attribute name,
followed by a colon, followed by the value of the attribute. The
following table summarizes the recognized attributes and their possible
values.
color
#F00, #FF0000, red, rgb(255,0,0), rgb(100%,0%,0%)
background
font-size
10pt, 1.5em, 150%
font-style
normal or italic
font-weight
normal, bold, lighter, darker, or 100 to 900
font-family
monospace, sans-serif, serif, cursive, \...
font
*style weight size family*
text-decoration
none, underline
text-align
right, left, or center
vertical-align
top, middle, bottom
text-indent
0.25in, 3em, 20pt
margin-left
margin-right
width
16px, 32px, auto
height
line-height
1.2
### fonts


The `font` attribute is a special short-hand for assigning
`font-size`, `font-style`, `font-weight`, and `font-family` in one
statement. Any properties that are not specified in the `font` statement
are assigned to their default values. 

The font family may be a
specific font name or a more general category such as monospace or
sans-serif. Since not all users necessarily have the same fonts
installed, it is a good idea to list alternate fonts. The desired font
is placed first, followed by other possible fall-backs, each separated
by a comma. Usually a general family such as monospace is listed last of
all. Any font names containing a space should have quotes around them.


The following example sets the font for the `<body>` tag. Even
if you don\'t explicitly use `<body>` in output text, it is applied
implicitly. 
``` dm
 body {font: 12pt \'Times New Roman\',
sans-serif} 
```
 

This sets the font to 12 point and
selects `Times New Roman` if it is available and otherwise falls back on
a system-determined sans-serif font. This command also implicitly
specifies not to use italics and to use a normal font weight (not bold).


Font sizes may be specified in points (1pt = 1/72 of an inch),
picas (1pc = 12pt), pixels (px), inches (in), centimeters (cm), and
millimeters (mm). There are also various levels corresponding to the old
1 to 7 HTML scale. These are `xx-small`, `x-small`, `small`, `medium`,
`large`, `x-large`, and `xx-large`. In addition to these absolute font
sizes, it is possible to use a relative size, such as 150% or
equivalently 1.5em (1em = 100% of the current font size). This scales
the font relative to the currently active font setting. 

In
addition to regular classes, there are special pseudo-classes for
handling embedded hyperlinks. These are specified in the selector with
the class starting with a colon rather than a dot. They are `:link`,
`:visited`, and `:active`. These only apply to the `<a>` tag. The
`:link` class applies to hyperlinks in their normal state. Once a link
has been clicked, it belongs instead to the `:visited` class. When the
user holds the mouse over a link, it temporarily belongs to the
`:active` class. The only attribute that may change in an active or
visited link is the text color.
### margins and indents


Paragraphs can be given different margins according to your
preferences. The `margin-left` attribute controls the left margin, and
`margin-right` is the right margin. You can use specific sizes like
inches or points, or a relative size unit like em or ex. (A percentage
is interpreted so that 100% is 1em, not the width of the window.) Using
the `text-indent` attribute will indent the first line of a paragraph
from the left margin. It is possible to create a hanging indent by using
a negative value for `text-indent`, like so: 
``` dm
 body
{text-indent: -0.5in; margin-left: 0.5in} 
```

### background colors


The background attribute is only relevant to the `body`
context. It causes the entire terminal background to change color. When
doing this, it is usually necessary to change the foreground colors of
text or it may become unreadable. The various standard classes of output
generated by DreamSeeker are in the following table.
### system colors
system notice
general notices from the client
system command echo
command echoing
system command expansion
command-line expansion list
system pager
pager messages
system irc
IRC command prefix


The value of the CLASS attribute may contain a list of classes
separated by spaces. This permits client output to be in the \'system\'
class as well as more specific ones. That allows you to change all of
these colors in one shot if you are too lazy to change them each
individually. For example, if you define a style sheet that changes the
background color, you might need to redefine the various foreground
colors like this: 
``` dm
 body {background: aqua; color: black}
.system {color: red; font-weight: bold} .command {color: green}

```
 

In this example, the background color of the
terminal will be aqua, normal text from the server will be black, and
all output from the client will be bold and red, except echoed commands
and expansion lists, which will be bold and green. The more specific
.command rule is placed after the general .system rule so that its color
takes precedence. This is how style sheets are composed---you write
general rules first followed by any exceptions.
### style rule precedence


The order in which rules are specified is one of the factors
that determines precedence of style sheet commands. The language is
known as Cascading Style Sheets because of its ability to handle several
layers of stylistic rules, intermingling the configurations of the user
and the designer in an ordered fashion. 

Rules are selected by
first finding all matching candidates for a given attribute in the
current HTML tag being processed. If there is more than one, rules from
a higher level style sheet take precedence over lower level ones. That
means the basic user configurable settings in DreamSeeker are the lowest
priority, followed by a style sheet in the user\'s `.dms` script file,
followed by a style sheet from the designer\'s `client.script` setting,
because that is the order in which these are read by the style sheet
manager. 

Rules from the same style sheet are ordered by
specificity. The selector `span.chat` is more specific than `.chat` and
`.chat em` is more specific than `em`. In general, the more classes
referenced by a selector, the more specific it is. When that results in
a tie, the selector with the greater number of tags takes precedence.


If two rules about the same attribute come from the same sheet
and have the same specificity, the final one to be defined takes
precedence. 

In the rare event that a rule needs to break out of
the normal order of precedence, it can be flagged as important. In this
case it will take precedence over all other \"unimportant\" rules.
However, if more than one rule is important, the normal rules of
precedence will be used to resolve the conflict. 

The important
flag is applied after the attribute assignment like this: 
``` dm

body {background: white ! important; font: serif} 
```
 

In
the above example, only the background color is important, not the font
specification.
### `style` attribute


Style commands may also be inserted directly in an html tag to
control its appearance. This does not have the advantages of style
sheets, which separate content from presentation, but it does allow you
to use the style sheet syntax when formatting text. 

The
following example uses the style attribute to color some text:

``` dm
 usr \<\< \"That [HURT]{style="color: red"}!\" 
```



As you can see, the `style` attribute of any tag can be
assigned to a text string containing a list of attribute assignments.
Just the body of the style rule is given, since no selector is needed to
match the current context.
### Maptext options


The [atom.maptext](/ref/atom/var/maptext.md) var supports some
additional CSS attributes.
vertical-align
top, middle, bottom
text-shadow
*x-offset y-offset blur color*
-dm-text-outline
*width color style*


Additionally, you can use the `:hover` pseudo-class to change
the color of a link. As with other link pseudo-classes, only the text
color can currently be changed.

> [!TIP] 
> **See also:**
> +   [CSS attributes](/ref/%7B%7Bappendix%7D%7D/css.md) 
> +   [entities (text)](/ref/DM/text/entities.md) 
> +   [macros (text)](/ref/DM/text/macros.md) 
> +   [script var (client)](/ref/client/var/script.md) 
> +   [tags (text)](/ref/DM/text/tags.md) 
> +   [text](/ref/DM/text.md) 