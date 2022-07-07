# Websocket framework

Recieve and send messages over a self hosted python websocket, replying to specific messages based on a set of rules.

Stupidly simple, not many features.




## Explanation

#### ruleSet

Formatted in a list, `[["incoming","to go out"],["incoming 2","to go out 2"]]`

#### startWebsocket

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `port` | `integer` | **Required** - the port to host the websocket on |
| `keepAlive` | `boolean` | wether to act as a reciever only, or to send packets back |
| `consoleOut` | `boolean` | wether to print the incoming data to console |

## Dependencies

```http
  asyncio
  websockets
```
`warnings` is to disable DeprecationWarnings

