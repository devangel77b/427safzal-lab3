import matplotlib.pyplot as plt
plt.rcParams['text.usetex']=False
plt.rcParams['svg.fonttype']='none'
plt.rcParams['font.size']=8

# Data
x = [0.000, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040, 0.045, 0.050, 0.055, 0.060]
y = [0.071, 1.47, 2.94, 4.41, 5.70, 7.35, 8.57, 7.48, 6.18, 5.53, 4.24, 4.66, 4.68]

# Plot
plt.figure(figsize=(3.4167, 2),dpi=600)
plt.plot(x, y, marker='o',markersize=4.2)
plt.xlabel(r'displacement, \unit{\meter}')
plt.ylabel(r'force, \unit{\newton}')
plt.grid(True)
plt.tight_layout()

# Save
plt.savefig('force_vs_displacement.png',dpi=600)
plt.savefig('force_vs_displacement.svg')

