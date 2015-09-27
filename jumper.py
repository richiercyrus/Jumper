#-----Jumper v 1.0---------
# Richie Cyrus @rrcyrus


import os, sys, getopt, datetime

def main(argv):
    path = ''
    try:
        opts, args = getopt.getopt(argv,"hp:",["dirPath="] )
    except getopt.GetoptError:
        print 'Jumper.py -p <path to Automatic Destination or Custom Destination Directory>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Jumper.py -p <path to Automatic Destination or Custom Destination Directory>'
            sys.exit()
        elif opt in ("-p", "--dirPath"):
            path = arg
            if (path.find('AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations')> -1):
                continue
            elif (path.find('AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations')> -1):
                continue
            else:
                print 'Jumper.py -p <path to Automatic Destination or Custom Destination Directory>'
                sys.exit()
            
    dirs = os.listdir(path)

    appIDDict = {'44a398496acc926d': 'Adobe Premiere Pro CS5 (64-bit)', 'b8c29862d9f95832': 'Microsoft Office InfoPath 2010 x86', '28c8b86deab549a1': 'Internet Explorer 8 / 9 / 10 (32-bit)',
     'a4a5324453625195': 'Microsoft Office Word 2013 x86', 'd5c3931caad5f793': 'Adobe Soundbooth CS5 (32-bit)', '9c7cc110ff56d1bd': 'Microsoft Office PowerPoint 2010 x86', '5c450709f7ae4396': 'Firefox 3.6.13 (32-bit)',
     '44a3621b32122d64': 'Microsoft Office Word 2010 x64', '12dc1ea8e34b5a6': 'Microsoft Paint 6.1', 'f0275e8685d95486': 'Microsoft Office Excel 2013 x86', '5d6f13ed567aa2da': 'Microsoft Office Outlook 2010 x64',
     '3094cdb43bf5e9c2': 'Microsoft Office OneNote 2010 x86', '89b0d939f117f75c': 'Adobe Acrobat 9 Pro Extended (32-bit)', '9839aec31243a928': 'Microsoft Office Excel 2010 x86',
     '84f066768a22cc4f': 'Adobe Photoshop CS5 (64-bit)', '65009083bfa6a094': 'app launched via XPMode)', '83b03b46dcd30a0e': 'iTunes 10', 'a8c43ef36da523b1': 'Microsoft Office Word 2003 Pinned and Recent.',
     '23646679aaccfae0': 'Adobe Reader 9 x64', 'b0459de4674aab56': '(.vmcx)', '5f6e7bc0fb699772': 'Microsoft Office PowerPoint 2010 x64', 'd38adec6953449ba': 'Microsoft Office OneNote 2010 x64',
     '6e855c85de07bc6a': 'Microsoft Office Excel 2010 x64', 'c7a4093872176c74': 'Paint Shop Pro Pinned and Recent.', '9b9cdc69c1c24e2b': 'Notepad (64-bit)', '26717493b25aa6e1': 'Adobe Dreamweaver CS5 (32-bit',
     'f5ac5390b9115fdb': 'Microsoft Office PowerPoint 2007', 'cdf30b95c55fd785': 'Microsoft Office Excel 2007', '5da8f997fd5f9428': 'Internet Explorer x64', 'c765823d986857ba': 'Adobe Illustrator CS5 (32-bit)',
     'e2a593822e01aed3': 'Adobe Flash CS5 (32-bit)', '918e0ecb43d17e23': 'Notepad (32-bit)', 'a7bd71699cd38d1c': 'Microsoft Office Word 2010 x86', 'be71009ff8bb02a2': 'Microsoft Office Outlook x86',
     'e70d383b15687e37': 'Notepad++ 5.6.8 (32-bit)', '7e4dca80246863e3': 'Control Panel (?)', 'd64d36b238c843a3': 'Microsoft Office InfoPath 2010 x86', 'bc03160ee1a59fc1': 'Foxit PDF Reader 5.4.5',
     '469e4a7982cea4d4': '(.job)', '271e609288e1210a': 'Microsoft Office Access 2010 x86', 'adecfb853d77462a': 'Microsoft Office Word 2007 Pinned and Recent', '23646679aaccfae0': 'Adobe Acrobat 9.4.0',
     '59f56184c796cfd4': 'ACDSee Photo Manager 10 (Build 219)', 'b39c5f226977725d': 'ACDSee Pro 8.1.99', 'f0468ce1ae57883d': 'Adobe Reader 7.1.0', 'e31a6a8a7506f733': 'Image AXS Pro 4.1',
     'ee462c3b81abb6f6': 'Adobe Reader X 10.1.0', '8bd5c6433ca967e9': 'ACDSee Photo Manager 2009 (v11.0 Build 113)', 'c2d349a0e756411b': 'Adobe Reader 8.1.2', '386a2f6aa7967f36': 'EyeBrowse 2.7',
     'd838aac097abece7': 'ACDSee Photo Manager 12 (Build 344)', '5df4765359170e26': 'Firefox 4.0.1', '8a1c1c7c389a5320': 'Safari 3.2.3 (525.29)', '5d696d521de238c3': 'Chrome 9.0.597.84 / 12.0.742.100 / 13.0.785.215 / 26',
     '1461132e553e2e6c': 'Firefox 6.0', '5c450709f7ae4396': 'Firefox 1.0 / 2.0 / 3.0', '1da3c90a72bf5527': 'Safari 4.0.5 (531.22.7) / 5.1 (7534.50)', '16ec093b8f51508f': 'Opera 8.54 build 7730 / 9.64 build 10487 / 11.50',
     'cfb56c56fa0f0a54': 'Mozilla 0.9.9', '1eb796d87c32eff9': 'Firefox 5.0', '28c8b86deab549a1': 'Internet Explorer 8 / 9', 'bfc1d76f16fa778f': 'Ares (Galaxy) 1.8.4 / 1.9.8 / 2.1.0 / 2.1.7.3041',
     'ba3a45f7fd2583e1': 'Blubster 3.1.1', 'f001ea668c0aa916': 'Cabos 0.8.2', '4a7e4f6a181d3d08': 'broolzShare', '1434d6d62d64857d': 'BitLord 1.2.0-66', '9ad1ec169bf2da7f': 'FlylinkDC++ r405 (Build 7358)',
     'c9374251edb4c1a8': 'BitTornado T-0.3.17', '2db8e25112ab4453': 'Deluge 1.3.3', '2ff9dc8fb7e11f39': 'I2P 0.8.8 (no window)', '2d61cccb4338dfc8': 'BitTorrent 5.0.0 / 6.0.0 / 7.2.1 (Build 25548)',
     '2437d4d14b056114': 'EiskaltDC++ 2.2.3', 'a75b276f6e72cf2a': 'Kazaa Lite Tools K++ 2.7.0', '223bf0f360c6fea5': 'I2P 0.8.8 (restartable)', 'e1d47cb031dafb9f': 'BearShare 6.0.0.22717 / 8.1.0.70928 / 10.0.0.112380',
     '73ce3745a843c0a4': 'FrostWire 5.1.4', 'c8e4c10e5460b00c': 'iMesh 6.5.0.16898', '4aa2a5710da3efe0': 'DCSharpHub 2.0.0', '784182360de0c5b6': 'Kazaa Lite 1.7.1', 'e6ea77a1d4553872': 'Gnucleus 1.8.6.0',
     'a31ec95fdd5f350f': 'BitComet 0.49 / 0.59 / 0.69 / 0.79 / 0.89 / 0.99 / 1.07 / 1.28', 'e73d9f534ed5618a': 'BitSpirit 1.2.0.228 / 2.0 / 2.6.3.168 / 2.7.2.239 / 2.8.0.072 / 3.1.0.077 / 3.6.0.550',
     'f61b65550a84027e': 'iMesh 11.0.0.112351', '5b186fc4a0b40504': 'Dtella 1.2.5 (Purdue network only)', 'cb5250eaef7e3213': 'ApexDC++ 1.4.3.957', 'a746f9625f7695e8': 'HeXHub 5.07', 'f214ca2dd40c59c1': 'FrostWire 4.20.9',
     'cbbe886eca4bfc2d': 'ExoSee 1.0.0', 'bcd7ba75303acbcf': 'BitLord 1.1', 'ccb36ff8a8c03b4b': 'Azureus 2.5.0.4 / Vuze 3.0.5.0', '76f6f1bd18c19698': 'aMule 2.2.6', 'cc4b36fbfb69a757': 'gtk-gnutella 0.97',
     '558c5bd9f906860a': 'BearShare Lite 5.2.5.1', 'b3016b8da2077262': 'eMule 0.50a', 'ed49e1e6ccdba2f5': 'GNUnet 0.8.1a', '98b0ef1c84088': 'fulDC 6.78', '4dd48f858b1a6ba7': 'Free Download Manager 3.0 (Build 852)',
     'e0f7a40340179171': 'imule 1.4.5 (rev. 749)', 'accca100973ef8dc': 'Azureus 2.0.8.4', 'd460280b17628695': 'Java Binary', '560d789a6a42ad5a': 'DC++ 0.261 / 0.698 / 0.782 (r2402.1)',
     'f1a4c04eebef2906': '[i2p] Robert 0.0.29 Preferences', '8f852307189803b8': 'Far Manager 2.0.1807', '2544ff74641b639d': 'WiseFTP 6.1.5', 'c99ddde925d26df3': 'Robo-FTP 3.7.9 CronMaker',
     '27da120d7e75cf1f': 'pbFTPClient 6.1', '10f5a20c21466e85': 'FTP Voyager 15.2.0.17', 'f82607a219af2999': 'Cyberduck 4.1.2 (Build 8999)', '4fceec8e021ac978': 'CoffeeCup Free FTP 3.5.0.0',
     '3a5148bf2288a434': 'Secure FTP 2.6.1 (Build 20101209.1254)', 'b7cb1d1c1991accf': 'FlashFXP 4.0.0 (Build 1548)', '79370f660ab51725': 'UploadFTP 2.0.1.0', '7904145af324576e': 'Total Commander 7.56a (Build 16.12.2010)',
     'fc999f29bc5c3560': 'Robo-FTP 3.7.9', '8deb27dfa31c5c2a': 'CoffeeCup Free FTP 4.4 (Build 1904)', '6a316aa67a46820b': 'Core FTP LE 1.3c (Build 1437) / 2.2 (Build 1689)',
     '3198e37206f28dc7': 'CuteFTP 8.3 Professional (Build 8.3.4.0007)', 'e107946bb682ce47': 'FileZilla 3.5.1', 'd28ee773b2cea9b2': '3D-FTP 9.0 build 7', '7937df3c65790919': 'FTP Explorer 10.5.19 (Build 001)',
     '4cdf7858c6673f4b': 'Bullet Proof FTP 1.26', '714b179e552596df': 'Bullet Proof FTP 2.4.0 (Build 31)', 'e42a8e0f4d9b8dcf': 'Sysax FTP Automation 5.15', 'b8c13a5dd8c455a2': 'Titan FTP Server 8.40 (Build 1338)',
     '4b632cf2ceceac35': 'Robo-FTP Server 3.2.5', 'f64de962764b9b0f': 'FTPRush 1.1.3 / 2.15', 'be4875bb3e0c158f': 'CrossFTP 1.75a', '9a3bdae86d5576ee': 'WinSCP 3.2.1 (Build 174) / 3.8.0 (Build 312)',
     'c54b96f328bdc28d': 'WiseFTP 7.3.0', 'e6ef42224b845020': 'ALFTP 5.20.0.4', 'b6267f3fcb700b60': 'WiseFTP 4.1.0', 'cd2acd4089508507': 'AbsoluteTelnet 9.18 Lite', '6a8b377d0f5cb666': 'WinSCP 2.3.0 (Build 146)',
     '226400522157fe8b': 'FileZilla Server 0.9.39 beta', 'a1d19afe5a80f80': 'FileZilla 2.2.32', '435a2f986b404eb7': 'SmartFTP 4.0.1214.0', '44a50e6c87bc012': 'Classic FTP Plus 2.15', 'a581b8002a6eb671': 'WiseFTP 5.5.9',
     '20ef367747c22564': 'Bullet Proof FTP 2010.75.0.75', 'c04f69101c131440': 'CuteFTP 5.0 (Build 50.6.10.2)', '6bb54d82fa42128d': 'WinSCP 4.3.4 (Build 1428)', 'f91fd0c57c4fe449': 'ExpanDrive 2.1.0',
     'a79a7ce3c45d781': 'CuteFTP 7.1 (Build 06.06.2005.1)', '49b5edbd92d8cd58': 'FTP Commander 8.02', '8628e76fd9020e81': 'Fling File Transfer Plus 2.24', '59e86071b87ac1c3': 'CuteFTP 8.3 (Build 8.3.4.0007)',
     'c01d68e40226892b': 'ClicksAndWhistles 2.7.146', 'd8081f151f4bd8a5': 'CuteFTP 8.3 Lite (Build 8.3.4.0007)', '9560577fd87cf573': 'LeechFTP 1.3 (Build 207)', 'fa7144034d7d083d': 'Directory Opus 10.0.2.0.4269 (JL tasks supported)',
     'b223c3ffbc0a7a42': 'Bersirc 2.2.14', '9e0b3f677a26bbc4': 'BitKinex 3.2.3'}

    def modification_date(filename):
        mtime = os.path.getmtime(filename)
        return datetime.datetime.fromtimestamp(mtime)

    def fileSize(filename):
        fsize = os.path.getsize(filename)
        return fsize


    #For each file in the directory, split by "." to strip out the appID
    for file in dirs:
        fileName = path + "\\" + file
        appID, dest = file.split(".")
        if appIDDict.has_key(appID):
            whatApp = appIDDict[appID]
            print "Application ID:" + appID + "    Application: " + whatApp + "   Date Modified:" + str(modification_date(fileName)) + "  File Size:" + str(fileSize(fileName)/1024) + " kb"
        else:
            print "Application ID:" + appID + "    Application not found for this ID."
        print "----------------------"

    
if __name__ == "__main__":
   main(sys.argv[1:])
