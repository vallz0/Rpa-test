import pyautogui as py
import webbrowser
import pandas
from time import sleep as wait
from constants import IMAGE_PATHS

table = pandas.read_csv("products.csv")

def register_product(line:int,nome:str):
    wait(0.5)
    py.press('tab')
    py.hotkey('ctrl', 'a')
    py.press("delete")
    wait(0.5)
    n: str = str(table.loc[line, nome])
    print(n)
    py.write(n)

def registrar():
    code_image: tuple | None = py.locateCenterOnScreen(IMAGE_PATHS["code_image"], confidence=0.8)
    register_image: tuple | None = py.locateCenterOnScreen(IMAGE_PATHS["register_image"], confidence=0.8)

    for line in table.index:
        code:str = table.loc[line,"code"]
        py.click(code_image)
        py.hotkey('ctrl','a')
        py.press("delete")
        wait(0.5)
        py.write(code)
        register_product(line, "brand")
        register_product(line,"type")
        register_product(line, "category")
        register_product(line, "price")
        register_product(line, "cost")
        register_product(line, "notes")

        py.click(register_image)
        wait(2)
        final_image: tuple | None = py.locateCenterOnScreen(IMAGE_PATHS["final_image"], confidence=0.8)

        if final_image:
            confirm_image: tuple | None = py.locateCenterOnScreen(IMAGE_PATHS["confirm_image"], confidence=0.8)
            if confirm_image:
                py.click(confirm_image)


def main(link:str,email:str,password:str):
    webbrowser.open(link)
    wait(1)

    email_image:tuple | None = py.locateCenterOnScreen(IMAGE_PATHS["email_image"], confidence=0.8)
    login_image:tuple | None = py.locateCenterOnScreen(IMAGE_PATHS["login_image"], confidence=0.8)

    if email_image:
        py.click(email_image)
        wait(0.5)
        py.write(email)
        py.press('tab')
        wait(0.5)
        py.write(password)
        wait(0.5)
        py.click(login_image)
        wait(0.5)
        py.click()
        wait(1)
        registrar()


if __name__ == "__main__":
    site: str = "http://127.0.0.1:5000"
    email: str = "EmailTest@Test.com"
    password: str = "PasswordTest123"

    main(site,email,password)