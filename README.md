_Settings are kept in a personal file on my home machine._

### To take pictures;
  * from the macbook: `sshpi5`
  * through the terminal;
    1. go to the source dir: `cd /home/pi/picturecollector/src/`
    2. reset the picture count: `python3 cheese.py -r`
    3. take a picture: `python3 cheese.py -c`
  * pictures are saved in the pi in `/home/pi/picturecollector/src/webcam/`

### Transfer pics
  * from the macbook;
    ```bash
    cd /home/pi/picturecollector/src/
    transferpics
    ```
  * pictures will be saved to `${GH}/picturecollector/pictures/webcam/`
  * view the pictures with: `open <somepic>`

### In case of error recognizing camera
  * from the pi, through the terminal on the macbook: `sudo reboot`
    or,
  * `python3 cheese.py -R`



### Other Notes
  * from the macbook:
	```bash
    scp pi@192.168.1.33:/home/pi/Pictures/webcam/* ${GH}/picturecollector/pictures/
    ```
    This was converted to the transferpics command

  * list controls with: `fswebcam -d /dev/video0 --list-controls`
  * list EDITED controls with: `fswebcam -d /dev/video0 --list controls -c /home/pi/picturecollector/src/c525config.txt`

### Settings
  * captured the settings with: `v4l2-ctl --list-ctrls`

c525 controls:  

Available Controls|Current Value|Range
:---|:---|---:
Brightness|128 (50%)|0 to 255
Contrast|32 (12%)|0 to 255
Saturation|32 (12%)|0 to 255
White Balance Temperature, Auto|True|True or False
Gain|64 (25%)|0 to 255
Power Line Frequency|60 Hz|Disabled or 50 Hz or 60 Hz
White Balance Temperature|5500 (72%)|2800 to 6500
Sharpness|22 (8%)|0 to 255
Backlight Compensation|1|0 to 1
Exposure, Auto|"Aperture Priority Mode" or "Manual Mode"|Aperture Priority Mode
Exposure (Absolute)|166 (7%)|3 to 2047
Exposure, Auto Priority|True|True or False
Pan (Absolute)|0 (50%)|-36000 to 36000
Tilt (Absolute)|0 (50%)|-36000 to 36000
Focus (absolute)|60 (23%)|0 to 255
Focus, Auto|True|True or False
Zoom, Absolute|1|1 to 5

Adjusted resolution from 384x288 to 352x288.

### fswebcam controls
Usage: `fswebcam [<options>] <filename> [[<options>] <filename> ... ]`  
 Options:

|flag|long name|description
:---|:---|:---
| -? |--help                    |Display this help page and exit.
| -c |--config `<filename>`     |Load configuration from file.
| -q |--quiet                   |Hides all messages except for errors.
| -v |--verbose                 |Displays extra messages while capturing
|    |--version                 |Displays the version and exits.
| -l |--loop `<seconds>`        |Run in loop mode.
| -b |--background              |Run in the background.
| -o |--output `<filename>`     |Output the log to a file.
| -d |--device `<name>`         |Sets the source to use.
| -i |--input `<number/name>`   |Selects the input to use.
| -t |--tuner `<number>`        |Selects the tuner to use.
| -f |--frequency `<number>`    |Selects the frequency use.
| -p |--palette `<name>`        |Selects the palette format to use.
| -D |--delay `<number>`        |Sets the pre-capture delay time. (seconds)
| -r |--resolution `<size>`     |Sets the capture resolution.
|    |--fps `<framerate>`       |Sets the capture frame rate.
| -F |--frames `<number>`       |Sets the number of frames to capture.
| -S |--skip `<number>`         |Sets the number of frames to skip.
|    |--dumpframe `<filename>`  |Dump a raw frame to file.
| -s |--set `<name>=<value>`    |Sets a control value.
|    |--revert                  |Restores original captured image.
|    |--flip `<direction>`      |Flips the image. (h, v)
|    |--crop `<size>[<offset>]` |Crop a part of the image.
|    |--scale `<size>`          |Scales the image.
|    |--rotate `<angle>`        |Rotates the image in right angles.
|    |--deinterlace             |Reduces interlace artifacts.
|    |--invert                  |Inverts the images colours.
|    |--greyscale               |Removes colour from the image.
|    |--swapchannels `<c1c2>`   |Swap channels c1 and c2.
|    |--no-banner               |Hides the banner.
|    |--top-banner              |Puts the banner at the top.
|    |--bottom-banner           |Puts the banner at the bottom. (Default)
|    |--banner-colour `<colour>`|Sets the banner colour. (#AARRGGBB)
|    |--line-colour `<colour>`  |Sets the banner line colour.
|    |--text-colour `<colour>`  |Sets the text colour.
|    |--font `<[name][:size]>`  |Sets the font and/or size.
|    |--no-shadow               |Disables the text shadow.
|    |--shadow                  |Enables the text shadow.
|    |--title `<text>`          |Sets the main title. (top left)
|    |--no-title                |Clears the main title.
|    |--subtitle `<text>`       |Sets the sub-title. (bottom left)
|    |--no-subtitle             |Clears the sub-title.
|    |--timestamp `<format>`    |Sets the timestamp format. (top right)
|    |--no-timestamp            |Clears the timestamp.
|    |--gmt                     |Use GMT instead of local timezone.
|    |--info `<text>`           |Sets the info text. (bottom right)
|    |--no-info                 |Clears the info text.
|    |--underlay `<PNG image>`  |Sets the underlay image.
|    |--no-underlay             |Clears the underlay.
|    |--overlay `<PNG image>`   |Sets the overlay image.
|    |--no-overlay              |Clears the overlay.
|    |--jpeg `<factor>`         |Outputs a JPEG image. (-1, 0 - 95)
|    |--png `<factor>`          |Outputs a PNG image. (-1, 0 - 10)
|    |--save `<filename>`       |Save image to file.
|    |--exec `<command>`        |Execute a command and wait for it to complete.
    
The commands I want to use:  

flag|long name|description
:---|:---|:---
 -o,|--output `<filename>`      |Output the log to a file.
 -d,|--device `<name>`          |Sets the source to use.
 -i,|--input `<number/name>`    |Selects the input to use.
 -p,|--palette `<name>`         |Selects the palette format to use.
 -r,|--resolution `<size>`      |Sets the capture resolution.
 -s,|--set `<name>=<value>`     |Sets a control value.
    |--flip `<direction>`       |Flips the image. (h, v)
    |--crop `<size>[<offset>]`  |Crop a part of the image.
    |--scale `<size>`           |Scales the image.
    |--rotate `<angle>`         |Rotates the image in right angles.
    |--greyscale                |Removes colour from the image.
    |--no-banner                |Hides the banner.

### YouTube Notes
[This video](https://www.raspberrypi.org/forums/viewtopic.php?t=142489) showed this info.

Setting|Values
:---|:---
brightness (int)|min=30 max=255 step=1 default=-8193 value=116
contrast (int)|min=0 max=10 step=1 default=57343 value=5
saturation (int)|min=0 max=200 step=1 default=57343 value=103
white balance temperature auto (bool)|default=1 value=1
power line frequency (menu)|min=0 max=2 default=2 value=2
white balance temperature (int)|min=2500 max=10000 step=1 default=57343 value=4500 flags=inactive
sharpness (int)|min=0 max=50 step=1 default=57343 value=25
backlight compensation (int)|min=0 max=10 step=1 default=57343 value=0
exposure auto (menu)|min=0 max=3 default=0 value=3
exposure absolute (int)|min=1 max=10000 step=1 default=156 value=156 flags=inactive
pan absolute (int)|min=-529200 max=529200 step=3600 default=0 value=0
tilt absolute (int)|min=-432000 max=432000 step=3600 default=0 value=0
focus absolute (int)|min=0 max=40 step=1 default=57343 value=0
focus auto (bool)|default=1 value=0
zoom absolute (int)|min=0 max=317 step=1 default=57343 value=0
