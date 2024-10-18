# AWS WAF WhiteList Update

이 프로젝트는 자동으로 바뀌는 AWS 리소스 IP Range를 AWS WAF의 화이트리스트에 등록하도록 자동화하는 스크립트입니다.

## 기능

- AWS에서 제공하는 SNS Topic을 구독하여 IP 범위 변경 알림을 수신
- 변경된 IP 범위를 AWS WAF 화이트리스트에 자동으로 등록

## 아키텍처

- AWS SNS Topic (예: `arn:aws:sns:us-east-1:806199016981:AmazonIpSpaceChanged`)을 구독합니다.
- 해당 SNS Topic을 AWS Lambda 트리거로 추가합니다.
- Lambda 함수를 사용하여 WAF 화이트리스트에 해당 서비스의 IP 범위 (예: CloudFront IP Range)를 등록합니다.

![Architecture Diagram](https://user-images.githubusercontent.com/43159901/187220882-e2d6251b-adc7-4f2e-9604-7ff1265b0fa6.png)

## 사용 방법

1. **AWS Lambda 함수 설정**
   - 위 코드를 AWS Lambda에 배포합니다.
   - 환경 변수로 `IP_SET_NAME`과 `IP_SET_ID`를 설정합니다.

2. **SNS Topic 구독**
   - AWS 콘솔에서 제공하는 SNS Topic을 생성하고, Lambda 함수가 해당 Topic을 구독하도록 설정합니다.

3. **IAM 권한**
   - Lambda 함수가 AWS WAF와 SNS에 접근할 수 있도록 적절한 IAM 역할을 설정합니다.

## 코드 설명

- `get_ip_ranges(url, expected_hash)`: 주어진 URL에서 IP 범위를 가져오고, MD5 해시를 확인합니다.
- `get_cf_range(service, ip_ranges)`: 주어진 서비스의 IP 프리픽스를 반환합니다.
- `update_waf_ip_set(ipsetName, ipsetId, addresses)`: WAF IP Set을 업데이트하여 주어진 주소 목록을 추가합니다.
- `lambda_handler(event, context)`: Lambda 함수의 엔트리 포인트로, SNS 메시지를 처리하고 WAF 화이트리스트를 업데이트합니다.
