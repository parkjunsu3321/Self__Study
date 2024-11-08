# 1. Node.js 이미지 선택
FROM node:14

# 2. 작업 디렉터리 설정
WORKDIR /app

# 3. 패키지 파일 복사 및 의존성 설치
COPY package.json package-lock.json ./
RUN npm install

# 4. 애플리케이션 코드 복사
COPY . .

# 5. 개발 서버 실행 (npm start)
CMD ["npm", "start"]