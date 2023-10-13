# CO2 Sensor List

|Device | Interface | Unit cost | Range | Avg Current | Sample Current | Voltage | datasheet
|------|-------|------|-----|--------|----------|------|------- 
|SCD30| I2C,UART,  PWM | $62 | 400 - 10,000ppm| | | | [datasheet](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/743/CD_DS_SCD30_Datasheet_D1.pdf)
|SCD40 | I2C         | $30 | 400 - 2000ppm | | | | [datasheet](https://cdn.sparkfun.com/assets/d/4/9/a/d/Sensirion_CO2_Sensors_SCD4x_Datasheet.pdf) |
|SCD41 | I2C         | $37 | 400 - 5000ppm | | | | [datasheet](https://cdn.sparkfun.com/assets/d/4/9/a/d/Sensirion_CO2_Sensors_SCD4x_Datasheet.pdf) |
|Senseair S8| UART, I2C | $47 | 400 - 2000ppm | 30mA | | 4.5-5.25V| [datasheet](https://rmtplusstoragesenseair.blob.core.windows.net/docs/publicerat/PSP107.pdf)
|Senseair Sunrise | UART, I2C | $55 | 400 - 5000ppm | 34 µA | 90mA | 3.05-5.5 V | [datasheet](https://rmtplusstoragesenseair.blob.core.windows.net/docs/Dev/publicerat/PSH12460.pdf)
|MH-Z14A | UART | 
|MH-Z19B | UART |
|MQ135| analog | $6 |10～1000ppm | 40mA | 40mA | 5V| [datasheet](https://www.olimex.com/Products/Components/Sensors/Gas/SNS-MQ135/resources/SNS-MQ135.pdf)

* CCS811 and ENS160 are I2C "eCO2" sensors which estimate CO2, not a true CO2 sensors

