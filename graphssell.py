from matplotlib import pyplot as plt

#Percentage of area in apartment for sales

plt.style.use('fivethirtyeight')

top_10_location_median_price=[5043.478260869565, 6922.222222222223, 4807.407407407407, 7696.663472427912, 4500.0, 5500.530222693531, 8214.066653036189, 5944.444444444444, 6000.0, 3352.059925093633]
sell_percentge=[0.22837370242214533, 0.1051518646674356, 0.09246443675509419, 0.0790080738177624, 0.06362937331795464, 0.0523836985774702, 0.02768166089965398, 0.025182622068435218, 0.02114571318723568, 0.019223375624759707]
sell_y=[]
for sell in sell_percentge:
    sell=sell*100
    sell_y.append(sell)

labels_sell=['Mirpur', 'Uttara', 'Mdpur', 'Bashndhara R-A', 'Dakshin Khan', 'Badda', 'Dhanmondi', 'Bashabo', 'Adabor', 'Savar']

plt.rcParams.update({'font.size': 8})


fig, ax1 = plt.subplots()


ax2=ax1.twinx()

ax1.bar(labels_sell, sell_y, label="Percentage Listing")
ax1.grid(False)
ax2.plot(labels_sell, top_10_location_median_price, label="Median Price Per Sqf", color="Orange",)
ax2.grid(False)
plt.title("Area Preference in Apartment for Sale")
plt.xlabel("Locations")
ax1.set_ylabel("Percentage of Listing")
#ax2.set_ylabel("Median Price Per Square Feet")
plt.legend(loc='best')
plt.tight_layout()

print(sum(sell_y))
#
plt.show()
