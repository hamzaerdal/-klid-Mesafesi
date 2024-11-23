import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Noktaların tanımlanması
points = [(0, 0), (3, 4), (5, 12), (8, 15)]  # Örnek noktalar

# Mesafeleri saklamak için bir liste
distances = []

# Mesafelerin hesaplanması
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı çiftleri tekrar hesaplamamak için i+1'den başlıyoruz
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonuçların yazdırılması
print("Tüm noktalar arasındaki mesafeler:", distances)
print("En kısa mesafe:", min_distance)
