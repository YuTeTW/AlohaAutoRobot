# import os
# with open("C:/Users/Dave/OneDrive - fastwise.net/Dave" + "/abc.txt", "wt") as file:
#     file.write("hello")

import pyautogui
import time
import os

timer = 0.1 #間隔時間
#地點三部
# source = [1, 2, 3, 4]
# for i in source:
#     for
pyautogui.click(x=130, y=43, duration=timer)
pyautogui.click(x=167, y=70, duration=timer)
pyautogui.click(x=1153, y=380, duration=timer)

#選擇氣象
pyautogui.click(x=183, y=44, duration=timer)
pyautogui.click(x=237, y=100, duration=timer)
pyautogui.click(x=546, y=105, duration=timer)
#輸入風速
pyautogui.typewrite('20')
#輸入風向
pyautogui.click(x=826, y=328, duration=timer)
pyautogui.typewrite('20')
#輸入溫度
pyautogui.click(x=1022, y=746, duration=timer)
pyautogui.typewrite('20')
#點擊確認
pyautogui.click(x=1082, y=688, duration=timer)


#化學4不
pyautogui.click(x=201, y=43, duration=timer)
pyautogui.click(x=252, y=79, duration=timer)
pyautogui.click(x=773, y=426, duration=timer)
pyautogui.click(x=1194, y=398, duration=timer)

#Direct 4不
pyautogui.click(x=209, y=59, duration=timer)
pyautogui.click(x=247, y=127, duration=timer)
pyautogui.click(x=590, y=144, duration=timer)
#選擇單位(公斤)
pyautogui.click(x=897, y=370, duration=timer)
#選擇瞬間
#pyautogui.click(x=1010, y=479, duration=1)
#選擇持續
pyautogui.click(x=1010, y=479, duration=timer)
pyautogui.click(x=729, y=565, duration=timer)
#輸入洩漏量
pyautogui.typewrite('2')
pyautogui.click(x=857, y=563, duration=timer)
#輸入時間
#pyautogui.click(x=1087, y=567, duration=1)
#pyautogui.typewrite('2')
#輸入高度
pyautogui.click(x=898, y=638, duration=timer)
pyautogui.typewrite('25')
#按下確認
pyautogui.click(x=827, y=695, duration=timer)

#顯示危害強度
pyautogui.click(x=254, y=46, duration=timer)
pyautogui.click(x=349, y=164, duration=timer)


#建立資料夾
localtime = time.localtime()
result = time.strftime("%S",localtime)
#path = 'strength/Direct/'+result
path = r"C:\Users\user\OneDrive - fastwise.net\Desktop\strength\Direct"+"\\"+result
os.mkdir(path)

#截圖
pngpath = path+'/'+result+'.png'
pyautogui.screenshot(pngpath,region=(587, 338, 900, 500))
#pyautogui.click(pyautogui.locateCenterOnScreen('None.png'))

#Alo檔
pyautogui.click(x=21, y=50, duration=timer)
pyautogui.click(x=58, y=184, duration=timer)
#輸入檔名路徑
pyautogui.click(x=518, y=789, duration=timer)
outpath = r"C:\Users\user\OneDrive - fastwise.net\Desktop\strength\Direct"
alopath = outpath +"\\"+ result+"\\"+result+'.alo'
pyautogui.typewrite(alopath)

#存檔
pyautogui.click(x=1244, y=691, duration=timer)