#!/usr/bin/env python3
#
# Copyright Noriaki Ando <Noriaki.Ando@gmail.com>
#
# This scprit extracts an original URL from the Outlook's safelink URL. 
#
import re
import urllib.parse
import sys

# Safe Links文字列からURLを抽出する関数
def extract_original_url(safelinks_string):
    # 正規表現パターンを定義
    pattern = r'URL=https?://jpn01\.safelinks\.protection\.outlook\.com/\?url=([^&]+)'

    # 正規表現を使用してURLを抽出
    match = re.search(pattern, safelinks_string)
    
    if match:
        # マッチした部分を取得
        url_encoded = match.group(1)
        
        # URLデコードして元のURLを取得
        original_url = urllib.parse.unquote(url_encoded)
        
        return original_url
    else:
        return None

def help():
    print("""Usage:
    %s \"https://<outlook safelink URL>\" 
    Safelinkはダブルクオート(\")で囲ってください。
    """ % sys.argv[0])

#----------
# main
#----------
if len(sys.argv) < 2:
    help()
    sys.exit(1)

# Safe Links文字列の例
safelinks_string = "SafeLinks: URL=" + sys.argv[1]
# URLを抽出
original_url = extract_original_url(safelinks_string)

if original_url:
    print("元のURL:", original_url)
else:
    print("元のURLは見つかりませんでした。")
