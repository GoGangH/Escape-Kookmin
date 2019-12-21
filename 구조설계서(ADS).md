# 소프트웨어 구조설계서(ADS)
---
## 목차

- main.py
- game.py
- sprites.py
- tilemap.py
- chat.py
- settings.py
- quiz.py
- showmap.py
- sound.py

---
<br></br>
#### - [main.py](https://github.com/rhrkd1020/Escape-Kookmin/blob/master/%ED%83%88%EA%B5%AD%EB%AF%BC/main.py)

<p>game객체를 생성하고 프롤로그와 시작화면을 띄운다.</p> 

<br></br>

#### - [game.py](https://github.com/rhrkd1020/Escape-Kookmin/blob/master/%ED%83%88%EA%B5%AD%EB%AF%BC/game.py)

| 클래스 | 메서드 | 입력인자 | 출력인자 | 기능 |
| ---- | ---- | ---- | ---- | ---- |
| Game | `__init__` | - | - | 스크린, 스테이지, 믹서의 초기값을 설정해준다. |
|  | `load_data` | - | - | 맵의 이미지와 정보를 불러온다. |
|  | `new` | - | - | 종류별 sprite그룹을 생성하고 종류에 맞는 sprite를 저장한다. |
|  | `run` | - | - | event, new, update, draw 메서드를 호출 하여 게임의 변화를 체크하고 스테이지 확인과 pause확인을 한다. |
|  | `update` | - | - | camera와 sprtie의 정보를 갱신한다. |
|  | `draw` | - | - | sprite에 저장된 것들을 생성하고 그림자를 그리며 카메라를 조정한다. |
|  | `events` | - | - | 게임의 전체적인 키 동작을 처리한다. |
|  | `wait` | - | - | 키 입력이 들어오기 전까지 pause시킨다. |
|  | `startscreen` | - | - | 게임의 첫 화면을 띄워준다. |
|  | `prologue` | - | - | 시작하기전 전반적인 스토리를 설명해준다. |
|  | `ending` | - | - | 게임이 끝나면 엔딩 스토리와 크레딧을 띄워준다. |
|  | `render_shadow` | - | - | 게임화면에 그림자효과와 빛효과를 띄워준다. |
---
<br></br>
#### - [sprites.py](https://github.com/rhrkd1020/Escape-Kookmin/blob/master/%ED%83%88%EA%B5%AD%EB%AF%BC/sprites.py)

| 클래스 | 메서드 | 입력인자 | 출력인자 | 기능 |
| ---- | ---- | ---- | ---- | ---- |
| Player | `__init__` | game, x, y, screen, stage | - | class 객체를 선언시 class의 초기값을 정의 한다. |
|  | `set_pos` | - | - | 캐릭터의 위치를 정해준다. |
|  | `get_keys` | - | - | 캐릭터의 움직임을 조정하는 키 값과 아이템 체크, 탈출, 맵키 등 게임속 전체적인 키값을 설정한다. |
|  | `chkdirection` |  | - | 캐릭터가 바라보는 방향에 따른 이미지로 변환해준다. |
|  | `chk_walls` | dir | - | 캐릭터가 움직이기전 벽이 있는지 체크한다. |
|  | `chk_items` | - | - | 아이템 상호작용 키가 눌렸을 때 그 자리에 아이템이 있는지 확인해주고 설정한 정보에 따른 대화창과 모션을 한다. |
|  | `chk_potal` | - | - | 캐릭터가 포탈에 들어갔는지를 확인해주고 그 위치로 이동시킨다. |
|  | `chkdialogue` | - | - | 게임의 대화창을 체크해준다. |
|  | `chknpc` | - | - | 상호작용키를 눌렀을 때 npc를 만났는지 체크해주고 그에 맞는 대화창을 띄워준다. |
|  | `chatmake` | dialogue, num, name='' | - | 채팅창을 띄울때 들어가는 정보들을 매개변수로 받고 그 속성을 가진 객체를 만들어 대화창을 띄운다. |
|  | `update` | - | - | 캐릭터의 위치, 벽체크, npc 체크, 포탈 체크, 대화창 체크를 하게 하는 매서드이다. |
| Npc | `__init__` | game, x, y, type | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `chk_walls` | - | - | npc가 npc벽에 닿았는지 체크하고 그에 따른 변화를 준다. |
|  | `chkmove` | - | - | npc의 움직임을 제어한다. |
|  | `npckill` | - | - | npc를 제거한다. |
|  | `npcpause` | - | - | npc를 멈춘다. |
|  | `update` | - | - | npc의 움직임, 벽확인 등을 체크하게 하는 매서드이다. |
| Wall | `__init__` | game, x, y, w, h | - | class 객체를 선언시 class의 속성을 정의 한다. |
| npcWall | `__init__` |  game, x, y, w, h | - | class 객체를 선언시 class의 속성을 정의 한다. |
| Item | `__init__` | game, type, x, y, w, h, properties | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `make_dialogue` | - | - | tmx에서 properties를 입력받아 멤버 리스트에 대화를 저장한다. |
|  | `update` | - | - | 아이쳄의 위치를 업데이트한다. |
| Portal | `__init__` | game, type, x, y, w, h, properties | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `make_dialogue` | - | - | tmx에서 properties를 입력받아 멤버 리스트에 대화를 저장한다. |
| Dialogue | `__init__` | game, type, x, y, w, h, properties | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `make_dialogue` | - | - | tmx에서 properties를 입력받아 멤버 리스트에 대화를 저장한다. |
---
<br></br>
#### - [tilemap.py](https://github.com/rhrkd1020/Escape-Kookmin/blob/master/%ED%83%88%EA%B5%AD%EB%AF%BC/tilemap.py)

| 클래스 | 메서드 | 입력인자 | 출력인자 | 기능 |
| ---- | ---- | ---- | ---- | ---- |
| TileMap | `__init__` | filename | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `render` | surface | - | 맵을 화면에 bilt해준다. |
|  | `make_map` |  | - | 맵을 만들어준다. |
| Camera | `__init__` | width, height | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `apply` | entity | entity.rect.move(self.camera.topleft) | 입력받은 entity의 위치를 카메라의 좌측상단을 이용하여 변화 |
|  | `apply_rect` | rect | rect.move(self.camera.topleft) | 입력받은 rect를 카메라의 좌측상단을 이용하여 변화 |
|  | `update` | target | - | 카메라의 위치 변경과 카메라가 맵밖에 나가지 않았는지를 설정해준다. |
---
<br></br>
#### - [chat.py](https://github.com/rhrkd1020/Escape-Kookmin/blob/master/%ED%83%88%EA%B5%AD%EB%AF%BC/chat.py)

| 클래스 | 메서드 | 입력인자 | 출력인자 | 기능 |
| ---- | ---- | ---- | ---- | ---- |
| Chat | `__init__` | screen, dialogue, index=0, chat='' | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `drawback` | - | - | 채팅 배경 이미지를 게임 스크린에 그린다. |
|  | `drawchatter` | - | - | 채팅 이름 이미지를 게임 스크린에 그린다.
|  | `drawText` | - | - | 채팅 내용을 게임 스크린에 그린다. |
| | `drawchat` | - | - | `drawchatter`, `drawback`, `drawText` 메서드를 실행하여 스크린에 그려낸다. |
|  | `hasNextPage` | - | boolean | 더 보여줄 dialogue가 남아있는지 판단한다. |

---
<br></br>

#### - [settings.py](https://github.com/rhrkd1020/Escape-Kookmin/blob/master/%ED%83%88%EA%B5%AD%EB%AF%BC/settings.py)

<p> 게임의 상수를 정의한다.<p>

<br></br>

#### - [quiz.py](https://github.com/rhrkd1020/Escape-Kookmin/blob/master/%ED%83%88%EA%B5%AD%EB%AF%BC/quiz.py)

| 클래스 | 메서드 | 입력인자 | 출력인자 | 기능 |
| ---- | ---- | ---- | ---- | ---- |
| Quiz | `__init__` | screen, game, quizanswer, dialogue | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `drawEnter` | - | - | 정답 입력창 이미지를 화면에 그린다. |
|  | `drawQuiz` | - | - | 퀴즈 문제 이미지를 화면에 그린다. |
|  | `drawText` | - | - | 플레이어가 입력한 텍스트를 화면에 그린다. |
|  | `get_answer` | - | - | 키보드 입력을 처리한다. |
|  | `isCorrect` | - | - | 플레이어가 입력한 텍스트가 정답인지 확인한다. |
|  | `drawCorrect` | - | - | 플레이어의 정답 여부에 따라 다른 텍스트를 화면에 그린다. |
|  | `startQuiz` | - | - | 퀴즈 풀기를 시작한다. |

---
<br></br>
#### - [showmap.py](https://github.com/rhrkd1020/Escape-Kookmin/blob/master/%ED%83%88%EA%B5%AD%EB%AF%BC/showmap.py)

| 클래스 | 메서드 | 입력인자 | 출력인자 | 기능 |
| ---- | ---- | ---- | ---- | ---- |
| Maps | `__init__` | screen, index=0 | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `updateMapimg` | - | - | 맵 층수에 따라 맵 이미지를 업데이트한다. |
|  | `drawMap` | - | - | 맵 이미지를 화면에 그린다. |
|  | `drawArrow` | - | - | 좌측, 우측 화살표를 화면에 그린다. |
|  | `get_keys` | - | - | 키보드 입력을 처리한다. |
|  | `showMap` | - | - | 맵 보기를 시작한다. |

---
<br></br>
#### - [sound.py](https://github.com/rhrkd1020/Escape-Kookmin/blob/master/%ED%83%88%EA%B5%AD%EB%AF%BC/sound.py) 

| 클래스 | 메서드 | 입력인자 | 출력인자 | 기능 |
| ---- | ---- | ---- | ---- | ---- |
|  | `set_music` | filename, volume=0.5 | - | 파일이름에 맞는 노래를 설정해준다. |
| | `set_sfx` | filename, volume=0.5 | - | 파일이름에 맞는 효과음을 설정해준다.  |
---
