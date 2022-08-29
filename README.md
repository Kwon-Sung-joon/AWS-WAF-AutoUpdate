# AWS-WAF-AutoUpdate
서비스 운영 중 일부 사용자에게 403 Error로 서비스에 접속할 수 없는 것을 확인했다. <br>
운영계에는 어떠한 변경사항도 없었으며, 하루아침에 접속할 수 없는 사용자가 많아졌다. <br>
서비스 점검 중, ALB에 적용되어 있는 WAF Rule에 우연히 새로 바뀐 CloudFront Edge Location IP 대역이 BlackList에 적용되어 있었고, <br>
해당 Rule에서 제거하니 문제는 해결됐다. <br> 

# 조치 방안
Amazon은 내부 서비스 IP 대역으 주기적으로 변경한다. <br>
해당 IP 대역은 언제, 어떤식으로 바뀔지 알 수 없지만 AWS 측에서 IP Range가 변경될 시 SNS로 알람을 받을 수 있다. <br>


1. AWS 에서 제공하는 SNS Topic을 구독 (arn:aws:sns:us-east-1:806199016981:AmazonIpSpaceChanged)
2. 해당 Topic을 Lambda Trigger에 추가
3. Lambda를 사용하여 WAF WhiteList에 해당 서비스 IP Range 등록 (e.g. CloudFront Ip Range)

<img width="760" alt="image" src="https://user-images.githubusercontent.com/43159901/187220882-e2d6251b-adc7-4f2e-9604-7ff1265b0fa6.png">


## Step 1. Create Lambda
#### Lambda IAM Role에는 WAF Policy 필요 (본 과정에서는 생략)


#### 환경 변수 설정
#### WhiteList로 적용 할 IP set Name/ID 
<img width="743" alt="image" src="https://user-images.githubusercontent.com/43159901/187222811-8c400375-b565-4f3a-88aa-70efe44c078d.png">


## Step 2. Subscribe Topic (arn:aws:sns:us-east-1:806199016981:AmazonIpSpaceChanged)


## Step 3. Run Lambda (Test Event) 

<img width="1439" alt="image" src="https://user-images.githubusercontent.com/43159901/187221682-48ecba65-54c1-4e95-a4b7-9a8818739be6.png">


