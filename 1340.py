import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from datetime import datetime
if __name__ == '__main__':

  def convert_month_str_to_num(month_str):
    """
    월 이름을 숫자로 변환하는 함수
    :param month_str: 월 이름 (예: 'January', 'February')
    :return: 월 숫자 (1부터 12까지)
    """
    month_dict = {
      "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
      "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }
    return month_dict[month_str]


  def is_leap_year(year):
    """
    윤년 여부를 판단하는 함수
    :param year: 연도
    :return: 윤년이면 True, 아니면 False
    """
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


  def get_total_minutes_in_year(year):
    """
    해당 연도의 총 분 수를 반환하는 함수
    :param year: 연도
    :return: 해당 연도의 총 분 수
    """
    if is_leap_year(year):
      return 366 * 24 * 60  # 윤년인 경우 366일
    else:
      return 365 * 24 * 60  # 평년인 경우 365일


  def year_progress_bar(year_time):
    """
    주어진 날짜와 시간을 기준으로 연도 진행 바 퍼센트를 계산하는 함수
    :param year_time: 'Month DD, YYYY HH:MM' 형식의 문자열
    :return: 연도 진행 퍼센트
    """
    # 입력값 파싱
    month_str, day, year, time = year_time.split()
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
    total_time = end_of_year - start_of_year  # 전체 연도의 총 시간

    # 분 단위로 변환
    elapsed_minutes = elapsed_time.total_seconds() / 60  # 경과 시간을 분으로 변환
    total_minutes = total_time.total_seconds() / 60  # 총 시간을 분으로 변환

    # 퍼센트 계산
    progress_percentage = (elapsed_minutes / total_minutes) * 100
    return progress_percentage


  # 입력값 받기
  year_time = input()
  # 연도 진행 퍼센트 계산 및 출력
  print(f"{year_progress_bar(year_time):.15f}")