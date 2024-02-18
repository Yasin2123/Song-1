import os

class Config:
    API_ID = int(os.environ.get("API_ID", "25114508")) #Karışmayın
    API_HASH = os.environ.get("API_HASH", "993ccdfe81548dade420e81bcd6807ce") #Karışmayın
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6513972084:AAEg8zmeW-vR86jOpe7c3Oak8orZ_ehX7ts") #Botunuzun Tokenini Girin .  
