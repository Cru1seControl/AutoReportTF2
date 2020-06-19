# Prerequisites

The Python3x.x & Steam API key can be found here:
* [Python3x.x](https://www.python.org/downloads/release/python-383/)

* [Steam API](https://steamcommunity.com/dev/apikey)

* selenium (not used yet)
* PIL (Python Image Library)
* requests


# Functions / Usage
## PersonaState
```python
import autoreportbot
personaState = autoreportbot.getplayerstatus(steamid="steamID64", apiKey="steam API key")

print(personaState.PersonaState())
```
## ShowVanityMatches
```python
vanitymatches = autoreportbot.getplayerstatus(steamid=None, apiKey="steam API key")
vanitymatches.ShowVanityMatches(showSummaries=True)
```
## PlayerSummary
```python
playersummary = autoreportbot.getplayerstatus(steamid="steamID64", apiKey="steam API key")
playersummary.PlayerSummary()
```
## ResolveVanityUrl
```python
resolvevanity = autoreportbot.getplayerstatus(steamid=None, apiKey="steam API key", vanityUrl="vanityurl")
print(resolvevanity.ResolveVanityUrl())
```
## SteamMuteList
```python
mutelist = autoreportbot.getplayerstatus(steamid=None, apiKey=None)
mutelist.SteamMuteList()
```
## GetPlayerAvatar
```python
avatar = autoreportbot.getplayerstatus(steamid="steamID64", apiKey="steam API key")
avatar.GetPlayerAvatar(displayImage=True)
```
For more detailed information visit [AutoReportBot and you!](https://steamcommunity.com/sharedfiles/filedetails/?id=2124475472)
