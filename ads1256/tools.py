def convertToVoltage(rawData: int, vref: float, gain: int):
    """Converts raw data bytes from ads1256 to voltage mesurement"""
    if rawData > 0x7FFFFF: # if the 24th digit (sign) is 1, the number is negative
        rawData -= 16777216;  # conversion for the negative sign
        # "mirroring" around zero
        # 16777216 = 2^{24}
        #  2^{24} - 1 = 0x7FFFFF = 16777215

    voltage = ((2 * vref) / 8388608) * rawData / (pow(2, gain)) #8388608 = 2^{23} - 1
    #REF: p23, Table 16.

    return voltage