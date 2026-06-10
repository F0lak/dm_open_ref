
## style (info)
***
HTML tags, such as <code>&lt;font&gt;</code> may be used to directly format output text. Another approach, however, is to use HTML tags to specify purely structural information and use a style sheet to define how various elements within that structure should be treated. DM uses a <a href="#/{{appendix}}/css">subset of the Cascading Style Sheet (CSS) language</a>, which was introduced for this purpose in HTML documents.

This section discusses the syntax of style sheets as an independent element. For information on how to include the style sheets in your DM code, see the section on <a class="code" href="#/client/var/script">client.script</a>.

As an example of a style sheet, one might want combat and conversational messages to appear differently—perhaps using different colors. Instead of using the <code>&lt;font&gt;</code> tag to color the text, you could use <code>&lt;span&gt;</code> to mark the beginning and ending of the text and to specify what kind of message it is. The result might be text such as the following:


```dm

"[usr] spanks [targ]!"
"[usr] says, '[msg]'"

```


The <code>class</code> attribute may be used with any tag, but <code>span</code> and <code>div</code> are often convenient because they have no other side-effect but defining the style class. <code>span</code> is for text within a single paragraph and <code>div</code> is for whole paragraphs. The way text belonging to a particular class is formatted may be controlled in a style sheet such as the following:


```dm

.combat {color: red}
.chat {color: green}

```


This says that text in the `combat` class should be colored red and text in the `chat` class should be colored green. These classes are not pre-defined; you can create whatever new style classes you need. (The color names are predefined however. You can find a list of them in <a href="#/{{appendix}}/html-colors">HTML colors</a>.

The advantage of using style sheets instead of direct formatting tags is that you can cleanly separate structural information (such as combat and conversational messages) from formatting information (such as red and green text). By separating the two, you or the player can easily plug in different formatting schemes without changing any of the actual content.

A style sheet is composed of a list of rules, such as the two rules in the preceding example. Each rule contains one or more <em>selectors</em> followed by a body of attribute assignments (in braces). The selector specifies the context of the rule and the body specifies the format.

A selector may specify a container tag (such as <code>span</code>, <code>body</code>, or <code>p</code>) and a class. The above example could have been written with a selector of <code>span.chat</code>. However, by leaving out the tag, it applies to any tag with <code>class=chat</code>. It is also possible to only specify the tag and not the class. In that case, the selector applies to any matching tag, regardless of class.

To specify a <em>nested</em> context, several simple selectors may be listed one after the other. For example, emphasized text within a combat message could be enlarged with the following rule:


```dm

.combat em {font-size: larger}

```


It is also possible to list several selectors separated by commas in order to make them all apply to the same body. For example, this next rule is equivalent to the two following ones:


```dm

.combat em, .chat em {font-size: larger}
.combat em {font-size: larger}
.chat em {font-size: larger}

```


The style rule body contains a list of attribute assignments, delimited by semicolons. Each assignment takes the form of an attribute name, followed by a colon, followed by the value of the attribute. The following table summarizes the recognized attributes and their possible values.
***
**Related Pages:**
+    [CSS attributes](/ref/{{appendix}}/css)
+    [entities (text)](/ref/DM/text/entities)
+    [macros (text)](/ref/DM/text/macros)
+    [script var (client)](/ref/client/var/script)
+    [tags (text)](/ref/DM/text/tags)
+    [text](/ref/DM/text)
