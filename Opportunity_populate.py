def getcfvalue(cfname):
    value=Quote.GetCustomField(cfname).Content
    if value is None:
        value="Invalid Opportunity ID"
        Trace.Write(value)
    return value
def assignvalue(cfname,value):
    if value is None:
        Quote.GetCustomField(cfname).Content="No value from Salesforce"
        Trace.Write("Invalid Opportunity ID")
    else:
        Quote.GetCustomField(cfname).Content=str(value)
def setErrorMessage(cfname,value):
    formattedMessage = "<font color = 'red'><b>{0}</b></font>".format(value)
    Quote.GetCustomField(cfname).Content=formattedMessage
def resetnull(cfname):
    Quote.GetCustomField(cfname).Content=" "
def isvisible(cfname):
    Quote.GetCustomField(cfname).Visible=True
def ishiddden(cfname):
    Quote.GetCustomField(cfname).Visible=False
def isuneditable(cfname):
    Quote.GetCustomField(cfname).Editable=False
#OppId=getcfvalue("Opportunity Name")
resetnull("Opportunity Reference Number")
resetnull("Opportunity Type")
resetnull("Region")
resetnull("PO Number")
resetnull("Selling Currency")
resetnull("Sector")
resetnull("PO Issued Date")
resetnull("Account Manager")
resetnull("Opportunity Status")
resetnull("Quote Expiration Date")
OppId=getcfvalue("Opportunity Name")
ishiddden("Additional Comments")
if SFEnvironment is not None:
    res = SalesforceProxy.Binding.query("SELECT Opportunity_ID__c,Opportunity_Reference_Number__c,Opt_Status__c,AccountId,Type,CurrencyIsoCode,Sector__c,PO_Actual_Date__c,CloseDate,Purchase_Order_Number__c FROM  Opportunity where Name like '" + OppId + "'")
    #len1=res.size
    if res.size==0:
        #Trace.Write("Oppty is invalid")
        isvisible("Additional Comments")
        isuneditable("Additional Comments")
        setErrorMessage("Additional Comments","Error :Opportunity Reference Number is not valid.Please check in salesforce or connect with your salesforce administration")
        isuneditable("Additional Comments")
        ishiddden("Opportunity Type")
    	ishiddden("Opportunity Reference Number")
    	ishiddden("Opportunity Type")
    	ishiddden("Region")
    	ishiddden("PO Number")
    	ishiddden("Selling Currency")
    	ishiddden("Sector")
    	ishiddden("PO Issued Date")
    	ishiddden("Account Manager")
    	ishiddden("Opportunity Status")
    	ishiddden("Quote Expiration Date")
    elif res is not None and len(res.records)>0:
        isvisible("Opportunity Type")
    	isvisible("Opportunity Reference Number")
    	isvisible("Opportunity Status")
    	isvisible("Region")
    	isvisible("PO Number")
    	isvisible("Selling Currency")
    	isvisible("Sector")
    	isvisible("PO Issued Date")
    	isvisible("Account Manager")
    	isvisible("Opportunity Status")
    	isvisible("Quote Expiration Date")
        isuneditable("Additional Comments")
        ishiddden("Additional Comments")
        assignvalue("Opportunity Reference Number",res.records[0].Any[1].InnerText)
        assignvalue("Opportunity Status",res.records[0].Any[2].InnerText)
        assignvalue("Opportunity Type",res.records[0].Any[4].InnerText)
        assignvalue("Selling Currency",res.records[0].Any[5].InnerText)
        assignvalue("Sector",res.records[0].Any[6].InnerText)
        assignvalue("PO Issued Date",str(res.records[0].Any[7].InnerText))
        #getcfvalue("Quote Expiration Date")
        #assignvalue("Quote Expiration Date",str(res.records[0].Any[8].InnerText))
        assignvalue("PO Number",res.records[0].Any[9].InnerText)
        #Log.Write("Sector"+str(res.records[0].Any[8].Innertext))
        Accountid=res.records[0].Any[3].InnerText
        Accountsql=SalesforceProxy.Binding.query("SELECT Acct_Owner__c,Account_Manager__c,Company_Name__c,Status__c,Sector__c,Region__c,iD FROM  Account where iD = '" + Accountid + "'")
        if Accountsql is not None and len(Accountsql.records)>0:
            assignvalue("Account Manager",Accountsql.records[0].Any[1].InnerText)
            assignvalue("Region",Accountsql.records[0].Any[5].InnerText)
            assignvalue("Sector",Accountsql.records[0].Any[4].InnerText)
            customer=Quote.NewCustomer('BillTo')
            customer.OwnerName=Accountsql.records[0].Any[0].InnerText
            customer.CrmAccountId=Accountsql.records[0].Any[6].InnerText
            Trace.Write("Assign Customer" +str(customer.OwnerName))
            Quote.BillToCustomer=customer
            isuneditable("Opportunity Type")
            isuneditable("Opportunity Reference Number")
            isuneditable("Opportunity Status")
            isuneditable("Region")
            isuneditable("PO Number")
            isuneditable("Selling Currency")
            isuneditable("Sector")
            isuneditable("PO Issued Date")
            isuneditable("Account Manager")
            isuneditable("Quote Expiration Date")
            isuneditable("Additional Comments")
            ishiddden("Additional Comments")
