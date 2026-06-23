# 👗 오늘의 코디 추천기

> 날씨와 일정을 고려해 매일 아침 옷 선택에 걸리는 고민을 해결해주는 AI 코디 추천 서비스

---

## 📌 프로젝트 소개

매일 아침 "오늘 뭐 입지?"라는 고민을 해결하기 위해 만든 웹 앱입니다.
현재 위치의 날씨를 자동으로 불러오고, 오늘의 일정과 원하는 분위기를 선택하면
Google Gemini AI가 상의, 하의, 신발, 아우터를 맞춤 추천해줍니다.

---

## 🛠 사용된 기술

| 기술 | 용도 |
|------|------|
| Python | 전체 백엔드 로직 |
| Streamlit | 웹 앱 인터페이스 |
| Google Gemini API (`gemini-2.5-flash`) | AI 코디 추천 |
| OpenWeatherMap API | 실시간 날씨 데이터 |
| pyngrok | Colab 환경에서 외부 접속 |

---

## 📁 파일 구조

```
project/
├── logic.py   # 날씨 API 호출 및 Gemini AI 코디 추천 함수
├── app.py     # Streamlit 화면 구성
└── README.md  # 프로젝트 설명서
```

---

## 🔑 API 키 발급 방법

총 3개의 API 키가 필요합니다. 모두 무료로 발급 가능합니다.

### 1. Gemini API 키
1. [https://aistudio.google.com](https://aistudio.google.com) 접속 (개인 Google 계정 필요)
2. 왼쪽 메뉴 **"Get API key"** → **"Create API key"** 클릭
3. 생성된 키 복사

### 2. OpenWeatherMap API 키
1. [https://openweathermap.org](https://openweathermap.org) 접속 후 회원가입
2. 로그인 후 프로필 → **"My API keys"** 에서 키 확인
3. ⚠️ 가입 직후 최대 2시간 후 활성화됨

### 3. Ngrok 토큰
1. [https://ngrok.com](https://ngrok.com) 접속 후 회원가입
2. 대시보드에서 **"Your Authtoken"** 복사

---

## ⚙️ 설치 및 실행 방법

### 1단계 — 라이브러리 설치
```python
!pip install -q streamlit google-genai requests pyngrok
```

### 2단계 — Colab Secrets 등록
Colab 왼쪽 🔑 아이콘 클릭 후 아래 3개 키 등록:

| Name | Value |
|------|-------|
| `GEMINI_API_KEY` | Gemini API 키 |
| `WEATHER_API_KEY` | OpenWeatherMap API 키 |
| `NGROK_TOKEN` | Ngrok 토큰 |

> ⚠️ 각 키 옆 **"노트북 액세스 허용"** 토글을 반드시 켜주세요.

### 3단계 — logic.py 실행
```python
%%writefile logic.py
# (logic.py 코드 내용)
```

### 4단계 — app.py 실행
```python
%%writefile app.py
# (app.py 코드 내용)
```

### 5단계 — Streamlit 서버 실행
```python
from pyngrok import ngrok
from google.colab import userdata
import subprocess, time, os

os.environ["GEMINI_API_KEY"] = userdata.get("GEMINI_API_KEY")
os.environ["WEATHER_API_KEY"] = userdata.get("WEATHER_API_KEY")

ngrok.kill()
ngrok.set_auth_token(userdata.get("NGROK_TOKEN"))
subprocess.Popen(["streamlit", "run", "app.py",
                  "--server.port=8501", "--server.headless=true"])
time.sleep(3)
public_url = ngrok.connect(8501)
print("접속 주소:", public_url)
```

출력된 주소로 브라우저에서 접속하면 앱을 사용할 수 있습니다.

---

## 🖥 사용 방법

1. 앱 접속 시 **현재 부산 날씨**가 자동으로 표시됩니다.
2. **오늘 일정**을 선택합니다. (수업 / 친구 약속 / 집콕 / 데이트)
3. **원하는 분위기**를 선택합니다. (캐주얼 / 깔끔하게 / 편하게)
4. **"코디 추천받기 🎯"** 버튼을 클릭합니다.
5. AI가 상의, 하의, 신발, 아우터와 스타일링 Tip을 추천해줍니다.

---

## 🔮 향후 개선 방향

- 사용자가 본인의 옷장 사진을 직접 등록하여 실제 보유한 옷 중에서 추천받는 기능
- 과거 추천 기록 저장 및 즐겨찾기 기능
- 계절별 옷 교체 알림 기능
- 위치 자동 감지로 부산 외 다른 지역도 지원
