import matplotlib.pyplot as plt
import cv2
import random



def make_moon_plot(client_name = 'Dan Reeves', location = 'Bay Rainbows', acres = 1):
    location_arr = {'Bay Rainbows':[[30,50],[25,40],['N','W']],'Sea Rains':[[25,40],[10,25],['N','W']],
                'Lake Dream':[[30,40],[25,40],['N','E']], 'Sea Tranquility':[[5,15],[25,35],['N','E']],
                'Taurus Mountain':[[20,35],[35,45],['N','E']],'Lunar Alps':[[45,55],[0,5],['N','W']],
                'Lake Happiness':[[15,20],[5,10],['N','E']], 'Moscoviense':[[20,30],[140,155],['N','E']],
                'Orientale':[[15,25],[85,95],['S','W']],'Sea Nectar':[[10,20],[30,40],['S','E']],
                'Ocean Storms':[[15,20],[50,60],['N','W']],'Sea Serenity':[[20,30],[10,20],['N','E']],
                'Sea Ingenuity':[[30,35],[160,165],['S','E']],'Sea Clouds':[[15,25],[10,20],['S','W']],
                'Sea Vapors':[[10,15],[0,10],['N','E']]}
    acres_arr= acres*0.5
    if location == 'Bay Rainbows':
        img = cv2.cvtColor(plt.imread('moon_land_base/Bay_Rainbows.png'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Sea Rains':
        img = cv2.cvtColor(plt.imread('moon_land_base/Sea_Rains.png'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Lake Dream':
        img = cv2.cvtColor(plt.imread('moon_land_base/Lake_Dream.jpg'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Sea Tranquility':
        img = cv2.cvtColor(plt.imread('moon_land_base/Sea_Tranquility.jpg'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Lake Dream':
        img = cv2.cvtColor(plt.imread('moon_land_base/Lake_Dream.jpg'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Taurus Mountain':
        img = cv2.cvtColor(plt.imread('moon_land_base/Taurus_Mountains.png'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Lunar Alps':
        img = cv2.cvtColor(plt.imread('moon_land_base/Lunar_Alps.png'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Lake Happiness':
        img = cv2.cvtColor(plt.imread('moon_land_base/Lake_Happiness.jpg'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Moscoviense':
        img = cv2.cvtColor(plt.imread('moon_land_base/MOSCOVIENSE.png'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Orientale':
        img = cv2.cvtColor(plt.imread('moon_land_base/Orientale.png'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Sea Nectar':
        img = cv2.cvtColor(plt.imread('moon_land_base/Sea_Nectar.png'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Ocean Storms':
        img = cv2.cvtColor(plt.imread('Bay_Rainbows.png'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Sea Serenity':
        img = cv2.cvtColor(plt.imread('moon_land_base/Ocean_Storm.png'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Sea Ingenuity':
        img = cv2.cvtColor(plt.imread('moon_land_base/Sea_Inguenity.jpg'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Sea Clouds':
        img = cv2.cvtColor(plt.imread('moon_land_base/Sea_Clouds.png'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    elif location == 'Sea Vapors':
        img = cv2.cvtColor(plt.imread('moon_land_base/Sea_Vapors.jpg'), cv2.COLOR_BGR2RGB)
        lat_cords= location_arr.get(location)[0]
        long_cords = location_arr.get(location)[1]
        lat_pole = location_arr.get(location)[2][0]
        long_pole = location_arr.get(location)[2][1]
        latitude  = float("{:.2f}".format(random.uniform(lat_cords[0],lat_cords[1])))
        longitude =float("{:.2f}".format(random.uniform(long_cords[0],long_cords[1])))
    else :
        raise Exception('Oops something went wrong!')
        return 0

    fig, ax = plt.subplots()
    ax.imshow(img)
    ymin, ymax = ax.get_ylim()
    xmin, xmax = ax.get_xlim()
    random_x = random.uniform(xmin, xmax)
    random_y = random.uniform(ymin, ymax)
    circle_1 = plt.Circle((1 * random_x, 1 * random_y), 75 * acres, lw=1, color="blue", fill=False)
    ax.add_patch(circle_1)
    ax.axis('off')
    plt.title(f"{client_name} land property\nLatitude {latitude} ° {lat_pole} "
              f"Longitude {longitude} ° {long_pole}")
    plt.savefig(f'{client_name}_property.png',dpi = 1200)
    return print('success!')


make_moon_plot()
plt.show()