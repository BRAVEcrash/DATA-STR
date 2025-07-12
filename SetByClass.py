from ListByFucntion import ArrayList


list = ArrayList()
while True :
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료=> ")

    if command == 'i' :
        pos = int(input(" 입력행 번호: "))
        str = input(" 입력행 내용: ")
        list.insert(pos, str)


    elif command == 'd':
        pos_str = input(" 삭제행 번호: ")
        if pos_str.isdigit():
            pos = int(pos_str)
            if 0 <= pos < list.size and not list.isEmty():
                list.delete(pos)


    elif command == 'r':
        pos_str = input(" 변경행 번호: ")
        if pos_str.isdigit():
            pos = int(pos_str)
            if 0 <= pos < list.size:
                new_str = input(" 변경행 내용: ")
                list.array[pos] = new_str
                print(f"{pos}번 줄 변경 완료")
            else:
                print(" 변경 실패 ")
        else:
            print(" 숫자를 입력하세요.")

    elif command == 'p':
        print("Line Editor")
        for i in range(list.size):
            print(f"[{i}] {list.getEntry(i)}")

    elif command == 'l':
        filename = input("읽을 파일 이름 입력: ")
        file = open(filename, 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()
        list = ArrayList(max(100, len(lines)))
        i = 0
        while i < len(lines):
            list.insert(i, lines[i].strip())
            i += 1
        print(f"{filename} 파일 읽기 완료!")

    elif command == 's':
        filename = input("저장할 파일 이름 입력: ")
        file = open(filename, 'w', encoding='utf-8')
        i = 0
        while i < list.size:
            file.write(list.getEntry(i) + '\n')   # 현재 리스트를 파일에 저장
            i += 1
        file.close()
        print(f"{filename} 파일 저장 완료!")

    elif command == 'q' :
        print("종료합니다!")
        break

    else:
        print(" 잘못된 명령입니다 ")