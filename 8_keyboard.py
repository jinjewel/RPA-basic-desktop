#  pip install pyautogui
import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("jinseok", interval=1) # interval=1 : 각 요소 사이에 1초씩 틈을 띄운다.
# pyautogui.write("안녕하세요") # pyautogui.write는 한글을 지원하지 않는다. 숫자, 영어만 받을수 있다.

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval=0.5)

# 특수문자
# shift + 4 -> $
# pyautogui.keyDown("shift") # shift를 누르고
# pyautogui.press("4") # 4를 입력하고
# pyautogui.keyUp("shift") # 다시 shift를 땐다.

# 조합키
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")@
# pyautogui.keyUp("ctrl")

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "a") # ctrl 누르고 > alt 누르고 > a 누르고 > a 때고 > alt 때고 > ctrl 때고 순서대로 진행한다.
# pyautogui.hotkey("ctrl", "a")

# for i in range(1,11):
#     pyautogui.hotkey("ctrl", "a")
#     pyautogui.hotkey("ctrl", "c")
#     pyautogui.press("right")
#     pyautogui.hotkey("ctrl", "v")

# 한글을 넘기는 방법
# pip install pyperclip

import pyperclip

pyperclip.copy("코딩") # "코딩" 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v") # 클립보드에 있는것을 붙여넣기

# 자동화 프로그램 종료
# win : ctrl + shift + del
