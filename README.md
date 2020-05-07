# 개인 블로그 구현 프로젝트

# 프로젝트의 개요

이 프로젝트는 2018.03에 Java / Spring Framework로 구현하였던 '개인 블로그 구현 프로젝트'를 Python / Django로 다시 구현하는 프로젝트이다. 현재는 서버 파트만 구현할 예정이며, 웹 프론트는 추후 구현할 것이다.

# 프로젝트의 목적

이 프로젝트를 진행하는 목적은 다음과 같다.

1. Django 사용법 및 세부 기술에 대한 재숙지
2. 포트폴리오용
    - 이전 프로젝트의 Java 소스 코드가 유실되어 내 기술력을 어필할 수 없던 점을 보완
    - 이전 직장에서 습득한 기술들을 다시 사용해보고 숙지하여 이를 어필하려는 목적

기술력 어필을 위해서 거창한 주제로 크게 만드는 것이 중요한 것은 아닌 것 같다. 단순한 주제라도 습득했던 기술을 잘 사용한다면 괜찮을 것 같다.

# 사용 예정인 기술

- Python / Django
- Docker(docker, docker-compose, docker-machine)
- MySQL
- Redis
- AWS EC2
- Jenkins(Docker container)
- Celery 또는 RabbitMQ(분산처리 / 비동기 처리 메세지큐) → 사용할 부분이 있을지 확인해보아야 할 듯

# 프로젝트의 목표

- [ ]  DB 설계 및 구현
- [ ]  Django 웹 서버 구현
- [ ]  Redis를 이용한 로그인 세션 관리
- [ ]  docker-compose로 Django 웹 서버를 container로 만들기
- [ ]  EC2 배포 자동화를 위한 Jenkins 파이프라인 구축
- [ ]  다수의 웹 서버를 구동하고 LB 달아보기
- [ ]  분산처리 / 비동기 처리를 할 부분이 있을지 확인하고 Celery 적용해보기, docker-compose로 띄우기

목표 기한: 2주(20.05.06 ~ 20.05.20)

# 목표 달성을 위해 배워야 할 것들

1. Django ORM에서 외래키로 연결된 테이블 조작 및 관리
2. docker-compose 사용법
3. EC2 인스턴스 생성
4. LB 사용법
5. Celery Task 사용법