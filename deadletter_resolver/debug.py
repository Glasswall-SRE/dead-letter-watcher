import lambda_function


event = {
    "resource": "/resolve",
    "path": "/resolve",
    "httpMethod": "POST",
    "headers": {
        "Accept": "application/json,*/*",
        "Accept-Encoding": "gzip,deflate",
        "CloudFront-Forwarded-Proto": "https",
        "CloudFront-Is-Desktop-Viewer": "true",
        "CloudFront-Is-Mobile-Viewer": "false",
        "CloudFront-Is-SmartTV-Viewer": "false",
        "CloudFront-Is-Tablet-Viewer": "false",
        "CloudFront-Viewer-Country": "US",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "121mhh1ma6.execute-api.eu-west-2.amazonaws.com",
        "User-Agent": "Slackbot 1.0 (+https://api.slack.com/robots)",
        "Via": "1.1 aa0ac259128059e949248e63a3b6767e.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "yr4JQq_OiliTSvnugrA765nkC5ud6nKGg136t9RNV8j_lGkB4927-Q==",
        "X-Amzn-Trace-Id": "Root=1-5efa6d7b-181f937b3cf1183952f7a3b9",
        "X-Forwarded-For": "3.82.138.201, 70.132.60.149",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https",
        "X-Slack-Request-Timestamp": "1593470331",
        "X-Slack-Signature": "v0=931dbf8c926dc3d60dea0aefbe194d1f0ca0c01ee31d52651c119d9ad94db736"
    },
    "multiValueHeaders": {
        "Accept": [
            "application/json,*/*"
        ],
        "Accept-Encoding": [
            "gzip,deflate"
        ],
        "CloudFront-Forwarded-Proto": [
            "https"
        ],
        "CloudFront-Is-Desktop-Viewer": [
            "true"
        ],
        "CloudFront-Is-Mobile-Viewer": [
            "false"
        ],
        "CloudFront-Is-SmartTV-Viewer": [
            "false"
        ],
        "CloudFront-Is-Tablet-Viewer": [
            "false"
        ],
        "CloudFront-Viewer-Country": [
            "US"
        ],
        "Content-Type": [
            "application/x-www-form-urlencoded"
        ],
        "Host": [
            "121mhh1ma6.execute-api.eu-west-2.amazonaws.com"
        ],
        "User-Agent": [
            "Slackbot 1.0 (+https://api.slack.com/robots)"
        ],
        "Via": [
            "1.1 aa0ac259128059e949248e63a3b6767e.cloudfront.net (CloudFront)"
        ],
        "X-Amz-Cf-Id": [
            "yr4JQq_OiliTSvnugrA765nkC5ud6nKGg136t9RNV8j_lGkB4927-Q=="
        ],
        "X-Amzn-Trace-Id": [
            "Root=1-5efa6d7b-181f937b3cf1183952f7a3b9"
        ],
        "X-Forwarded-For": [
            "3.82.138.201, 70.132.60.149"
        ],
        "X-Forwarded-Port": [
            "443"
        ],
        "X-Forwarded-Proto": [
            "https"
        ],
        "X-Slack-Request-Timestamp": [
            "1593470331"
        ],
        "X-Slack-Signature": [
            "v0=931dbf8c926dc3d60dea0aefbe194d1f0ca0c01ee31d52651c119d9ad94db736"
        ]
    },
    "queryStringParameters": None,
    "multiValueQueryStringParameters": None,
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {
        "resourceId": "7rt221",
        "resourcePath": "/resolve",
        "httpMethod": "POST",
        "extendedRequestId": "O6YLVGc5LPEFiAQ=",
        "requestTime": "29/Jun/2020:22:38:51 +0000",
        "path": "/dev/resolve",
        "accountId": "433250546572",
        "protocol": "HTTP/1.1",
        "stage": "dev",
        "domainPrefix": "121mhh1ma6",
        "requestTimeEpoch": 1593470331664,
        "requestId": "3047926c-5de4-4d04-93d7-4d1014ed8ff5",
        "identity": {
            "cognitoIdentityPoolId": None,
            "accountId": None,
            "cognitoIdentityId": None,
            "caller": None,
            "sourceIp": "3.82.138.201",
            "principalOrgId": None,
            "accessKey": None,
            "cognitoAuthenticationType": None,
            "cognitoAuthenticationProvider": None,
            "userArn": None,
            "userAgent": "Slackbot 1.0 (+https://api.slack.com/robots)",
            "user": None
        },
        "domainName": "121mhh1ma6.execute-api.eu-west-2.amazonaws.com",
        "apiId": "121mhh1ma6"
    },
    "body": "payload=%7B%22type%22%3A%22block_actions%22%2C%22user%22%3A%7B%22id%22%3A%22URG1A1X6F%22%2C%22username%22%3A%22tpilvelis%22%2C%22name%22%3A%22tpilvelis%22%2C%22team_id%22%3A%22TRQU3V52S%22%7D%2C%22api_app_id%22%3A%22A0140DL5V3P%22%2C%22token%22%3A%2298mK44cYmUCpGrr13iRzfeTE%22%2C%22container%22%3A%7B%22type%22%3A%22message%22%2C%22message_ts%22%3A%221593467852.000500%22%2C%22channel_id%22%3A%22D014RLFBU4Q%22%2C%22is_ephemeral%22%3Afalse%7D%2C%22trigger_id%22%3A%221219108212532.874955991094.74bae55de677e567e86e51dcfd2df8e1%22%2C%22team%22%3A%7B%22id%22%3A%22TRQU3V52S%22%2C%22domain%22%3A%22glasswall-solutions%22%7D%2C%22channel%22%3A%7B%22id%22%3A%22D014RLFBU4Q%22%2C%22name%22%3A%22directmessage%22%7D%2C%22message%22%3A%7B%22bot_id%22%3A%22B0141R5SM98%22%2C%22type%22%3A%22message%22%2C%22text%22%3A%22deadletter%22%2C%22user%22%3A%22U01421WQ84B%22%2C%22ts%22%3A%221593467852.000500%22%2C%22team%22%3A%22TRQU3V52S%22%2C%22blocks%22%3A%5B%7B%22type%22%3A%22section%22%2C%22block_id%22%3A%22x3LGk%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22Hi+SRE%2C+Oopsie+Whoopsie%2C+UwU%2C+You+have+Service+Bus+Dead+Letters%3A%5CnCluster+%3A+dev%5CnService+%3A+smtptransmission%5CnCount+%3A+31.1105%22%2C%22verbatim%22%3Afalse%7D%7D%2C%7B%22type%22%3A%22divider%22%2C%22block_id%22%3A%22tbiO3%22%7D%2C%7B%22type%22%3A%22section%22%2C%22block_id%22%3A%22VzH%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22%2A%3CfakeLink.datadoglink.com%7C1234%3E%2A%5CnTenant+Name%3A+Cannot+Find+in+DataDog+Log%5CnSender%3A+Cannot+Find+in+DataDog+Log%5CnReceiver%3A+Cannot+Find+in+DataDog+Log%22%2C%22verbatim%22%3Afalse%7D%2C%22accessory%22%3A%7B%22type%22%3A%22static_select%22%2C%22placeholder%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Select+Action%22%2C%22emoji%22%3Atrue%7D%2C%22options%22%3A%5B%7B%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22replay%22%2C%22emoji%22%3Atrue%7D%2C%22value%22%3A%22value-replay%22%7D%2C%7B%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22reconstruct%22%2C%22emoji%22%3Atrue%7D%2C%22value%22%3A%22value-reconstruct%22%7D%5D%2C%22action_id%22%3A%22Gl0%3D%22%7D%7D%2C%7B%22type%22%3A%22divider%22%2C%22block_id%22%3A%22GgD%22%7D%2C%7B%22type%22%3A%22actions%22%2C%22block_id%22%3A%22Usthl%22%2C%22elements%22%3A%5B%7B%22type%22%3A%22button%22%2C%22action_id%22%3A%22sScW0%22%2C%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Run%22%2C%22emoji%22%3Atrue%7D%2C%22value%22%3A%22value-run%22%7D%5D%7D%5D%7D%2C%22response_url%22%3A%22https%3A%5C%2F%5C%2Fhooks.slack.com%5C%2Factions%5C%2FTRQU3V52S%5C%2F1206195374598%5C%2FLl4RoSzgrE1kALJjSQFWLN1L%22%2C%22actions%22%3A%5B%7B%22action_id%22%3A%22sScW0%22%2C%22block_id%22%3A%22Usthl%22%2C%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Run%22%2C%22emoji%22%3Atrue%7D%2C%22value%22%3A%22value-run%22%2C%22type%22%3A%22button%22%2C%22action_ts%22%3A%221593470331.396894%22%7D%5D%7D",
    "isBase64Encoded": False
}

event2 = {
    "resource": "/resolve",
    "path": "/resolve",
    "httpMethod": "POST",
    "headers": {
        "Accept": "application/json,*/*",
        "Accept-Encoding": "gzip,deflate",
        "CloudFront-Forwarded-Proto": "https",
        "CloudFront-Is-Desktop-Viewer": "true",
        "CloudFront-Is-Mobile-Viewer": "false",
        "CloudFront-Is-SmartTV-Viewer": "false",
        "CloudFront-Is-Tablet-Viewer": "false",
        "CloudFront-Viewer-Country": "US",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "121mhh1ma6.execute-api.eu-west-2.amazonaws.com",
        "User-Agent": "Slackbot 1.0 (+https://api.slack.com/robots)",
        "Via": "1.1 c242c974a465288488c7876cabca7752.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "NbkfEPZQsBcOSSViDD3aQaqlebrFo_5G8rp32596IhzOZ-IcEKxvsQ==",
        "X-Amzn-Trace-Id": "Root=1-5efa6b95-3d33dd3cff8050440fd2c5d4",
        "X-Forwarded-For": "54.175.25.232, 70.132.60.90",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https",
        "X-Slack-Request-Timestamp": "1593469844",
        "X-Slack-Signature": "v0=e963e3ca361df13fa77bf1a682b1d54bd92594a79a291a09b9da9e608c51e026"
    },
    "multiValueHeaders": {
        "Accept": [
            "application/json,*/*"
        ],
        "Accept-Encoding": [
            "gzip,deflate"
        ],
        "CloudFront-Forwarded-Proto": [
            "https"
        ],
        "CloudFront-Is-Desktop-Viewer": [
            "true"
        ],
        "CloudFront-Is-Mobile-Viewer": [
            "false"
        ],
        "CloudFront-Is-SmartTV-Viewer": [
            "false"
        ],
        "CloudFront-Is-Tablet-Viewer": [
            "false"
        ],
        "CloudFront-Viewer-Country": [
            "US"
        ],
        "Content-Type": [
            "application/x-www-form-urlencoded"
        ],
        "Host": [
            "121mhh1ma6.execute-api.eu-west-2.amazonaws.com"
        ],
        "User-Agent": [
            "Slackbot 1.0 (+https://api.slack.com/robots)"
        ],
        "Via": [
            "1.1 c242c974a465288488c7876cabca7752.cloudfront.net (CloudFront)"
        ],
        "X-Amz-Cf-Id": [
            "NbkfEPZQsBcOSSViDD3aQaqlebrFo_5G8rp32596IhzOZ-IcEKxvsQ=="
        ],
        "X-Amzn-Trace-Id": [
            "Root=1-5efa6b95-3d33dd3cff8050440fd2c5d4"
        ],
        "X-Forwarded-For": [
            "54.175.25.232, 70.132.60.90"
        ],
        "X-Forwarded-Port": [
            "443"
        ],
        "X-Forwarded-Proto": [
            "https"
        ],
        "X-Slack-Request-Timestamp": [
            "1593469844"
        ],
        "X-Slack-Signature": [
            "v0=e963e3ca361df13fa77bf1a682b1d54bd92594a79a291a09b9da9e608c51e026"
        ]
    },
    "queryStringParameters": None,
    "multiValueQueryStringParameters": None,
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {
        "resourceId": "7rt221",
        "resourcePath": "/resolve",
        "httpMethod": "POST",
        "extendedRequestId": "O6W_UHeQLPEFrwg=",
        "requestTime": "29/Jun/2020:22:30:45 +0000",
        "path": "/dev/resolve",
        "accountId": "433250546572",
        "protocol": "HTTP/1.1",
        "stage": "dev",
        "domainPrefix": "121mhh1ma6",
        "requestTimeEpoch": 1593469845181,
        "requestId": "412799b4-5c47-433b-ac59-f0e4cd319e2e",
        "identity": {
            "cognitoIdentityPoolId": None,
            "accountId": None,
            "cognitoIdentityId": None,
            "caller": None,
            "sourceIp": "54.175.25.232",
            "principalOrgId": None,
            "accessKey": None,
            "cognitoAuthenticationType": None,
            "cognitoAuthenticationProvider": None,
            "userArn": None,
            "userAgent": "Slackbot 1.0 (+https://api.slack.com/robots)",
            "user": None
        },
        "domainName": "121mhh1ma6.execute-api.eu-west-2.amazonaws.com",
        "apiId": "121mhh1ma6"
    },
    "body": "payload=%7B%22type%22%3A%22block_actions%22%2C%22user%22%3A%7B%22id%22%3A%22URG1A1X6F%22%2C%22username%22%3A%22tpilvelis%22%2C%22name%22%3A%22tpilvelis%22%2C%22team_id%22%3A%22TRQU3V52S%22%7D%2C%22api_app_id%22%3A%22A0140DL5V3P%22%2C%22token%22%3A%2298mK44cYmUCpGrr13iRzfeTE%22%2C%22container%22%3A%7B%22type%22%3A%22message%22%2C%22message_ts%22%3A%221593467852.000500%22%2C%22channel_id%22%3A%22D014RLFBU4Q%22%2C%22is_ephemeral%22%3Afalse%7D%2C%22trigger_id%22%3A%221213125741283.874955991094.ba194a4561a8951d445c384fc0fcf8b8%22%2C%22team%22%3A%7B%22id%22%3A%22TRQU3V52S%22%2C%22domain%22%3A%22glasswall-solutions%22%7D%2C%22channel%22%3A%7B%22id%22%3A%22D014RLFBU4Q%22%2C%22name%22%3A%22directmessage%22%7D%2C%22message%22%3A%7B%22bot_id%22%3A%22B0141R5SM98%22%2C%22type%22%3A%22message%22%2C%22text%22%3A%22deadletter%22%2C%22user%22%3A%22U01421WQ84B%22%2C%22ts%22%3A%221593467852.000500%22%2C%22team%22%3A%22TRQU3V52S%22%2C%22blocks%22%3A%5B%7B%22type%22%3A%22section%22%2C%22block_id%22%3A%22x3LGk%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22Hi+SRE%2C+Oopsie+Whoopsie%2C+UwU%2C+You+have+Service+Bus+Dead+Letters%3A%5CnCluster+%3A+dev%5CnService+%3A+smtptransmission%5CnCount+%3A+31.1105%22%2C%22verbatim%22%3Afalse%7D%7D%2C%7B%22type%22%3A%22divider%22%2C%22block_id%22%3A%22tbiO3%22%7D%2C%7B%22type%22%3A%22section%22%2C%22block_id%22%3A%22VzH%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22%2A%3CfakeLink.datadoglink.com%7C1234%3E%2A%5CnTenant+Name%3A+Cannot+Find+in+DataDog+Log%5CnSender%3A+Cannot+Find+in+DataDog+Log%5CnReceiver%3A+Cannot+Find+in+DataDog+Log%22%2C%22verbatim%22%3Afalse%7D%2C%22accessory%22%3A%7B%22type%22%3A%22static_select%22%2C%22placeholder%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Select+Action%22%2C%22emoji%22%3Atrue%7D%2C%22options%22%3A%5B%7B%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22replay%22%2C%22emoji%22%3Atrue%7D%2C%22value%22%3A%22value-replay%22%7D%2C%7B%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22reconstruct%22%2C%22emoji%22%3Atrue%7D%2C%22value%22%3A%22value-reconstruct%22%7D%5D%2C%22action_id%22%3A%22Gl0%3D%22%7D%7D%2C%7B%22type%22%3A%22divider%22%2C%22block_id%22%3A%22GgD%22%7D%2C%7B%22type%22%3A%22actions%22%2C%22block_id%22%3A%22Usthl%22%2C%22elements%22%3A%5B%7B%22type%22%3A%22button%22%2C%22action_id%22%3A%22sScW0%22%2C%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Run%22%2C%22emoji%22%3Atrue%7D%2C%22value%22%3A%22value-run%22%7D%5D%7D%5D%7D%2C%22response_url%22%3A%22https%3A%5C%2F%5C%2Fhooks.slack.com%5C%2Factions%5C%2FTRQU3V52S%5C%2F1225541710913%5C%2FGYRHJqrkBDGZg6Jl2AWrXY9p%22%2C%22actions%22%3A%5B%7B%22type%22%3A%22static_select%22%2C%22action_id%22%3A%22Gl0%3D%22%2C%22block_id%22%3A%22VzH%22%2C%22selected_option%22%3A%7B%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22reconstruct%22%2C%22emoji%22%3Atrue%7D%2C%22value%22%3A%22value-reconstruct%22%7D%2C%22placeholder%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Select+Action%22%2C%22emoji%22%3Atrue%7D%2C%22action_ts%22%3A%221593469844.839423%22%7D%5D%7D",
    "isBase64Encoded": False
}
lambda_function.lambda_handler(event2, None)