### GateWayTool概述
1. GateWayTool使用Python开发。主要是为了将路由矩阵转为C数组，方便后续的网关路由开发而设计的一个简单工具。
2. 使用TKinterDesigner进行界面设计。为了更好的进行界面设计，目前使用的TD为最新的v1.7.3版本。但TD目前版本使用python3.10.4进行开发，而python3.10已不再支持win7操作系统。因此GateWayTool暂时放弃对win7的兼容。
[TD的Github](https://github.com/honghaier-game/PyMe)
[TD的说明手册](https://github.com/honghaier-game/PyMe/blob/master/README_Cn.md)
[TD的API说明](https://github.com/honghaier-game/PyMe/blob/master/API_Manual_Cn.md)


### GateWayTool技术栈
- 解释器版本：
  - python-3.10.2
- 第三方库：
  - [xlwings](https://www.xlwings.org/)
- UI框架
  - tkinter
- 脚手架：
  - [TKinterDesigner-v1.7.3](http://www.tkinterdesigner.com/bbs/)
- 测试框架：
  - unittest


### 目录结构
> - Gateway_Tool —— 主目录
>   - Gateway_Tool —— 项目代码
>       - ... —— 除了pyt包以外的部分基本由TKinterDesigner设计和生成
>       - pyt —— 主要业务的代码包
>           - config —— 路由矩阵相关的配置
>           - src —— 存放业务代码的源码
>               - server ——为UI提供服务，里面包含服务层和线程任务
>           - test —— 测试代码
>       - ...
>   - TKinterDesigner-v1.7.3-win64 —— 界面设计工具
>   - README.md —— 自述文件


### 主要功能
- [x] 从Excel中读取路由矩阵，并生成C数组
- [x] 使用Josn和Template文件进行替换，生成文件
- [x] 可以进行DBC解码
- [x] 自动生成符合一定格式的DBC回调函数


### 可优化内容
- [x] 对路由的CAN通道和路由矩阵配置映射进行解耦
- [X] 重构测试框架
- [x] 路径记忆
- [X] 文件路径预测和重载
- [ ] 可以将生成的C数组直接写入替换的模板中。
- [ ] UI重新设计，目前版本的TKinterDesigner无法将组件放在一个面板内进行统一管理。
- [ ] 兼容Win7环境
- [ ] 重构目录结构
- [ ] 使用模板模式重构任务线程和对应的方法
- [ ] 修改读取Excel文件中路由矩阵的方式。尽量选择更具有泛用性的方式，例如外部配置。
- [ ] 配置文件的Json支持注释。方便查看以后可以使用那些配置项
- [ ] 菜单上添加生成配置项的按钮（生成缺少的配置）
- [ ] 菜单上添加重置配置项的按钮（重置所有配置，重新生成默认配置）


### 无法避免的问题
- [ ] 暂时无法解决系数、偏移量的小数问题。可能系数出现小数，可能偏移量出现小数。即使将两者转为整数计算也可能因为除不尽出现小数而损失精度。导致报文接收和报文发送的数值不一致。

### 食用方法
会生成解包打包的函数，打包解包函数会有解包前和解包后的方法，但只给出声明，需要自己去实现这部分内容。工具分为ECU和GW的生成模式，可以生成以下结构的文件：

ECU模式下：
> - ECU —— 主目录
>   - binutil.c
>   - binutil.h —— 信号报文列表的声明，信号报文接收与打包函数的声明
>   - config.h —— 与配置相关的宏定义
>   - definition.c
>   - definition.h —— 报文与信号结构定义，与打包解包函数的声明
>   - monitorutil.c
>   - monitorutil.h —— 报文监控相关的内容的声明
>   - timeoutUtil.c —— 这部分仅给出定义，具体业务需要开发者自己实现
>   - timeoutUtil.h —— 报文超时的声明
>   - timingUtil.c —— 这部分仅给出定义，具体业务需要开发者自己实现
>   - timingUtil.h —— 报文超时的声明

GW模式下，假设有两路CAN通道：
> - GW —— 主目录
>     - monitorutil.c —— 里面包含获取系统时间的函数，需要用户自己实现。该函数与报文监控相关。
>     - monitorutil.h —— 报文监控相关的内容的声明
>     - config.h —— 与配置相关的宏定义
>   - CAN1 —— CAN1通道目录
>     - CAN1_binutil.c
>     - CAN1_binutil.h —— 信号报文列表的声明，信号报文接收与打包函数的声明
>     - CAN1_definition.c
>     - CAN1_definition.h —— 报文与信号结构定义，与打包解包函数的声明
>     - CAN1_monitorutil.c —— 中间层
>     - CAN1_timeoutUtil.c —— 这部分仅给出定义，具体业务需要开发者自己实现
>     - CAN1_timeoutUtil.h —— 信号报文收到后执行函数的声明
>     - CAN1_timeoutUtil.c —— 这部分仅给出定义，具体业务需要开发者自己实现
>     - CAN1_timeoutUtil.h —— 报文超时的声明
>     - CAN1_timingUtil.c —— 这部分仅给出定义，具体业务需要开发者自己实现
>     - CAN1_timingUtil.h —— 报文周期执行函数的声明
>   - CAN2 —— CAN2通道目录
>     - CAN2_binutil.c
>     - CAN2_binutil.h —— 信号报文列表的声明，信号报文接收与打包函数的声明
>     - CAN2_definition.c
>     - CAN2_definition.h —— 报文与信号结构定义，与打包解包函数的声明
>     - CAN2_monitorutil.c —— 中间层
>     - CAN2_timeoutUtil.c —— 这部分仅给出定义，具体业务需要开发者自己实现
>     - CAN2_timeoutUtil.h —— 报文超时的声明，这部分表示信号超时后需要执行的
>     - CAN2_timingCycUtil.c —— 这部分仅给出定义，具体业务需要开发者自己实现
>     - CAN2_timingCycUtil.h —— 报文周期执行函数的声明，这部分表示周期到了之后我需要执行的
>     - CAN2_timingUtil.h —— 报文定时执行，这部分表示报文定期需要执行的。
timing函数里面应该包含周期之前和周期之后执行的函数。

若使用了合并配置的设置，则会为每路CAN创建单独的monitorutil文件和config文件。

