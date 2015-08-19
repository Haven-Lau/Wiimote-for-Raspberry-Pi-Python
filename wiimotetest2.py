import cwiid
import time
import uinput

#initializes uinput object for keyboard buttons and mouse movements
device = uinput.Device([uinput.KEY_W,uinput.KEY_A,uinput.KEY_S,uinput.KEY_D,uinput.REL_X,uinput.REL_Y,uinput.BTN_LEFT,uinput.BTN_RIGHT,uinput.KEY_SPACE])

def main():

print 'Press button 1 + 2 on your Wii Remote...'
time.sleep(1.5)

#creates a wiimote object
wm=cwiid.Wiimote()
	print 'Wii Remote connected...'
	print '\nPress the PLUS button to disconnect the Wii and end the application'
time.sleep(1)

	#vibartion off	
	Rumble = False

	#initializes the values to be detected from wiimote
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_EXT

#sets led 1 to be displayed
#accepts value 0 – 15, leds display as binary of the value set
wm.led = 1

wm.state

#get the initial XYZ values as offset
defaultX = wm.state['acc'][cwiid.X]
defaultY = wm.state['acc'][cwiid.Y]
defaultZ = wm.state['acc'][cwiid.Z]

while True:
            
        time.sleep(0.01)
        if wm.state.has_key('nunchuk'):
            Rumble = False
        else:
            print 'no nunchuck found'

        #tilt forward, press ‘w’
        if (wm.state['acc'][cwiid.Z] - defaultZ) > 10:
            device.emit(uinput.KEY_W,1)
            device.emit(uinput.KEY_S,0)

        #tilt backward, press ‘s’
        elif (defaultZ - wm.state['acc'][cwiid.Z]) > 10:
            device.emit(uinput.KEY_S,1)
            device.emit(uinput.KEY_W,0)

        #stopped, release ‘w’/’s’
        else:
            device.emit(uinput.KEY_S,0)
            device.emit(uinput.KEY_W,0)
            
        #tilt right, press ‘d’
        if (wm.state['acc'][cwiid.X] - defaultX) > 10:
            device.emit(uinput.KEY_D,1)
            device.emit(uinput.KEY_A,0)

        #tilt left, press ‘a’
        elif (defaultX - wm.state['acc'][cwiid.X]) > 10:
            device.emit(uinput.KEY_A,1)
            device.emit(uinput.KEY_D,0)
		

        #stopped, release ‘a’/’d’
        else:
            device.emit(uinput.KEY_A,0)
            device.emit(uinput.KEY_D,0)
            
        #maps nunchuk joystick to mouse
        if (wm.state['nunchuk']['stick'][cwiid.X] - 128) > 10 or (128 - wm.state['nunchuk']['stick'][cwiid.X]) > 10:
            device.emit(uinput.REL_X,int((wm.state['nunchuk']['stick'][cwiid.X] - 128)/3), syn=False)
        else:
            device.emit(uinput.REL_X,0)
        if (wm.state['nunchuk']['stick'][cwiid.Y] - 128) > 10 or (128 - wm.state['nunchuk']['stick'][cwiid.Y]) > 10:    
            device.emit(uinput.REL_Y,-int((wm.state['nunchuk']['stick'][cwiid.Y] - 128)/4))
        else:
            device.emit(uinput.REL_Y,0)

        #shake nunchuk, press mouse right button
        if wm.state['nunchuk']['acc'][cwiid.Z] > 220:
            device.emit(uinput.BTN_RIGHT,1)
        #release mouse right button
        else:
            device.emit(uinput.BTN_RIGHT,0) 
            
        #press ‘A’ + ‘B’, recalibrate offset
        if wm.state['buttons'] == 12:
            defaultX = wm.state['acc'][cwiid.X]
            defaultY = wm.state['acc'][cwiid.Y]
            defaultZ = wm.state['acc'][cwiid.Z]
                
        #press ‘A’ + ‘+’ + ‘2’, disconnect
    if wm.state['buttons'] == 4106:
	print 'closing Bluetooth connection. Good Bye!'
	time.sleep(1)
	exit(wm)


if __name__ == '__main__':
    main()