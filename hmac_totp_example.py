import hashlib
import hmac
import datetime

'''
hmac을 이용한 TOTP 사용

otp_key : bytes형, otp 키 데이터
refresh_time : int형, OTP 갱신 시간
digest_mode : hashlib, 암호화 해시 모드
current_time : int형, 현재 시간(밀리세컨드)
'''
def totp_hmac(otp_key, refresh_time, digest_mode, current_time):        
    otp_time_data = [0] * 8

    steps = int(current_time/refresh_time)
    
    otp_time_data[4] = ((steps>>24) & 0xFF)
    otp_time_data[5] = ((steps>>16) & 0xFF)
    otp_time_data[6] = ((steps>>8) & 0xFF)
    otp_time_data[7] = (steps & 0xFF)

    otp_digest = hmac.new(otp_key, bytes(otp_time_data), digestmod=digest_mode).digest()

    #digest length
    #sha1 = 20
    #sha256 = 32
    #sha384 = 48
    #sha512 = 64    
    offset = otp_digest[len(otp_digest)-1] & 0x0F
    truncatedHash = 0
    for n in range(0,4):
        truncatedHash = truncatedHash << 8        
        truncatedHash = truncatedHash | otp_digest[offset + n]
    truncatedHash = (truncatedHash & 0x7FFFFFFF) % 1000000
    
    return truncatedHash


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

# hmac 사용
print('      by hmac :', totp_hmac(otp_key, refresh_time, digest_mode, now.timestamp()))