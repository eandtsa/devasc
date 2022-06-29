class Router:
    '''Router Class'''
    def __init__(self, model, swversion, ip_add):
        '''initialize values'''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add

    def getdesc(self):
        '''return a formated description of the router'''
        desc = f'Router Model                  :{self.model}\n'\
               f'Router Version                :{self.swversion}\n'\
               f'Router Management IP Address  :{self.ip_add}'
        return desc  # print values of the desc in the print function below

rtr1 = Router('iosV', '15.6.7', '10.10.10.1')
rtr2 = Router('isr4221', '16.9.5', '10.10.10.5')

print('Rtr1\n', rtr1.getdesc(), '\n', sep='')
print('Rtr2\n', rtr2.getdesc(), '\n', sep='')


        