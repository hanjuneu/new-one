krw = input("환전하고자 하는 금액을 입력하세요.: ")
choose = input("무슨 화폐의 환전을 원하니?(1.usd, 2.aud, 3.nzd)")

if choose == 1:
  usd = round(int(krw)/1141.50,2)
  print('미국: ', usd, 'USD')
else if choose == 2:
  aud = round(int(krw)/905.15,2)
  print('호주: ', aud, 'AUD')
else if choose == 3:
  nzd = round(int(krw)/836.15,2)
  print('뉴질랜드: ', nzd, 'NZD')
else:
  print("다시 입력해주세요.)
