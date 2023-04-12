# AliyunECS_Reboot
**阿里云ECS实例重启脚本**

本文档介绍了如何使用Python脚本以及阿里云SDK在Windows环境下自动重启阿里云ECS实例。脚本会提示用户输入确认信息，以避免误操作。

## 1. 设置RAM用户权限

1. 登录阿里云管理控制台。
2. 在左侧导航栏中，单击**访问控制**。
3. 在访问控制页面中，选择**RAM用户**。
4. 单击**新建用户**，输入用户名，勾选**编程访问**。创建用户后，记下**AccessKey ID**和**AccessKey Secret**，这将用于脚本中进行API调用。
5. 在左侧导航栏中，选择**策略管理**。
6. 在策略管理页面中，单击**新建策略**。
7. 选择**自定义策略**，输入策略名称，如"ECSInstanceReboot"。在策略内容中，添加以下JSON：

```json
{
  "Version": "1",
  "Statement": [
    {
      "Action": [
        "ecs:DescribeInstances",
        "ecs:RebootInstance"
      ],
      "Resource": [
        "acs:ecs:*:*:instance/实例ID"
      ],
      "Effect": "Allow"
    }
  ]
}
```

将`实例ID`替换为您要重启的ECS实例ID。

1. 单击**确定**创建策略。
2. 返回**RAM用户**页面，找到刚才创建的用户，单击用户名右侧的**添加权限**。
3. 在搜索框中输入刚创建的策略名称，勾选并单击**确定**。

现在已经成功创建了RAM用户并为其分配了重启ECS实例的权限。

## 2. Python脚本

请参照此仓库中的`reboot_ecs.py`文件，该文件包含了用于重启阿里云ECS实例的Python脚本。



**本文档和脚本均由OpenAI ChatGPT生成。**
