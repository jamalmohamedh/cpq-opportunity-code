Package= Product.Attributes.GetByName("Package").GetValue()
Paymentoption= Product.Attributes.GetByName("Payment Method").GetValue()
Device=Product.Attributes.GetByName("FleetControlDevice").GetValue()
Sensors=Product.Attributes.GetByName("FleetControlExtras").GetValue()
priceQuery="select One_Time_Cost,Monthly_Recurring_Charge from PRICELOOKUP where Main_Component='Application' and Package='{0}' ".format(Package)
PriceList=SqlHelper.GetFirst(priceQuery)
for Attr in Product.Attributes:
    if Attr.IsLineItem:
        if Attr.Name == "Application Component":
            for value in Attr.Values:
                Trace.Write("Value inside attribute "+str(value))
                value.PriceFormula =str(PriceList.One_Time_Cost)
                value.MrcPriceFormula = str(PriceList.Monthly_Recurring_Charge)
            #Trace.Write("ATTR VALUE"+Attr.GetValue())
            Trace.Write("ATTR "+Attr.Name)
            #Attr.ShowMrcPrice = True
            #Attr.ShowPrice = True
'''if Quote.Items.Count>0:
    for item in Quote.Items:
        #Trace.Write("Item inside Quote "+item.Description)
        if item.IsLineItem:
            if item.Description == "Application Component":
                #Trace.Write("Application Component MRC PRICE "+str(item.MrcListPrice)+"One Time Price "+str(item.ListPrice))
                item.ListPrice =PriceList.One_Time_Cost
                item.MrcListPrice =PriceList.Monthly_Recurring_Charge
                item.MrcExtendedListPrice=item.MrcListPrice*item.Quantity
                Trace.Write("zfter Application Component MRC PRICE "+str(item.MrcListPrice)+" One Time Price "+str(item.ListPrice))
#Quote.Save()'''

def DevicePriceList(AttrName):
    priceQuery1="select One_Time_Cost,Monthly_Recurring_Charge from PRICELOOKUP where Main_Component='Device' and Sub_Component='{0}' and Payment_Type='{1}'and Package='{2}'".format(AttrName,Paymentoption,Package)
    PriceList1=SqlHelper.GetFirst(priceQuery1)
    Trace.Write(priceQuery1)
    return PriceList1

for Attr in Product.Attributes:
         if Attr.Name == "FleetControlDevice":
              for value in Attr.Values:
                    Trace.Write("Value inside attribute "+str(value))
                    Price=DevicePriceList(value.Display)
                    Trace.Write("Price is" +str(Price))
                    value.PriceFormula =str(Price.One_Time_Cost)
                    value.MrcPriceFormula = str(Price.Monthly_Recurring_Charge)
              Trace.Write("ATTR "+Attr.Name)



def SensorPriceList(AttrName):
    priceQuery2="select One_Time_Cost,Monthly_Recurring_Charge from PRICELOOKUP where Main_Component='Sensors & Accessories Support' and Sub_Component='{0}' and Payment_Type='{1}'".format(AttrName,Paymentoption)
    PriceList2=SqlHelper.GetFirst(priceQuery2)
    Trace.Write("Price " +priceQuery2)
    return PriceList2

for Attr in Product.Attributes:
    if Attr.Name == "FleetControlExtras":
        for value in Attr.Values:
            Trace.Write("Value inside attribute "+str(value))
            Price2=SensorPriceList(value.Display)
            Trace.Write("Price 2 is" +str(Price2))
            value.PriceFormula =str(Price2.One_Time_Cost)
            value.MrcPriceFormula = str(Price2.Monthly_Recurring_Charge)
        Trace.Write("ATTR "+Attr.Name)


priceQuery3="select One_Time_Cost,Monthly_Recurring_Charge from PRICELOOKUP where Main_Component='Connectivity' and Sub_Component='Sim Card Subscription' and Package='{0}' ".format(Package)
PriceList3=SqlHelper.GetFirst(priceQuery3)
Trace.Write("Price " +priceQuery3)
for Attr in Product.Attributes:
    if Attr.IsLineItem:
        if Attr.Name == "Connectivity":
            for value in Attr.Values:
                Trace.Write("Value inside attribute "+str(value))
                value.PriceFormula =str(PriceList3.One_Time_Cost)
                value.MrcPriceFormula = str(PriceList3.Monthly_Recurring_Charge)

