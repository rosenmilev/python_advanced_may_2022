
while products:
    current_time_in_sec += 1

    if current_time_in_sec == 86400:
        current_time_in_sec = 0
    if current_time_in_sec in working_robots:
        robots_list.append(working_robots[current_time_in_sec])
        working_robots.pop(current_time_in_sec)

    if robots_list:
        current_product = products.popleft()
        current_robot = robots_list.popleft()
        name = current_robot[0]
        working_time = int(current_robot[1])
        m, s = divmod(current_time_in_sec, 60)
        h, m = divmod(m, 60)
        print(f"{name} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
        working_robots[current_time_in_sec + working_time] = current_robot
    else:
        products.append(products.popleft())
