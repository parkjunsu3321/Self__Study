# 1. Python 이미지 선택
FROM python:3.9

# 2. 작업 디렉터리 설정
WORKDIR /app

# 3. 필요한 파일들을 이미지에 복사
COPY requirements.txt .

# 4. 의존성 설치
RUN pip install -r requirements.txt

# 5. 애플리케이션 파일 복사
COPY . .

# 6. Python 애플리케이션 실행 (예: app.py 실행)
CMD ["python", "app.py"]