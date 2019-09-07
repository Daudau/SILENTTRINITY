from core.teamserver.module import Module


class STModule(Module):
    def __init__(self):
        self.name = 'boo/bypassAMSI'
        self.language = 'boo'
        self.description = 'Disable AMSI using AmsiScanBuffer'
        self.author = '@Daudau'
        self.references = []
        self.options = {}

    def payload(self):
        with open('core/teamserver/modules/boo/src/bypassAMSI.boo', 'r') as module_src:
            src = module_src.read()
            return src
