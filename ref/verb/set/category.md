## category setting (verb)
**See also:**
*   [default_verb_category var
    (client)](/ref/client/var/default_verb_category.md) -m
*   [show_verb_panel var (client)](/ref/client/var/show_verb_panel.md) -m
<!-- -->
**Format:**
*   set category = \"Category\"
<!-- -->
**Args:**
*   Category* A text string for the category.


Verbs in the same category are visually grouped together in the
verb panels. The default is \"\", which is displayed in the default
panel titled \"Commands\". You can change that default by setting
`client/default_verb_category`. 

To hide a verb from all panels,
set the category to null. The verb may still show up in right-click
popup menus, so you may want to use the [hidden](/ref/verb/set/hidden.md) -m or
[popup_menu](/ref/verb/set/popup_menu.md) -mverb properties instead.