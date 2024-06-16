import os
from flask import Flask

app = Flask(__name__)

@app.route('/')



import time 

import random 

yoga=['제철과일','블루베리','카라멜','딸기','망고','오렌지','초코','오레오','민초레오','바나나 초코'] 

print('======== 요거바라 메뉴 추천 키오스크  ========') 

a1=0#남자 선택횟수 

b1=0 

c1=0 

d1=0 

e1=0 

f1=0 

g1=0 

h1=0 

i1=0 

j1=0 

  

a2=0#여자 선택횟수 

b2=0 

c2=0 

d2=0 

e2=0 

f2=0 

g2=0 

h2=0 

i2=0 

j2=0 

  

print('제철과일    == 3500원') 

print('블루베리    == 3300원') 

print('카라멜      == 3300원') 

print('딸기        == 3300원') 

print('망고        == 3500원') 

print('오렌지      == 3500원') 

print('초코        == 3300원') 

print('오레오      == 3300원') 

print('민초레오    == 3500원') 

print('바나나 초코 == 3500원') 

print() 

print() 

def funa1():  # a1  남자 횟수 증가시키는 함수 + 계산 

    global a1 

    global sum1 

    a1=a1+1 

    print('제철과일을 선택하셨습니다. 가격은 3500원입니다.') 

    print() 

    sum1=sum1+3500 

def funb1(): 

    global b1 

    global sum1 

    b1=b1+1 

    print('블루베리를 선택하셨습니다. 가격은 3300원입니다.') 

    print() 

    sum1=sum1+3300 

def func1(): 

    global c1 

    global sum1 

    c1=c1+1 

    print() 

    print('카라멜을 선택하셨습니다. 가격은 3300원입니다.') 

    sum1=sum1+3300 

def fund1(): 

    global d1 

    global sum1 

    d1=d1+1 

    print('딸기를 선택하셨습니다. 가격은 3300원입니다.') 

    print() 

    sum1=sum1+3300 

def fune1(): 

    global e1 

    global sum1 

    e1=e1+1 

    print('망고를 선택하셨습니다. 가격은 3500원입니다.') 

    print() 

    sum1=sum1+3500 

def funf1(): 

    global f1 

    global sum1 

    f1=f1+1 

    print('오렌지를 선택하셨습니다. 가격은 3500원입니다.') 

    print() 

    sum1=sum1+3500 

def fung1(): 

    global g1 

    global sum1 

    g1=g1+1 

    print('초코를 선택하셨습니다. 가격은 3300원입니다.') 

    print() 

    sum1=sum1+3300 

def funh1(): 

    global h1 

    global sum1 

    h1=h1+1 

    print('오레오를 선택하셨습니다. 가격은 3300원입니다.') 

    print() 

    sum1=sum1+3300 

def funi1(): 

    global i1 

    global sum1 

    i1=i1+1 

    print('민초레오을 선택하셨습니다. 가격은 3500원입니다.') 

    print() 

    sum=sum+3500 

def funj1(): 

    global j1 

    global sum1 

    j1=j1+1 

    print('바나나 초코를 선택하셨습니다. 가격은 3500원입니다.') 

    print() 

    sum1=sum1+3500 

  

  

  

     

def funa2():  # a2 여자 횟수 증가시키는 함수 +계산  

    global a2 

    global sum 

    a2=a2+1 

    print('제철과일을 선택하셨습니다. 가격은 3500원입니다.') 

    print() 

    sum1=sum1+3500 

def funb2(): 

    global b2 

    global sum1 

    b2=b2+1 

    print('블루베리를 선택하셨습니다. 가격은 3300원입니다.') 

    print() 

    sum1=sum1+3300 

def func2(): 

    global c2 

    global sum1 

    c2=c2+1 

    print('카라멜을 선택하셨습니다. 가격은 3300원입니다.') 

    print() 

    sum1=sum1+3300 

def fund2(): 

    global d2 

    global sum1 

    d2=d2+1 

    print('딸기를 선택하셨습니다. 가격은 3300원입니다.') 

    print() 

    sum1=sum1+3300 

def fune2(): 

    global e2 

    global sum1 

    e2=e2+1 

    print('망고를 선택하셨습니다. 가격은 3500원입니다.') 

    print() 

    sum1=sum1+3500 

def funf2(): 

    global f2 

    global sum1 

    f2=f2+1 

    print('오렌지를 선택하셨습니다. 가격은 3500원입니다.') 

    print() 

    sum1=sum1+3500 

def fung2(): 

    global g2 

    global sum1 

    g2=g2+1 

    print('초코를 선택하셨습니다. 가격은 3300원입니다.') 

    print() 

    sum=sum+3300 

def funh2(): 

    global h2 

    global sum1 

    h2=h2+1 

    print('오레오를 선택하셨습니다. 가격은 3300원입니다.') 

    print() 

    sum1=sum1+3300 

def funi2(): 

    global i2 

    global sum1 

    i2=i2+1 

    print('민초레오를 선택하셨습니다. 가격은 3500원입니다.') 

    print() 

    sum=sum+3500 

def funj2(): 

    global j2 

    global sum1 

    j2=j2+1 

    print('바나나 초코를 선택하셨습니다. 가격은 3500원입니다.') 

    print() 

    sum1=sum1+3500 

def cho1(): #각각의 메뉴들 함수로 이동(남자) 

    while True: 

        n=input('메뉴를 입력하세요:') 

        if n=='제철과일': 

            funa1() 

            break 

        elif n=='블루베리': 

            funb1() 

            break 

        elif n=='카라멜': 

            func1() 

            break 

        elif n=='딸기': 

            fund1() 

            break 

        elif n=='망고': 

            fune1() 

            break 

        elif n=='오렌지': 

            funf1() 

            break 

        elif n=='초코': 

            fung1() 

            break 

        elif n=='오레오': 

            funh1() 

            break 

        elif n=='민초레오': 

            funi1() 

            break 

        elif n=='바나나 초코' : 

            funj1() 

            break 

        elif n=='바나나초코' : 

            funj1() 

            break 

        else: 

            print('메뉴이름을 다시 입력해 주세요.') 

         

def cho2(): #각각의 메뉴들 함수로 이동(여자) 

    while True: 

        n=input('메뉴를 입력하세요:') 

        if n=='제철과일': 

            funa2() 

            break 

        elif n=='블루베리': 

            funb2() 

            break 

        elif n=='카라멜': 

            func2() 

            break 

        elif n=='딸기': 

            fund2() 

            break 

        elif n=='망고': 

            fune2() 

            break 

        elif n=='오렌지': 

            funf2() 

            break 

        elif n=='초코': 

            fung2() 

            break 

        elif n=='오레오': 

            funh2() 

            break 

        elif n=='민초레오': 

            funi2() 

            break 

        elif n=='바나나 초코' : 

            funj2() 

            break 

        elif n=='바나나초코' : 

            funj2() 

            break 

        else: 

            print('메뉴이름을 다시 입력해 주세요.') 

sum1=0 

li=[] 

while True: 

    print('현재 요거바라 메뉴들에대한 사람들의 구매횟수는 다음과 같습니다.') 

    print(f'제철과일    남자:{a1}회 여자:{a2}회') 

    print(f'블루베리    남자:{b1}회 여자:{b2}회') 

    print(f'카라멜      남자:{c1}회 여자:{c2}회') 

    print(f'딸기        남자:{d1}회 여자:{d2}회') 

    print(f'망고        남자:{e1}회 여자:{e2}회') 

    print(f'오렌지      남자:{f1}회 여자:{f2}회') 

    print(f'초코        남자:{g1}회 여자:{g2}회') 

    print(f'오레오      남자:{h1}회 여자:{h2}회') 

    print(f'민초레오    남자:{i1}회 여자:{i2}회') 

    print(f'바나나 초코 남자:{j1}회 여자:{j2}회') 

    print() 

    print('======== 메뉴 ========') 

    print('1. 상품선택') 

    print('2. 종료') 

    print('3. 결제하기') 

    print('4. 상품 추천하기') 

    print('5. 오늘의 요거바라(랜덤 추천)') 

     

    w=int(input('메뉴를 입력하세요:')) 

    if w==1: 

        while True: 

            q=input('성별을 입력하세요:') 

            if q=='남성': 

                cho1() 

                break 

            elif q=='남자': 

                cho1() 

                break 

            elif q=='남': 

                cho1() 

                break 

            elif q=='여성' : 

                cho2() 

                break 

            elif q=='여자' : 

                cho2() 

                break 

            elif q=='여' : 

                cho2() 

                break 

            else: 

                print('성별을 다시 입력해 주세요.') 

         

    elif w==2: 

        print('종료합니다') 

        break 

    elif w==3: 

        print('결제를 시작합니다.') 

        print(f'총 금액은 {sum1}원 입니다.') 

        time.sleep(5) 

        sum1=0 

        print(f'잔액은 {sum1}원 입니다.') 

        print() 

    elif w==4: 

        add=input('어떤상품을 추가하길 희망하십니까:') 

        li.append(add) 

        print(f'현재 대중들이 추가하신 희망하는 메뉴는 {li}입니다.') 

        print() 

        print() 

        print() 

    elif w==5: 

        recommend = random.sample(yoga,1) 

        print(f'오늘의 요거바라 추천 메뉴는 {recommend}입니다.') 

        print() 

         
if __name__ == '__main__':
    app.run(debug=True)
