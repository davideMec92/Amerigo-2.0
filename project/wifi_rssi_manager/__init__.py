from threading import Thread
import rssi
import time

class WifiRssiManager(Thread):
    interface = 'wlan0'
    rssi_scanner = rssi.RSSI_Scan(interface)
    nearSignalThreshold = 33
    continuoslyScanStatus = 'ENABLED'

    def __init__(self):
        self.ssids = []
        self.wifiSsids = []
        self.wifiSsidsToNormalAssoc = {}
        self.wifiSsidsMeasurements = {}
        Thread.__init__(self)
        self.name = self.__class__.__name__

    def run(self):
        while self.continuoslyScanStatus == 'ENABLED':
            if len(self.wifiSsids) == 0:
                continue
            for ssidPowersMeasurements in self.rssi_scanner.getAPinfo(networks=self.wifiSsids, sudo=True):
                self.wifiSsidsMeasurements[ssidPowersMeasurements['ssid']] = abs(ssidPowersMeasurements['signal'])

    def parseSsidToWifiSyntax(self, ssid):
        return ssid if len(ssid) <= 30 else ssid[0:30]

    def stopContinuoslyScanStatus(self):
        self.continuoslyScanStatus = 'DISABLED'

    def getWifiSsidsMeasurements(self):
        return self.wifiSsidsMeasurements

    def getWifiSsidMeasurements(self, ssid):
        ssid = self.parseSsidToWifiSyntax(ssid)
        if ssid in self.wifiSsidsMeasurements:
            return self.wifiSsidsMeasurements[ssid]
        return None

    def setSsids(self, ssids):
        self.ssids = ssids
        self.wifiSsids = []
        self.wifiSsidsToNormalAssoc = {}
        for ssid in self.ssids:
            wifiSsid = self.parseSsidToWifiSyntax(ssid)
            self.wifiSsids.append(wifiSsid)
            self.wifiSsidsToNormalAssoc[wifiSsid] = ssid
        print('wifiSsidsToNormalAssoc: ' + str(self.wifiSsidsToNormalAssoc))
        print('wifiSsids: ' + str(self.wifiSsids))

    def getSsidsPowers(self):

        if len(self.wifiSsids) == 0:
            return None

        ssidPowers = []
        for x in 'necri':
            for ssidPowersMeasurements in self.rssi_scanner.getAPinfo(networks=self.wifiSsids, sudo=True):
                ssidPowers.append(ssidPowersMeasurements)
                time.sleep(0.15)

        print("ssidPowers: " + str(ssidPowers))

        return self.getAvgSsidsPowers(ssidPowers, self.wifiSsids)

    def getSsidPower(self, ssid, convertSsidsToNormal = False):

        ssid = self.parseSsidToWifiSyntax(ssid)

        if ssid not in self.wifiSsids:
            raise Exception('SSID not declared in wifi ssids')

        ssidPowers = []
        for x in 'necri':
            for ssidPowersMeasurements in self.rssi_scanner.getAPinfo(networks=[ssid], sudo=True):
                ssidPowers.append(ssidPowersMeasurements)
                time.sleep(0.15)

        print("ssidPowers: " + str(ssidPowers))

        return self.getAvgSsidsPowers(ssidPowers, [ssid], convertSsidsToNormal)


    def getAvgSsidsPowers(self, ssidPowers, ssids, convertSsidsToNormal = False):

        avgSsidPowers = {}

        for ssid in ssids:
            ssidPowerSum = 0
            for ssidPower in ssidPowers:
                if ssidPower['ssid'] == ssid:
                    ssidPowerSum = ssidPowerSum + abs(ssidPower['signal'])

            if ssidPowerSum <= 0:
                avgSsidPowers[self.wifiSsidsToNormalAssoc[ssid] if convertSsidsToNormal is True else ssid] = None
            else:
                avgSsidPowers[self.wifiSsidsToNormalAssoc[ssid] if convertSsidsToNormal is True else ssid] = ssidPowerSum / 5

        print("avgSsidPowers: " + str(avgSsidPowers))

        return avgSsidPowers

    def getSsidNearToMe(self):
        ssidsPowers = self.getSsidsPowers()

        ssidNearToMe = None
        ssidNearToMeSignalPower = None

        if ssidsPowers is not None:
            for ssid, ssidPowerSignal in ssidsPowers.items():
                if ssidPowerSignal is not None and ssidPowerSignal <= self.nearSignalThreshold:
                    if ssidNearToMeSignalPower is None:
                        ssidNearToMe = ssid
                        ssidNearToMeSignalPower = ssidPowerSignal
                    elif ssidPowerSignal < ssidNearToMeSignalPower:
                        ssidNearToMe = ssid
                        ssidNearToMeSignalPower = ssidPowerSignal

        print ('ssidNearToMe: ' + str(ssidNearToMe))

        if ssidNearToMe is None:
            return None

        return self.wifiSsidsToNormalAssoc[ssidNearToMe]

    def checkIfSsidIsNearToMe(self, ssid):
        ssidPower = self.getWifiSsidMeasurements(self.parseSsidToWifiSyntax(ssid))

        if ssidPower is None:
            return False

        print(str(ssid) + ' Power: ' + str(ssidPower))

        if 0 < ssidPower <= self.nearSignalThreshold:
            return True

        return False