<div align="center">
  <a href="https://github.com/mikumifa/biliTickerBuy" target="_blank">
    <img width="160" src="icon.ico" alt="logo">
  </a>
  <h1 id="koishi">biliTickerBuy</h1>

![GitHub all releases](https://img.shields.io/github/downloads/mikumifa/biliTickerBuy/total)
![GitHub release (with filter)](https://img.shields.io/github/v/release/mikumifa/biliTickerBuy)
![GitHub issues](https://img.shields.io/github/issues/mikumifa/biliTickerBuy)
![GitHub Repo stars](https://img.shields.io/github/stars/mikumifa/biliTickerBuy)

</div>

经过源代码审查的无后门版BiliTickerBuy，将同步[mikumifa/biliTickerBuy](https://github.com/mikumifa/biliTickerBuy)更新，一旦发现后门将在本README.md中置顶通知并删除后门。

开源免费，简单易用，图形界面, 速度极快的B站会员购辅助工具


## 快速安装

所需环境：Python 3.9及以上

Windows：请依次复制并运行以下命令：

```
git clone https://github.com/lclty/BiliTicker_NoBackDoor.git
cd ./BiliTicker_NoBackDoor
pip install -r requirements.txt
python main.py
```
> **NOTE**
>
> 如果 ``` git clone ``` 失败或过程过慢，请自行使用 VPN 等代理链接；
>
> 如果 ``` pip install ``` 失败或过程过慢，请尝试将 pip 更换为清华源
>
> 更换方法：复制下面代码并在 ```pip install -r requirements.txt``` 这一行上面运行即可
>
> ```pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple ```

MacOS 与 linux：

请提前部署好 Docker .

依次复制并运行以下命令：

```
git clone https://github.com/lclty/BiliTicker_NoBackDoor.git
cd ./BiliTicker_NoBackDoor
docker build -t bilitickerbuy .
docker run -d -p xxxx:xxxx --name bilitickerbuy_container bilitickerbuy
```

其中，```xxxx```所代表的内容为端口号，取值范围为(1024,65535]∪N*.

## 使用说明书
重构了UI，启动终端第一行会显示

```
Running on local URL:  http://127.0.0.1:xxx
```

访问对应的网址即可

[点我前往更加详细的使用说明书](https://github.com/mikumifa/biliTickerBuy/wiki/%E6%8A%A2%E7%A5%A8%E8%AF%B4%E6%98%8E)

| 抢票过程                                                     | 滑块过程                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![tutieshi_640x360_26s](https://github.com/mikumifa/biliTickerBuy/assets/99951454/be7c072a-7449-4df9-aeb5-fca0c49b0a0e) | ![tutieshi_640x360_13s](https://github.com/mikumifa/biliTickerBuy/assets/99951454/508e7c08-2cdd-42a9-9529-34f74e08036e) |

## 项目问题

程序使用问题： [点此链接前往discussions](https://github.com/mikumifa/biliTickerBuy/discussions)

反馈程序BUG或者提新功能建议： [点此链接向项目提出反馈BUG](https://github.com/mikumifa/biliTickerBuy/issues/new/choose)

## 其他可用脚本

| 链接                                                      | 主要特色               |
| --------------------------------------------------------- | ---------------------- |
| https://github.com/bilibili-ticket/bilibili-ticket-python | 蹲回流票               |
| https://github.com/biliticket/BHYG                        | 多种抢票策略、支持代理（不建议使用！！会被撤票！！） |

## 项目贡献者

<!-- readme: collaborators,contributors -start -->
<table>
	<tbody>
		<tr>
            <td align="center">
                <a href="https://github.com/mikumifa">
                    <img src="https://avatars.githubusercontent.com/u/99951454?v=4" width="100;" alt="mikumifa"/>
                    <br />
                    <sub><b>mikumifa</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/WittF">
                    <img src="https://avatars.githubusercontent.com/u/108567138?v=4" width="100;" alt="WittF"/>
                    <br />
                    <sub><b>W1ttF</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/gpc123456">
                    <img src="https://avatars.githubusercontent.com/u/78298238?v=4" width="100;" alt="gpc123456"/>
                    <br />
                    <sub><b>gpc123456</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/Amorter">
                    <img src="https://avatars.githubusercontent.com/u/63935225?v=4" width="100;" alt="Amorter"/>
                    <br />
                    <sub><b>秦诗染</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/howarle">
                    <img src="https://avatars.githubusercontent.com/u/63032487?v=4" width="100;" alt="howarle"/>
                    <br />
                    <sub><b>HowarLi</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/xmbhjQAQ">
                    <img src="https://avatars.githubusercontent.com/u/72352414?v=4" width="100;" alt="xmbhjQAQ"/>
                    <br />
                    <sub><b>xmbhjQAQ</b></sub>
                </a>
            </td>
		</tr>
		<tr>
            <td align="center">
                <a href="https://github.com/ZianTT">
                    <img src="https://avatars.githubusercontent.com/u/53261506?v=4" width="100;" alt="ZianTT"/>
                    <br />
                    <sub><b>ZianTT</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/BestLemoon">
                    <img src="https://avatars.githubusercontent.com/u/53417050?v=4" width="100;" alt="BestLemoon"/>
                    <br />
                    <sub><b>ChillWay</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/ChisatoNishikigi73">
                    <img src="https://avatars.githubusercontent.com/u/89033115?v=4" width="100;" alt="ChisatoNishikigi73"/>
                    <br />
                    <sub><b>Chisato73</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/CinnabarCHU">
                    <img src="https://avatars.githubusercontent.com/u/79802118?v=4" width="100;" alt="CinnabarCHU"/>
                    <br />
                    <sub><b>CinnabarCHU</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/shirok1">
                    <img src="https://avatars.githubusercontent.com/u/12044683?v=4" width="100;" alt="shirok1"/>
                    <br />
                    <sub><b>Shiroki Satsuki</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/codycjy">
                    <img src="https://avatars.githubusercontent.com/u/64593412?v=4" width="100;" alt="codycjy"/>
                    <br />
                    <sub><b>codycjy</b></sub>
                </a>
            </td>
		</tr>
		<tr>
            <td align="center">
                <a href="https://github.com/ipid">
                    <img src="https://avatars.githubusercontent.com/u/5251264?v=4" width="100;" alt="ipid"/>
                    <br />
                    <sub><b>ipid</b></sub>
                </a>
            </td>
		</tr>
	<tbody>
</table>
<!-- readme: collaborators,contributors -end -->



## 免责声明

详见[MIT License](./LICENSE)，切勿进行盈利，所造成的后果与本人无关。

## 捐赠

如果你想支持这个项目的话 [爱发电](https://afdian.net/a/mikumifa)
