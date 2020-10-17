import hashlib
import datetime
import pyotp_totp_example as pyotp_totp
import hmac_totp_example as h_totp

if __name__ == "__main__":
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

    # pyotp 사용
    print('      by pyotp :', pyotp_totp.totp(otp_key, refresh_time, digest_mode, now.timestamp()))
    # hmac 사용
    print('      by hmac :', h_totp.totp(otp_key, refresh_time, digest_mode, now.timestamp()))
    