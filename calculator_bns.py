def inputNumEnh():
    expression = input("Enter expression: ").replace(" ", "")  # 공백 제거

    operators = ['+', '-', '*', '/'] 
    
    found_operator = ''
    operator_index = -1

    # 연산자를 찾는 핵심 로직: 가장 먼저 발견되는 유효한 연산자를 찾습니다.
    # 단, 첫 번째 '-'는 피연산자의 부호일 수 있으므로 특별히 처리합니다.
    
    # 덧셈, 뺄셈, 곱셈, 나눗셈 연산자를 순서대로 확인 (우선순위 고려 아님, 단순 탐색 순서)
    # 실제로는 곱셈/나눗셈을 먼저 찾는 것이 더 안정적일 수 있습니다.
    # 예를 들어, "5+2*3" 같은 복잡한 수식이 아니라, "A op B" 형태만 다룹니다.
    
    # 특정 연산자가 표현식 내에서 몇 번째 인덱스에 있는지 확인하고,
    # 해당 연산자 앞뒤의 문자열이 유효한 숫자인지 검증하는 방식으로 접근합니다.

    # 1. 연산자의 가능한 인덱스 찾기
    possible_operator_indices = []
    for i, char in enumerate(expression):
        if char in operators:
            # 첫 번째 문자가 '-'인 경우는 일단 후보에서 제외 (음수 부호일 가능성)
            if i == 0 and char == '-':
                continue
            
            # 연산자 뒤에 숫자가 와야 함.
            # 연산자 뒤에 '-'가 오는 경우 (예: '2 * -2')를 처리
            if i + 1 < len(expression) and expression[i+1] == '-':
                # '-X'가 아닌 다른 연산자 뒤에 오는 '-'는 두 번째 피연산자의 부호일 수 있음
                if i + 2 < len(expression) and expression[i+2].isdigit():
                    possible_operator_indices.append(i)
                else: # '-X'가 숫자가 아니거나, 끝에 '-'만 있는 경우 오류
                    continue # 이 연산자 인덱스는 유효하지 않음
            elif i + 1 < len(expression) and expression[i+1] in operators: # 연산자 중복 '++'
                continue # 이 연산자 인덱스는 유효하지 않음
            elif i == len(expression) - 1: # 연산자가 문자열 끝에 있음
                continue # 이 연산자 인덱스는 유효하지 않음
            else: # 일반적인 유효한 연산자
                possible_operator_indices.append(i)

    # 2. 가능한 연산자 인덱스 중에서 가장 적합한 것 선택
    # 여기서는 가장 첫 번째로 발견된 유효한 연산자를 선택합니다.
    if not possible_operator_indices:
        print("Invalid expression format. Please use 'number operator number'.")
        exit()
    
    # 이제 모든 가능한 연산자 인덱스를 확인하면서 유효한 파싱 조합을 찾습니다.
    # 첫 번째 유효한 조합을 사용합니다.
    for p_idx in possible_operator_indices:
        temp_operator_char = expression[p_idx]
        temp_left_str = expression[:p_idx]
        temp_right_str = expression[p_idx + 1:]

        # 피연산자가 유효한 숫자인지 확인하는 헬퍼 함수
        def _is_valid_number_string(s: str) -> bool:
            if not s:
                return False
            
            if s.startswith('-'):
                s = s[1:]
                if not s: 
                    return False

            parts = s.split('.')
            if len(parts) > 2: 
                return False
            
            # ".5", "5." 같은 경우 처리, "."만 있는 경우는 제외
            if len(parts) == 1: 
                return parts[0].isdigit()
            elif len(parts) == 2: 
                if not parts[0] and not parts[1]: 
                    return False
                return (parts[0].isdigit() or parts[0] == '') and \
                       (parts[1].isdigit() or parts[1] == '')
            return False 

        if _is_valid_number_string(temp_left_str) and _is_valid_number_string(temp_right_str):
            found_operator = temp_operator_char
            operator_index = p_idx
            break # 유효한 연산자를 찾았으므로 루프 종료

    if operator_index == -1: # 적합한 연산자를 찾지 못하면
        print("Invalid expression format. Please use 'number operator number'.")
        exit()

    left_str = expression[:operator_index]
    right_str = expression[operator_index + 1:]

    try:
        left = int(float(left_str))
        right = int(float(right_str))
    except ValueError:
        print("Invalid number input after parsing.")
        exit()

    operator_idx = operators.index(found_operator)
    
    return left, right, operator_idx

# 연산함수  
def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if(b != 0):
        return a/b
    else:
        print("Error: Division by zero." )
        exit()
#연산함수 주소 배열
opFunc = [add, subtract, multiply, divide]
if __name__ == "__main__":

    # 계산식을 입력 받아 숫자2개 연산자로 분리함
    num1, num2, operator= inputNumEnh()
    # 연산을함 연산자에 해당하는 함수를 배열로 처리
    result = opFunc[operator](num1, num2)
    #결과 출력
    operatorstr = '+-*/'  # 연산자 목록을 다시 정의
    print(f"Result: <{num1} {operatorstr[operator]} {num2} = {result}>")
else:
    print("Plase execute at main")


