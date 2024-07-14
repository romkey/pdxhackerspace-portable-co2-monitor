# Prototype

I built a quick prototype using STEMMA QT/Qwiic connectors. I didn't have any BME280s handy so I used the BME680, which is basically the same thing with a VOC sensor added to it.

STEMMA QT and Qwiic are Adafruit and Sparkfun's branding for identical connectors that allow you to quickly connect 3.3V I2C boards. I2C is great for sensors and very small monochrome displays but it's not fast enough for larger or more colorful displays that need much more data transferred. I2C devices rarely support speeds faster than 400Kbps. Displays that need more speed generally use SPI or parallel or proprietary interfaces.

## Parts

[Adafruit ESP32-S3 QT PY](https://learn.adafruit.com/adafruit-qt-py-esp32-s3/overview)
[SCD40](https://learn.adafruit.com/adafruit-scd-40-and-scd-41)
[BME680](https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas)
[PMSA003I](https://learn.adafruit.com/pmsa003i)
[OLED display]()

## Software

ESPHome components:
[SCD40](https://esphome.io/components/sensor/scd4x)
[BME680](https://esphome.io/components/sensor/bme680)
[PMSA003I](https://esphome.io/components/sensor/pmsa003i)
[SSD1306 OLED](https://esphome.io/components/display/ssd1306)
[Display pages](https://esphome.io/components/display/#display-pages)
[Graphs](https://esphome.io/components/display/#graph-component)

## TODO

The first prototype serves as a proof-of-concept. There are still several areas that need to be verified:

1. running off a battery
2. wireless charging
3. SPI TFT display
4. e-ink display
5. PMS5003 via serial

