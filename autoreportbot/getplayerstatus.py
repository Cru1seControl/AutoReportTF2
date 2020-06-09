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


    def ImitateReport(self):
        for driverToGet in driver.get("https://steamcommunity.com/id%s" % (self.MassReportVanityURL()[0])):
            print(driverToGet)

        pass



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


    def ProfileSettingType(self):
        CanSeeContent = False

        #0 - Offline, 1 - Online, 2 - Busy, 3 - Away, 4 - Snooze, 5 - looking to trade, 6 - looking to play. If the player's profile is private, this will always be "0"
        contentTypes = {"Private": 0, "Offline": 0, "Online": 1, "Busy": 2, "Away": 3, "Snooze": 4, "Looking to Trade": 5, "Looking to Play": 6}
        pass

    def IsPlayerVacBanned(self):
        banned = False
        pass

    def GetFriendsList(self):
        friendList = []
        pass

    def GetPlayerLevel(self):
        PlayerLevelReferingUrl = ""
        pass

    def ReportSteamAccount(self):
        #Required arguments :key, steamid, appid:

        pass

    def RequestPlayerGameBan(self):
        pass

    def GetPlayerAvatar(self, displayImage=False):
        #ISteamUser developer api reference url
        AvatarRefUrl = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s" % (self.apiKey, self.steamid)
        AvatarRequest = requests.get(AvatarRefUrl)

        AvatarResponse = json.dumps(json.loads(AvatarRequest.content)["response"]["players"][0])
        AvatarRefUrl = json.loads(AvatarResponse)["avatarfull"]
        
        if displayImage is True:
            Avatar = Image.open(io.BytesIO(requests.get(AvatarRefUrl).content))
            Avatar.show()

def player_status_check(self):
    pass


#CheckSteamCheat = CheckSteamCheat("76561199050850901", apiKey="1C939844B2BF19E345DD1FC3BD83843E")

#CheckSteamCheat.GetPlayerAvatar(False)

#print(CheckSteamCheat.ResolveVanityUrl())

#CheckSteamCheat.MassReportVanityURL()