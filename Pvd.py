# -*- coding:utf-8 -*-
import requests
import os
import re

def Pvd(bot, message):

    root_id = bot.root_id
    # bot_id = bot.bot_id
    # author = bot.author
    # version = bot.version
    # plugin_dir = bot.plugin_dir
    # plugin_bridge = bot.plugin_bridge
    # uptime = bot.uptime
    # response_times = bot.response_times
    # response_chats = bot.response_chats
    # response_users = bot.response_users    

    chat_id = message["chat"]["id"]
    user_id = message["from"]["id"]
    message_id = message["message_id"]

    message_type = message["message_type"]
    chat_type = message["chat"]["type"]

    prefix = ""
    with open(bot.path_converter(bot.plugin_dir + "Pvd/__init__.py"), "r", encoding="utf-8") as init:
        prefix = init.readline()[1:].strip()


    # Write your plugin code below

    # do nothing if user is not you   
    if str(user_id) != str(root_id):        
        return

    if message_type == "video":
        file_id = message["video"]["file_id"] 
        bot.sendMessage(chat_id, "Begin to download file in local server...", reply_to_message_id=message_id)       
        
        try:
            icount=1
            # when downloading duriation gets too long and may return Fasle, so need to do getFile agian.
            while bot.getFile(file_id) == False:
                bot.sendMessage(chat_id,"retrying... x" + str(icount),reply_to_message_id=message_id)
                icount=icount+1
        except Exception as e:            
            bot.sendMessage(chat_id,e)                
        file_path = bot.getFile(file_id)["file_path"]
        try:
            # omite all symbol 
            file_rename=re.sub(r"[^a-zA-Z0-9\u4E00-\u9FA5]","",message["caption"])
            # cut string ,leave /xxx/.xxmp4
            video_path1=re.sub(r".+//","/",file_path)            
            # rename with video caption
            video_path2=re.sub(r"file_\d+",file_rename,video_path1)
            os.rename(video_path1,video_path2)            
            bot.sendMessage(chat_id, "Finish!  File name is :    "  + file_rename + ".mp4" , reply_to_message_id=message_id)
            return
        except KeyError:            
            bot.sendMessage(chat_id, "Finish!  File name is :    "  + file_path , reply_to_message_id=message_id)
            return        
    if message_type == "text":
        bot.sendMessage(chat_id,"Bot is on duty")
    return

