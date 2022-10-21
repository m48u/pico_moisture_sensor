import machine
import utime

analog_value = machine.ADC(26)

while(True):
    read = analog_value.read_u16()
    print("ADC: ", read)
    print(type(read))
    utime.sleep(0.5)
