import refinitiv.dataplatform as rdp
from refinitiv.dataplatform.content import ipa
from refinitiv.dataplatform.content.ipa import bond
import datetime as datetime
import json
import pandas as pd


rdp.open_desktop_session("eb2ef552be9f428395f4b41b0a05b232f9250fdf")

endpoint = rdp.Endpoint(None, 
           "data/quantitative-analytics/v1/financial-contracts")
request_body={
  "outputs": [
    "Headers",
    "Data"
  ],
  "fields": [
    "MarketDataDate",
    "ValuationDate",
    "IndexRic",
    "IborRatePercent",
    "Price",
    "AdjustedPrice",
    "NeutralPrice",
    "DiscountMarginBp",
    "SimpleMarginBp",
    "YieldPercent",
    "NeutralYieldPercent",
    "AccruedDays",
    "Accrued"
  ],
  "universe": [
    {
      "instrumentType": "Bond",
      "instrumentDefinition": {
        "issueDate": "2021-02-28",
        "endDate": "2032-02-28",
        "issuerCountry" : "MT",
        "notionalCcy": "EUR",
        "interestPaymentFrequency": "Quarterly",
        "indexFixingRic": "EURIBOR3MD=",
        "interestType": "Float",
        "interestCalculationMethod": "Dcb_Actual_Actual"
        
 #       
      },
      "pricingParameters": {
 #       "discountMarginBp": 10,
        "yieldPercent" : 1
      }
    }
  ]
}
response = endpoint.send_request(method = rdp.Endpoint.RequestMethod.POST,body_parameters = request_body)
#bond_Data = json.loads(response)
#print(response.data.raw)

headers_name = [h['name'] for h in response.data.raw['headers']]
df = pd.DataFrame(data=response.data.raw['data'], columns=headers_name)
print(df)

dtstr = datetime.datetime.now()
format = "%d_%m_%Y %H-%M-%S"
df.to_csv("FRNOut_" +  dtstr.strftime(format) + ".csv")

#print(bond_Data(AdjustedPrice))