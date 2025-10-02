# AutoReader-ephk_esmart
a auto answer reading in esmart 2.0

# Docs (ZH-HK)
## 概述

此 Selenium 自動化腳本旨在透過導航至登入頁面、輸入使用者憑證並點擊登入按鈕來登入「我愛閲讀花園」網站。該腳本將操作記錄到文字檔案中，以便進行自動答題。

## 要求

- **Python 3.x**：確保您已安裝 Python。您可以從 [python.org](https://www.python.org/downloads/) 下載。
- **Selenium**：使用 pip 安裝 Selenium 庫：
```bash
pip install selenium
```
- **Edge WebDriver**：從 [Microsoft 官方網站](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) 下載與您的 Edge 瀏覽器版本相符的 Edge WebDriver 版本。

## 安裝說明

1. **安裝 Python 和 Selenium**：
- 從官方網站安裝 Python。
- 開啟終端機或命令提示字元並執行：
```bash
pip install selenium
```

2. **下載 Edge WebDriver**：
- 確保 Edge WebDriver 已安裝在系統 PATH 中，或在腳本中指定路徑。

3. **更新憑證**：
- 將腳本中的佔位符替換為您的實際使用者名稱和密碼：
```python
username_input.send_keys("your_username") # 替換為您的使用者名稱
password_input.send_keys("your_password") # 替換為您的密碼```

### 日誌函數
此函數將操作記錄到名為 `automation_log.txt` 的文字檔案中。

### 主要功能
`perform_tasks` 函數包含腳本的主要邏輯：

1. **開啟登入頁面**：
- 導航到指定的 URL。

2. **點擊按鈕**：
- 等待某個元素，如果存在則點擊它。

3. **輸入使用者名稱和密碼**：
- 在指定欄位中輸入使用者憑證。

4. **點擊登入按鈕**：
- 啟動登入流程。

### 運行腳本
要運行腳本，請導航至包含“login_script.py”的目錄並執行：

## 日誌記錄
腳本會將每個操作記錄到「automation_log.txt」檔案中。該檔案與腳本位於同一目錄中。

## 故障排除

- **未找到元素**：如果腳本未找到元素，請根據實際網頁檢查腳本中的類別名稱和 ID。
- **WebDriver 問題**：確保 Edge WebDriver 版本與您的瀏覽器版本相符。
- **逾時**：如果腳本逾時，請考慮增加 `WebDriverWait` 中的逾時時長。

## 貢獻

歡迎增加實際功能，我也會在有空的時候更新這個項目，你可以創建Pull Request

## 許可證

本項目採用 `GPL 3.0` 許可證。

# Docs (en)
## Overview

This Selenium automation script is designed to log in to the "I Love Reading Garden" website by navigating to the login page, entering user credentials, and clicking the Login button. The script records the actions to a text file for automated answering.

## Requirements

- **Python 3.x**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Selenium**: Install the Selenium library using pip:
```bash
pip install selenium
```
- **Edge WebDriver**: Download the version of Edge WebDriver that matches your Edge browser version from the [Microsoft official website](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

## Installation Instructions

1. **Install Python and Selenium**:
- Install Python from the official website.
- Open a terminal or command prompt and execute:
```bash
pip install selenium
```

2. **Download Edge WebDriver**:
- Ensure Edge WebDriver is installed in your system PATH, or specify the path in the script.

3. **Update Credentials**:
- Replace the placeholders in the script with your actual username and password:
```python
username_input.send_keys("your_username") # Replace with your username
password_input.send_keys("your_password") # Replace with your password
```

### Logging Function
This function logs operations to a text file named `automation_log.txt`.

### Main Functionality
The `perform_tasks` function contains the main logic of the script:

1. **Open Login Page**:
- Navigates to the specified URL.

2. **Click Button**:
- Waits for an element to be found and clicks it if it exists.

3. **Enter Username and Password**:
- Enters the user credentials in the specified fields.

4. **Click Login Button**:
- Initiates the login process.

### Running the Script
To run the script, navigate to the directory containing `login_script.py` and execute:

## Logging
The script logs each action to the `automation_log.txt` file. This file is located in the same directory as the script.

## Troubleshooting

- **Element Not Found**: If the script fails to find an element, check the class name and ID in the script against the actual web page.

- **WebDriver Issues**: Ensure that the Edge WebDriver version matches your browser version.
- **Timeout**: If your script times out, consider increasing the timeout in `WebDriverWait`.

## Contributing

Feature additions are welcome. I'll update this project when I have time. You can also create a pull request.

## License

This project is licensed under the `GPL 3.0` license.
