# pip install pyautogui 
import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# test = pyautogui.locateOnScreen("test.png")
# print(test)
# pyautogui.click(test)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen) # 이미지를 찾지 못하면 None으로 반환한다.

# for i in pyautogui.locateAllOnScreen("file_menu.png"):
#     print(i)
#     pyautogui.click(i) # 같은 모양이 여러 개 일때 모든 정보를 불러와서 하나씩 선택을 한다.

# 속도 개선
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True) # grayscale=True : 색상을 흑백으로 통일한다음 이미지를 찾는다. 
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정
# pyautogui.mouseInfo()
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1798,669, 150,40)) # region=(x, y, width, height) : 범위를 지정하여 그 사이에서 매칭을 한다. 
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정
# pip install opencv-python
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.8) # confidence=0.8 : 80%만 일치해도 같은 이미지라고 인식하게 한다.
# pyautogui.moveTo(run_btn)


# 자동화 대상이 바로 보여지지 않는 경우
# 1. 무한반복을 이용한 방법(계속 기다리기)
# while menu_note is None: 
#     menu_note = pyautogui.locateOnScreen("menu_note.png", confidence=0.8)
#     print("발견 실패") 
# pyautogui.moveTo(menu_note)

# 2. 일정 시간동안 기다리기 (Time_out)
# import time
# import sys

# timeout = 5 # 5초 대기
# start = time.time() # 시작 시간 설정
# menu_note = None
# while menu_note is None:
#     menu_note = pyautogui.locateOnScreen("menu_note.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()
# pyautogui.moveTo(menu_note)        

# 함수로 만들어서 사용하기

import time
import sys

def find_target(img_file, timeout):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end-start > timeout:
            print("time over")
            break
    return target    

def my_click(img_file, timeout):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.moveTo(target)
    else:
        print(f"[Timeout {timeout}s] Target not find {img_file}")    
        sys.exit()

my_click("menu_note.png", 6)