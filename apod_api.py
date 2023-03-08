'''
Library for interacting with NASA's Astronomy Picture of the Day API.
'''
import requests
import datetime from date 
def main():
    # TODO: Add code to test the functions in this module
    apod_date = '2023-02-15'
    
    return

def get_apod_info(apod_date):
    """Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.

    Args:
        apod_date (date): APOD date (Can also be a string formatted as YYYY-MM-DD)

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """
#Request URL 
url_api = "https://images-api.nasa.gov"
resp_msg = requests.get(url_api)

#URL for NASA Astronomy Picture API 

url_params = {'api_dev_key': 'KhXJQV3Ch8BejzsHNN7XnSsxNilb6rNGCUa4qhdw', 
               'Date' : apod_date }
if resp.msg.status_code == requests.codes.ok:
    print('Request Successful')
else: 
    print(f'Request failed.')
    print (f'Status code: {resp_msg.status_code}')
    return   

def get_apod_image_url(apod_info_dict):
    """Gets the URL of the APOD image from the dictionary of APOD information.

    If the APOD is an image, gets the URL of the high definition image.
    If the APOD is a video, gets the URL of the video thumbnail.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    return

if __name__ == '__main__':
    main()