import logging, sys, os, requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
TOKEN = ''
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
def getSiteMetas(update: Update, Context: CallbackContext) -> None:
    userText = update.message.text
    if len(userText) <= 7:
        update.message.reply_text('请输入站点网址')
        vaildStats = False
    else:
        vaildStats = True
        if vaildStats == True:
            siteURL = userText[7:]
            siteURL = siteURL.split('//')[-1]
            getSiteURL = 'https://' + siteURL + '/api/'
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
                    maintainerName = '未提供'
                maintainerEmail = handledSiteMetasJSON['maintainerEmail']
                if maintainerEmail == '':
                    maintainerEmail = '未提供'
                enableTwitterIntegration = handledSiteMetasJSON['enableTwitterIntegration']
                enableGithubIntegration = handledSiteMetasJSON['enableGithubIntegration']
                enableDiscordIntegration = handledSiteMetasJSON['enableDiscordIntegration']
                cacheRemoteFiles = handledSiteMetasJSON['cacheRemoteFiles']
                proxyRemoteFiles = handledSiteMetasJSON['proxyRemoteFiles']
                elasticsearch = handledSiteMetasJSON['features']['elasticsearch']
                update.message.reply_text(
                    """
                    Metas of {}:
站点名称： {}
站点描述： {}
站点Misskey版本： {}
ToS地址： {}
维护者名称： {}
维护者联络邮箱： {}
开启reCaptcha？： {}
开启Elastic Search？： {}
不允许注册？： {}
未开启本地时间线？： {}
未开启远程站点时间线？： {}
最长字数限制： {}
整合Twitter？： {}
整合Github？： {}
整合Discord？： {}
缓存远程站点资源？： {}
代理远程站点资源？： {}
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
        update.message.reply_text('请输入站点网址')
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
                    'Stats of {}: \n已知文章总数：{}\n本地文章总数：{}\n已知用户总数：{}\n本地用户总数：{}\n已知站点数：{}\n本站点内容于本站磁盘使用之大小：{}\n远程站点内容于本站磁盘使用之大小：{}'.format(siteURL ,notesCount, originalNotesCount, usersCount, originalUsersCount, instances, driveUsageLocal, driveUsageRemote)
                )
            else:
                update.message.reply_text('Error.\nError code: {}'.format(str(rawGetSitesStatsCode)))
        else:
            pass
def helpCommand(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        '帮助:\n/help: 显示本帮助\n/stats: 获得站点目前状态(stats)\n示范:\n/stats https://rosehip.moe\n/ping: Pong!\n/metas: 获得站点详细讯息\n示例：\n/metas https://rosehip.moe\n'
    )
def startMessage(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        '使用/help 来获得详细使用说明'
    )
def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', startMessage))
    dispatcher.add_handler(CommandHandler('help', helpCommand))
    dispatcher.add_handler(CommandHandler('stats', getCurrentSiteStats))
    dispatcher.add_handler(CommandHandler('ping', pingPong))
    dispatcher.add_handler(CommandHandler('metas', getSiteMetas))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
