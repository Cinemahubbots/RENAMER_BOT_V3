"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month
	
	**VIP3**
	Daily Upload limit 100GB
	Price Rs 150  🇮🇳/🌎 1.81$  per Month
	
	
	Pay Using Upi I'd ```adishsureshtg@oksbi```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/logan_of_tg")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/logan_of_tg"),
        			InlineKeyboardButton("Paytm",url = "https://t.me/logan_of_tg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month
	
	**VIP3**
	Daily Upload limit 100GB
	Price Rs 150  🇮🇳/🌎 1.81$  per Month
	
	
	Pay Using Upi I'd ```adishsureshtg@oksbi```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/logan_of_tg")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/logan_of_tg"),
        			InlineKeyboardButton("Paytm",url = "https://t.me/logan_of_tg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
