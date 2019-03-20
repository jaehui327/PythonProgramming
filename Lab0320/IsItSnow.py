while True:
    isSnow = input("밖에 비가 오면 yes, 아니면 no를 입력하세요: ")
    if isSnow == "yes":
        hasUmbrella = input("우산이 있으면 yes, 아니면 no를 입력하세요: ")
        if hasUmbrella == "yes":
            break
        elif hasUmbrella == "no":
            print("비가 그칠 때 까지 기다리세요..")
    elif isSnow == "no":
        break
print("외출하세요!")