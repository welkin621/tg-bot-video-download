# tg-bot-video-download
a telegram bot plugin to download videos

## 有什么用？
有时候在telegram频道发现一些值得搜藏的视频，想在NAS上长期保存。如果通过手机下载，再导入NAS，比较麻烦不太方便。
如果有个机器人，你只需要把telegram频道里的视频转发给它，然后它就自动把视频下载到NAS，同时还把文件名自动更改（下载的默认是file_xx.mp4）。那就太方便了。
本插件就是干这个的。

效果图

<img src=https://github.com/welkin621/tg-bot-video-download/blob/main/demo.PNG>

## 基本说明
1. 需要teelebot框架下运行。
2. 必须要在本地运行一个telegram-api-server 并且将teelebot配置成local模式，否则不能下载大于20M的视频。
3. 此插件仅个人兴趣制作，满足本人最小需求，不提供任何技术支持和定制开发。感兴趣的可以在此基础上增加或者修改功能。
