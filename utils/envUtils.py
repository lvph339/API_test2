def envUtils(self,env):
    if str(env) == 'qa':
        DOMAIN = 'XXXXXXXX'
    elif str(env) == '预生产':
        DOMAIN = 'XXXXXXXX'
    else:
        DOMAIN = 'XXXXXXXx'
    return DOMAIN
