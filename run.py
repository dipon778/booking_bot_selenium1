from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='EUR')
    bot.select_place(place='New York')
    bot.select_dates(ch_in="2022-03-25",ch_out="2022-03-28")
    bot.select_adults(adults=4)
    bot.click_search()

