import configparser
import os
# root=os.chdir("../../")
USER_CFG_SECTION="binance_user_config"
CFG_NAME="user.cfg"
class Setting:
    def __init__(self): 
      
        self.ROOT_DIC=os.path.abspath(os.path.join(os.path.dirname(__file__),"..",))
        self.configPath=os.path.join(self.ROOT_DIC,CFG_NAME)
        config=configparser.ConfigParser()
        config["DEFAULT"]={}
        whether_exist = os.path.exists(os.path.join(self.ROOT_DIC, CFG_NAME))
        if not whether_exist:
            print("No user config file detected")
        else:
            config.read(self.configPath)
        self.API_KEY=config.get(USER_CFG_SECTION, "api_key")
        self.API_SECRET=config.get(USER_CFG_SECTION,"api_secret_key")

            





