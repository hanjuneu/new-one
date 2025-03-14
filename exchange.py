krw = input("환전하고자 하는 금액을 입력하세요.: ")

usd = round(int(krw)/1141.50,2)
aud = round(int(krw)/905.15,2)
nzd = round(int(krw)/836.15,2)

print('미국: ', usd, 'USD')
print('호주: ', aud, 'AUD')
print('뉴질랜드: ', nzd, 'NZD')
