# 소프트웨어 상세 설계서(DDS)
---
## 목차

1. [클래스 명세](https://github.com/rhrkd1020/Escape-Kookmin/blob/master/%EC%83%81%EC%84%B8%EC%84%A4%EA%B3%84%EC%84%9C(DDS).md#1-%ED%81%B4%EB%9E%98%EC%8A%A4-%EB%AA%85%EC%84%B8)

2. [클래스별 상세 명세](https://github.com/rhrkd1020/Escape-Kookmin/blob/master/%EC%83%81%EC%84%B8%EC%84%A4%EA%B3%84%EC%84%9C(DDS).md#2-%ED%81%B4%EB%9E%98%EC%8A%A4%EB%B3%84-%EC%83%81%EC%84%B8-%EB%AA%85%EC%84%B8)
    - [Chat](https://github.com/rhrkd1020/Escape-Kookmin/blob/master/%EC%83%81%EC%84%B8%EC%84%A4%EA%B3%84%EC%84%9C(DDS).md#--chat)
    
---

## 1. 클래스 명세

| 클래스 ID | 클래스 이름 | 설명                                                         |
| :-------: | :---------: | ------------------------------------------------------------ |
|  CL - 01  |    Chat     | 게임 내의 채팅창 UI를 담당한다. 채팅창은 플레이어에게 정보를 전달하기 위해 사용된다. |
|  CL - 02  |    Game     | 게임 메인 로직과 시작화면, 프롤로그, 엔딩화면을 담당한다.    |
|  CL - 03  |    Quiz     | 게임 내의 퀴즈 UI와 퀴즈 로직을 담당한다.                    |
|  CL - 04  |    Maps     | 게임 내의 맵 기능 UI를 담당한다.                             |
|  CL - 05  |   Player    | 플레이어 캐릭터를 담당하며                                   |
|  CL - 06  |     NPC     | NPC의 이동과 업데이트를 담당한다.                            |
|  CL - 07  |    Wall     | Wall sprite를 담당한다.                                      |
|  CL - 08  |   npcWall   | npcWall sprite를 담당한다.                                   |
|  CL - 09  |    Item     | Item sprite를 담당하며 Item이 가진 tmx properties의 dialogues를 list로 저장한다 |
|  CL - 10  |   Portal    | Portal sprite를 담당하며 Portal이 가진 tmx properties의 dialogues를 list로 저장한다 |
|  CL - 11  |  Dialogue   | Dialogue sprite를 담당하며  Dialogue가 가진 tmx properties의 dialogues를 list로 저장한다 |
|  CL - 12  |  TiledMap   | tmx형식으로 저장된 map파일을 pygame의 이미지 형식으로 렌더링한다. |
|  CL - 13  |   Camera    |                                                              |

## 2. 클래스별 상세 명세
#### - Chat

|                         |     이름      | 역할, 설명                                                   |
| :---------------------: | :-----------: | :----------------------------------------------------------- |
| attributes (properties) |    chatter    | 대화창 UI에서 이름에 들어갈 문자열                           |
|                         |    screen     | 게임화면                                                     |
|                         | backgroundimg | 대화창 UI의 대화창 배경이 될 pygame 이미지                   |
|                         |  chatterimg   | 대화창 UI의 이름 배경이 될 pygame 이미지                     |
|                         |   chatRect    | backgroundimg의 영역                                         |
|                         |  chatterRect  | chatterimg의 영역                                            |
|                         |     font      | 대화창에 그릴 텍스트의 pygame 폰트                           |
|                         |    indexX     | 대화창의 페이지                                              |
|                         |    indexY     | 대화 횟수                                                    |
|                         |   dialogue    | 대화창의 내용이 될 문자열 리스트                             |
|         method          |   drawback    | 대화창 배경을 screen에 그린다.                               |
|                         |  drawchatter  | 대화창 이름 배경을 screen에 그린다.                          |
|                         |   drawText    | 대화창의 텍스트를 설정하고 screen에 그린다.                  |
|                         |   drawchat    | chatter가 빈 문자열이 아니면 drawchatter() 함수를 호출한다. 이후에 drawback(), drawText() 함수를 호출하고 indexY값에 1을 더한다. pygame.display.update() 함수를 호출한다. |
|                         |  hasNextPage  | 더 넘길 대화창이 있는지 판단한다.                            |

---
#### - Game

|                         |     이름      | 역할, 설명                                                   |
| :---------------------: | :-----------: | :----------------------------------------------------------- |
| attributes (properties) |    screen    | 게임화면 저장 |
|                         |    rect     | 게임화면 위치 저장 |
|                         | clock | 시간 저장 |
|                         |  mapStage   | 지금 스테이지 list index |
|                         |   beforStage    | 이전 스테이지 list index |
|                         |  paused  | 정지 체크 |
|                         |     mapname      | 스테이지 맵의 이름 |
|                         | shadow | pygame의 크기를 shadow의 크기로 저장 |
|                         | shadow.fill | 채우는 색상 저장 |
|                         |   shadow_mask    | 그림자의 이미지 저장 |
|                         |   shadow_rect    | 그림자의 위치 |
|                         |   all_sprites    | 모든 sprite 저장 |
|                         |   player    | Player객체 저장 변수 |

---
#### - Player

|                         |     이름      | 역할, 설명                                                   |
| :---------------------: | :-----------: | :----------------------------------------------------------- |
| attributes (properties) |    groups    | all sprite group 저장 |
|                         |    game     | pygame 정보 저장 |
|                         | image | 캐릭터 이미지 저장 |
|                         |  game_folder   | 폴더 위치 설정 |
|                         |   img_folder    | img폴더 위치 설정 |
|                         |  beforKey  | 이전 키값 저장 |
|                         |     rect      | 플레이어의 맵상 위치 저장 |
|                         | vel | 플레이어의 이동 속도별 이동 저장 |
|                         | pos | 플레이어 임시 위치 저장 |
|                         |   Beforpos    | 이전 위치 저장 |
|                         |   screen    | 게임 화면 저장 |
|                         |   map    | 맵 저장 |
|                         |   chat    | chat객체 생성 저장 |
|                         |   chating    | 체팅을 하는지 확인 |
|                         |   mapping    | 맵을 보는지 확인 |
|                         |   Mapstage    | 맵의 스테이지 저장 |
|                         |   stupidDegree    | 아무것도 없는 곳에 클릭했을때 뜰 chat index값 저장 |
|                         |   direction    | 캐릭터가 보는 방향 설치 |
|                         |   posdirection    | 캐릭터의 보는 방향 맵 위치 값 저장 |
|                         |   beformove    | 이전 캐릭터 움직임 저장 |
|                         |   escape    | 탈출할 위치 저장 |
|                         |   move    | 캐릭터가 가만히 있는 시간 저장 |
|                         |   imgname    | 이미지 이름 list index 저장 |
|                         |   stageChk    | 스테이지속 상호작용 횟수 체크 |
