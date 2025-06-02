import os
import sys

# =====================================================
# 1. os 모듈: 운영 체제와 상호작용
# =====================================================

# 1.1. 현재 작업 디렉토리 확인 및 변경
print("현재 작업 디렉토리:", os.getcwd())

# 디렉토리 변경 (원하는 디렉토리 경로로 수정)
# os.chdir('/path/to/your/directory')  # 실제 경로로 변경 필요
# print("디렉토리 변경 후:", os.getcwd())

# 1.2. 새로운 디렉토리 만들기
dir_name = "새로운_디렉토리"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"디렉토리 '{dir_name}' 생성 완료")
else:
    print(f"디렉토리 '{dir_name}' 이미 존재")

# 1.3. 디렉토리 삭제하기
if os.path.exists(dir_name):
    os.rmdir(dir_name)
    print(f"디렉토리 '{dir_name}' 삭제 완료")
else:
    print(f"디렉토리 '{dir_name}' 존재하지 않음")

# 1.4. 현재 디렉토리 파일 목록 확인
files = os.listdir('.')
print("현재 디렉토리 파일/폴더 목록:", files)

# 1.5. 파일 경로 결합
file_path = os.path.join(os.getcwd(), "example.txt")
print(f"결합된 파일 경로: {file_path}")

# 1.6. 환경 변수 조회
path_env = os.environ.get('PATH')
print("PATH 환경 변수:", path_env)

# 1.7. 환경 변수 설정 (현재 세션에만 적용)
os.environ['MY_VAR'] = 'Hello, World!'
print("MY_VAR 환경 변수:", os.environ['MY_VAR'])


# =====================================================
# 2. sys 모듈: 시스템과 관련된 기능
# =====================================================

# 2.1. 명령행 인수 처리
# 명령행에서 인수를 전달하면 sys.argv 리스트에 저장됩니다.
print("명령행 인수:", sys.argv)

# 2.2. 파이썬 버전 정보 확인
print("Python 버전:", sys.version)
print(f"Python 버전 세부 정보: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

# 2.3. 표준 출력과 입력 처리
sys.stdout.write("이 메시지는 표준 출력으로 출력됩니다.\n")

# 표준 입력 받기 (사용자가 입력할 때까지 대기)
input_value = sys.stdin.readline().strip()
print(f"입력 받은 값: {input_value}")

# 2.4. 프로그램 종료
# sys.exit("프로그램을 종료합니다.")  # 실제로 종료시키는 코드 (주석 처리)

# =====================================================
# 3. os와 sys 함께 사용
# =====================================================

# 3.1. 현재 작업 디렉토리 확인 후 변경
current_dir = os.getcwd()
print("현재 작업 디렉토리:", current_dir)

# 사용자가 입력한 새 디렉토리로 변경
new_dir = input("새로운 디렉토리 경로를 입력하세요: ")
if os.path.exists(new_dir):
    os.chdir(new_dir)
    print(f"디렉토리 변경 완료: {new_dir}")
else:
    print(f"{new_dir} 디렉토리가 존재하지 않습니다.")

# 3.2. 새로운 파일 생성 및 내용 쓰기
file_name = "test_file.txt"
with open(file_name, 'w') as file:
    file.write("Hello, this is a test file created using os and sys modules!\n")
    print(f"파일 '{file_name}'에 내용이 작성되었습니다.")

# 3.3. 파일 내용 읽기
with open(file_name, 'r') as file:
    content = file.read()
    print(f"파일 '{file_name}' 내용:")
    print(content)

# 3.4. 파일 삭제
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"파일 '{file_name}' 삭제 완료")
else:
    print(f"파일 '{file_name}' 존재하지 않음")

# 3.5. 환경 변수 출력 (sys.argv 활용)
print(f"프로그램 시작 시 명령행 인수로 전달된 값: {sys.argv}")
