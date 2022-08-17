# 파일 기본

import os
# print(os.getcwd()) # current working directory 현재 작업 공간
# os.chdir("RPA(RoboticProcessAutomation)") # RPA(RoboticProcessAutomation) 으로 작업 공간 이동
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd())
# os.chdir("C:/")# 주어진 절대 경로로 이동
# print(os.getcwd())

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(),"my_file.txt") # 절대경로 생성
# print(file_path)

# 파일경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"c:/ohcoding/RPA(RoboticProcessAutomation)/2_desttop/11_file_system.py"))

# # 파일 정보 가져오기
# import time
# import datetime

# # 파일의 생선 날
# file_path = r"RPA(RoboticProcessAutomation)\2_desttop\11_file_system.py"
# ctime = os.path.getctime(file_path)
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime))
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S")) # 날짜 정보를 strftime을 통해 연원일 시분초 형태로 출력

# # 파일의 수정날짜
# mtime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime(file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# # 파일 크기
# size = os.path.getsize(file_path)
# print(size) # 크기를 바이트 단위로 가져온다.


# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록을 가져오기
# print(os.listdir("RPA(RoboticProcessAutomation)")) # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기

# 파일 목록 가져오기 (하위 폴더 모두 포함)
# result = os.walk("RPA(RoboticProcessAutomation)")
# print(result)
# for root, dirs, files in result:
#     print(root) # 주어진 폴더 밑에서 모든 폴더, 파일 목록을 list로 가져오기
#     print()
#     print(dirs) # root 안에 있는 서로 다른 폴더들
#     print()
    # print(files) # dir 폴더안에 있는 하위 폴더, 파일들
    # print()

# 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root, name))
# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, *.txt, 자동화*.png
# import fnmatch
# from unittest import result
# pattern = "*.py" # .py로 끝나는 모든 파일
# result = []
# for root, dir, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): # 이름이 패턴과 일치하면
#             result.append(os.path.join(root, name))
# print(result)            

# 주어진 경로가 파일인지, 폴더인지?
# print(os.path.isdir("RPA(RoboticProcessAutomation)")) # 해당 경로는 폴더인가? Ture
# print(os.path.isfile("RPA(RoboticProcessAutomation)")) # 해당 경로는 파일인가? False

# print(os.path.isdir("run_btn.png"))
# print(os.path.isfile("run_btn.png"))

# 만약 지정된 경로에 해당하는 파일/ 폴더가 없다면?
# print(os.path.isfile("run_btnnnnnn.png"))

# 주어진 경로가 존재하는가?
# if os.path.exists("run_btn.png"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")

# 파일 만들기
# open("new_file.txt", "a").close() # 빈 파일 생성하기

# 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt") # new_file.txt 파일 이름이 new_file_rename.txt 이름으로 바뀐다.

# 파일 삭제하기
# os.remove("new_file_rename.txt")

# 폴더 만들기
# os.mkdir("new_folder") # 현재 경로 기준으로 폴더 생성
# os.mkdir("C:\ohcoding\RPA(RoboticProcessAutomation)") # 절대 경로 기준으로 폴더 생성

# os.mkdir("new_folers/a/b/c") # 실패 : 하위 폴더 생성 시도
# os.makedirs("new_folers/a/b/c") # 성공 : 하위 폴더를 가지는 폴더 생성

# 폴더명 변경하기
# os.rename("new_folers","new_folers_rename")

# 폴더 지우기
# os.rmdir("new_folers_rename") # 폴더 안이 비어있을 때만 삭제 가능

import shutil # shull utilities
# shutil.rmtree("new_folers_rename") # 폴더 안이 비어 있지 않아도 완전 삭제 가능, 모든 파일이 삭제 될수 있으므로 주의!!

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("run_btn.png","test_folder") # 원본 경로, 대상 경로
# 어떤 파일을 폴더 안에 새로운 파일 이름으로 복사하기
# shutil.copy("run_btn.png","test_folder/copied_run_btn.png") # 원본 파일 경로, 대상 파일 경로(변경된 파일명까지)
# shutil.copyfile("run_btn.png","test_folder/copied_run_btn_2.png") # 원본 파일 경로, 대상 파일 경로(경로가 아닌 파일명 만 적으면 오류가 난다.)
# shutil.copy2("run_btn.png", "test_folder/copy2.png") # 원본 파일 경로, 대상 폴더(파일) 경로

# copy, copyfile : 메타정보 복사 X
# copy2 : 메타정보 복사 O

# 폴더 복사
# shutil.copytree("test_folder", "test_folder2") # 원본 폴더 경러, 대상 폴더 경로
# shutil.copytree("test_folder", "test_folder3") # 원본 폴더 경러, 대상 폴더 경로(파일 경로가 들어가면 오류가 난다.)

# 폴더 이동
# shutil.move("test_folder", "test_folder3") # test_folder을 test_folder3 밑으로 이동
# shutil.move("test_folder2", "test_folder3") # test_folder2을 test_folder3 밑으로 이동
# shutil.move("test_folder3", "test_folder") # 폴더명이 변경되는 효과를 가져옴







