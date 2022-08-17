# pip install pyautogui

import pyautogui

# pyautogui.sleep(3) # 3초간 대기
# print(pyautogui.position())

# pyautogui.click(56, 15, duration=1) # 1초 동안 (56, 15) 좌표를 클릭한다.
# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp() # 두개를 합치면 click이 된다. 드레그를 할때 사용한다.

# pyautogui.doubleClick() # 더블클릭
# pyautogui.click(clicks=2) # 더블클릭

# pyautogui.sleep(3) # 3초간 대기
# pyautogui.mouseDown()
# pyautogui.move(100, 100)
# pyautogui.move(100, -100)
# pyautogui.move(-100, -100)
# pyautogui.move(-100, 100)
# pyautogui.mouseUp()

# # 상처밴드 모양 만들기
# def dw():
#     pyautogui.mouseDown()
#     pyautogui.move(100, 100)
#     pyautogui.move(100, -100)
#     pyautogui.move(-100, -100)
#     pyautogui.move(-100, 100)
#     pyautogui.mouseUp()

# pyautogui.sleep(3) # 3초간 대기
# pyautogui.moveTo(250,250) 
# dw()
# pyautogui.moveTo(350,350) 
# dw()
# pyautogui.moveTo(250,450) 
# dw()
# pyautogui.moveTo(450,250) 
# dw()
# pyautogui.moveTo(450,450) 
# dw()

# pyautogui.sleep(1.5) # 3초간 대기
# pyautogui.rightClick() # 우 클릭
# pyautogui.middleClick() # 휠 클릭

# print(pyautogui.position())
# pyautogui.moveTo(868, 300)
# pyautogui.drag(-400, -300, duration=2) # 현재 위치에서 상대적으로 좌표만큼 이동
# pyautogui.dragTo(500, 0, duration=2) # 현재 위치에서 절대적으로 좌표로 이동

pyautogui.scroll(300) # 양수이면 위 방향으로, 음수이면 아래 방향으로 스크롤 이동