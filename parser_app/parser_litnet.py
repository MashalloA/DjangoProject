# import requests
# from bs4 import BeautifulSoup as bs
#
# URL = 'https://litnet.com'
#
# HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
# }
#
# #1 make request
# def get_html(url, params=""):
#     req = requests.get(url, headers=HEADERS, params=params)
#     return req
#
# #2 get data
# def get_data(html):
#     soup = bs(html, 'html.parser')
#     items = soup.find_all('div', class_="bx-viewport")
#     lit_net_list = []
#     for item in items:
#         title = item.find('div', class_="bw-title").get_text(strip=True)
#         image = URL + item.find('div', class_="book-img transparent-marks").find('img').get('src')
#         lit_net_list.append({
#             'title': title,
#             'image': image,
#         })
#         return lit_net_list
#
# #func parsing
# def parsing():
#     response = get_html(URL)
#     if response.status_code == 200:
#         lit_net_list2 = []
#         for page in range(1, 2):
#             response = get_html("https://litnet.com/ru", params={"page": page})
#             lit_net_list2.extend(get_data(response.text))
#             return lit_net_list2
#     else:
#         raise Exception('Error in parsing')
#
# print(parsing())