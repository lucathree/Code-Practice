# 서버실행 요구사항
- 파이썬 버전: 3.9.5
- 사용 프레임워크: Django / Django REST Framework
- docker 및 docker-compose를 사용합니다.
- poetry 파이썬 패키지 관리 도구를 사용합니다.
  
  
# 패키지 설치
poetry.lock 및 pyproject.toml 파일이 있는 루트폴더 경로 안에서 다음 명령어를 실행합니다.
```
$ poetry install
```
  
  
# 도커 컨테이너 실행
docker-compose.yml 파일이 있는 루트폴더 경로 안에서 다음 명령어를 실행합니다.
```
$ docker-compose -f docker-compose.yml up --build -d
```

컨테이너와 함꼐 서버가 정상적으로 실행됐다면 아래 url을 사용하여 API를 호출할 수 있습니다.
```
http://127.0.0.1:8000/v1/musics

또는

http://localhost:8000/v1/musics
```

# Swagger 문서 참고
브라우저를 통해 아래 url로 접속하여 swagger documentation을 확인하고 API를 테스트 해볼 수 있습니다.
```
http://localhost:8000/swagger
```