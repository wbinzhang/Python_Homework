# win10安装Python并配置开发环境
## 下载Python
首先，进入Python官网**www.python.org**

![](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-23/1603460739087-image1.png)

在**Downloads**下拉菜单中选择**Windows**下载Windows版本的Python。

![](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-23/1603460850037-image2.png)

![](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-23/1603460922518-image3.png)

选择**Python3.9（64-bit）**进行下载，下载完成后进行安装。

![](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-23/1603461026025-image4.png)

将**Add Python 3.9 to PATH**勾选上，配置环境变量。

![](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-23/1603461060374-image5.png)

因为我的电脑中存在python3.6版本，所以需要对Python3.9再次进行环境变量的配置。将Python3.9的的启动文件修改为Python39，然后配置环境变量。

打开高级系统设置。

![](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-23/1603461083694-image6.png)

选择**环境变量**

![](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-23/1603461124446-image7.png)

添加环境变量：将python39的路径添加到环境变量，点击确定。

![](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-23/1603461365171-image8.png)

最后，调出CMD终端，在终端中输入“python39”，验证环境配置成功。

![](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-23/1603461152522-image9.png)
