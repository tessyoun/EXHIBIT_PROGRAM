# 💥수정해야 할 사항 💥

## 0. BUG 🦟

## 1. 전시회장 ( id : user / pw : admin123 )


## 2. 주최자 ( id : skid / pw : admin123456 )
    - 공지사항 홈페이지 제목+헤더 겹침 (css)

## 3. 기업 ( id : lgid / pw : admin123456 )
    - 프로그램 > * UI 수정

## 4. 일반 ( id : ktid / pw : admin123456 ) 
    - 전시회목록 > 레이아웃 > 부스 > 예약
        -> UI 옛날거...

    - 10조 기업 프로그램 3개 생성됨
    배치도 > 10조 예약 시도 하면 오류남
    MultipleObjectsReturned at /booth_program/reserve/10/
    get() returned more than one Program -- it returned 3!

    - 북마크리스트 로그인 권한 부여
    로그인 안한 사용자가 새 북마크를 등록할수는 없지만, 북마크리스트를 누를수있음
    (로그인 후 북마크 등록 > 로그아웃 > 북마크리스트 클릭시 로그인해놨던 북마크가 보임
    따라서 비로그인 고객은 북마크리스트 버튼을 눌러도 작동이 안 되도록 권한 부여 필요

## 추가하고 싶은 것?
    - 공지사항 페이지 이전/이후 글 왔다갔다?
    - 시큐어 코딩
        -> .env 파일 생성 후 key, API url 등 넣어서 사용
        -> 별도 파일 서버 구축?
        -> 파일 업로드 확장자 제한
    - 회원가입시 개인정보 제공 동의
    - 지도: 조사 필요(A* algorithm https://bgrins.github.io/javascript-astar/demo/)
        -> 이미지 흑백으로 주고 경로는 하얀색으로 두면 되지 않을까요??
