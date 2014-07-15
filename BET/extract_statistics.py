__author__ = 'yaxxu'
import re
import MySQLdb
from models import Schematic, Combine

def getstatistics(source):
    try:
        filehandle = open(source+'\\boardSummary.rpt','r')
        report=filehandle.read()
        #extract Part Number
        m = re.search("(BET/)([\d-]*)", report)
        Partnumber=m.group(2)
        #extract Pins
        m = re.search("(Pins).*?Total\D(\d*)", report)
        Pins=m.group(2)
        #extract Components
        m = re.search("(Components).*?Total\D(\d*)", report)
        Components=m.group(2)
        #extract Connections
        m = re.search("(Connections).*?Total\D(\d*)", report)
        Connections=m.group(2)
        #extract Nets
        m = re.search("(Nets).*?Total\D(\d*)", report)
        Nets=m.group(2)
        #extract Route keepin
        m = re.search("Router Keepin[^0-9-]*([-]*[\d.]*)[^0-9-]*([-]*[\d.]*)[^0-9-]*([-]*[\d.]*)[^0-9-]*([-]*[\d.]*)", report)
        #print m.group(1),m.group(2),m.group(3),m.group(4)
        keepinx=abs(float(m.group(3))-float(m.group(1)))
        keepiny=abs(float(m.group(4))-float(m.group(2)))
        #extract Layout_area
        m = re.search("(Layout area)\D*([\d.]*)", report)
        Layout_area=m.group(2)
        #extract pin density
        m = re.search("Design,[\d.]+,[\d.]+,[\d.]+,[\d.]+,([\d.]*)", report)
        Pin_density=m.group(1)
        print 'Summary report processed'
        Newtask = Combine(part_number=Partnumber, pins=int(Pins),components=int(Components),connections=int(Connections))
        return Newtask
    except:
        print 'Cannot open Summary Report'
        return 'Cannot open Summary Report'
    #extract things from cbm file
    #deal with BoM

def getbigcomponents(source,Newtask):
    try:
        filehandle = open(source+'\\boardBOM.rpt','r')
        report=filehandle.read()
        m = re.search("(BET/)([\d-]*)", report)
        Partnumber=m.group(2)
        m = re.findall(r'(?=BGA|LGA).*(?:IC|IO)\D*([\d]+)', report)
        if m:
            BGAs = sum(map(int,m))
        else:
            BGAs = 0

        m = re.findall(r'(?=DIMM).*(?:IC|IO)\D*([\d]+)', report)
        if m:
            DIMMs = sum(map(int,m))
        else:
            DIMMs = 0
        #print Partnumber,BGAs,DIMMs
        # insert the informaiton to mysql database
        if Newtask.part_number==Partnumber:
            Newtask.bga_lgas=int(BGAs)
            Newtask.dimms=int(DIMMs)
            return Newtask
        else:
            return "Summary report and BOM report doesn't match"
    except:
        return 'Cannot open BoM Report'

def getconstraints(source, Newtask):
    filehandle = open(source+'\\cr\\report.html','r')
    report=filehandle.read()
    try:
        m=re.search(r"Report summary(.*)",report,re.S)
        report_summary=m.group(1)
        #print report_summary
        try:
            Buses = (re.search(r"Buses(.*?)(\d+)(?=</TD>)",report_summary)).group(2)
        except AttributeError:
            Buses = 0
        try:
            Constraintsets=re.search(r"ConstraintSets(.*?)(\d+)(?=</TD>)",report_summary).group(2)
        except AttributeError:
            Constraintsets = 0
        try:
            Diffpairs=re.search(r"DiffPairs(.*?)(\d+)(?=</TD>)",report_summary).group(2)
        except AttributeError:
            Diffpairs = 0
        try:
            Matchgroups=re.search(r"MatchGroups(.*?)(\d+)(?=</TD>)",report_summary).group(2)
        except AttributeError:
            Matchgroups = 0
        try:
            Netclasses=re.search(r"NetClasses(.*?)(\d+)(?=</TD>)",report_summary).group(2)
        except AttributeError:
            Netclasses = 0
        try:
            NetC=re.search(r"Nets(.*?)(\d+)(?=</TD>)",report_summary).group(2)
        except AttributeError:
            NetC = 0
        try:
            Pinpairs=re.search(r"PinPairs(.*?)(\d+)(?=</TD>)",report_summary).group(2)
        except AttributeError:
            Pinpairs = 0
        try:
            Xnets=re.search(r"Xnets(.*?)(\d+)(?=</TD>)",report_summary).group(2)
        except AttributeError:
            Xnets = 0
        Newtask.buses=int(Buses)
        Newtask.constraintsets=int(Constraintsets)
        Newtask.diffpairs=int(Diffpairs)
        Newtask.matchgroups=int(Matchgroups)
        Newtask.netclasses=int(Netclasses)
        Newtask.netc=int(NetC)
        Newtask.pinpairs=int(Pinpairs)
        Newtask.xnets=int(Xnets)
        print Pinpairs
        return Newtask
    except:
        return "Cannot Open Constraint Report!"

