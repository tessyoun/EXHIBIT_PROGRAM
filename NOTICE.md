# 💥수정해야 할 사항 💥

## 0. BUG 🦟

## 1. 전시회장 ( id : user / pw : admin123 )


## 2. 주최자 ( id : skid / pw : admin123456 )


## 3. 기업 ( id : lgid / pw : admin123456 )
    - 프로그램 > * UI 수정

## 4. 일반 ( id : ktid / pw : admin123456 ) 
    - 전시회목록 > 레이아웃 > 부스 > 예약
        -> UI 옛날거...

    - 10조 기업 프로그램 3개 생성됨
    배치도 > 10조 예약 시도 하면 오류남
    MultipleObjectsReturned at /booth_program/reserve/10/
    get() returned more than one Program -- it returned 3!

## 추가하고 싶은 것?
    - 공지사항 페이지 이전/이후 글 왔다갔다?
    - 시큐어 코딩
        -> .env 파일 생성 후 key, API url 등 넣어서 사용
        -> 별도 파일 서버 구축?
        -> 파일 업로드 확장자 제한
    - 회원가입시 개인정보 제공 동의
    - 지도: 조사 필요(A* algorithm https://bgrins.github.io/javascript-astar/demo/)
        -> 이미지 흑백으로 주고 경로는 하얀색으로 두면 되지 않을까요??
