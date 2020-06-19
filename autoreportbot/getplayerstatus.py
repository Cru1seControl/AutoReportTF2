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
        
        #Persona states
        self.PersonaStates = {"0": "Private/Offline", "1": "Online", "2": "Busy", "3": "Away", "4": "Snooze", "5": "Looking To Trade", "6": "Looking To Play"}
        
        #base steam API summaries
        self.baseRefURL = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s" % (self.apiKey, self.steamid)
        
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

    def PersonaState(self):
        PersonaStateRequest = requests.get(self.baseRefURL).content
        self.PersonaState = str(json.dumps(json.loads(PersonaStateRequest)["response"]["players"][0]["personastate"]).strip('\"'))

        for values in self.PersonaStates:
            if self.PersonaState in values:
                if self.PersonaState == values:
                    StateAsString = self.PersonaStates[values]

        return str(StateAsString)
    
    
    def ShowVanityMatches(self, setCustomName=False, showSummaries=False):
        BotTypes = ["g0tb0t", "g0tb0tt", "g0tb6t", "g0tb7t", "g0tbot", "g0t", "g0tbottt"]
        BotExists = True
        BotCount = 0

        if setCustomName:
            BotTypes.append(setCustomName)

        if not setCustomName:
            for BotNumber in range(1, 21):
                for botname in BotTypes:
                    self.CustomBotId = "%s%s" % (botname, BotNumber)
                
                    BotVanityRef = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=%s&vanityurl=%s" % (self.apiKey, self.CustomBotId)
                    try:
                        BotContent = json.dumps(json.loads(requests.get(BotVanityRef).content)["response"]["steamid"]).strip('\"')
                        if showSummaries:
                            pass
                        elif showSummaries is False:
                            print(self.CustomBotId, ":", BotContent)
                        
                        if showSummaries:
                            SummaryRefUrl = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s" % (self.apiKey, BotContent)
                            SummaryRequest = lambda KEY : json.dumps(json.loads(requests.get(SummaryRefUrl).content)["response"]["players"][0][KEY]).strip('\"')
                            
                            SteamID = SummaryRequest("steamid")
                            PersonaState = SummaryRequest("personastate")
                            
                            PersonaName = SummaryRequest("personaname")
                            ProfileCreation = SummaryRequest("timecreated")
                            RealName = SummaryRequest("realname")

                            for values in self.PersonaStates:
                                if PersonaState in values:
                                    if PersonaState == values:
                                        StateAsString = self.PersonaStates[values]
                            
                            print("\n STEAMID: %s\n Persona Name: %s\n Real Name: %s\n Persona State: %s\n Date Created: %s" % (SteamID, PersonaName, RealName, StateAsString, datetime.fromtimestamp(int(ProfileCreation))))
                            
                    except Exception:
                        BotExists = False
                        if not BotExists:
                            pass
                        
    def ResolveVanityUrl(self, customVanity=None):
        if customVanity:
            VanityReferingUrl = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=%s&vanityurl=%s" % (self.apiKey, customVanity)
        else:
            VanityReferingUrl = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=%s&vanityurl=%s" % (self.apiKey, self.vanityUrl)
        VanityRequest = requests.get(VanityReferingUrl)

        VanityResponse = json.dumps(json.loads(VanityRequest.content)["response"]["steamid"]).strip('\"')
        return int(VanityResponse)

def PlayerSummary(self):
        SummaryRefUrl = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s" % (self.apiKey, self.steamid)
        SummaryRequest = requests.get(SummaryRefUrl).content

        base = json.dumps(json.loads(SummaryRequest)["response"]["players"][0])

        SteamID = json.dumps(json.loads(SummaryRequest)["response"]["players"][0]["steamid"]).strip('\"')
        PersonaState = str(json.dumps(json.loads(SummaryRequest)["response"]["players"][0]["personastate"]).strip('\"'))
        PersonaName = json.dumps(json.loads(SummaryRequest)["response"]["players"][0]["personaname"]).strip('\"')
        ProfileCreation = json.dumps(json.loads(SummaryRequest)["response"]["players"][0]["timecreated"]).strip('\"')
        RealName = json.dumps(json.loads(SummaryRequest)["response"]["players"][0]["realname"]).strip('\"')

        for values in self.PersonaStates:
            if PersonaState in values:
                if PersonaState == values:
                    StateAsString = self.PersonaStates[values]

        print("STEAMID: %s\n Persona Name: %s\n Real Name: %s\n Persona State: %s\n Date Created: %s" % (SteamID, PersonaName, RealName, StateAsString, datetime.fromtimestamp(int(ProfileCreation))))

        
    def SteamMuteList(self):
        """Resolves steamID3 to steamID64 from voice_ban.dt and returns a community URL"""
        with open("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Team Fortress 2\\tf\\voice_ban.dt", "rb") as muteList:
            steam64Base = 76561197960265728

            listCharsReplaced = muteList.read().replace(b"\x00", b"").replace(b"\x01", b"").decode().replace("[", "").replace("]", " ").replace("U:1:", "")
            steamID3 = listCharsReplaced.split()

            for steam in steamID3:
                newSteamID = int(steam) + steam64Base
                print("https://steamcommunity.com/id/" + str(newSteamID))
        
        
        
    def GetPlayerAvatar(self, displayImage=False):
        #ISteamUser developer api reference url
        AvatarRefUrl = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s" % (self.apiKey, self.steamid)
        AvatarRequest = requests.get(AvatarRefUrl)

        AvatarResponse = json.dumps(json.loads(AvatarRequest.content)["response"]["players"][0])
        AvatarRefUrl = json.loads(AvatarResponse)["avatarfull"]
        
        if displayImage is True:
            Avatar = Image.open(io.BytesIO(requests.get(AvatarRefUrl).content))
            Avatar.show()
            
        with io.BytesIO(requests.get(AvatarRefUrl).content) as imageBytes:
            return imageBytes.read()
