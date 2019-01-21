from selenium import webdriver
import xlwt
import xlrd

# book = xlrd.open_workbook(r'总结.xlsx')
# print("The number of workbook is:{}".format(book.nsheets))
# print("Worksheets name are {}".format(book.sheet_names))

# sht = book.sheet_by_index(0)
# print("第一页sheet名：{0}， {1}行 {2}列".format(sht.name,sht.nrows,sht.ncols))
# print("CellB1 value:{}".format(sht.cell_value(1,1)))

# for i in range(sht.nrows):
#     print(sht.row(i))

driver = webdriver.Chrome()
driver.get("https://list.jd.com/list.html?cat=9987,653,655")

phone_prices = driver.find_elements_by_css_selector('li.gl-item div.p-price')
phone_names = driver.find_elements_by_css_selector("li.gl-item i.promo-words")

book = xlwt.Workbook()
sheet = book.add_sheet("京东手机")

sheet.write(0,0,"手机名称")
sheet.write(0,1,"手机价格")

count = len(phone_names)
for i in range (count):
    sheet.write(i+1,0,phone_names[i].text)
    sheet.write(i+1,1,phone_prices[i].text)

book.save("phone.xls")