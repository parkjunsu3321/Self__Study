# 🚀 FastAPI 기반 이미지 업로드 및 다운로드 서버

이 프로젝트는 **FastAPI**를 사용하여 이미지 파일을 업로드하고 다운로드할 수 있는 간단한 웹 서버를 제공합니다.

---

## ✨ 주요 기능

- **📥 이미지 다운로드**: 저장된 이미지를 클라이언트로 반환합니다.  
  ➡️ **엔드포인트**: `GET /{img_name}`
- **📤 이미지 업로드**: 클라이언트에서 이미지를 업로드하여 서버에 저장합니다.  
  ➡️ **엔드포인트**: `POST /upload`

---

## ⚙️ 설치 및 실행

### 1️⃣ 로컬 환경에서 실행

#### 💻 요구 사항
- **Python 3.9 이상**

#### 🛠️ 설치 절차
```bash
# 1. 저장소 클론
git clone <repository-url>
cd <repository-directory>

# 2. 가상 환경 생성 및 활성화 (선택 사항)
python -m venv venv
source venv/bin/activate  # Windows의 경우 venv\Scripts\activate

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 서버 실행
python main.py
```

📍 **기본 실행 경로**:  
- 서버: `http://127.0.0.1:8000`  
- 이미지 저장 디렉토리: `./storage`

---

### 2️⃣ Docker를 사용한 실행

#### 🐋 요구 사항
- **Docker 설치**

#### 📦 빌드 및 실행
```bash
# 1. 도커 이미지 빌드
docker build -t fastapi-image-server .

# 2. 도커 컨테이너 실행
docker run -d -p 8000:8000 -v $(pwd)/storage:/app/storage fastapi-image-server
```

---

## 🔧 사용 예시

### 📤 이미지 업로드
```bash
curl -X POST "http://127.0.0.1:8000/upload" \
-H "Content-Type: multipart/form-data" \
-F "file=@<이미지 파일 경로>"
```

### 📥 이미지 다운로드
```bash
curl -X GET "http://127.0.0.1:8000/<이미지 이름>" --output <저장할 파일 경로>
```

---

## 📂 프로젝트 구조

```plaintext
.
├── main.py               # FastAPI 웹 서버 코드
├── requirements.txt      # Python 의존성 목록
├── Dockerfile            # Docker 환경 설정
└── storage/              # 업로드된 이미지 저장 디렉토리
```

---

## 🤝 사용 방법

1. 저장소를 **포크**합니다.
2. 새로운 브랜치를 생성합니다.  
   ```bash
   git checkout -b feature-branch
   ```
3. 변경 사항을 커밋합니다.  
   ```bash
   git commit -m "Add new feature"
   ```
4. 브랜치에 푸시합니다.  
   ```bash
   git push origin feature-branch
   ```