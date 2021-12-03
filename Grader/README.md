※ 김태원님의 [<파이썬 알고리즘 문제풀이 (코딩테스트 대비)>](https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8) 채점기가 작동하지 않을 경우 사용할 수 있는 채점 프로그램입니다. <br>

# Description
기능은 기존 채점기와 동일하며 추가로 구현한 부분은 다음과 같습니다. 
- 원하는 내용의 테스트 케이스를 추가할 수 있습니다. 
<br> 단, `txt` 파일명의 경우 입력값은 **in**, 출력값은 **out**으로 시작해야 합니다.

- 채점기를 여러 개의 폴더에 한 번에 복사하거나 제거할 수 있습니다. <br>

---

## Grader.py
※ 기존 채점기와 동일하게 채점기는 채점하려는 코드가 위치한 폴더 경로에 함께 위치해 있어야 합니다. 

```md
Inflearn
├── Sec2
├── Sec3
...
└── Sec8
    ├── 1, 2. 네트워크 선 자르기
        ├── Sec8_1.py --> 채점하려는 코드
        ├── in1.txt   --> 1번째 테스트 케이스 입력값
        ├── in2.txt
        ...
        ├── out5.txt --> 5번째 테스트 케이스 출력값
        ├── Grader.py --> 채점기
        └──
    ├── 3.도전과제
    ...
    ├── 13. 회장뽑기
    └── 소스뽑기
```

채점하려는 코드가 위치한 경로의 cmd창에서 `Grader.py`를 다음과 같이 실행합니다.

```bash
# Default filename is AA.py
$ Python Grader.py -c [filename you want to grade] 

# ex 1. 
$ Python Grader.py 
```

채점하려는 코드의 파일명이 `AA.py`가 아닐 경우 해당 파일명을 함께 입력합니다.
```bash
# ex 2. 
$ Python Grader.py -c Sec8_1.py
```

---

## Setting.py
채점하려는 폴더가 여러 개일 경우 `Setting.py`를 실행해 한 번에 `Grader.py`를 복사하거나 제거할 수 있습니다. 
<br>
단, 해당 문제 폴더가 아닌 Section 폴더가 위치한 경로에 `Grader.py`와 `Setting.py`를 위치시켜야 합니다.

```md
Inflearn
├── Sec2
├── Sec3
...
├── Sec8
...
├── Grader.py
└── Setting.py 

```

`Setting.py`가 위치한 모든 폴더의 모든 **하위** 디렉토리 폴더에 `Grader.py`를 복사하거나 제거합니다.

```bash
# Copy to each subdirectory(default)
$ python Setting.py

# Remove all Grader.py 
$ python Setting.py -o remove
```

---

# License
```
Copyright (c) 2021 Yumin Cho
```
