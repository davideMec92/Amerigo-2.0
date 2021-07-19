import rssi
import time

class WifiRssiManager:
    ssids = []
    interface = 'wlan0'
    rssi_scanner = rssi.RSSI_Scan(interface)
    nearSignalThreshold = 40

    def __init__(self, ssids):
        self.ssids = ssids

    def getSsidsPowers(self):

        ssidPowers = []
        for x in 'necri':
            for ssidPowersMeasurements in self.rssi_scanner.getAPinfo(networks=self.ssids, sudo=True):
                ssidPowers.append(ssidPowersMeasurements)
                time.sleep(0.15)

        print("ssidPowers: " + str(ssidPowers))

        return self.getAvgSsidsPowers(ssidPowers, self.ssids)

    def getSsidPower(self, ssid):

        if ssid not in self.ssids:
            raise Exception('SSID not declared')

        ssidPowers = []
        for x in 'necri':
            for ssidPowersMeasurements in self.rssi_scanner.getAPinfo(networks=[ssid], sudo=True):
                ssidPowers.append(ssidPowersMeasurements)
                time.sleep(0.15)

        print("ssidPowers: " + str(ssidPowers))

        return self.getAvgSsidsPowers(ssidPowers, [ssid])


    def getAvgSsidsPowers(self, ssidPowers, ssids):

        avgSsidPowers = {}

        for ssid in ssids:
            ssidPowerSum = 0
            for ssidPower in ssidPowers:
                if ssidPower['ssid'] == ssid:
                    ssidPowerSum = ssidPowerSum + abs(ssidPower['signal'])

            if ssidPowerSum <= 0:
                avgSsidPowers[ssid] = None
            else:
                avgSsidPowers[ssid] = ssidPowerSum / 5

        print("avgSsidPowers: " + str(avgSsidPowers))

        return avgSsidPowers

    def getSsidNearToMe(self):
        ssidsPowers = self.getSsidsPowers()

        ssidNearToMe = None
        ssidNearToMeSignalPower = None

        for ssid, ssidPowerSignal in ssidsPowers.items():
            if ssidPowerSignal is not None and ssidPowerSignal <= self.nearSignalThreshold:
                if ssidNearToMeSignalPower is None:
                    ssidNearToMe = ssid
                    ssidNearToMeSignalPower = ssidPowerSignal
                elif ssidPowerSignal < ssidNearToMeSignalPower:
                    ssidNearToMe = ssid
                    ssidNearToMeSignalPower = ssidPowerSignal

        print ('ssidNearToMe: ' + str(ssidNearToMe))
        return ssidNearToMe
