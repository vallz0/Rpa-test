# Product Form Automation

This project automates the process of filling out product forms using `pyautogui` for GUI interaction. It extracts data from a CSV file and uses predefined image templates to input the data into a web-based form, simulating mouse clicks and keyboard presses.
## Preview

![preview](preview.gif)
## Features

- Automates form filling based on product data.
- Supports product attributes such as `code`, `brand`, `type`, `category`, `price`, `cost`, and `notes`.
- Uses `pyautogui` to simulate keyboard and mouse interactions.
- Loads product data from a CSV file.
- Logs into a web portal automatically using predefined email and password.

## Pre requisites

- Python 3.x
- `pyautogui` library
- `pandas` library
- CSV file (`products.csv`) containing product information

### Libraries

Make sure to install the following libraries before running the script:

```bash
pip install -r requirements.txt
```

## Usage

   1.  **Set up the ```constants.py``` file:**
    In the ``constants.py`` file, update the ``IMAGE_PATHS`` dictionary with the correct file paths for your image templates. These images will be used by ``pyautogui`` to locate buttons and input fields on the screen.

  2.  Update the ``products.csv`` file:
    Make sure your ``products.csv`` file is formatted with columns like ``code``, ``brand``, ``type``, ``category``, ``price``, ``cost``, and ``notes``.

  3.   Run the script:
    After updating the necessary files, you can run the ``main.py`` script to start the automation process:

```bash
python main.py
```

The script will:

  1.  Open the predefined website URL.
  2.  Perform the login using the email and password defined in ``constants.py``.
  3.  Process each product from the CSV file and input the details into the web form.
