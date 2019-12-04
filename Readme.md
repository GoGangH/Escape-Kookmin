# SW2 Ad project
------------------------
### What is This?

 - python 언어를 사용한 탈출 게임
# Prerequisites

### Install List

 - Python `3.7.1`

 ```
    pip install pygame
 ```

## USAGE (사용방법)

 1. Clone file
 2. run main.py
------------------------
# 추가해야할 것(급한 순서)

- 시도 해봐야 할 것 : map생성 시 object layer 에서 name이 아닌 type 설정 후 type 별로 다른 행동하게 설정
- ex) name : 은수, type : 마크 : 마크를 실행
- name : 은수 , type : 하스 : 하스를 실행

1. 대화창 위로 올리기
    - chat에서 대화창을 display에 blit하고 난 뒤에, g.run()에서 계속 draw()가 실행되서 chat이 blit된 후 다시 맵 이미지가 blit 되서 덮어 그려짐.
    - sprites의 Player.chk_items() while문 break가 제대로 작동 안함. 
    - 대화창이 떠 있는 동안 (다음 스페이스바 입력 전까지) blit되면  안 됨.


2. 화면 clear

3. 맵 화면 전환

4. npc 추가 및 대화 설정

5. player 가방 추가

6. player 이미지 생성

7. 맵 생성

8. 사운드 추가

9. 로드 데이터

