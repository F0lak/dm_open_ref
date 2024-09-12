## images var (client)
**See also:**
+   [image objects](/ref/image.md) 
+   [image proc](/ref/proc/image.md) 

This is a list of images that are displayed to the user. The
output operator is one way to add entries to this list. Deleting an
image object will automatically remove it from the display, but if you
want to retain an image (so other people can still see it), it can be
removed by directly modifying this list.
### Example:

```
 var/image/I = new(\'image.dmi\',usr) usr.client.images += I
//display it sleep(50) usr.client.images -= I //remove it from the
display 
```
 Displaying the image can also be achieved like this:

```
 usr \<\< I 
```
