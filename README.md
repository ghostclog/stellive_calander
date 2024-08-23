# 스텔라이브 다시보기 및 키리누키(클립) 캘린더 프로잭트

## 개요(overview)
한국 버튜버 그룹 '스텔라이브'의 방송 일정 캘린더입니다.
해당 사이트에선 방송한 날짜에 대한 유투브에 올라온 다시보기 및 키리누키(방송 클립)을 방송한 날에 맞추어 한 눈에 볼 수 있도록 설계한 사이트입니다.

This is the broadcast schedule calendar of the Korean YouTuber group 'Stellive'.
The site is designed to allow you to see the replay and Kirinuki (broadcast clip) posted on YouTube on the broadcast date at a glance.

## 프로잭트를 시작 한 이유(why to start this project)
시간이 흘러, 스텔라이브의 팬층 규모가 커짐에 따러서 맴버들의 방송 클립(키리누키)를 만드는 사람들의 수 또한 늘어남에 따라서 특정 날짜에 진행한 방송의 엑기스라 볼 수 있는 키리누키를 찾아보는 것도. 그리고, 지금 보고있는 키리누키의 원본 방송 영상도 찾아보기 점점 힘들어졌습니다. 이에 저는 특정 날짜에 대한 클립과 다시보기를 한 페이지에서 볼 수 있는 페이지의 필요성을 느끼게 되었고, 23년도 12월 말부터 24년도 1월까지. 대략 5주의 기간에 걸친 프로잭트를 시작하게되었습니다.

As time went by, as the number of people making the broadcast clips of the members of Stell Live increased, so did looking for kirinuki, which is an extract from a specific date. Also, it became increasingly difficult to find the original video of kirinuki being watched. This made me feel the need for a single page of clips and replay on a specific date, and I started the project from the end of December 23rd to January 24th, which lasted approximately five weeks.

## 프로잭트 개발 환경(Project Development Environment)
- django(python)
- sqlite(db)
- JS

## 개발 및 업데이트 기간(development and update period)
1차: 2023.12.25 ~ 2024.01.26(기본 개발 및 배포)
2차: 2024.04.26 ~ 2024.07.06(디자인 수정 및 버그 픽스)
3차: 예정(재배포 및 반 자동화 업데이트)

## 주요 기능들(main function)
- 다시보기 및 키리누키 링크 추가(Add replay and keirinuki links):'add/<str:category>'
- 특정 맴버와 특정 날짜에 대한 방송 정보 제공(Provide broadcast information for specific members and specific dates): 'mains/<str:stella>/<str:date>/<str:day>'
- 특정 맴버와 특정 날짜에 대한 다시보기 및 키리누키를 볼 수 있는 페이지(Page where you can view replay and keirinuki for specific members and specific dates):'mains/<str:stella>/<str:date>/<str:day>/show'




## 프로잭트 후기(after project)
 처음으로 프론트 엔드 담당해주는 이 없이 홀로 진행했던 프로잭트였습니다. 그만큼 웹다인이나 css. 그리고, js에서 많은 곤욕을 치뤘고, 치른 곤욕만큼 제법 많은 것을 배울 수 있었습니다. 비록 기본적인 디자인 틀부터 캘린더와 다시보기 페이지까지. 부트스트랩 이용 없이 처음부터 만들었던지라 디자인이 너무나도 난잡하고 지저분하게 만들어었지만, 앞서 말했던것처럼 많은 것들을 배울 수 있었기에 그 많은 시간들을 허비했다고 생각하진 않습니다.
웹 페이지 제작과 백엔드 구성에 대한 노하우가 조금 더 늘었으며, 파이썬에서 발생 할 수 있는 문제들(대표적으로 순환 참조)에 대한 대처 능력이 이번 프로잭트를 진행하고 나서 크게 발전했다는 것을 느낄 수 있었습니다.
 그리고, 무엇보다 제가 계속 애정을 쏟을 수 있는 프로잭트가 생겼다는 것이 가장 마음에 들었습니다.

 It was my first solo project without a front-end manager. That's how much I struggled with WebDine, css, and js, and I could learn quite as much as I struggled with it. Even though I built it from scratch without using bootstraps, the design was so messy and messy, but I don't think I wasted a lot of time because I could learn a lot of things like I said before.
There was a little more know-how in web page creation and backend configuration, and I could feel that my ability to deal with problems (typically circulating) that might arise in Python has improved significantly since this project.
 And, most of all, I liked that I had a project that I could continue to love.
