import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from datetime import datetime
if __name__ == '__main__':

  # 월 이름을 숫자로 변환
  def convert_month_str_to_num(month_str):
    month_dict = {
      "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
      "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }
    return month_dict[month_str]

  def year_progress_bar(year_time):
    month_str, day, year, time = year_time.split() # 입력값 파싱
    day = int(day[:-1])  # 일 정보에서 쉼표 제거 후 정수로 변환
    year = int(year)  # 연도를 정수로 변환
    hour, minute = map(int, time.split(":"))  # 시간과 분을 파싱

    # 월 이름을 숫자로 변환
    month = convert_month_str_to_num(month_str)

    # 주어진 날짜와 시간의 datetime 객체 생성
    current_datetime = datetime(year, month, day, hour, minute)
    start_of_year = datetime(year, 1, 1)  # 해당 연도 시작 시점
    end_of_year = datetime(year + 1, 1, 1)  # 다음 연도 시작 시점

    # 경과 시간 계산
    elapsed_time = current_datetime - start_of_year  # 현재 시점까지의 경과 시간
    total_time = end_of_year - start_of_year  # 해당 연도 총 시간

    # 분으로 단위 변환
    elapsed_minutes = elapsed_time.total_seconds() / 60  # 경과 시간 변환
    total_minutes = total_time.total_seconds() / 60  # 총 시간 변환

    # 퍼센트 계산
    progress_percentage = (elapsed_minutes / total_minutes) * 100
    return progress_percentage


  year_time = input()
  print(f"{year_progress_bar(year_time):.15f}")