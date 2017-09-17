# IMPORTS       BEGIN
from lib.character import *
# IMPORTS       END

# CONSTANTS   BEGIN
# # LIMB SLOTS
HEAD                = 'Head'
TORSO               = 'Torso'
ARML                = 'Arm (Left)'
ARMR                = 'Arm (Right)'
LEGL                = 'Leg (Left)'
LEGR                = 'Leg (Right)'
# # LIMB STATES
ORIGINAL            = 'Organic'
CYBERNETIC          = 'Cybernetic'
MISSING             = 'Missing'
# CONSTANTS   END

# MAIN FUNCTION BEGIN
def main():
    # METATYPES
    METATYPEdwarf   = Metatype([ 2,1,1, 3,1,1,1, 2,1], \
                               [ 7,6,5, 8,6,6,6, 7,6], \
                               [10,9,7,12,9,9,9,10,6], \
                               ['Thermographic Vision'])
    METATYPEhuman   = Metatype([1,1,1,1,1,1,1,1,2], \
                               [6,6,6,6,6,6,6,6,7], \
                               [9,9,9,9,9,9,9,9,7], \
                               [None])
    METATYPEelf     = Metatype([1, 2,1,1, 3,1,1,1,1], \
                               [6, 7,6,6, 8,6,6,6,6], \
                               [9,10,9,9,12,9,9,9,6], \
                               ['Low-Light Vision'])
    METATYPEork     = Metatype([ 4,1,1, 3,1,1,1,1,1], \
                               [ 9,6,6, 8,5,6,5,6,6], \
                               [13,9,9,12,7,9,7,9,6], \
                               ['Low-Light Vision'])
    METATYPEtroll   = Metatype([ 5,1,1, 5,1,1,1,1,1], \
                               [10,5,6,10,4,5,5,6,6], \
                               [15,7,9,15,6,7,7,9,6], \
                               ['Thermographic Vision'])
    # initialization

    runner = Runner(CHname,CHalias,                         \
                    metatype=eval(CHmetatype),              \
                    statarray=[ CHbod, CHagi, CHrea, CHstr, \
                                CHcha, CHint, CHlog, CHwil, \
                                CHess, CHedg, CHmag, CHres ])
    for event in makehappen:
        eval(event)
    runner.printRunner()
    # mainloop
    while True:
        eval( "runner."+input("Awaiting input: ") )
    pass
# MAIN FUNCTION END

# CLASSES       BEGIN
class Metatype():
    def __init__(self,minimums,maximums,augmentedmaximums,qualities):
        # minimums is a list of numbers
        self.BODmin     = minimums[0]
        self.AGImin     = minimums[1]
        self.REAmin     = minimums[2]
        self.STRmin     = minimums[3]
        self.CHAmin     = minimums[4]
        self.INTmin     = minimums[5]
        self.LOGmin     = minimums[6]
        self.WILmin     = minimums[7]
        self.EDGmin     = minimums[8]
        # maximums is a list of numbers
        self.BODmax     = maximums[0]
        self.AGImax     = maximums[1]
        self.REAmax     = maximums[2]
        self.STRmax     = maximums[3]
        self.CHAmax     = maximums[4]
        self.INTmax     = maximums[5]
        self.LOGmax     = maximums[6]
        self.WILmax     = maximums[7]
        self.EDGmax     = maximums[8]
        # augmentedmaximums is a list of numbers
        self.BODaugmax  = augmentedmaximums[0]
        self.AGIaugmax  = augmentedmaximums[1]
        self.REAaugmax  = augmentedmaximums[2]
        self.STRaugmax  = augmentedmaximums[3]
        self.CHAaugmax  = augmentedmaximums[4]
        self.INTaugmax  = augmentedmaximums[5]
        self.LOGaugmax  = augmentedmaximums[6]
        self.WILaugmax  = augmentedmaximums[7]
        self.EDGaugmax  = augmentedmaximums[8]
        # qualities is a list of string elements
        self.qualities  = qualities

class Name():
    def __init__(self,short,full):
        self.short  = short
        self.full   = full

class Stat():
    def __init__(self,stat,name,val,metatype,averaged,essencestat,augmentable,specialstat):
        self.name = Name(stat,name)
        self.isAveraged     = averaged
        self.isEssenceStat  = essencestat
        self.isAugmentable  = augmentable
        self.isSpecialStat  = specialstat
        if averaged:
            self.base   = val
        self.current    = val
        if essencestat:
            self.minimum    = 0
            self.maximum    = 6
        else:
            self.minimum    = eval( 'metatype.'+stat+'min')
            self.maximum    = eval( 'metatype.'+stat+'max')
        if augmentable:
            self.augmaximum = eval( 'metatype.'+stat+'augmax')
        pass

class StatBlock():
    def __init__(self,statarray,metatype):
        self.BOD = Stat( 'BOD', 'Body',      statarray[ 0], metatype, True,  False,  True, False )
        self.AGI = Stat( 'AGI', 'Agility',   statarray[ 1], metatype, True,  False,  True, False )
        self.REA = Stat( 'REA', 'Reaction',  statarray[ 2], metatype, False, False,  True, False )
        self.STR = Stat( 'STR', 'Strength',  statarray[ 3], metatype, True,  False,  True, False )
        self.CHA = Stat( 'CHA', 'Charisma',  statarray[ 4], metatype, False, False,  True, False )
        self.INT = Stat( 'INT', 'Intuition', statarray[ 5], metatype, False, False,  True, False )
        self.LOG = Stat( 'LOG', 'Logic',     statarray[ 6], metatype, False, False,  True, False )
        self.WIL = Stat( 'WIL', 'Will',      statarray[ 7], metatype, False, False,  True, False )
        self.ESS = Stat( 'ESS', 'Essence',   statarray[ 8], metatype, False,  True, False,  True )
        self.EDG = Stat( 'EDG', 'Edge',      statarray[ 9], metatype, False, False, False,  True )
        self.MAG = Stat( 'MAG', 'Magic',     statarray[10], metatype, False,  True, False,  True )
        self.RES = Stat( 'RES', 'Resonance', statarray[11], metatype, False,  True, False,  True )


class Limb():
    def __init__(self,slot,BOD,AGI,STR):
        self.slot     = slot
        self.BOD      = BOD.base
        self.AGI      = AGI.base
        self.STR      = STR.base
        self.state    = ORIGINAL

    def cyberize(self,BOD,AGI,STR):
        self.state    = CYBERNETIC
        self.BOD      = BOD
        self.AGI      = AGI
        self.STR      = STR

    def remove(self):
        self.state    = MISSING
        self.BOD      = 0
        self.AGI      = 0
        self.STR      = 0

class Runner():
    def __init__(self,name,alias=None,metatype=None,statarray=[1,1,1,1,1,1,1,1,6,1,0,0]):
        # name and alias are strings
        self.name = name
        self.alias = alias
        # metatype is a Metatype() class object
        self.metatype = metatype
        # create statblock
        StatBlock.__init__(self, statarray, self.metatype)
        self.stats = [ self.BOD, self.AGI, self.REA, self.STR, self.CHA, self.INT, self.LOG, self.WIL, self.ESS, self.EDG, self.MAG, self.RES]
        for i in range(len(self.stats)):
            self.stats[i].current = min( max( statarray[ i], self.stats[i].minimum ), self.stats[i].maximum )

        # limbs
        self.head = Limb( HEAD,  self.BOD, self.AGI, self.STR )
        self.torso= Limb( TORSO, self.BOD, self.AGI, self.STR )
        self.armL = Limb( ARML,  self.BOD, self.AGI, self.STR )
        self.armR = Limb( ARMR,  self.BOD, self.AGI, self.STR )
        self.legL = Limb( LEGL,  self.BOD, self.AGI, self.STR )
        self.legR = Limb( LEGR,  self.BOD, self.AGI, self.STR )
        # limbs index
        self.limbs = ( self.head, self.torso, self.armL, self.armR, self.legL, self.legR )
        # the limbs used for cyberlimb averaging
        self.averaging = ( TORSO, ARML, ARMR, LEGL, LEGR )
        pass

    def getAvgPhysicalStats(self):
        """Averages out cyberlimbs with the rest of the body."""
        BOD, AGI, STR, i = 0, 0, 0, 0
        for limb in self.limbs:
            if limb.slot in self.averaging:
                i   += 1
                BOD += limb.BOD
                AGI += limb.AGI
                STR += limb.STR

        BOD = min( max( int( BOD / i ), self.metatype.BODmin ), self.metatype.BODaugmax )
        AGI = min( max( int( AGI / i ), self.metatype.AGImin ), self.metatype.AGIaugmax )
        STR = min( max( int( STR / i ), self.metatype.STRmin ), self.metatype.STRaugmax )

        self.BOD.current, self.AGI.current, self.REA.current, self.STR.current = BOD, AGI, self.REA.current, STR
        pass

    def printRunner(self):
        self.getAvgPhysicalStats()
        print("\n"+"Name: "+str(self.name)+"\nAlias: "+str(self.alias)+"\nStat Block:")
        for stat in self.stats:
            if stat.isAveraged == True and stat.base != stat.current:
                ins1  = str(stat.base)
                ins1.ljust(4)
                ins2  = "("+str(stat.current)+")"
                ins2.rjust(4)
            else:
                ins1  = str(stat.current)
                ins1.ljust(4)
                ins2  = "   "
                if stat.isSpecialStat: ins2 = ""
            ins3 = ""
            if stat.isAugmentable == True: ins3 = " ("+str(stat.augmaximum)+")"
            print("    "+str(stat.name.short)+"  "+ins1+ins2+"/"+str(stat.maximum)+ins3)
        for limb in self.limbs:
            print(str(limb.slot).ljust(12)+str(limb.state).rjust(12))
# CLASSES       END

# INITIALIZATION
if __name__ == '__main__':
    main()