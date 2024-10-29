#ismlar = ['Muhammadali','Sanjar','Abdulloh','Ibrohim']
#print(ismlar[0] + " takorpga pul yo'q")
#print(ismlar[2] + " siqilma hammasi o'tib ketadi")
#print(ismlar[3] + " tirikmisiz")
#print(ismlar[1] + " fizika qachin endi")

sonlar = [2, -3, 8, 5.5]
print(sonlar)
print(sonlar[0] + sonlar[1])
print(sonlar[1] / sonlar[1])
print(sonlar[2]-sonlar[3])
print(sonlar[1]**sonlar[0])
sonlar.append(7.3)
sonlar.insert(0, 20)
del sonlar[2]
print(sonlar)
t_shaxslar = ['Hasanxon domla', 'Alijon Qori', 'Murod Nazarov', 'Zafar Hoshimov']
z_shaxslar = ['Muhammad s.a.v.', 'Muhammad Sodiq,', 'Umar r.a.', 'Abu Hanifa']
paygambar = z_shaxslar[0]
mashhur = t_shaxslar[0]
print("Men tarixiy shaxslardan " + paygambar + " bilan, " + " zamonaviy shaxslardan esa " + mashhur +
      " bilan suhbat qilishni istar edim")

friends = []
friends.append('Sanjar')
friends.append('Ibrohim')
friends.append('Abdulloh')
friends.append('Muhammad Ali')
friends.append('Shuxrat')
print(friends)
friends.remove('Ibrohim')
friends.remove('Shuxrat')
print(friends)
friends.append("Umid")
friends.insert(0, "Rahmatilla")
friends.insert(3, "Sardor")
print(friends)
mehmonlar = []
mehmonlar.append(friends[1])
mehmonlar.append(friends[2])
mehmonlar.append(friends[4])
mehmonlar.append(friends[5])
print(friends)
print(mehmonlar)
