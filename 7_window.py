# pip install pyautogui
from time import sleep
import pyautogui

# 유동적인 창의 좌표를 이용한 클릭
# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 (VSCode)
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left+60, fw.top+20)

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기

# for w in pyautogui.getWindowsWithTitle("제목 없음"): # 제목이 "제목 없음"인 창을 찾아서 반환한다.
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화 ( 맨 앞으로 가져오기 )
pyautogui,sleep(1)

if w.isMaximized == False: # 창 최대화가 되어있지 않았다면
    w.maximize() # 창 최대화   
pyautogui,sleep(1)

if w.isMinimized == False: # 창 최소화가 되어있지 않았다면
    w.minimize() # 창 최소화
pyautogui,sleep(1)

w.restore() # 화면 원상복구

w.close() # 윈도우 닫기