import cv2 as cv

path = "/home/test/spect" 

spectrogramm = cv.imread(path)

if spectrogramm is None:
    print('cant find file')
    exit(0)

input_vec = open('vec_info.txt','r')
image_vec = input_vec.read()

if image_vec is None:
   print('vector is empty')
   exit(0)

color = (255,0,0) #BGR color for borders 
thickness = 2

#checking energy 
energy_exist = false
if image_vec[0] == 0:
    energy_exist = true

#signal band calc
band = 60e6 #MHz band
band_percent = image_vec[1]
band_herz = (band/100)*band_percent

#text for image
modulations = ('cant define modulation','8-PSK','16-PSK','32-PSK','8-QAM','16-QAM','32-QAM')
mod_text = modulations[image_vec[2]]

#display params
win_name = 'spectrogramm'
font = cv.FONT_HERSHEY_PLAIN
color_t = (255,0,0)
thickness_t =1
#start_p =
#end_p =
#mt_leftp = 
#bt_leftp = 

#display rectangle and text
if energy_exist:
    spectrogramm = cv.rectangle(spectrogramm, start_p, end_p, color, thickness)
    spectrogramm = cv.putText(spectrogramm, mod_text, mt_leftp, font, .5, color_t, thickness_t, cv.LINE_AA)
    spectrogramm = cv.putText(spectrogramm, band_percent, bt_leftp, font, .5, color_t, thickness_t, cv.LINE_AA)
    
    cv.imshow(win_name,spectrogramm)
    if cv.waitKey(0) & 0xFF == ord('q')
        cv.destroyAllWindows()
        exit(0)
else:
    print('no detected signals')
    cv.imshow(win_name,spectrogramm)
    if cv.waitKey(0) & 0xFF == ord('q')
        cv.destroyAllWindows()
        exit(0)




