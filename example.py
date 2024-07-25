from ads1256.board import ADS1256
from ads1256.constants import DRATE, ADCON
from ads1256.tools import convertToVoltage

# Pins
DRDY_PIN = 17

# Settings
SPI_SPEED = 2500000
GAIN = ADCON.PGA.g_1
DATA_RATE = DRATE.sps_1000
VREF = 2.5 # calculated from multimeter on pin 4 of the ads1256

adc = ADS1256(DRDY_PIN, None, 0)

adc.init(SPI_SPEED, GAIN, DATA_RATE)

while(1):
    values = adc.read_channels()
    voltage = convertToVoltage(values[0], VREF, GAIN)
    print(voltage)