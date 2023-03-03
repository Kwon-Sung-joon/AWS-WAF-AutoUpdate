# AWS WAF WhiteList Update
- 자동으로 바뀌는 AWS 리소스 IP Range를 WhiteList에 등록하도록 자동화


# Architecture
- AWS 에서 제공하는 SNS Topic을 구독 (arn:aws:sns:us-east-1:806199016981:AmazonIpSpaceChanged)
- 해당 Topic을 Lambda Trigger에 추가
- Lambda를 사용하여 WAF WhiteList에 해당 서비스 IP Range 등록 (e.g. CloudFront Ip Range)

<img width="760" alt="image" src="https://user-images.githubusercontent.com/43159901/187220882-e2d6251b-adc7-4f2e-9604-7ff1265b0fa6.png">

