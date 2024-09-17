# AQI Smile / 空气情况可视化

基于和风天气API的空气质量指数(AQI)可视化工具。

A visualization tool for Air Quality Index (AQI) based on QWeather API.

## 功能 / Features

- 绘制各省份的AQI地图
- 支持全国所有省份
- 使用和风天气API获取实时AQI数据

- Draw AQI maps for each province
- Support for all provinces in China
- Utilize QWeather API to fetch real-time AQI data

## 如何使用 / How to Use

1. 获取和风天气API密钥 / Get your QWeather API key
   - 访问 [和风天气控制台](https://console.qweather.com/#/apps/create-app/create) 创建应用
   - Visit [QWeather Console](https://console.qweather.com/#/apps/create-app/create) to create an application

2. 安装依赖 / Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. 配置API密钥 / Configure API key
   - 在项目根目录创建 `.env` 文件,并添加你的API密钥，或直接将demo.env文件的名字改为 `.env`并添加密钥。
   - Create a `.env` file in the project root and add your API key:
     ```
     QWEATHER_API_KEY=your_api_key_here
     ```

4. 运行脚本 / Run the script
   ```
   python main.py
   ```

## 文档 / Documentation

有关和风天气API的更多信息,请参阅 [官方文档](https://dev.qweather.com/docs/configuration/project-and-key/)。

For more information about the QWeather API, please refer to the [official documentation](https://dev.qweather.com/docs/configuration/project-and-key/).

## 待办事项 / TODO

- [ ] 适配所有省份 / Adapt for every province
- [ ] 添加更多可视化选项 / Add more visualization options
- [ ] 实现历史数据分析 / Implement historical data analysis

## 现存BUG

- [ ] _cities若为省份绘图会出现错误，但四个直辖市没有问题。

## 贡献 / Contributing

欢迎提交问题和拉取请求。

Issues and pull requests are welcome.

## 许可 / License

本项目采用 AP2 许可证。详情请见 [LICENSE](LICENSE) 文件。

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


