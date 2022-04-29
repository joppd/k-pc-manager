from control.kakao_control import KakaoControl


if __name__ == "__main__":
    # # 카톡창 이름 (열려있는 상태, 최소화 X, 창뒤에 숨어있는 비활성화 상태 가능)
    kakao_opentalk_name = '윤정♥'

    kc = KakaoControl(kakao_opentalk_name)

    # # 채팅 전송
    chat_message = "this is test for you. hello world."
    kc.kakao_sendtext(chat_message)