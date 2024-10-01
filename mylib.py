# - **********************************************************
# - Author: Suchin T
# - Date: 2024-10-01 (YYYY-MM-DD)
# - Version: 0.2
# - Function: my library function
# - Description: Added Force_none flag for testing.
# - **********************************************************

def Change_form_data_2_json_format(input, Force_none = False):
    check_str = isinstance(input,str)
    check_bytes = isinstance(input,bytes)
    temp = ""
    if check_str == True:
       temp = input            # check data, it is string type
    elif check_bytes == True:
       temp = input.decode()   # check data, it is bytes type and change it to be string.
    
    if temp.find("=") and temp.find("&"): #change 'html form data format' to 'json data format'
       temp = temp.replace('=','":"')
       temp = temp.replace('&','","')
       temp = '{"'+ temp + '"}'
    else:
       temp = 'none' # return 'none' in case data, that is not html data format
    
    if Force_none == True: # Force the function to give 'none'
       temp = 'none'

    return temp