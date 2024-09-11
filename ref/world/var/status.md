## status var (world)
**See also:**
*   [hub var (world)](/world/var/hub)
*   [game_state var (world)](/world/var/game_state)
*   [visibility var (world)](/world/var/visibility)


This is a short text string used in BYOND hub to describe the
state of a game in progress. For example, you might want to indicate if
new players will be able to actively play, or whether they would have to
join as spectators.
### Example:

```
 world status = \"accepting players\" mob/verb/start_game()
world.status = \"accepting spectators\" //\... 
```
