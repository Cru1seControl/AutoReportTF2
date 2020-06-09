from PIL import Image
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
import json
import io

class getplayerstatus(object):
    def __init__(self, steamid, apiKey, vanityUrl=None, appId=None, steamIdReporter=None, playerReport=None):
        #Set valid keys 
        self.steamid = steamid
        self.apiKey = apiKey
        
        #Set vanity url to resolve
        self.vanityUrl = vanityUrl
        
        #Report player account
        self.steamIdReporter = steamIdReporter 
        self.appId = appId                      #steam://rungameid/440 TF2 gameid
        self.playerReport = playerReport


    def SteamID(self):
        return self.steamid

    def APIKey(self):
        return self.apiKey

    def ShowVanityMatches(self, setCustomName=False):
        BotTypes = ["g0tb0t", "g0tb0tt", "g0tb6t", "g0tb7t", "g0tbot", "g0t", "g0tbottt"]
        BotExists = True
        BotCount = 0

        if setCustomName:
            BotTypes.append(setCustomName)

        if not setCustomName:
            for BotNumber in range(1, 21):
                for botname in BotTypes:
                    CustomBotId = "%s%s" % (botname, BotNumber) 
                
                    BotVanityRef = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=%s&vanityurl=%s" % (self.apiKey, CustomBotId)
                    try:

                        BotContent = json.dumps(json.loads(requests.get(BotVanityRef).content)["response"]["steamid"]).strip('\"')
                        print(CustomBotId, "|", BotContent)
                    
                    except KeyError:
                        BotExists = False
                        print("*")


    def ResolveVanityUrl(self, customVanity=None):
        if customVanity:
            VanityReferingUrl = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=%s&vanityurl=%s" % (self.apiKey, customVanity)
        else:
            VanityReferingUrl = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=%s&vanityurl=%s" % (self.apiKey, self.vanityUrl)
        VanityRequest = requests.get(VanityReferingUrl)

        VanityResponse = json.dumps(json.loads(VanityRequest.content)["response"]["steamid"]).strip('\"')
        return int(VanityResponse)

    def GetPlayerAvatar(self, displayImage=False):
        #ISteamUser developer api reference url
        AvatarRefUrl = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s" % (self.apiKey, self.steamid)
        AvatarRequest = requests.get(AvatarRefUrl)

        AvatarResponse = json.dumps(json.loads(AvatarRequest.content)["response"]["players"][0])
        AvatarRefUrl = json.loads(AvatarResponse)["avatarfull"]
        
        if displayImage is True:
            Avatar = Image.open(io.BytesIO(requests.get(AvatarRefUrl).content))
            Avatar.show()
