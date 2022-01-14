
#For sale
below1ksale=2046
Upto15ksale=5410
upto2ksale=1727
more2k=980

salesize=[below1ksale, Upto15ksale, upto2ksale, more2k]

import matplotlib.pyplot as plt
import numpy as np



#plt.style.use('_mpl-gallery-nogrid')


# make data


colors = plt.get_cmap('Accent')(np.linspace(0.2, 0.7, len(salesize)))
labels = ['Below 1k sq feet', 'From 1k-1.5k sq feet', 'From 1.5k-2k sq feet', 'More than 2k sq feet']

# plot
fig, ax = plt.subplots()
ax.pie(salesize, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "black"}, autopct='%1.1f%%')
plt.title("Apartment Size Preference in Sale Listings")

ax.legend(labels, loc="best")
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)

ax.set(xlim=(0, 8),
       ylim=(0, 8),)





#plt.show()


#For rent
below1krent=20811
Upto15krent=9734
upto2krent=2299
more2krent=1407

rentsize=[below1krent, Upto15krent, upto2krent, more2krent]

import matplotlib.pyplot as plt
import numpy as np



#plt.style.use('_mpl-gallery-nogrid')


# make data


colors = plt.get_cmap('Paired')(np.linspace(0.2, 0.7, len(rentsize)))
labels = ['Below 1k sq feet', 'From 1k-1.5k sq feet', 'From 1.5k-2k sq feet', 'More than 2k sq feet']

# plot
fig, ax = plt.subplots()
ax.pie(rentsize, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "black"}, autopct='%1.1f%%')
plt.title("Apartment Size Preference in Rent Listings")

ax.legend(labels, loc="best")
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)

ax.set(xlim=(0, 8),
       ylim=(0, 8),)

plt.show()
