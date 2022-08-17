# import logging

# logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s") # level=logging.DEBUG : dedug 이상의 레벨만 출력한다.

# 크기 순서, debug < info < warning < error < critical
# logging.debug("아 힘들다이")
# logging.info("실행 준비")
# logging.warning("샐행 중 오타가 있습니다.")
# logging.error("에러 발생")
# logging.critical("복구가 불가능한 상태에 들어섰습니다.")

# 터미널과 파일에 함께 로그 남기기
import logging
from datetime import datetime

logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") # 시간 [로그레벨] 메시지 형태로 로그를 작성
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)
 
# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHander = logging.FileHandler(filename, encoding="utf-8")
fileHander.setFormatter(logFormatter)
logger.addHandler(fileHander)

logger.debug("로그를 남겨보는 테스트를 진행합니다.")