# pip install pyautogui 
import pyautogui

# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 17,15 33,117,173 #2175AD

pixel = pyautogui.pixel(17,15) # 해당 위치의 RGB값을 반환한다.
print(pixel)

print(pyautogui.pixelMatchesColor(17,15, pixel))