count = 0
distance = 100
first_friend_speed = 1
second_friend_speed = 1
dog_speed = 5
friend = 2


while distance > 10:
    if friend == 1:
        time = distance / (first_friend_speed + dog_speed)
        friend = 2
        distance = distance - (first_friend_speed + second_friend_speed) * time
        count = count + 1
    if friend == 2:
        time = distance / (second_friend_speed + dog_speed)
        friend = 1
        distance = distance - (first_friend_speed + second_friend_speed) * time
        count = count + 1
print('Собака пробежит', count, 'раз.')