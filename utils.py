from kavenegar import *
def send_otp_code(phone_number,code):
    try:
        api = KavenegarAPI('645850486565684278763146413374767A634472364F50746C6F396F4D734C53477A464B2B336C696E59593D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'your verification code is this : {code}',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


