## Automatic Punch the Clock

This code aims to automate a routine task present in the day to day of remote work, such as clocking in through a browser, using the python programming language and having as main reference the **selenium** library, in addition to other fundamental libraries like **pyautogui** and **pytesseract**.

##

### Basic information about the script

Functions and how they perform:

###### 1. Date and time function:
This function will capture the current date, hour, minute, second and day of the week, in order to use them to trigger the function that will clock in. Below are its definition and return, respectively:
```python
# Function name:
def captura_data_e_horario():
```

```python
# Function return:
return data, hora, minuto, segundo, dia_da_semana
```

<br>

###### 2. Clock in macro function:
This function will open the browser, access the application uri to clock in, fill in the employee's access data and capture the alphanumeric code and interpret it in string format to clock in. Below are its definition and return, respectively:
```python
# Function name:
def macro_ponto():
```

```python
# Function return:
return none
```

<br>

###### 3. Notifying through whatsapp:
Finally, I added a notification through whatsapp to certify correct bot operation:
```python
# Whatsapp notification:
pywp.sendwhatmsg_instantly('+5561900000000', f'[ ! ] - Clock in punched at {hora}:{minuto}:{segundo} in {data}.', 15, True, 5);
```

<br>

###### 4. Operation flow:

1. The script will open a new tab in Chrome browser and will access the application uri to clock in;
2. Fill in the type of login, the login, password and location fields;
3. So it will be capturing the HTML element that contains the code, ``` ZMO7 ``` in this case and saving it as ``` captcha-nexus.png ```;
4. Finally with the help of the pytesseract library it will transcribe to string format and apply it to the final field;
5. And finally press the register button, if the code is not correct, the process is repeated until success.

<p align="center">
    <img src="https://user-images.githubusercontent.com/96185134/225164817-05b20229-a4cd-4cd4-82c7-f6c2a44cbeba.png">
</p>

##

### Remider

Remember that this code can be used in a generic way to fill in any type of form in browsers and interpret texts in images and convert them to strings.
