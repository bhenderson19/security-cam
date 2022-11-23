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
  * Install repo onto raspberry pi
  * Install all requirements
  * Set up creds.txt file
     * "send_address" is the gmail address to send from
     * "password_for_send_address" is the password for the gmail account (I recommend setting up an app password for security)
     * "recieve_address" is the email address that you would like the notifications to be sent to

## Running:
To run the program, run the "security-cam.py" file.

I recommend editing the \etc\rc.local file (or using another method) to run the program from boot. This way, the raspberry pi just needs to be switched on for the program to run.

## Notes:
I would recommend getting a large sd card. Once motion has been detected, the program will record the video and attempt to send an email notification. If the raspberry pi were to lose Wi-Fi connection, the email would not send. To overcome this, the video file will be saved. This allows you to have access the recordings, even without a Wi-Fi connection.
