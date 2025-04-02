##### 암기 항목

isdigit() : 숫자만 있으면 True

isinstance(변수, 자료형) : 변수가 자료형이면 True


##### 정규 표현식 (Regular Expression) 주요 기호 정리

\d    : 숫자 하나 (0~9)
       예: re.findall(r'\d', "abc123") → ['1', '2', '3']

\D    : 숫자가 아닌 문자
       예: re.findall(r'\D', "abc123") → ['a', 'b', 'c']

\w    : 단어 문자 (알파벳 대소문자, 숫자, 밑줄 _)
       예: re.findall(r'\w', "a_1@") → ['a', '_', '1']

\W    : 단어 문자가 아닌 문자
       예: re.findall(r'\W', "a_1@") → ['@']

\s    : 공백 문자 (스페이스, 탭, 줄바꿈 등)
       예: re.findall(r'\s', "a b\tc\nd") → [' ', '\t', '\n']

\S    : 공백이 아닌 문자
       예: re.findall(r'\S', " a ") → ['a']

.     : 아무 문자 하나 (줄바꿈 제외)
       예: re.findall(r'.', "Hi!") → ['H', 'i', '!']

+     : 앞의 패턴이 1개 이상 반복
       예: re.findall(r'\d+', "ab123cd45") → ['123', '45']

*     : 앞의 패턴이 0개 이상 반복
       예: re.findall(r'a*', "aaab") → ['aaa', '', '', '']

?     : 앞의 패턴이 0개 또는 1개
       예: re.findall(r'a?', "abac") → ['a', '', 'a', '', '']

[]    : 문자 집합. 대괄호 안에 있는 문자 중 하나와 매칭
       예: re.findall(r'[abc]', "apple") → ['a', 'p', 'p']

[^]   : 부정 문자 집합. 괄호 안에 없는 문자와 매칭
       예: re.findall(r'[^0-9]', "a1b2c") → ['a', 'b', 'c']

^     : 문자열의 시작과 일치
       예: re.match(r'^Hello', "Hello World") → 매칭됨

$     : 문자열의 끝과 일치
       예: re.search(r'world$', "hello world") → 매칭됨

()    : 그룹. 괄호 안의 패턴을 하나의 단위로 묶음
       예: re.findall(r'(\d+)', "a12b34") → ['12', '34']

|     : OR 조건 (또는). 양쪽 패턴 중 하나와 매칭
       예: re.findall(r'apple|banana', "apple pie") → ['apple']