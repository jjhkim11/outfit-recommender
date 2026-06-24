import requests
import os
from google import genai

def get_weather(city="Busan"):
    try:
        api_key = os.environ.get("WEATHER_API_KEY")

        if not api_key:
            return 23, "❌ API키 없음"

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=kr"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return 23, f"❌ API오류: {data.get('message', '알수없음')}"

        temp = round(data["main"]["temp"])
        condition = data["weather"][0]["description"]
        condition = condition.replace("온흐림", "흐림").replace("튼구름", "구름 많음").replace("약한 비", "비")
        return temp, condition

    except Exception as e:
        return 23, f"❌ 예외: {e}"


def get_outfit_recommendation(temp, condition, schedule, style):
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)

        prompt = f"""
당신은 패션 코디 전문가입니다.

오늘의 조건:
- 날씨: {temp}도, {condition}
- 오늘 일정: {schedule}
- 원하는 분위기: {style}

위 조건에 맞는 코디를 추천해줘.
상의/하의/신발/아우터로 나눠서 설명하고,
추천 이유도 한 줄씩 붙여줘.
마지막에 "Tip)" 으로 시작하는 짧은 스타일링 조언을 한 줄 추가해줘.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"오류 발생: {e}"
