# pip install pyautogui

import pyautogui

# 마우스 정보(좌표, 색상 등)
# pyautogui.mouseInfo()

# pyautogui.FAILSAFE = False # 자동화중 마우스를 모서리에 가져다 놔도 실행이 계속 된다.

pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용

for i in range(1,11):
    pyautogui.move(100,100)
    # pyautogui.sleep(0.5)
    # 자동화가 되고 있을때 실행을 종료하고 싶으면 마우스를 네 귀퉁이로 갔다 놓으면된다.

