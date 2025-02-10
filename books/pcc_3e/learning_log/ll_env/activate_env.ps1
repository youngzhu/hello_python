# 临时更改执行策略以允许运行脚本
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force

# 激活虚拟环境
.\ll_env\Scripts\Activate.ps1