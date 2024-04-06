from observer import Subject, AmericanStockMarket, EuropeanStockMarket


really_big_company =  Subject()

american_observer = AmericanStockMarket()
really_big_company.register(american_observer)

european_observer = EuropeanStockMarket()
really_big_company.register(european_observer)


really_big_company.update_observers('Important Update',msg='CEO Unpectedly Resigns')
