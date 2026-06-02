import pandas as pd

# Read the data into a Pandas DataFrame
df = pd.read_csv('visualizationData.csv')

# Group the DataFrame by drug name and count the number of times each drug appears and sorting it by desending 
drug_counts = df.groupby('drug_name').count()
drugs=drug_counts.sort_values(by=['drug_id'],ascending=False)

#group Allergy
allergy_counts = df.groupby('Allergy').count()
allergy=allergy_counts.sort_values(by=['allergy_id'],ascending=False)

#group address
address_count = df.groupby('address').count()
address=address_count.sort_values(by=['drug_id'],ascending=False)

from matplotlib import pyplot as plt

#visualization
#the most five drugs
bar_drug=plt.barh(drugs.head(5).index,drugs['drug_id'].head(5));
plt.savefig('bar_drug.svg')
#allergys
bar_allergy7=plt.barh(allergy.head(7).index,allergy['allergy_id'].head(7))
plt.savefig('bar_allergy7.svg')
#the most five governmentors
bar_address=plt.barh(address.head(5).index,address['address_id'].head(5))
plt.savefig('bar_address.svg')
#allergy with drugs most 5 drugs
bar_allergy_drug5=plt.barh(allergy.head(5).index,drugs.head(5).index)
plt.savefig('bar_allergy_drug5.svg')
#allergy with address 5 most drugs
bar_allergy_address5=plt.barh(allergy.head(5).index,address.head(5).index)
plt.savefig('bar_allergy_address5.svg')
#address with drugs most 5 
bar_drug_address5=plt.barh(drugs.head(5).index,address.head(5).index)
plt.savefig('bar_drug_address5.svg')
#drugs with address
bar_address_drug5=plt.barh(address.head(5).index,drugs['drug_id'].head(5))
plt.savefig('bar_address_drug5.svg')
#allergy with drugs
bar_allergy_drug5=plt.barh(allergy.head(5).index,drugs['drug_id'].head(5))
plt.savefig('bar_allergy_drug5.svg')











