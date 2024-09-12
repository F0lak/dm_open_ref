## SetAPI proc (client) 
###### BYOND Version 514
**See also:**
+   [GetAPI proc (client)](/ref/client/proc/GetAPI.md) 
+   [CheckPassport proc (client)](/ref/client/proc/CheckPassport.md) <!-- -->
**Format:**
+   SetAPI(Api, Key, Value)
<!-- -->
**Args:**
+   Api+ the name of the API (e.g. \"steam\")
+   Key+ the name of the value to change
+   Value+ the new value to set


Interfaces with supported external APIs to write information.
Currently this only has meaning for Steam, for specially built games
that have a Steam app ID. 

This proc returns null any time the
call or its results are invalid.
  --------------------------------------------------------------------------
  Key                  Return type       Description       
  -------------------- ----------------- ----------------- -----------------
  `"steam"` API\                                           
  Requires that the                                        
  server and client                                        
  are using a valid                                        
  Steam app ID, such                                       
  as when a game is                                        
  built for standalone                                     
  distribution.                                            
  stat:*Name*          num               Changes the value 
                                         of the stat       
                                         called `Name`.    
                                         Returns 1 on      
                                         success. This may 
                                         fail if the stat  
                                         change is too     
                                         much or is out of 
                                         range.            
  achievement:*Name*   num               Earns the         
                                         achievement       
                                         called `Name`, or 
                                         clears it. Value  
                                         is expected to be 
                                         a number, or      
                                         number in text    
                                         form, where 0     
                                         will clear the    
                                         achievement and 1 
                                         will earn it.     
  --------------------------------------------------------------------------