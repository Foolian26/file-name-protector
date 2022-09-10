import os
import asyncio

name = os.path.basename(__file__)

class Foolian:
    def Foolian_exit(self):
        os._exit(0)

    async def init(self):
        if name == 'protect.py':
            pass
        else:
            self.Foolian_exit()
asyncio.run(Foolian().init())
#put your code here
print("Hello World")
