import json
import boto3
import hashlib
import urllib.request,urllib.error,urllib.parse
import os

'''
create by ksj
e-mail kofdx7@gmail.com

'''

def get_ip_ranges(url,expected_hash):
    
    response=urllib.request.urlopen(url);
    ip_json=response.read();
    
    m = hashlib.md5();
    m.update(ip_json);

    hash = m.hexdigest();
    
    if hash != expected_hash:
        raise Exception('MD5 Mismatch: got '+ hash + ' expected ' + expected_hash)
    return ip_json

def get_cf_range(service,ip_ranges):
    cf_range=[]
    [cf_range.append(str(i['ip_prefix'])) for i in ip_ranges if i['service'] == service]
    return cf_range;
    
def update_waf_ip_set(ipsetName, ipsetId,addresses):
    wafv2 = boto3.client('wafv2')
    get_ip_set = wafv2.get_ip_set(Name=ipsetName, Scope='REGIONAL',Id=ipsetId)
    LockToken=get_ip_set['LockToken'];
    update_ip_set=wafv2.update_ip_set(Name=ipsetName, Scope='REGIONAL', Id=ipsetId,LockToken=LockToken,Addresses=addresses); 


def lambda_handler(event, context):
    IP_SET_NAME = os.getenv('IP_SET_NAME')
    IP_SET_ID = os.getenv('IP_SET_ID')
    
    
    msg = json.loads(event['Records'][0]['Sns']['Message']);
    ip_range=json.loads(get_ip_ranges(msg['url'],msg['md5']))
    cf_range=get_cf_range("CLOUDFRONT",ip_range['prefixes']);
    result = update_waf_ip_set(IP_SET_NAME,IP_SET_ID,cf_range)
    
    
    return result;

    
    
    
    

    
    
    
    
