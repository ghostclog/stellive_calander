0. 2023.12.25: 프로잭트 시작

1. 2023.12.29: 기본 탬플릿 완성 / html과 css로 구성.

2. 2024.01.03: 기본 탬플릿에 대한 피드백을 받고, 피드백 받은 부분들을 수정 / 헤더 및 푸터 수정. 캘린더 부분 수정

3. 2024.01.04: 기본 탬플릿을 django탬플릿에 업로드함.

4. 2024.01.05: 탬플릿 테스트 이후, 탬플릿 상속을 진행. / main_page와 stella_page를 제작

5. 2024.01.09: 기존에 만들어두었던 데이터베이스(model.py)를 조금 더 웹페이지와 프로잭트에 적합하게 수정함. / 캘린더 내의 임시 데이터 테스트 완료 및 패턴을 벗어난 url에 대한 부분적인 예외처리 완료.

6. 2024.01.11: 연월에 따른 캘린더 동적 변경을 위한 자바스크립트 작성 완료

7. 2024.01.12: url가 변경되도록 자바스크립트 작성. 그러나, 캘린더의 연월 바꾸는 부분에서 에러가 발생함. 코드를 다시 짜야하지 않을까 생각중임(수정 완료)

8. 2024.01.13(새벽1): 캘린더 완성 및 연관 자바스크립트 작성 완료.

9. 2024.01.13(새벽2): 피드백 과정에서 알게된 페이지 버그 수정

10. 2024.01.13 ~ 19: 나머지 탬플릿 작업 시작
10-1. 2024.01.15: add에 필요한 폼 및 탬플릿 완성
      2024.01.16: css를 제외한 add 기능 구현 완성. 예외 처리는 아직 미구현
10-2. 2024.01.18: 클립 및 다시보기 보는 페이지 구조 제작 완료. 테스트는 내일 시작.
      2024.01.19: 클립 및 다시보기 페이지 완성.

11. 2024.01.19 ~ 28 : 버그 픽스 및 남아있는 자바스크립트 및 css 작업 시작
11-1. 2024.01.23: 클립 탭 닫고 열기 자바스크립트 기능 완성
11-2. 2024.01.24: 클립 및 동영상 다시보기 링크 등록페이지로 이동하는 모달 작업 완료 / url예외처리 및 js작업(alert창이 뜨지 않는 문제 발생.)
11-3. 2024.01.26: 방송한 날짜에 한해서 bold처리 성공
11-4. 2024.01.28: 남아있던 css 작업 완료 및 forms.py를 수정하여 일부 입력 폼의 형태를 수정
      
12. 2024.01.26: 미 구현 기능들(문의사항) 작업
12-1. 2024.01.26: 문의사항에 사용할 view, form, model, html 작업 완료

13. 2024.04.26: 프로잭트 재시작. 일부 주석 및 코드 부분 수정

14. 2024.04.27: 기존에 제작한 모달창 삭제 / 에러 페이지 제작 및 일부 예외처리 손봄
13-1. 모달창 삭제 이유: 테스터들에게 디자인이 별로다라는 답변을 들음.
13-2. 예외처리는 자바스크립트가 아닌, django의 view에서 try-exception으로 에러페이지로 리다이랙트 시킴

15. 2024.04.30: 아이콘 추가 및 에러 페이지 다듬는 작업 / 기존에 있던 데이터들 삭제

16. 2024.05.10: 영상 다시보기 페이지 일부 버그 수정 / 전반적인 css 수정 / 퍼스널컬러에 따른 html 구조 일부 수정

17. 2024.05.15~: 영상 링크 데이터 추가 시작.

18. 2024.05.17~: 페이지 디자인 수정
18-1. 3기생이 데뷔하면서 페이지 디자인을 수정했습니다.
18-2. 디자인 피드백 적용

19. 2024.05.24: 영상 데이터 중복에 대한 처리 코드를 추가했습니다

20. 2024.06.30: 배포 전 마지막 피드백 사항을 적용했습니다. XSS 공격에 대한 약간의 대비를 추가했습니다. / 404와 500에 대해 따로 처리를 만들었으나... 순환 참조 문제가 발생하였고, 순환 참조 문제를 해결하자 추후에 DB(model)를 호출하는 view.py의 함수의 실행 속도가 현저히 느려지는 문제로 404와 500 발생에 대한 처리를 되돌렸습니다.