# pip install pyautogui
# pip install pyperclip

import pyautogui
from time import sleep
import sys
import pyperclip

# 그림판 열기
pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

# #그림판 최대화
pyautogui.sleep(1)
window = pyautogui.getWindowsWithTitle("제목 없음")[0]
if window.isMaximized == False: # 전체 창이 아니라면
    window.maximize() # 창 최대화

# 그림판에 글자 버튼 틀릭
pyautogui.sleep(1)
input_icon = pyautogui.locateOnScreen("text_input_icon.png", confidence=0.8)
if input_icon:
    pyautogui.click(input_icon)
else:
    print("찾기 실패")
    sys.exit()

# 흰 영역 틀릭
pyautogui.click(200, 200)
pyperclip.copy("참 잘했어요") # 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v") # 클립보드에 있는것을 붙여넣기

# 5초 대기
pyautogui.sleep(5)

# 그림판 종료(이미지 사용)
ex = pyautogui.locateOnScreen("exit.png", confidence=0.8)
pyautogui.click(ex)
pyautogui.sleep(1)
nosave = pyautogui.locateOnScreen("nosave.png", confidence=0.8)
pyautogui.click(nosave)

# 그림판 종료(단축키 사용)
# window.close()
# pyautogui.sleep(0.5)
# pyautogui.press("n")










# 자동화 프로그램 종료
# win : ctrl + shift + del
