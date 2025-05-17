import imageio.v2 as imageio

filenames = ['foto-1.jpeg', 'foto-2.jpeg', 'foto-3.jpeg', 'foto-4.jpeg']
images = []

for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave('Poggers.gif', images, duration = 0.5, loop = 0)
