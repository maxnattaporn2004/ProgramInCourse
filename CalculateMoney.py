from forex_python.converter import CurrencyRates

#ทำประเทศให้เป็นdict
country_currency = {
    "Japan": "JPY",
    "Czech republic": "CZK",
    "Denmark": "DKK",
    "United kingdom": "GBP",
    "Hungary": "HUF",
    "Poland": "PLN",
    "Romania": "RON",
    "Sweden": "SEK",
    "Switzerland": "CHF",
    "Iceland": "ISK",
    "Norway": "NOK",
    "Turkey": "TRY",
    "Australia": "AUD",
    "Brazil": "BRL",
    "Canada": "CAD",
    "China": "CNY",
    "Hong kong": "HKD",
    "Indonesia": "IDR",
    "Israel": "ILS",
    "India": "INR",
    "South korea": "KRW",
    "Mexico": "MXN",
    "Malaysia": "MYR",
    "New zealand": "NZD",
    "Philippines": "PHP",
    "Singapore": "SGD",
    "Thailand": "THB",
    "South africa": "ZAR",
    "Eurozone": "EUR"
}

# โชว์ประเทศที่จะไป
def show_countries():
    print("Japan : JPY")
    print("Czech republic : CZK")
    print("Denmark : DKK")
    print("United kingdom : GBP")
    print("Hungary : HUF")
    print("Poland : PLN")
    print("Romania : RON")
    print("Sweden : SEK")
    print("Switzerland : CHF")
    print("Iceland : ISK")
    print("Norway : NOK")
    print("Turkey : TRY")
    print("Australia : AUD")
    print("Brazil : BRL")
    print("Canada : CAD")
    print("China : CNY")
    print("Hong kong : HKD")
    print("Indonesia : IDR")
    print("Israel : ILS")
    print("India : INR")
    print("South korea : KRW")
    print("Mexico : MXN")
    print("Malaysia : MYR")
    print("New zealand : NZD")
    print("Philippines : PHP")
    print("Singapore : SGD")
    print("Thailand : THB")
    print("South africa : ZAR")
    print("Eurozone : EUR")


#เลื่อกประเทศที่จะไป
def get_country():
    country = input("Enter country name: ").capitalize()
    return country

#แปลงเป็นสกุลเงิน
def tranfer_country_to_money(country):
    return country_currency[country]


#ระบุจำนวนเงินที่่ใช้ในทิปนี้
def get_money():
    money = int(input("Enter money: "))
    return money


#ระบุว่าไปกี่วัน
def get_day():
    day = int(input("Enter day: "))
    return day


#แปลงค่าเงิน
def tranfer_money(country,money):
    tranfer = CurrencyRates()
    return tranfer.convert("THB", country, money)


#คำนวณเงิน
def calculate_money_thb(amount,day):
    result = amount / day
    return result


#คำนวณเงินนอก
def calculate_money_country(amount_country,day):
    result = amount_country / day
    return result


#แสดงผล
def show_stats():
    show_countries()
    country = get_country()
    tranfered = tranfer_country_to_money(country)
    amount = get_money()
    day = get_day()
    result_thb = round(calculate_money_thb(amount,day),2)
    result_country = round(calculate_money_country(tranfer_money(tranfered,amount),day),2)
    print("------User------")
    print("ประเทศ : " + country)
    print("เงินที่มี : " , amount , " THB")
    print("จำนวนวันที่ไป : " , day , " Day")
    print("----------------")
    print("----เงินที่ใช้ได้----")
    print("เงินที่ใช้ได้ต่อวัน : " , result_thb , " THB")
    print("เงินที่ใช้ได้ต่อวัน : " , result_country , tranfered)
    print("----------------")



show_stats()