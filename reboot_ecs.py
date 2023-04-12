import json
import time
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.RebootInstanceRequest import RebootInstanceRequest
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest

access_key_id = "你的access_key_id"
access_key_secret = "你的access_key_secret"
region_id = "你的region_id"
instance_id = "你的实例ID"

def get_instance_status(instance_id):
    client = AcsClient(access_key_id, access_key_secret, region_id)
    request = DescribeInstancesRequest()
    request.set_accept_format('json')
    request.add_query_param("RegionId", region_id)
    request.set_InstanceIds(json.dumps([instance_id]))
    response = client.do_action_with_exception(request)
    response = json.loads(response.decode('utf-8'))
    instances = response['Instances']['Instance']
    if len(instances) == 0:
        raise ValueError(f"未找到ID为 {instance_id} 的实例，请检查实例ID是否正确")
    status = instances[0]['Status']
    return status

def reboot_instance(instance_id):
    client = AcsClient(access_key_id, access_key_secret, region_id)
    request = RebootInstanceRequest()
    request.set_accept_format('json')
    request.set_InstanceId(instance_id)
    response = client.do_action_with_exception(request)
    return response

print("请输入大写\"YES\"重启服务器：")
user_input = input()
if user_input == "YES":
    status = get_instance_status(instance_id)
    print(f"当前实例状态: {status}")
    print("正在重启实例...")
    reboot_instance(instance_id)
    while True:
        time.sleep(10)
        status = get_instance_status(instance_id)
        print(f"实例状态: {status}")
        if status == "Running":
            break
    print("实例已成功重启")
else:
    print("输入不正确，退出程序。")
