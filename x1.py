#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from urllib.parse import parse_qs,urlparse
from django.http.request import QueryDict
#
v = 'http://47.92.87.172:8000/?total_amount=100.00&timestamp=2017-08-15+23%3A53%3A34&sign=e9E9UE0AxR84NK8TP1CicX6aZL8VQj68ylugWGHnM79zA7BKTIuxxkf%2FvhdDYz4XOLzNf9pTJxTDt8tTAAx%2FfUAJln4WAeZbacf1Gp4IzodcqU%2FsIc4z93xlfIZ7OLBoWW0kpKQ8AdOxrWBMXZck%2F1cffy4Ya2dWOYM6Pcdpd94CLNRPlH6kFsMCJCbhqvyJTflxdpVQ9kpH%2B%2Fhpqrqvm678vLwM%2B29LgqsLq0lojFWLe5ZGS1iFBdKiQI6wZiisBff%2BdAKT9Wcao3XeBUGigzUmVyEoVIcWJBH0Q8KTwz6IRC0S74FtfDWTafplUHlL%2Fnf6j%2FQd1y6Wcr2A5Kl6BQ%3D%3D&trade_no=2017081521001004340200204115&sign_type=RSA2&auth_app_id=2016080600180695&charset=utf-8&seller_id=2088102170208070&method=alipay.trade.page.pay.return&app_id=2016080600180695&out_trade_no=20170202185&version=1.0'
o = urlparse(v)
query = parse_qs(o.query)
print(query)
for item,v in query.items():
    print(item,v)
print('===============')

result = b'gmt_create=2017-11-24+12%3A18%3A01&charset=utf-8&gmt_payment=2017-11-24+12%3A18%3A09&notify_time=2017-11-24+12%3A18%3A10&subject=%E5%85%85%E6%B0%94%E5%BC%8F%E9%9F%A9%E7%BA%A2&sign=f9PuoOKIMxplXxw4%2FRxMRoZ5lpJhVA8n5rkJBb0oR8%2BPOiTfPqLE8fBVaszYIMi2gxaC%2FL%2FIwCt7zDLhjzrmf4lVs2KL9F4%2B3KF9HTCXfmkqkFjLbrQEe5DR%2BEzUDFGb%2FPuEO25lzvdOekhi%2B8EJfWP%2FmZGWexz5KjTJbcmWOIab1bZdbU%2FNZztRU5EzgJHyA6LhnA5wVAZ1mo63pjyU%2BQDFq9ojZQDMeA84N4qiEQ%2FhPm8DzCozBtySDbYvjJygOtC9CjKslWi9EeE37EfVcYWd5gi4f5yssz73MoBp2MneVHrCGh6Grkukp4M0OTtjwk4IYJ09x99q%2FGoFkXRKPQ%3D%3D&buyer_id=2088102175098973&invoice_amount=11.00&version=1.0&notify_id=f61477b4c872979cd6a743c280d5fbcnhi&fund_bill_list=%5B%7B%22amount%22%3A%2211.00%22%2C%22fundChannel%22%3A%22ALIPAYACCOUNT%22%7D%5D&notify_type=trade_status_sync&out_trade_no=order1511497073&total_amount=11.00&trade_status=TRADE_SUCCESS&trade_no=2017112421001004970200328644&auth_app_id=2016082500309412&receipt_amount=11.00&point_amount=0.00&app_id=2016082500309412&buyer_pay_amount=11.00&sign_type=RSA2&seller_id=2088102172939262'
data =result.decode('utf-8')
v1 = parse_qs(data)
for k,v in v1.items():
    print(k,v)


