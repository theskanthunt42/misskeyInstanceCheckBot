import logging, sys, os, requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
TOKEN = ''
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
def getSiteServerInfo(update: Update, Context: CallbackContext) -> None:
    userText = update.message.text
    print(userText)
    if len(userText) <= 12:
        update.message.reply_text("Please give the instance's url.")
        vaildStats = False
    else:
        vaildStats = True
        if vaildStats == True:
            siteURL = userText[12:].split('//')[-1]
            getSiteURL = 'https://' + siteURL + '/api/server-info/'
            rawGetSitesInfo = requests.post(getSiteURL, data='{}')
            rawGetSitesInfoStatusCode = rawGetSitesInfo.status_code
            print(f'{rawGetSitesInfoStatusCode} {siteURL} SERVERINFO') #Might do better job than just jam tons of text
            if rawGetSitesInfoStatusCode == 200:
                apiStats = True
            else:
                apiStats = False
            if apiStats == True:
                handledSiteInfoJSON = rawGetSitesInfo.json()
                serverName = handledSiteInfoJSON['machine']
                cpuName = handledSiteInfoJSON['cpu']['model']
                cpuCores = handledSiteInfoJSON['cpu']['cores']
                totalRAM = handledSiteInfoJSON['mem']['total'] / 1000000
                fileSystemTotal = handledSiteInfoJSON['fs']['total'] / 100000000 #From Bytes to Gigabytes
                fileSystemUsed = handledSiteInfoJSON['fs']['used'] / 100000000 #Same as up
                update.message.reply_text(
                    f"""
                    Server Info of {siteURL}:
Server's name: {serverName}
CPU: {cpuName}
Core(s) of CPU: {cpuCores}
Total amount of RAM: {totalRAM} MBytes
Total amount of filesystem: {fileSystemTotal} GBytes
Total amount of filesystem that is in use: {fileSystemUsed} GBytes
                    """
                )
            else:
                update.message.reply_text('Error.\nError code: {}'.format(str(rawGetSitesInfoStatusCode)))
        else:
            pass

#def getUserInfoFromSite(update: Update, Context: CallbackContext) -> None:
#    userText = update.message.text
#    #Get user info from site  #May add, cancel due to 100 user limit
def getSiteMetas(update: Update, Context: CallbackContext) -> None:
    userText = update.message.text
    if len(userText) <= 7:
        update.message.reply_text("Please give instance's url.")
        vaildStats = False
    else:
        vaildStats = True
        if vaildStats == True:
            siteURL = userText[7:]
            siteURL = siteURL.split('//')
            getSiteURL = 'https://' + siteURL[-1] + '/api/'
            getMetasURL = getSiteURL + 'meta/'
            postPayLoad = '{"detail":true}'
            rawGetSitesMetas = requests.post(getMetasURL, data=postPayLoad)
            rawGetSitesMetasCode = rawGetSitesMetas.status_code
            print(rawGetSitesMetasCode)
            print(rawGetSitesMetas.text)
            if rawGetSitesMetasCode == 200:
                apiStats = True
            else:
                apiStats = False
            if apiStats == True:
                handledSiteMetasJSON = rawGetSitesMetas.json()
                version = handledSiteMetasJSON['version']
                name = handledSiteMetasJSON['name']
                description = handledSiteMetasJSON['description']
#                annoCount = len(handledSiteMetasJSON['announcements'])
#                annoAll = ''
#                for anno in annoCount - 1:
#                    title = handledSiteMetasJSON['announcements'][anno][0]
#                    text = handledSiteMetasJSON['announcements'][anno][1]
#                    annoAll = annoAll + '公告：{}\n内容：{}\n\n'.format(title, text)
                disableRegistration = handledSiteMetasJSON['disableRegistration']
                disableLocalTimeline = handledSiteMetasJSON['disableLocalTimeline']
                disableGlobalTimeline = handledSiteMetasJSON['disableGlobalTimeline']
                if handledSiteMetasJSON['tosUrl'] != '' or None:
                    tosURL = handledSiteMetasJSON['tosUrl']
                maxNoteTextLength = str(handledSiteMetasJSON['maxNoteTextLength'])
                enableRecaptcha = handledSiteMetasJSON['enableRecaptcha']
                maintainerName = handledSiteMetasJSON['maintainerName']
                if maintainerName == '':
                    maintainerName = 'N/A'
                maintainerEmail = handledSiteMetasJSON['maintainerEmail']
                if maintainerEmail == '':
                    maintainerEmail = 'N/A'
                enableTwitterIntegration = handledSiteMetasJSON['enableTwitterIntegration']
                enableGithubIntegration = handledSiteMetasJSON['enableGithubIntegration']
                enableDiscordIntegration = handledSiteMetasJSON['enableDiscordIntegration']
                cacheRemoteFiles = handledSiteMetasJSON['cacheRemoteFiles']
                proxyRemoteFiles = handledSiteMetasJSON['proxyRemoteFiles']
                elasticsearch = handledSiteMetasJSON['features']['elasticsearch']
                update.message.reply_text(
                    """
                    Metas of {}:
Name： {}
Description： {}
Misskey version： {}
ToS url： {}
Maintainer's name： {}
Maintainer's email： {}
Enable reCaptcha?： {}
Enable Elastic Search?： {}
Disable sign up?： {}
Disable local timeline?： {}
Disable remote timeline?： {}
Max note lenght： {}
Enable Twitter Integration?： {}
Enable Github Integration?： {}
Enable Discord Integration?： {}
Enable cache remote instance's files?： {}
Enable proxy remote instance's files： {}
                    """.format(siteURL, name, description, version, tosURL, maintainerName, maintainerEmail, enableRecaptcha, elasticsearch, disableRegistration, disableLocalTimeline, disableGlobalTimeline, maxNoteTextLength, enableTwitterIntegration, enableGithubIntegration, enableDiscordIntegration, cacheRemoteFiles, proxyRemoteFiles)
                )
            else:
                update.message.reply_text('Error.\nError code: {}'.format(str(rawGetSitesMetasCode)))
        else:
            pass
                    

def pingPong(update: Update, Context: CallbackContext) -> None:
    update.message.reply_text('Pong!')
    userText = update.message.text
    print(userText)
def getCurrentSiteStats(update: Update, Context: CallbackContext) -> None:
    userText = update.message.text
    if len(userText) <= 7:
        update.message.reply_text("Please give the site's url.")
        vaildStats = False
    else:
        vaildStats = True
        if vaildStats == True:
            siteURL = userText[7:]
            siteURL = siteURL.split('//')[-1]
            getSiteURL = 'https://' + siteURL + '/api/'
            getStatsURL = getSiteURL + 'stats/'
            postPayLoad = '{}'
            rawGetSitesStats = requests.post(getStatsURL, data=postPayLoad)
            rawGetSitesStatsCode = rawGetSitesStats.status_code
            print(rawGetSitesStatsCode)
            print(rawGetSitesStats.text)
            if rawGetSitesStatsCode == 200:
                apiStats = True
            else:
                apiStats = False
            if apiStats == True:
                handledGetSitesJSON = rawGetSitesStats.json()
                notesCount = str(handledGetSitesJSON['notesCount'])
                originalNotesCount = str(handledGetSitesJSON['originalNotesCount'])
                usersCount = str(handledGetSitesJSON['usersCount'])
                originalUsersCount = str(handledGetSitesJSON['originalUsersCount'])
                instances = str(handledGetSitesJSON['instances'])
                driveUsageLocal = str(handledGetSitesJSON['driveUsageLocal'])
                driveUsageRemote = str(handledGetSitesJSON['driveUsageRemote'])
                update.message.reply_text(
                    'Stats of {}: \nKnown notes count: {}\nLocal notes count: {}\nKnown users count: {}\nLocal users: {}\nknown instances count: {}\nSize of local content on local drive: {}\nSize of remote instance content on local drive: {}'.format(siteURL ,notesCount, originalNotesCount, usersCount, originalUsersCount, instances, driveUsageLocal, driveUsageRemote)
                )
            else:
                update.message.reply_text('Error.\nError code: {}'.format(str(rawGetSitesStatsCode)))
        else:
            pass
def helpCommand(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Help:\n/help: Show this help\n/stats: Get the instance's stats\nExample:\n/stats https://rosehip.moe\n/ping: Pong!\n/metas: Get metas of the instances\nExample: \n/metas https://rosehip.moe\n"
    )

def showUID(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    userID = user['id']
    update.message.reply_text(
        f'UID: {userID}'
    )
def startMessage(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Use /help to see how to deal with this bot.'
    )
def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', startMessage))
    dispatcher.add_handler(CommandHandler('help', helpCommand))
    dispatcher.add_handler(CommandHandler('stats', getCurrentSiteStats))
    dispatcher.add_handler(CommandHandler('ping', pingPong))
    dispatcher.add_handler(CommandHandler('metas', getSiteMetas))
    dispatcher.add_handler(CommandHandler('serverinfo', getSiteServerInfo))
    dispatcher.add_handler(CommandHandler('getuid', showUID))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
