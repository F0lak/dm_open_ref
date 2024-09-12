## link proc
**See also:**
+   [\<\< output operator](/ref/operator/%3c%3c/output.md) 
+   [Topic proc (client)](/ref/client/proc/Topic.md) 
+   [file proc](/ref/proc/file.md) 
+   [run proc](/ref/proc/run.md) <!-- -->
**Format:**
+   O \<\< link(url)


This causes the recipient (O) to view the specified url. The
url could be a web or BYOND address. In the latter case, the player will
disconnect from the current world and connect to the specified one.


The format of a BYOND url is as follows+ 
```

byond://address:port?TopicData 
```
 

To access a
registered world, address:port may be replaced by the registered name in
the hub. The optional topic data is processed by the world once the
player has connected. If only a topic is specified, the current world
processes it.
### Example:

```
 usr \<\< link(\"byond://byond.com:6000\") //BYOND address usr
\<\< link(\"http://www.byond.com\") //web address usr \<\<
link(\"?myTopic\") //topic 
```
