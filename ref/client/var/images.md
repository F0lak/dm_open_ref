
## images (var)
***
This is a list of images that are displayed to the user. The output operator is one way to add entries to this list. Deleting an image object will automatically remove it from the display, but if you want to retain an image (so other people can still see it), it can be removed by directly modifying this list.


```dm

var/image/I = new('image.dmi',usr)
usr.client.images += I  //display it
sleep(50)
usr.client.images -= I  //remove it from the display

```



```dm

usr << I

```

***
**Related Pages:**
+    [image objects](/ref/image)
+    [image proc](/ref/proc/image)
