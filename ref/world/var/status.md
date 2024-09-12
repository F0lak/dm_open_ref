## status var (world)
**See also:**
*   [hub var (world)](/ref/world/var/hub.md) 
*   [game_state var (world)](/ref/world/var/game_state.md) 
*   [visibility var (world)](/ref/world/var/visibility.md) 

This is a short text string used in BYOND hub to describe the
state of a game in progress. For example, you might want to indicate if
new players will be able to actively play, or whether they would have to
join as spectators.
### Example:

```
 world status = \"accepting players\" mob/verb/start_game()
world.status = \"accepting spectators\" //\... 
```
