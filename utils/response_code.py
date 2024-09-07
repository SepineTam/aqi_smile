#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : response_code.py

_RESPONSE_CODES = {
    "200": "请求成功",
    "204": "请求成功，但你查询的地区暂时没有你需要的数据。",
    "400": "请求错误，可能包含错误的请求参数或缺少必选的请求参数。",
    "401": "认证失败，可能使用了错误的KEY、数字签名错误、KEY的类型错误（如使用SDK的KEY去访问Web API）。",
    "402": "超过访问次数或余额不足以支持继续访问服务，你可以充值、升级访问量或等待访问量重置。",
    "403": "无访问权限，可能是绑定的PackageName、BundleID、域名IP地址不一致，或者是需要额外付费的数据。",
    "404": "查询的数据或地区不存在。",
    "429": "超过限定的QPM（每分钟访问次数），请参考QPM说明",
    "500": "无响应或超时，接口服务异常请联系我们"
}

def response_state(code: str) -> tuple[bool, str]:
    if type(code) is int:
        code = str(code)
    if code == "200":
        return True, _RESPONSE_CODES["200"]
    else:
        if code in _RESPONSE_CODES:
            return False, f"{code}, {_RESPONSE_CODES[code]}"
        else:
            return False, f"{code}, 未知错误"


if __name__ == "__main__":
    print(response_state("200")[0])

