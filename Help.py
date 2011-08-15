### Imports ###

### End imports ###

### System ###
__Name__ = 'Help Menu'
__Created__ = 'August 09, 2011'
__Version__ = 1.0
__Updated__ = 'August 15, 2011'
### End System ###

### Class definitions ###
class HelpMenu(object):
    """The help menu class"""
    def __init__(self, perms):
        """Perms = PermissionsHandler class"""
        self.perms = perms
        self.helpstrings = {}
        self.header = '### Help ###'
    def send(self, sender):
        """Sends the help menu to the command sender"""
        playerperms = self.perms.getPermissions(sender, self.helpstrings.keys())
        message = self.header
        for node in self.helpstrings:
            if playerperms[node]:
                message += self.helpstrings[node]
        sender.sendMessage(message)
    def addHelpString(self, help, node):
        """Addes a help string"""
        self.helpstrings[node] = help
    def addHelpDict(self, diction):
        """diction = dictionary of node (key) with the helpstring (value)"""
        try:
            self.helpstrings.update(diction)
        except:
            for node in diction:
                self.addHelpString(node, diction[node])
    def setHeader(self, header):
        """Set the help header"""
        self.header = header

### End classes ###

### Definitions ###

### End definitions ###