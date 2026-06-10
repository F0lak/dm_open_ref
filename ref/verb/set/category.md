
## category (info)

**Format:**
+   set category = "Category"

**Arguments:**
+   Category: A text string for the category.
***
Verbs in the same category are visually grouped together in the verb panels. The default is "", which is displayed in the default panel titled "Commands". You can change that default by setting <code>client/default_verb_category</code>.

To hide a verb from all panels, set the category to null. The verb may still show up in right-click popup menus, so you may want to use the <a href="#/verb/set/hidden">hidden</a> or <a href="#/verb/set/popup_menu">popup_menu</a> verb properties instead.
***
**Related Pages:**
+    [default_verb_category var (client)](/ref/client/var/default_verb_category)
+    [show_verb_panel var (client)](/ref/client/var/show_verb_panel)
