### Imports ###
from org.bukkit.plugin.python import PythonPlugin
from org.bukkit.event.Event import Type, Priority

from PermissionsHandler import PermissionsHandler
from Help import HelpMenu
### End imports ###

### System ###
__Name__ = 'Redcraft Dungeons'
__Created__ = 'August 09, 2011'
__Version__ = 0.0
__Updated__ = 'August 09, 2011'
### End System ###

### Class definitions ###
class RCDungeons(PythonPlugin):
        def onEnable(self):
                pm = self.getServer().getPluginManager()
                respawn = RespawnListener()
                self.perms = PermissionsHandler(plugin)
                self.help = HelpMenu(self.perms)
                pm.registerEvent(Type.PLAYER_RESPAWN, respawn, Priority.Normal, self)
                print "RCDungeons version " + __Version__ + " is now loaded. :)"

        def onDisable(self):
                print "RCDungeons version " + __Version__ + " is now unloaded. :("

        def onCommand(self, sender, command, label, args):
                if len(args) == 0:
                        self.help.send(sender)
                else:
                        print "You issued the following command: " + args[0]
                return 1;

class RespawnListener(object):
    """Listens for player respawns"""
### End classes ###

### Definitions ###

### End definitions ###
