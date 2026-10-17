import matplotlib.pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

plt.bar(ismlar, ballar, color="teal")
plt.title("O'quvchilar natijalari")
plt.xlabel("O'quvchilar")
plt.ylabel("Ball")
plt.grid(axis="y")
plt.savefig("oquvchilar_natijasi.png")
plt.show()