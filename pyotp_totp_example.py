import hashlib
import base64
import pyotp
import datetime

'''
pyotp 라이브러리를 이용한 TOTP 사용

otp_key : bytes형, otp 키 데이터
refresh_time : int형, OTP 갱신 시간
digest_mode : hashlib, 암호화 해시 모드
current_time : int형, 현재 시간(밀리세컨드)
'''
def totp_pyotp(otp_key, refresh_time, digest_mode, current_time):
    key = base64.b32encode(otp_key)    
    totp = pyotp.TOTP(key, interval=refresh_time, digest=digest_mode)
    return totp.at(current_time)



# 암호화 해시 모드
digest_mode = hashlib.sha256
'''
hashlib.md5
hashlib.sha1
hashlib.sha256
hashlib.sha512
'''

# 현재 시간
now = datetime.datetime.now()

# OTP 키
otp_key = bytes([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32])

# 갱신 주기
refresh_time = 180

print('TOTP hash mode : ', digest_mode().name)
print('current time : ', now)
print('current time(ms) : ', now.timestamp())
print('OTP key : ', otp_key.hex())
print('refresh time(sec) : ', refresh_time)

# pytop 사용
print('      by pyotp :', totp_pyotp(otp_key, refresh_time, digest_mode, now.timestamp()))