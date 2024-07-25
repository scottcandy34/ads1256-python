# ADS1256-python
This is a Python wrapper using sdidev and RPi.GPIO python libraries. Please make sure to install both.

## Installation

1. Install dependencies

		sudo pip install spidev RPi.GPIO

2. Download this library and place in project directory

## Usage
There is an example.py that has simple code of it working.

#### Create the adc by:
```
DRDY_PIN = 17

adc = ADS1256(DRDY_PIN, None, 0)
```
Where the `0` is the SDI bus number. Replace None the CS pin; has to be a different GPIO than the one for the bus.

#### Initialize the adc by:
```
from ads1256.constants import DRATE, ADCON

SPI_SPEED = 2500000
GAIN = ADCON.PGA.g_1
DATA_RATE = DRATE.sps_1000

adc.init(SPI_SPEED, GAIN, DATA_RATE)
```

The `SPI_SPEED` is in Hz. Select the gain from `ADCON.PGA.` it follows the ADS1256 datasheet. Select the Data rate from `DRATE.` it also follows the datasheet. Once it is initialized you can call any of the functions from `adc.` to communicate to the ADS1256 board.

#### To read the all 8 channels call:
```
values = adc.read_channels()
```
This will return a Tuple with 8 values

#### Or to read the diff channels call:
```
values = adc.read_diff_channels()
```
#### To return one channel call:
single channel
```
from ads1256.constants import MUX
value = adc.read_digital_out(MUX.PSEL.i_0 | MUX.ncom)
```
diff channel
```
from ads1256.constants import MUX
value = adc.read_digital_out(MUX.PSEL.i_0 | MUX.NSEL.i_1)
```
#### Close
call `adc.close()` this will close out of both sdidev and GPIO

## Multiple SDI buses or CS ports.
Right now it can only handle 1 cs per sdi bus. But it can handle all 6 sdi buses at once. 

## Voltage Reading
To read back the correct voltages, declare `from ads1256.tools import convertToVoltage` and call by `voltage = convertToVoltage(values[0], VREF, GAIN)` where `GAIN` is the same as above and `VREF` is either default of 2.5 or what ever you measured it from the device is.