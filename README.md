# Prerequisites

The Python3x.x & Steam API key can be found here:
* [Python3x.x](https://www.python.org/downloads/release/python-383/)

* [Steam API](https://steamcommunity.com/dev/apikey)

* selenium (not used yet)
* PIL (Python Image Library)
* requests


# Consept
The original idea for this program was to brute force steam vanity URL's or custom URL's looking for a pattern used by most MYG)T bots. I am still working on this consept and the AutoReport feature but now with voice_ban.dt file you can get bots by just muting them in game. The voice_ban.dt file will be updated after every match and the program will convert steamID3 to steamID64 and give a steam community URL. 

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
