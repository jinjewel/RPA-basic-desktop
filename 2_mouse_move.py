# pip install pyautogui

import pyautogui

# 절대 좌표로 마우스 이동
# pyautogui.moveTo(200, 100) # 지정한 위치(가로, 세로)로 마우스를 이동
# pyautogui.moveTo(100, 200, duration=0.25) # o.25초 동안 100, 200 위치로 이동한다.

# pyautogui.moveTo(100, 100, duration=0.25)
# pyautogui.moveTo(200, 200, duration=1)
# pyautogui.moveTo(300, 300, duration=4)

# 상대 좌표로 마우스 이동 (현재 커서가 있는 위치로부터)
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position()) # print(x, y)
# pyautogui.move(200, 200, duration=1)
# print(pyautogui.position()) # print(x, y)
# pyautogui.move(300, 300, duration=4)
# print(pyautogui.position()) # print(x, y)

p = pyautogui.position()
print(p[0], p[1]) 
print(p.x , p.y)

