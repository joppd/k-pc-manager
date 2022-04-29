import time
import win32con
import win32api
import win32gui


class KakaoControl:
    def __init__(self, kakao_opentalk_name: str):
        # # 핸들
        self._hwndMain = win32gui.FindWindow(None, kakao_opentalk_name)
        print('hwndMain = ' + str(self._hwndMain))
        self._hwndEdit = win32gui.FindWindowEx(self._hwndMain, None, "RichEdit50W", None)
        print('hwndEdit = ' + str(self._hwndEdit))

    def kakao_sendtext(self, chat_message: str):
        if self._hwndEdit <= 0:
            return
        _res = win32api.SendMessage(self._hwndEdit, win32con.WM_SETTEXT, 0, chat_message)
        print('SendMessage result = ' + str(_res))
        self._send_return(self._hwndEdit)

    # # 엔터
    def _send_return(self, hwnd):
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        time.sleep(0.01)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

