구조설계서(ADS)
===
st=>start: Start:>http://www.google.com[blank]
e=>end:>http://www.google.com
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
cond=>condition: Yes
or No?:>http://www.google.com
io=>inputoutput: catch something...
para=>parallel: parallel tasks

st->op1->cond
cond(yes)->io->e
cond(no)->para
para(path1, bottom)->sub1(right)->op1
para(path2, top)->op1
---
game.py
| 클래스 | 메서드 | 입력인자 | 출력인자 | 기능 |
| ---- | ---- | ---- | ---- | ---- |
| Game | `load_data` | - | - | 맵, 캐릭터 등 이미지의 데이터를 가져온다. |
|  | `new` | - | - | 종류별 sprite그룹을 생성하고 종류에 맞는 sprite를 저장한다. |
|  | `run` | - | - | event, new, update, draw 메서드를 호출 하여 게임의 변화를 체크하고 변경하여 게임을 돌린다. |
|  | `update` | - | - | camera와 캐릭터의 정보를 갱신한다. |
|  | `draw` | - | - | sprite에 저장된 것들을 생성하고 카메라를 조정한다. |
|  | `events` | - | - | 게임의 전체적인 키 동작을 처리한다. |
|  | `wait` | - | - | 키 입력이 들어오기 전까지 동결시킨다. |
|  | `prologue` | - | - | 시작하기전 전반적인 스토리를 설명해준다. |
|  | `ending` | - | - | 끝! |
---
sprites.py
| 클래스 | 메서드 | 입력인자 | 출력인자 | 기능 |
| ---- | ---- | ---- | ---- | ---- |
| Player | `__init__` | game, x, y, screen, stage | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `set_pos` | - | - | 캐릭터의 위치를 정해준다. |
|  | `get_keys` | - | - | 캐릭터의 움직임을 조정하는 키 값을 처리한다. |
|  | `chk_walls` | dir | - | 캐릭터가 움직이기전 벽이 있는지 체크한다. |
|  | `chk_items` | - | - | camera와 캐릭터의 정보를 갱신한다. |
|  | `chk_potal` | - | - | sprite에 저장된 것들을 생성하고 카메라를 조정한다. |
|  | `update` | - | - | 게임의 전체적인 키 동작을 처리한다. |
| Wall | `__init__` | game, x, y, w, h | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `make_dialogue` | - | - | tmx에서 properties를 입력받아 멤버 리스트에 대화를 저장한다. |
| Item | `__init__` | game, type, x, y, w, h, properties | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `make_dialogue` | - | - | tmx에서 properties를 입력받아 멤버 리스트에 대화를 저장한다. |
---
tilemap.py

| 클래스 | 메서드 | 입력인자 | 출력인자 | 기능 |
| ---- | ---- | ---- | ---- | ---- |
| TileMap | `__init__` | filename | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `render` | surface | - | 캐릭터의 위치를 정해준다. |
|  | `get_keys` | - | - | 캐릭터의 움직임을 조정하는 키 값을 처리한다. |
|  | `make_map` | dir | - | 캐릭터가 움직이기전 벽이 있는지 체크한다. |
| Camera | `__init__` | width, height | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `apply` | entity | entity.rect.move(self.camera.topleft) | 캐릭터의 위치를 정해준다. |
|  | `apply_rect` | rect | rect.move(self.camera.topleft) | 캐릭터의 움직임을 조정하는 키 값을 처리한다. |
|  | `update` | target | - | 캐릭터가 움직이기전 벽이 있는지 체크한다. |

---
chat.py

| 클래스 | 메서드 | 입력인자 | 출력인자 | 기능 |
| ---- | ---- | ---- | ---- | ---- |
| Chat | `__init__` | screen, dialogue, index=0, chat='' | - | class 객체를 선언시 class의 속성을 정의 한다. |
|  | `chating` | - | - |  |
|  | `drawText` | - | - |  |
|  | `hasNextPage` | - | - |  |

