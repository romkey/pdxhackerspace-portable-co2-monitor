import time
import board
import displayio
import busio

import adafruit_il0373
import adafruit_il0398
import adafruit_ssd1675
import adafruit_ssd1680

import adafruit_scd4x
import adafruit_bme680

from adafruit_pm25.uart import PM25_UART

import terminalio
import adafruit_display_text.label

from displayio import FourWire

IL0373 = 1
WAVESHARE_42 = 2
WAVESHARE_HAT_213 = 3
WAVESHARE_BW_29 = 4
WAVESHARE_BW_154 = 5
SSD1675 = 6
ADAFRUIT_TRI_154 = 7

DISPLAY_TYPE = WAVESHARE_42

print("Hello world")

displayio.release_displays()

print("Displays released")

spi = busio.SPI(board.IO7, board.IO9, board.IO8)
epd_cs = board.IO1
epd_dc = board.IO2
epd_reset = board.IO3
print("busio")

try:
    # SCL, SDA
    i2c = busio.I2C(board.IO6, board.IO5)
    i2c.try_lock()
    print(i2c.scan())
    i2c.unlock()
except:
    print("I2C fail")

try:
    scd4x = adafruit_scd4x.SCD4X(i2c)
    print("Serial number:", [hex(i) for i in scd4x.serial_number])

    scd4x.start_periodic_measurement()
except:
    print("SCD4x init failed")

try:
    bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
    # change this to match the location's pressure (hPa) at sea level
    bme680.sea_level_pressure = 1013.25
except:
    print("BME init failed")

try:
    # TX, RX
    uart = busio.UART(board.IO43, board.IO44, baudrate=9600)
    pm25 = PM25_UART(uart)
except:
    print("PM2.5 init failed")

display_bus = FourWire(
    spi, command=epd_dc, chip_select=epd_cs, reset=epd_reset, baudrate=1000000
)

print("SPI/display_bus created")

if DISPLAY_TYPE == IL0373:
    display = adafruit_il0373.IL0373()

if DISPLAY_TYPE == WAVESHARE_42:
    print("400x300 Waveshare 4.2in display")
    display = adafruit_il0398.IL0398(
        display_bus, width=300, height=400, seconds_per_frame=20
    )


if DISPLAY_TYPE == WAVESHARE_BW_154:
    print("200x200 BW display")
    display = adafruit_ssd1608.SSD1608(display_bus, width=200, height=200)


# Waveshare 2.13" e-ink hat rev 2.1
if DISPLAY_TYPE == WAVESHARE_HAT_213:
    display = adafruit_ssd1675.SSD1675(display_bus, width=250, height=122, rotation=270)

# Adafruit docs suggest also 1.54" and 2.13" tri-color, and 2.9" B&W
#    display_bus,
#    width=250,
#    height=122,
#    highlight_color=0xFF0000,
#    rotation=270,
# )

if DISPLAY_TYPE == WAVESHARE_BW_29:
    display = adafruit_ssd1680.SSD1680(
        display_bus,
        width=296,
        height=128,
        highlight_color=0xFF0000,
        rotation=270,
    )

if DISPLAY_TYPE == ADAFRUIT_TRI_154:
    print("Adafruit Tricolor 1.54 200x200")
    display = adafruit_ssd1681.SSD1681(display_bus, width=200, height=200, rotation=180)


g = displayio.Group()

temp_text = adafruit_display_text.label.Label(
    terminalio.FONT, color=0xFFFFFF, text="Hello world"
)
g.append(temp_text)
display.root_group = g
display.refresh()

print("displayed Hello World")

while True:
    try:
        print("\nTemperature: %0.1f C" % bme680.temperature)
        print("Gas: %d ohm" % bme680.gas)
        print("Humidity: %0.1f %%" % bme680.relative_humidity)
        print("Pressure: %0.3f hPa" % bme680.pressure)
        print("Altitude = %0.2f meters" % bme680.altitude)
        print()
    except:
        print("no BME")

    try:
        if scd4x.data_ready:
            print("CO2: %d ppm" % scd4x.CO2)
            print("Temperature: %0.1f *C" % scd4x.temperature)
            print("Humidity: %0.1f %%" % scd4x.relative_humidity)
            print()
    except:
        print("no SCD4x")

    try:
        aqdata = pm25.read()

        print()
        print("Concentration Units (standard)")
        print("---------------------------------------")
        print(
            "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
            % (
                aqdata["pm10 standard"],
                aqdata["pm25 standard"],
                aqdata["pm100 standard"],
            )
        )
        print("Concentration Units (environmental)")
        print("---------------------------------------")
        print(
            "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
            % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
        )
        print("---------------------------------------")
        print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
        print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
        print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
        print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
        print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
        print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
        print("---------------------------------------")

    except RuntimeError:
        print("No PM2.5")

    time.sleep(5)
