# Raspberry Pi Motion Detection Security Camera

Requirements:
  * Raspberry Pi with Internet connection
  * PIR Motion Sensor
  * Pi Camera Module

## Set Up:
  * Connect PIR sensor
     * Vcc + 5V: Pin 2
     * GND: Pin 6
     * Data: Pin 11
  * Connect Pi Camera Module via camera port
  * Install all requirements
  * Set up creds.txt file
     * "send_address" is the gmail address to send from
     * "password_for_send_address" is the password for the gmail account (I recommend setting up an app password for security)
     * "recieve_address" is the email address that you would like the notifications to be sent to
