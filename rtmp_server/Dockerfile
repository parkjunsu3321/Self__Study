# Node.js 이미지를 기반으로 합니다.
FROM node:14

# 작업 디렉토리 생성 및 설정
WORKDIR /usr/src/app

# package.json 및 package-lock.json을 복사하여 의존성 설치
COPY package*.json ./
RUN npm install

# 애플리케이션 소스 복사
COPY . .

# 포트 설정
EXPOSE 1935 8000 3000

# 컨테이너 시작 시 실행할 명령어
CMD ["node", "server.js"] 