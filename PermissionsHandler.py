### Imports ###
### End imports ###

### System ###
__Name__ = 'Permissions Handler'
__Created__ = 'August 09, 2011'
__Version__ = 0.0
__Updated__ = 'August 15, 2011'
### End System ###

### Class definitions ###
class PermissionsHandler(object):
    """The Permissions Handler
    Supports only Permissions 3.1.6 at the moment"""
    def __init__(self, pluginmanager):
        """pluginmanager = the server's plugin manager"""
        self.perm = pluginmanager.getPlugin("Permissions")
        if self.perm:
            self.handler = self.perm.getHandler()
            self.ptype = "P3"
            print "Found " + self.perm.getDescription().getFullName()
        else:
            self.ptype = "OP"
            print "Couldn't find Permissions. Defaulting to OP commands"
    def has(self, user, node):
        """Checks to see if user has node"""
        if self.ptype == "P3":
            return self.handler.has(user, node)
        elif self.ptype == "OP":
            oponly = opOnly(node)
            if oponly and user.isOp():
                return True
            elif oponly and not user.isOp():
                return False
            else:
                return True
    def getPermissions(self, player, nodes):
        """Provide a list of nodes, returns dictionary of true nodes for player"""
        trueNodes = {}
        if self.ptype == "P3":
            for node in nodes:
                trueNodes[node] = self.has(player, node)
        elif self.ptype == "OP":
            for node in nodes:
                if oponly(node):
                    trueNodes[node] = player.isOp()
                else:
                    trueNodes[node] = True
        return trueNodes

### End classes ###

### Definitions ###

### End definitions ###