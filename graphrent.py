from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')



rent_percentage= [0.25, 0.11, 0.07, 0.05, 0.05, 0.04, 0.04, 0.035, 0.026, 0.02]
rent_y=[]
for rent in rent_percentage:
    rent=rent*100
    rent_y.append(rent)

labels_rent=['Mirpur', 'Mohammadpur', 'Uttara', 'Badda', 'Jatra Bari', 'Bashundhara R-A', 'Banasree', 'Dakshin Khan', 'Shyampur', 'Dhanmondi']
rent_median=[16.0, 17.333333333333332, 18.94736842105263, 18.055555555555557, 14.375, 17.91044776119403, 16.363636363636363, 15.0, 12.0, 23.076923076923077]
plt.rcParams.update({'font.size': 8})

fig, ax1 = plt.subplots()

ax2=ax1.twinx()

#bar labels
#for i, txt in enumerate(rent_y):
    #ax1.annotate(txt,(labels_rent[i],rent_y[i],  ))

ax1.bar(labels_rent, rent_y, label="Percentage Listing")
ax1.grid(False)
ax2.plot(labels_rent, rent_median, label="Median Rent Per Sqf", color="Orange",)
ax2.grid(False)
plt.title("Area Preference in Apartment for Rent")
plt.xlabel("Locations")
ax1.set_ylabel("Percentage of Listing")
#ax2.set_ylabel("Median Price Per Square Feet")
plt.legend(loc='best')
plt.tight_layout()

plt.show()

print(sum(rent_percentage))
